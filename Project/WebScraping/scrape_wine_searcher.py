import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scraper(df, url, pairing_food):
    session = requests.Session()

    session.headers = {
        "User-Agent": "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "cookie": "COOKIE_ID=1ZR8CF8D3NS0BCZ; visit=1ZR8CF8D3NS0BCZ%7C20231002142329%7C%2Ffood-wine%7C%7Cend%20; _pxvid=e05597d6-6126-11ee-9f2f-7096df9006cc; NPS_bc24fa74_last_seen=1696253010754; cookie_consent=allow; search=start%7Cdom%2Bde%2Bla%2Bromanee%2Bconti%2Bmontrachet%2Bgrand%2Bcru%2Bcote%2Bbeaune%2Ble%2Bpuligny%2Bburgundy%2Bfrance%7C1%7CSweden%7CSEK%7C%7C%7C%7C%7C%7C%7C%7C%7Ce%7Ci%7C%7C%7CN%7C%7Ca%7C%7C%7C%7CCUR%7Cend; _gid=GA1.2.884907382.1696254377; cookie_enabled=true; ID=KN88C7823JT003H; IDPWD=I12898041; _csrf=rtex5cBL4ryhKumnGhu8Rc6NX-uSGXtV; pxcts=af8490ee-61c5-11ee-9805-378000b1548a; NPS_bc24fa74_throttle=1696367802292; _pxhd=/BYdcHumhlAc0nm4/b0H5ShKopZZo9lAZn4WnU0BO8zjLC9TVvHeShlstx0665Ore2YacQaKj8bzq2FBWrerOQ==:ZKZ77ZfIOegmWn87rsfY5RR1l03cvCRyj3M16S/0U5-VMYucsmu/AtcGPCQr2c0oh0mZuRXV2pWMMErbERzSjymuGWdFuhuyFRNN9HwwrGE=; geoinfo=59.3492963%7C18.0678324%7CStockholm%7CSweden%7CSE%7C158.174.187.208%7C0%7CManual%2C%25C3%2596stermalm%252C%2BStockholm%252C%2BStockholms%2Bl%25C3%25A4n%252C%2BSweden%3B%20path%3D%2F%3B%20domain%3Dwine-searcher.com%3B%20expires%3DTue%2C%2031-Dec-2030%2000%3A00%3A00%20GMT; biz=59.349243%2C18.068005; ws_prof=NqS4LbwOxjts7prGWNyshHA6YEeYMjnqhzI2znXaD5TZ; user_status=F%7C; _ga=GA1.1.476784031.1696253011; _ga_M0W3BEYMXL=GS1.1.1696331538.10.1.1696331941.0.0.0; _px3=d64119a9a92d4e863a325baec53d13b746596a0db26fd531dede47462b6e62b4:ppxADH7uc2N7yYp1vZm1LaujS8L/WhuK9RykAA+h/NKsRRNoHft9masivqvOB30EbwRY7lQoBdIxBRQdi69Tsg==:1000:yIFFa6uyi2psX3OJG7b5i4MVVd6UjZQ6p+R7w5IqbMyVdOg4r1dEFpfBdXTl3rgz7W2kEBT2J0ZIcgbcip9mLHefoNXQz4we0kP77HssyZzfSCr4iveBu1m4QQcaM+9j515PFx8n7VMjs+XECu+wBObEoE/Ex1cqqt+R6bwBCSZBzuknlPH/gtBEeztFh4mKUEEridZWFUgbmsvA/rW4NWmRYYsDJfeZlJdr+2M8hj8=; _px2=eyJ1IjoiYTZkY2I0NjAtNjFkZS0xMWVlLTgwZmEtYTVjNzJiM2Q4NjU0IiwidiI6ImUwNTU5N2Q2LTYxMjYtMTFlZS05ZjJmLTcwOTZkZjkwMDZjYyIsInQiOjE2OTYzMzI1MzE5ODgsImgiOiJjNjA5NjYwODgzNjI1Mjk0OTk5Yzc0Mjc4MDdjOTRmMGQ3M2ZlMjk3OTQ2YjRhNzZhN2ZlMTc0ZTE1MTNlNDJkIn0=; _pxde=314ad4a990518a1dc2566d1936be8235c5b48dccb82a60a1ba7509455cca1c64:eyJ0aW1lc3RhbXAiOjE2OTYzMzIyMzE5ODgsImZfa2IiOjAsImlwY19pZCI6W119",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "Referer": "https://www.wine-searcher.com/food-wine",
        "Origin": "https://www.wine-searcher.com",
    }

    # proxy_ip = '15.204.161.192'
    # proxy_port = 18080
    # session.proxies = {
    #     'http': f'http://{proxy_ip}:{proxy_port}',
    #     'https': f'https://{proxy_ip}:{proxy_port}'
    # }

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

# df = scraper(df, "https://www.wine-searcher.com/food-wine-18", "chicken and turkey").copy()
# df.to_csv("pairing_food.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-5", "duck, goose and game birds").copy()
# df.to_csv("pairing_food_duck.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-17", "pork, ham and cold meats").copy()
# df.to_csv("pairing_food_pork.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-6", "lamb").copy()
# df.to_csv("pairing_food_lamb.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-1", "beef and venison").copy()
# df.to_csv("pairing_food_beef.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-21", "salads and green vegetables").copy()
# df.to_csv("pairing_food_salads")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-19", "root vegetables and squashes").copy()
# df.to_csv("pairing_food_root_vegetables.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-2", "mushrooms").copy()
# df.to_csv("pairing_food_mushrooms.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-3", "tomato-based dishes").copy()
# df.to_csv("pairing_food_tomato.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-11", "chilis and hot spicy foods").copy()
# df.to_csv("pairing_food_chilis.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-15", "white fish").copy()
# df.to_csv("pairing_food_white_fish.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-8", "meaty and oily fish").copy()
# df.to_csv("pairing_food_meaty_fish.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-7", "shellfish, crab and lobster").copy()
# df.to_csv("pairing_food_shellfish.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-25", "goats' cheese and feta").copy()
# df.to_csv("pairing_food_goat_cheese.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-20", "manchego and parmesan").copy()
# df.to_csv("pairing_food_manchego.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-27", "cheddar and gruyere").copy()
# df.to_csv("pairing_food_cheddar.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-4", "blue cheeses").copy()
# df.to_csv("pairing_food_blue_cheese.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-24", "brie and camembert").copy()
# df.to_csv("pairing_food_brie.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-34", "fruit-based desserts").copy()
# df.to_csv("pairing_food_fruit.csv")

# df = scraper(df, "https://www.wine-searcher.com/food-wine-16", "chocolate and caramel").copy()
# df.to_csv("pairing_food_chocolate.csv")

df = scraper(df, "https://www.wine-searcher.com/food-wine-32", "cakes and cream").copy()
df.to_csv("pairing_food_cakes.csv")
