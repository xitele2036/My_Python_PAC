import bs4
import requests
from bs4 import BeautifulSoup

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}
for page in range(1,5):
    IPurl = 'http://www.xicidaili.com/nn/' + str(page)
    rIP=requests.get(IPurl,headers=headers)
    IPContent=rIP.text
    soupIP = BeautifulSoup(IPContent,"lxml")
    # print(soupIP)
    trs = soupIP.find_all('tr')
    # print(trs)
    for tr in trs.find_all("tr"):
        bookSoup = bs4.BeautifulSoup(str(tr), "lxml")
        ip = bookSoup.tb.a["tb"]
        print(ip)
