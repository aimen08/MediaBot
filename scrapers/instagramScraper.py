import requests
import js2py
import json


instagramDomains = (
    'https://www.instagram.com',
    'https://instagram.com'
)


def getInstagramVideo(url):
    if not url.startswith('http'):
        url = 'https://' + url

    if url.lower().startswith(instagramDomains):
        url = url.split('?')[0]  

        try:
            
            headers= {
                'url':url,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'origin': 'https://instavideosave.net',
                'accept': '*/*'
            }

            response = requests.get('https://api.instavideosave.com/allinone', headers=headers, allow_redirects=True)

            link = json.loads(response.content.decode('unicode_escape'))["video"][0]["video"]
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

    else:
        return {
                    'success': False,
                    'error': 'invalidUrl'
                }
