"""generate word cloud from words in file"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#import json
#import pandas as pd

FILE = 'tender_buttons_full.txt'

def generate_word_cloud_from_file(thisfile):
  """generate word cloud from words in file"""
  with open(thisfile,'r',encoding='utf-8') as myinfile:
    text = myinfile.read()
  print(text)

  tokens = text.lower().split()

  caption_words = ""
  caption_words += " ".join(tokens) + " "

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

generate_word_cloud_from_file(FILE)
