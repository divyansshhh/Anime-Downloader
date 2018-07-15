#! python3

import requests, bs4,re, cfscrape, webbrowser,time

NUMBERS = '0123456789'

def increment(s,x):
    out = ''

    number = ''
    for c in s:
        if c in NUMBERS:
            number += c
        else:
            if number != '':
                out += str(int(number) + x)
                number = ''
            out += c

    if number != '':
        out += str(int(number) + x)
        number = ''

    return out

def LoadNewEP(BaseUrl,Epinum):
    print('New url is:')
    print(BaseUrl)
    print('Please wait while we look for episode #' +  str(Epinum))
    scraper = cfscrape.create_scraper()
    res = scraper.get(BaseUrl)
    print('Loading....')
    pageCode = str(res.content)
    SiteTemp = 'https://www.rapidvideo.com'
    pos = pageCode.find(SiteTemp)
    length = 0
    while pageCode[pos+length] != '"':
            length = length+1
    StreamUrl = pageCode[pos:pos+length]
    print('Video streaming from:'+ StreamUrl)
    webbrowser.open(StreamUrl)
    print('****'+str(Epinum) +' is loaded on chrome****')

print('DC-ANIME')

print('Enter base url of the show:')
BaseUrl = input()

print('Enter the number of episodes you want to watch:')
numberOfEpi = int(input())

print('Enter the starting episode: ')
Epinum = int(input())

while numberOfEpi > 0:
    urlnums = re.findall(r'\d+', BaseUrl)
    urlnums = [int(i) for i in urlnums]
    urlnums.sort()
    cnt=0
    i=0
    while cnt < 5:
        if BaseUrl[i] == '/':
            cnt= cnt+1
        i=i+1
    x = BaseUrl[i:]
    print(urlnums)
    x = increment(x,Epinum-int(urlnums[0]))
    BaseUrl = BaseUrl[:i]+x
    print(BaseUrl)
    LoadNewEP(BaseUrl,Epinum)
    Epinum = Epinum +1
    numberOfEpi = numberOfEpi - 1
    #time.sleep(1200)
