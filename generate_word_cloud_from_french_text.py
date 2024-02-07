"""generate word cloud from words in file"""
import re
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wordcloud_utils
#import json
import pandas as pd

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

def save_wordcloud(wordcloud,string):
  # plot the WordCloud image
  plt.figure(figsize = (8, 8), facecolor = None)
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.tight_layout(pad = 0)
  plt.savefig('cache/' + str(string) + '.png')
#  # this is necessary without jupyter
#  plt.show()

def save_wordcloudfr(wordcloud,string):
  # plot the WordCloud image
  plt.figure(figsize = (8, 8), facecolor = None)
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.tight_layout(pad = 0)
  plt.savefig('cache/fr/' + str(string) + '.png')
  plt.close()

def get_all_litlist():
  df = pd.read_csv('litlist.csv')
  print(df)

  for index,row in df.iterrows():
    title = row['title']
    author = row['author']
    url = row['url']
    text = wordcloud_utils.get_text_from_pg(url)
    wordcloud = wordcloud_utils.generate_word_cloud_from_text(text)
    save_wordcloud(wordcloud,index)

def get_all_litlistfr():
  df = pd.read_csv('litlistfr.csv')
  print(df)

  for index,row in df.iterrows():
    if index >= 118:
      title = row['title']
      author = row['author']
      url = row['url']
      text = wordcloud_utils.get_text_from_pg(url)
      wordcloud = wordcloud_utils.generate_word_cloud_from_french_text(text)
      save_wordcloudfr(wordcloud,index)

URL = 'https://www.gutenberg.org/cache/epub/22741/pg22741.txt' # brill-sav
URL = 'https://www.gutenberg.org/cache/epub/56708/pg56708.txt' # rimbaud
URL = 'https://www.gutenberg.org/cache/epub/19657/pg19657.txt' # hugo-nd
URL = 'https://www.gutenberg.org/cache/epub/29302/pg29302.txt' # verlaine
URL = 'https://www.gutenberg.org/cache/epub/52489/pg52489.txt' # lavoisier
URL = 'https://www.gutenberg.org/cache/epub/64427/pg64427.txt' # proust 1
URL = 'https://www.gutenberg.org/cache/epub/5097/pg5097.txt'   # verne
URL = 'https://www.gutenberg.org/cache/epub/1256/pg1256.txt'   # cyrano
URL = 'https://www.gutenberg.org/cache/epub/16884/pg16884.txt'   # jarry
URL = 'https://www.gutenberg.org/cache/epub/12005/pg12005.txt'   # other
text = wordcloud_utils.get_text_from_pg(URL)
#wordcloud = wordcloud_utils.generate_word_cloud_from_text(text)
wordcloud = wordcloud_utils.generate_word_cloud_from_french_text(text)
plot_wordcloud(wordcloud)
save_wordcloud(wordcloud,1)

#get_all_litlistfr()
