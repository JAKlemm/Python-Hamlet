import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from collections import Counter

with open('hamlet.txt', 'r') as f:
    text = f.read()

words = text.lower().split()
word_count = Counter(words)

top_words = dict(word_count.most_common(20))

plt.bar(top_words.keys(), top_words.values())
plt.xticks(rotation=90)
plt.title('Top 20 Word Frequencies in Hamlet')
plt.show()

mask = np.array(Image.open('mask_oval.png'))

wordcloud = WordCloud(background_color='white', mask=mask).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

