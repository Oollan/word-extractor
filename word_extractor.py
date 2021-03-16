import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from bidi.algorithm import get_display
from rich import print

input = ["https://he.wikipedia.org/",
         "https://www.mako.co.il/",
         "https://www.ynet.co.il/",
         ]

total = [None] * 50
output = [None] * 50

for website in input:
    r = requests.get(website)
    soup = BeautifulSoup(r.content, "html.parser")
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower()
                 for y in text for x in y.split()))

    arr = [None] * 50

    for i in c.most_common():
        count = len(i[0]) - 1
        if count > 0 and type(i[0]) is str and not arr[count]:
            arr[count] = i
            if total[count] is None or i > total[count]:
                total[count] = i
                output[count] = get_display(
                    "length %d: %s" % (count + 1, i[0]))

print(list(filter(None, output)))
