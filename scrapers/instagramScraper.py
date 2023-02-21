import requests
import json
import cloudscraper

scraper = cloudscraper.create_scraper() 

def getInstagramVideo(url):

    try:   
        headers= {
            'url':url,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'origin': 'https://instavideosave.net',
            'accept': '*/*'
        }

        response = scraper.get('https://api.instavideosave.com/allinone', headers=headers)

        link = json.loads(response.text)["video"][0]["video"]
        return link

    except Exception as e:
        return {
            'success': False,
            'error': e
        }
        

