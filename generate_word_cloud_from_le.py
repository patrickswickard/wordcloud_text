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
  plt.close()

def get_all_litlist():
  df = pd.read_csv('litlist.csv')
  print(df)

  for index,row in df.iterrows():
    if index >= 156:
      title = row['title']
      author = row['author']
      url = row['url']
      text = wordcloud_utils.get_text_from_pg(url)
      wordcloud = wordcloud_utils.generate_word_cloud_from_text(text)
      save_wordcloud(wordcloud,index)

def get_wc_from_le(url):
  text = get_text_from_le(url)
  wordcloud = wordcloud_utils.generate_word_cloud_from_text(text)
  return wordcloud

def get_text_from_le(url):
  numpages = get_numpages_from_le(url)
  print(numpages)
  rawtextlist = []
  for i in range(1,int(numpages) + 1):
    thisurl = URL + '/?page=' + str(i)
    print('trying ' + thisurl)
    rawtext = wordcloud_utils.get_text_from_url(thisurl)
    rawtextlist.append(rawtext)
  foundlist = []
  for thistext in rawtextlist:
    result = re.findall(r"<div\s+class=\"aa_ht\">\s*(.*?)<div\s+class=\"aa_ht\">",thistext,re.DOTALL)[0]
    foundlist.append(result)
  found = ' '.join(foundlist)
  foundclean = wordcloud_utils.strip_tags(found)
  print(foundclean)
  return foundclean

def get_numpages_from_le(url):
  rawtext = wordcloud_utils.get_text_from_url(URL)
  resultre = re.findall(r"<a\s+class=\"l_bJ\"[^>]*>\s*(\d+)\s*</a>\s*<form",rawtext,re.DOTALL)
  if resultre:
    result = resultre[0]
  else:
    result = '1'
  return result

URL = 'https://www.literotica.com/s/taylor-swift-meeting-ellie'
URL = 'https://www.literotica.com/s/the-birth-of-bella-the-bimbo-clown'
#URL = 'https://www.literotica.com/s/the-adventures-of-scarlett-holmes'

###print(get_numpages_from_le(URL))

wordcloud = get_wc_from_le(URL)

#wordcloud = wordcloud_utils.generate_word_cloud_from_french_text(text)

plot_wordcloud(wordcloud)

#save_wordcloud(wordcloud,1)

#get_all_litlist()
