"""generate word cloud from words in file"""
import re
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wordcloud_utils
#import json
#import pandas as pd

#FILE = 'tender_buttons_full.txt'
#FILE = 'fannyhill.txt'
FILE = 'mobydick.txt'
FILE = 'rabelais.txt'
URL = 'https://www.gutenberg.org/cache/epub/541/pg541.txt'

def plot_wordcloud(wordcloud):
  # plot the WordCloud image
  plt.figure(figsize = (8, 8), facecolor = None)
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.tight_layout(pad = 0)

  # this is necessary without jupyter
  plt.show()


text = wordcloud_utils.get_text_from_pg(URL)
wordcloud = wordcloud_utils.generate_word_cloud_from_text(text)
plot_wordcloud(wordcloud)
# plot the WordCloud image
#plt.figure(figsize = (8, 8), facecolor = None)
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.tight_layout(pad = 0)
#
## this is necessary without jupyter
#plt.show()
