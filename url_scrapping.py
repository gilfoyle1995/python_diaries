import urllib
import bs4 as bs

def getWashPostText(url , token):
    '''
    input : url is the http address
            token the tag to be searched
    output: a tuple with paragraph , title
    
    '''
    try:
        page = urllib.request.urlopen(url).read().decode('utf8')
    except:
        return (None , None)

    soup = bs.BeautifulSoup(page , "lxml")
    if soup is None:
        return (None , None)
    
    text = ""

    if soup.find_all(token) is not None:
        text = ''.join(map(lambda p: p.text , soup.find_all(token)))
        soup2 = bs.BeautifulSoup(text)
        if soup2.find_all('p') is not None:
            text = ''.join(map(lambda p: p.text , soup2.find_all('p')))

    return (text , soup.title.text)






        
