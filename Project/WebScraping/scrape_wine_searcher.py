##
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scraper(df, url, pairing_food):
    session = requests.Session()
    # a user agent simulating browser behavior
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }

    for page in range(1, 501, 25):
        time.sleep(1)
        response = session.get(url + f"?page={page}")
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            all_products = soup.findAll("a", attrs={"class": "superlative-list__name font-light-bold"})
            all_grapes = soup.findAll("div", attrs={
                "class": "text-md-center superlative-list-md-w-19 order-md-1 mb-1 mb-md-0"})
            all_popularities = soup.findAll("div", attrs={
                "class": "text-md-center superlative-list-md-w-16 order-md-2 mb-1 mb-md-0"})
            all_scores = soup.findAll("div", attrs={"class": "superlative-list__score"})
            all_prices = soup.findAll("div", attrs={
                "class": "text-md-center superlative-list-md-w-15 order-md-4 mb-1 mb-md-0"})

            for product, grape, popularity, score, price in zip(all_products, all_grapes, all_popularities, all_scores,
                                                                all_prices):
                df = df.append({
                    "Pairing Food": pairing_food,
                    "Product": product.text.strip(),
                    "Grape": grape.a.text.strip(),
                    "Popularity": popularity.text.strip().split()[0],
                    "Critics' Score": score.text.strip(),
                    "Avg. Price kr / 750ml": price.text.strip().split()[0]
                }, ignore_index=True)
        else:
            print(f"error: {response.status_code}")

    return df

# initialize a dataframe
df = pd.DataFrame(columns=["Pairing Food", "Product", "Grape", "Popularity", "Critics' Score", "Avg. Price kr / 750ml"])

##
df = scraper(df, "https://www.wine-searcher.com/food-wine-18", "chicken and turkey").copy()

##
df = scraper(df, "https://www.wine-searcher.com/food-wine-5", "duck, goose and game birds").copy()
print(df)


# session = requests.Session()
# session.headers = {
#     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
# }
#
#
# response = session.get("https://www.wine-searcher.com/food-wine-5")
#
# print(response)
