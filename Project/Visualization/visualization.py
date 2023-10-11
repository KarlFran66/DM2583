from wordcloud import WordCloud
import matplotlib.pyplot as plt


data = []
with open('phrased_food_sentences.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = line.strip().split(' ')
        data.append(words)

text = ' '.join([' '.join(words) for words in data])

wordcloud = WordCloud(width=800, height=400, background_color='white')
wordcloud.generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("food_reviews_wordcloud.png")
plt.show()
