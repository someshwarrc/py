import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import string
import re

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(path.abspath('__FILE__'))
mask = np.array(Image.open(path.join(d, "hp_mask.png")))

book = {}

def txttodict():
    with open(path.join(d, 'text.txt')) as file:
        for word in file.read().translate(str.maketrans('\n',' ',string.punctuation)).split(" "):
            word = word.lower()
            if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|you|that|be|he|she|mr|mrs|miss|madam|was|had|it|his|am|i", word):
                continue
            book[word] = book.get(word, 0) + 1
    return book


hp_mask = np.array(Image.open(path.join(d, "hp_mask.jpg")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white",max_words=1000, mask=hp_mask,
               stopwords=stopwords)

# generate word cloud
wc.generate_from_frequencies(txttodict())

# store to file
wc.to_file(path.join(d, "hp_wordcloud.png"))

# cmap = ImageColorGenerator(hp_mask)
# show
plt.imshow(wc, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.show()
