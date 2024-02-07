"""generate word cloud from words in file"""
import re
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
#import json
#import pandas as pd

#FILE = 'tender_buttons_full.txt'
#FILE = 'fannyhill.txt'
FILE = 'mobydick.txt'
FILE = 'rabelais.txt'
URL = 'https://www.gutenberg.org/cache/epub/289/pg289.txt'

def get_text_from_pg(url):
  """Get text from project gutenberg"""
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
  rawtext = requests.get(url,headers=headers).text
  result = re.findall(r"\*\*\*\s+START\s+OF\s+THE\s+PROJECT\s+GUTENBERG.*?\*\*\*(.*?)\*\*\*\s+END\s+OF\s+THE\s+PROJECT\s+GUTENBERG",rawtext,re.DOTALL)[0]
  return result

def get_text_from_url(url):
  """Get text from project gutenberg"""
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
  rawtext = requests.get(url,headers=headers).text
  return rawtext

def strip_tags(text):
  modtext = re.sub("<[^>]*>"," ",text)
  return modtext

def enhance_stopwords_french(stopwords):
  """enhance french stopwords"""
  stopwords.add('ii')
  stopwords.add('c\'est')
  stopwords.add('d\'un')
  stopwords.add('d\'une')
  stopwords.add('qu\'il')
  stopwords.add('qu\'on')
  stopwords.add('qu\'un')
  stopwords.add('j\'un')
  stopwords.add('n\'en')
  stopwords.add('n\'est')
  stopwords.add('non')
  stopwords.add('bien')
  stopwords.add('bon')
  stopwords.add('été')
  stopwords.add('qu\'elle')
  stopwords.add('qu\'ils')
  stopwords.add('qu\'elles')
  stopwords.add('j\'ai')
  stopwords.add('j\'avais')
  stopwords.add('s\'en')
  stopwords.add('faut')
  stopwords.add('fut')
  stopwords.add('l\'on')
  stopwords.add('l\'un')
  stopwords.add('l\'une')
  stopwords.add('n\'a')
  stopwords.add('m\'en')
  stopwords.add('j\'en')
  stopwords.add('j\'y')
  stopwords.add('faire')
  stopwords.add('fait')
  stopwords.add('jamais')
  stopwords.add('c\'était')
  stopwords.add('s\'il')
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
  stopwords.add('qu')
  stopwords.add('qu\'un')
  stopwords.add('qu\'une')
  stopwords.add('m\'avait')
  stopwords.add('n\'avait')
  stopwords.add('j\'étais')
  stopwords.add('j\'avais')
  stopwords.add('j\'aurais')
  stopwords.add('m\'étais')
  stopwords.add('n\'étais')
  stopwords.add('n\'était')
  stopwords.add('s\'était')
  stopwords.add('n\'avais')
  stopwords.add('d\'elle')
  stopwords.add('jusqu\'à')
  stopwords.add('qu\'à')
  stopwords.add('d\'avoir')
  stopwords.add('d\'etre')
  stopwords.add('n\'y')
  stopwords.add('venait')
  stopwords.add('madame')
  stopwords.add('monsieur')
  stopwords.add('mme')
  stopwords.add('mademoiselle')
  stopwords.add('mlle')
  stopwords.add('disait')
  stopwords.add('vn')
  stopwords.add('ie')
  stopwords.add('vne')
  stopwords.add('dis')
  stopwords.add('dit')
  stopwords.add('illustration')
  stopwords.add('ii')
  stopwords.add('iii')
  stopwords.add('iv')
  stopwords.add('vi')
  stopwords.add('vii')
  stopwords.add('viii')
  stopwords.add('ix')
  stopwords.add('cf')
  stopwords.add('ung')
  stopwords.add('chapitre')
  stopwords.add('foi')
  stopwords.add('rien')
  stopwords.add('trop')
  stopwords.add('ici')
  stopwords.add('voir')
  stopwords.add('voit')
  stopwords.add('chose')
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
  stopwords.add('la')
  stopwords.add('le')
  stopwords.add('de')
  stopwords.add('et')
  stopwords.add('en')
  stopwords.add('un')
  stopwords.add('dans')
  stopwords.add('les')
  stopwords.add('mr')
  stopwords.add('didn')
  stopwords.add('don')
  stopwords.add('isn')
  stopwords.add('doesn')
  stopwords.add('hasn')
  stopwords.add('hadn')
  stopwords.add('wouldn')
  stopwords.add('couldn')
  stopwords.add('ain')
  stopwords.add('ve')
  stopwords.add('nt')
  stopwords.add('er')
  stopwords.add('jesu')
  stopwords.add('chapter')
  stopwords.add('book')
  stopwords.add('think')
  stopwords.add('make')
  stopwords.add('let')
  stopwords.add('thing')
  stopwords.add('way')
  stopwords.add('man')
  stopwords.add('made')
  stopwords.add('day')
  stopwords.add('never')
  stopwords.add('always')
  return stopwords

def generate_word_cloud_from_text(text):
  """generate word cloud from words in file"""
#  with open(thisfile,'r',encoding='utf-8') as myinfile:
#    text = myinfile.read()
#  print(text)
#  result = re.findall(r"\*\*\*\s+START\s+OF\s+THE\s+PROJECT\s+GUTENBERG.*?\*\*\*(.*?)\*\*\*\s+END\s+OF\s+THE\s+PROJECT\s+GUTENBERG",text,re.DOTALL)
  tokens = text.lower().split()

  caption_words = ""
  caption_words += " ".join(tokens) + " "

  stopwords = enhance_stopwords(set(STOPWORDS))

  wordcloud = WordCloud(width = 800, height = 1100,
                  background_color ='white',
                  stopwords = stopwords,
                  min_font_size = 10).generate(caption_words)
  return wordcloud

def generate_word_cloud_from_french_text(text):
  """generate word cloud from words in file"""
#  with open(thisfile,'r',encoding='utf-8') as myinfile:
#    text = myinfile.read()
#  print(text)
#  result = re.findall(r"\*\*\*\s+START\s+OF\s+THE\s+PROJECT\s+GUTENBERG.*?\*\*\*(.*?)\*\*\*\s+END\s+OF\s+THE\s+PROJECT\s+GUTENBERG",text,re.DOTALL)
  tokens = text.lower().split()

  caption_words = ""
  caption_words += " ".join(tokens) + " "

  stopwords = enhance_stopwords_french(set(fr_stop))

  wordcloud = WordCloud(width = 800, height = 1100,
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
