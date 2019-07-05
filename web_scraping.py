import bs4

import requests
url = "http://mycodingzone.net/blog/english"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
print(soup.prettify())
for para in soup.find_all('p'):
    print(para)

for para in soup.find_all('p'):
    print(para.text)

for para in soup.find_all('a'):
    link = para.get("href")
    if link[0:3] =="../" and link!="#":
        print("http://mycodingzone.net"+link[2:len(link)])
    elif link[0]=="/" and link!="#":
        print("http://mycodingzone.net"+link)
    elif link!="#":
        print(link)

url2 = "https://www.youtube.com/channel/UCi7DM6_Y0EXPdKN_YJIrzKg/videos?disable_polymer=1"
data = requests.get(url2)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
for para in soup.find_all('a'):
    link = para.get("href")
    if link[0:3] =="/wa":
        print("https://www.youtube.com"+link)


