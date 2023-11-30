import json
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# this data is available here for further exploration if desired, e.g. below lists all display urls for all posts

file = 'tender_buttons_full.txt'
with open(file) as fd:
  text = fd.read()

print(text)

tokens = text.split()

for i in range(len(tokens)):
  tokens[i] = tokens[i].lower()

caption_words = ""
caption_words += " ".join(tokens)+" "

stopwords = set(STOPWORDS)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(caption_words)

# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# this is necessary without jupyter
plt.show()
