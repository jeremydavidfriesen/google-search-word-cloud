# necessary imports
from os import path
import os

import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from wordcloud import WordCloud as wc
from wordcloud import STOPWORDS


# open and read in Google activity doc
with open ('My Activity.html', 'r', encoding='utf8') as myfile:
    data=myfile.readlines()
d = ''.join(data)


# find all searches and put into list
def findSearchEnd(i):
    for i in range(i, len(d)):
        if(d[i] == '<'):
            return i
    return -1

token = 0
searches = []

for i in range(0, len(d)):
    if(token == 1 and d[i] == '>'):
        searches.append(d[i+1:findSearchEnd(i+1)])
        token = 0
    if(d[i:i+12] == 'Searched for'):
        token = 1


# join all searches into one string
text = ' '.join(searches)


# load in google logo mask
p = path.dirname(__file__) if '__file__' in locals() else os.getcwd()
googleMask = np.array(Image.open(path.join(p, 'googlemask.png')))


# add any strings you want to exclude to exclude
exclude = []
stopwords = set(STOPWORDS)
stopwords.update(exclude)


# generate wordcloud
vis = wc(background_color='white', max_words=1000, mask=googleMask,
               stopwords=stopwords, colormap='tab10')
vis.generate(text)


# show wordcloud
plt.imshow(vis, interpolation='bilinear')
plt.axis('off')
plt.show()


# save wordcloud
vis.to_file(path.join(p, "googleWordCloud.png"))