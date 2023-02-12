import requests
from bs4 import BeautifulSoup




def extract_video_id_from_url(url):
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )

def getToken(url):
    try:
        
        response = requests.post('https://musicaldown.com/')    
        cookies = response.cookies
        soup = BeautifulSoup(response.content, 'html.parser').find_all('input')

        data = {
            soup[0].get('name'):url,
            soup[1].get('name'):soup[1].get('value'),
            soup[2].get('name'):soup[2].get('value')
        }
        
        return True, cookies, data
    
    except Exception:
        return None, None, None

def getTikTokVideo(url):

       
    status, cookies, data = getToken(url)
    if status:
        headers = {
            'Cookie': f"session_data={cookies['session_data']}",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '96',
            'Origin': 'https://musicaldown.com',
            'Referer': 'https://musicaldown.com/en/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Te': 'trailers'
        }
        
        try:
            response = requests.post('https://musicaldown.com/download', data=data, headers=headers, allow_redirects=False)              
            soup = BeautifulSoup(response.content, 'html.parser')                   
            link = soup.findAll('a',attrs={'class':'btn waves-effect waves-light orange'})[1]['href']
            return link

        except Exception as e:
            return {
                'success': False,
                'error': e
            }  
    else:
        return {
                    'success': False,
                    'error': 'exception'
                }


gg = getTikTokVideo("https://www.tiktok.com/@wv.1l/video/7180771695194672386?is_from_webapp=1&sender_device=pc")
