import os
import telebot
from dotenv import load_dotenv
from loguru import logger
from scrapers.tikTokScraper import getTikTokVideo
from scrapers.instagramScraper import getInstagramVideo
from scrapers.twitterScraper import getTwitterVideo
from scrapers.snapchatScraper import SnapchatDL
from scrapers.keyboard import *
import uuid


load_dotenv()

API_KEY= os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY,threaded=True,num_threads=10)
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60

instagramDomains = (
    'https://www.instagram.com',
    'https://instagram.com'
)
tikTokDomains = (
    'http://vt.tiktok.com', 'http://app-va.tiktokv.com', 'http://vm.tiktok.com', 'http://m.tiktok.com', 'http://tiktok.com', 'http://www.tiktok.com', 'http://link.e.tiktok.com', 'http://us.tiktok.com',
    'https://vt.tiktok.com', 'https://app-va.tiktokv.com', 'https://vm.tiktok.com', 'https://m.tiktok.com', 'https://tiktok.com', 'https://www.tiktok.com', 'https://link.e.tiktok.com', 'https://us.tiktok.com',
)
twitterDomains = (
    'https://twitter.com', 
)


@bot.message_handler(commands=['start','mychannel'])
def start(message):
   
    bot.send_message(message.chat.id,
    """بوت تيليجرام خاص بتحميل فيديوهات من سناب شات و إنستغرام وتيكتوك وتويتر يسمح للمستخدم بتحميل الفيديوهات بطريقة سهلة وسريعة من أشهر تطبيقات التواصل الاجتماعي دون الحاجة إلى تحميل أي تطبيقات إضافية
    
    للمزيد تابعني عبر قناتي https://t.me/false10

    أو عبر حسابي في السناب https://www.snapchat.com/add/rashed
    """) 

@bot.message_handler(commands=['instagram','twitter','tiktok'])
def send_mysnap(message):
    bot.send_message(message.chat.id, "الرجاء إدخال رابط الفيديو 🎬")

@bot.message_handler(commands=['snapchat'])
def send_mysnap(message):
    bot.send_message(message.chat.id, "الرجاء إدخال إسم المستخدم 👻")


@bot.message_handler()
def prompt(message):
    chatId = message.chat.id
    user = message.chat.username 
    url = message.text.split()
    messageID = message.id
    if len(url) > 1 :
        bot.send_message(message.chat.id, "الرجاء التأكد من الرابط 🔗")
        return 
    url = url[0]
    if url.lower().startswith(instagramDomains):
        if not url.startswith('http'):
            url = 'https://' + url
        url = url.split('?')[0]
        instagram(chatId,user,url,messageID)
        return

    if url.lower().startswith(tikTokDomains):
        if not url.startswith('http'):
            url = 'https://' + url
        url = url.split('?')[0]
        tiktok(chatId, user, url,messageID)
        return
    
    if url.lower().startswith(twitterDomains):
        if not url.startswith('http'):
            url = 'https://' + url
        url = url.split('?')[0]
        twitter(chatId, user, url,messageID)
        return
    
    snapchat(chatId, user, url,messageID)

          

def instagram(chatId,user,url,messageID):

    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] instagram video to user {} started ".format( user ))
    link = getInstagramVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video') 
    bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
    bot.delete_message(chatId, messageID)

    logger.info("[✔] {} instagram video downloaded".format(user))
    bot.send_message(chatId, "تم التحميل بنجاح ✅",reply_markup=successKeyboard())



def tiktok(chatId,user,url,messageID):
 
    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] tiktok video to user {} started ".format( user ))
    link = getTikTokVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video') 
    try :
        bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
        bot.delete_message(chatId, messageID)
        logger.info("[✔] {} tiktok video downloaded".format(user))
        bot.send_message(chatId, "تم التحميل بنجاح ✅",reply_markup=successKeyboard())
    except: 
        bot.send_message(chatId,  "الفيديو كبير التيلغرام لا يسمح بتنزيله ⚠️") 



def twitter(chatId,user,url,messageID):

    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] twitter video to user {} started ".format( user ))
    link = getTwitterVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video')   
    bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
    bot.delete_message(chatId, messageID)
    logger.info("[✔] {} twitter video downloaded".format(user))
    bot.send_message(chatId, "تم التحميل بنجاح ✅",reply_markup=successKeyboard())



def snapchat(chatId,user,snapuser,messageID): 
    logger.info("[+] snapchat stories to user {} started ".format( user ))
    SnapchatDL().download(snapuser, chatId, bot)
    bot.delete_message(chatId, messageID)
    logger.info("[✔] {} snapchat stories downloaded".format(user))




bot.infinity_polling(allowed_updates=telebot.util.update_types)



