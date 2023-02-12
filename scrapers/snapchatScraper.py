
import json
import time
import re
import requests
from .keyboard import successKeyboard


class APIResponseError(Exception):
    """Invalid API Response"""
    pass


class SnapchatDL:

    def __init__(
        self,   
        limit_story=-1,
        sleep_interval=1,
    ):
        
        self.limit_story = limit_story
        self.sleep_interval = sleep_interval
        self.endpoint_web = "https://story.snapchat.com/@{}"
        self.regexp_web_json = (
            r'<script\s*id="__NEXT_DATA__"\s*type="application\/json">([^<]+)<\/script>'
        )
        self.reaponse_ok = requests.codes.get("ok")

    def _api_response(self, username):
        web_url = self.endpoint_web.format(username)
        return requests.get(web_url).text

    def _web_fetch_story(self, username):

        response = self._api_response(username)
        response_json_raw = re.findall(self.regexp_web_json, response)

        try:
            response_json = json.loads(response_json_raw[0])

            def util_web_user_info(content: dict):
                if "userProfile" in content["props"]["pageProps"]:
                    user_profile = content["props"]["pageProps"]["userProfile"]
                    field_id = user_profile["$case"]
                    return user_profile[field_id]
                else:
                    return None

            def util_web_story(content: dict):
                if "story" in content["props"]["pageProps"]:
                    return content["props"]["pageProps"]["story"]["snapList"]
                return list()

            user_info = util_web_user_info(response_json)
            
            
            stories = util_web_story(response_json)
            return stories, user_info
        except (IndexError, KeyError, ValueError):
            raise APIResponseError

    def download(self, username,chatId,bot):
        try :
            stories, snap_user = self._web_fetch_story(username)
            if snap_user == None:
                bot.send_message(chatId, "المستخدم غير موجود 📪")
                return
        except APIResponseError:
            bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️")
            return
        
       
            
        if len(stories) == 0:
            bot.send_message(chatId, "المستخدم قد لا يكون لديه قصة خلال الـ 24 السابقة \n أو ليس لديه ملف تعريفي عام .")
            return
                
        if self.limit_story > -1:
            stories = stories[0 : self.limit_story]
        bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")   

        for media in stories:
            
            media_url = media["snapUrls"]["mediaUrl"]
            try:
                bot.send_video(chatId,media_url)
                time.sleep(0.1)
            except :
                bot.send_message(chatId, "هذا الحساب ليس لديه ملف تعريفي عام 👻")                    
                return 
        bot.send_message(chatId, "تم التحميل بنجاح ✅",reply_markup=successKeyboard())
