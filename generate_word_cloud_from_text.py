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
URL = 'https://www.gutenberg.org/cache/epub/289/pg289.txt'

FILE = wordcloud_utils.get_text_from_pg(URL)
wordcloud_utils.generate_word_cloud_from_text(FILE)
