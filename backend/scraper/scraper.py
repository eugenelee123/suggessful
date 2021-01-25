import urllib
from bs4 import BeautifulSoup
from googlesearch import search
req = urllib.request.Request("https://www.urbanoutfitters.com/", headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen(req)
soup = BeautifulSoup(con.read(), features = "html.parser")

#get company name
meta_title = soup.find("meta", property = "og:title")
title = soup.find("title")
title = title.string
url = soup.find("meta", property = "og:url")

# print("meta title: ", meta_title)
# print("title: ", title)
# print("url: ", url)

query = "Brands like {}".format(title)
# print(query)

url_search = "https://www.google.com/search?lr=lang_en&" \
             "q=%{}&btnG=Google+Search&tbs=0&safe=off&" \
             "cr=''&filter=0".format(query)

req = urllib.request.Request(url_search, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen(req)
soup = BeautifulSoup(con.read(), features = "html.parser")

print(url_search)
# print(soup.prettify())


# Fill in search bar with <query>
# hit google search
# scrap class i8Z77e
    # return all items under that class


# for i in search(query, tld = "co.in", num = 10, stop = 10, pause = 2):
#     print(i)

