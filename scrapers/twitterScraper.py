import requests
from bs4 import BeautifulSoup




def getTwitterVideo(url):
   
    data = {
        "url":url,
    }
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '96',
        'Origin': 'https://twittermate.com/',
        'Referer': 'https://twittermate.com/en/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers'
    }

    try:
        response = requests.post('https://twittermate.com/download.php', data=data, headers=headers, allow_redirects=False)                      
        soup = BeautifulSoup(response.content, 'html.parser')                  
        link = soup.findAll('a',attrs={'class':'btn waves-effect waves-light light-blue darken-4'})[4]['href']
        return link

    except Exception as e:
        return {
            'success': False,
            'error': e
        }

