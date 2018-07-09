#! python3

import requests,re,cfscrape,webbrowser,time

NUMBERS = '0123456789'

def increment(s,x):     #This function changes the episode number and id present in the link
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

def LoadNewEP(BaseUrl,Epinum):     #This function loads a new episode by searching for the video source in the html source file. This is easily available for RapidVideo
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
    print('****'+str(Epinum) +' is loaded on chrome****\n')

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
    print(urlnums)
    BaseUrl = increment(BaseUrl,Epinum-int(urlnums[0]))
    LoadNewEP(BaseUrl,Epinum)
    Epinum = Epinum +1
    numberOfEpi = numberOfEpi - 1
    time.sleep(1200)
