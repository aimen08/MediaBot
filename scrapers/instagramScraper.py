import requests
import json
import cloudscraper
from bs4 import BeautifulSoup
from loguru import logger

scraper = cloudscraper.create_scraper() 

def getInstagramVideo(url):

    try:   
        headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'origin':'https://snapinsta.io',
            'referer':'https://snapinsta.io/en2/instagram-downloader',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': '*/*'
        }
        data = {
            'q': url,
            'vt': 'facebook'
        }
        response = scraper.post('https://snapinsta.io/api/ajaxSearch/instagram',data=data, headers=headers)  
        soup = BeautifulSoup(json.loads(response.text)['data'], 'html.parser')   
        link = soup.findAll('a',attrs={'class':'abutton is-success is-fullwidth btn-premium mt-3'})[0]['href']
        return link

    except Exception as e:
        logger.info(e)
        return {
            'success': False,
            'error': e
        }
        