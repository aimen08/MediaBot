import requests
import json
import cloudscraper
from bs4 import BeautifulSoup


scraper = cloudscraper.create_scraper() 

def getInstagramVideo(url):

    try:   
        headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'origin':'https://instaoffline.net',
            'referer':'https://instaoffline.net/video-downloader/',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': '*/*'
        }
        data = {
            'q': url,
            'downloader': 'video'
        }
        response = scraper.post('https://instaoffline.net/process/',data=data, headers=headers)
       
        soup = BeautifulSoup(json.loads(response.text)['html'], 'html.parser')    
        link = soup.findAll('a',attrs={'class':'button'})[0]['href']
        return link

    except Exception as e:
        return {
            'success': False,
            'error': e
        }
        
