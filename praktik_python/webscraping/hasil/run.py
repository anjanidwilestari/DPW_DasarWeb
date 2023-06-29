import requests
import csv

url=' https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
r = requests.get(url)
type(r)

html = r.text
print(html)

#Mengimpor BeautifulSoup dari bs4
from bs4 import BeautifulSoup

#Membuat objek BeautifulSoup dari HTML
soup= BeautifulSoup(html, "html5lib")
type(soup)

soup.title

soup.title.string

soup.findAll('a')[:8]

text = soup.get_text()
print(text)

import nltk
nltk.download()

#Impor paket regex
import re

#Definisikan sentence
sentence = 'peter piper pick a peck of pickled peppers'

#Definisikan regex
ps = 'p\w+'

#Mencari semua kata di sentence yang cocok dengan regex kemudian cetak
re.findall(ps,sentence)

re.findall('\w+',sentence)

tokens = re.findall('\w+',text)
tokens[:8]

# Impor RegexpTokenizer dari nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Buat tokenizer
tokenizer = RegexpTokenizer('\w+')

# Buat tokens
tokens = tokenizer.tokenize(text)
tokens[:8]

#Mengisialisasi ke dalam list
words = []

#Loop dari list tokens dan buat huruf kecil/lowercase
for word in tokens:
    words.append(word.lower())

#Cetak beberapa
word[:8]  

#Impor modul nltk
import nltk
nltk.download('stopwords')

#Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')
sw[:5]

#Mengisialisasi ke dalam list
words_ns = []

#Tambahkan ke words_ns semua kata yang ada dalam words tetapi tidak dalam sw
for word in words:
    if word not in sw:
        words_ns.append(word)

#Cetak beberapa
words_ns[:5]

#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

#Figures inline dan setting style visualisasi 
%matplotlib inline
sns.set()

#Buat frekuensi distribusi dan plot 25 kata
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)