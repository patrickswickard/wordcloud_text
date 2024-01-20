"""generate word cloud from words in file"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#import json
#import pandas as pd

#FILE = 'tender_buttons_full.txt'
#FILE = 'fannyhill.txt'
FILE = 'mobydick.txt'
FILE = 'rabelais.txt'

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
  stopwords.add('gave')
  stopwords.add('get')
  stopwords.add('got')
  stopwords.add('still')
  stopwords.add('till')
  stopwords.add('thought')
  stopwords.add('us')
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
  stopwords.add('jesu')
  return stopwords

def generate_word_cloud_from_file(thisfile):
  """generate word cloud from words in file"""
  with open(thisfile,'r',encoding='utf-8') as myinfile:
    text = myinfile.read()
  print(text)

  tokens = text.lower().split()

  caption_words = ""
  caption_words += " ".join(tokens) + " "

  stopwords = enhance_stopwords(set(STOPWORDS))

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
