"""generate word cloud from words in file"""
import re
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#import json
#import pandas as pd

#FILE = 'tender_buttons_full.txt'
#FILE = 'fannyhill.txt'
FILE = 'mobydick.txt'
FILE = 'rabelais.txt'
URL = 'https://www.gutenberg.org/cache/epub/289/pg289.txt'

def get_text_from_pg(url):
  """Get text from project gutenberg"""
  result = requests.get(url).text
  return result

def enhance_stopwords_french(stopwords):
  """enhance french stopwords"""
  stopwords.add('ii')
  stopwords.add('c\'est')
  stopwords.add('d\'un')
  stopwords.add('d\'une')
  stopwords.add('qu\'un')
  stopwords.add('j\'un')
  return stopwords

def enhance_stopwords(stopwords):
  """enhance english stopwords"""
  stopwords.add('one')
  stopwords.add('two')
  stopwords.add('three')
  stopwords.add('four')
  stopwords.add('five')
  stopwords.add('six')
  stopwords.add('seven')
  stopwords.add('eight`')
  stopwords.add('nine')
  stopwords.add('ten')
  stopwords.add('go')
  stopwords.add('see')
  stopwords.add('well')
  stopwords.add('come')
  stopwords.add('came')
  stopwords.add('went')
  stopwords.add('give')
  stopwords.add('gave')
  stopwords.add('must')
  stopwords.add('may')
  stopwords.add('might')
  stopwords.add('all')
  stopwords.add('some')
  stopwords.add('many')
  stopwords.add('none')
  stopwords.add('no')
  stopwords.add('much')
  stopwords.add('thus')
  stopwords.add('upon')
  stopwords.add('toward')
  stopwords.add('behind')
  stopwords.add('above')
  stopwords.add('below')
  stopwords.add('gave')
  stopwords.add('get')
  stopwords.add('got')
  stopwords.add('still')
  stopwords.add('till')
  stopwords.add('thought')
  stopwords.add('us')
  stopwords.add('thy')
  stopwords.add('thou')
  stopwords.add('thee')
  stopwords.add('ye')
  stopwords.add('unto')
  stopwords.add('ask')
  stopwords.add('asked')
  stopwords.add('know')
  stopwords.add('knew')
  stopwords.add('said')
  stopwords.add('say')
  stopwords.add('one')
  stopwords.add('yet')
  stopwords.add('now')
  stopwords.add('will')
  stopwords.add('saw')
  stopwords.add('ll')
  stopwords.add('s')
  stopwords.add('don t')
  stopwords.add('won t')
  stopwords.add('a')
  stopwords.add('b')
  stopwords.add('c')
  stopwords.add('d')
  stopwords.add('e')
  stopwords.add('f')
  stopwords.add('g')
  stopwords.add('h')
  stopwords.add('i')
  stopwords.add('j')
  stopwords.add('k')
  stopwords.add('l')
  stopwords.add('m')
  stopwords.add('n')
  stopwords.add('o')
  stopwords.add('p')
  stopwords.add('q')
  stopwords.add('r')
  stopwords.add('s')
  stopwords.add('t')
  stopwords.add('u')
  stopwords.add('v')
  stopwords.add('w')
  stopwords.add('x')
  stopwords.add('y')
  stopwords.add('z')
  stopwords.add('ve')
  stopwords.add('nt')
  stopwords.add('jesu')
  return stopwords

def generate_word_cloud_from_text(text):
  """generate word cloud from words in file"""
#  with open(thisfile,'r',encoding='utf-8') as myinfile:
#    text = myinfile.read()
#  print(text)
  result = re.findall(r"\*\*\*\s+START\s+OF\s+THE\s+PROJECT\s+GUTENBERG.*?\*\*\*(.*?)\*\*\*\s+END\s+OF\s+THE\s+PROJECT\s+GUTENBERG",text,re.DOTALL)
  tokens = result[0].lower().split()

  caption_words = ""
  caption_words += " ".join(tokens) + " "

  stopwords = enhance_stopwords(set(STOPWORDS))

  wordcloud = WordCloud(width = 800, height = 800,
                  background_color ='white',
                  stopwords = stopwords,
                  min_font_size = 10).generate(caption_words)
  return wordcloud

#  # plot the WordCloud image
#  plt.figure(figsize = (8, 8), facecolor = None)
#  plt.imshow(wordcloud)
#  plt.axis("off")
#  plt.tight_layout(pad = 0)
#
#  # this is necessary without jupyter
#  plt.show()