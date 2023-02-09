import os
import telebot
from dotenv import load_dotenv
from loguru import logger
from scrapers.tikTokScraper import getTikTokVideo
from scrapers.instagramScraper import getInstagramVideo
from scrapers.twitterScraper import getTwitterVideo
from scrapers.snapchatScraper import SnapchatDL
from keyboard import *
import uuid


load_dotenv()

API_KEY= os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY,threaded=True,num_threads=10)
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60



@bot.message_handler(commands=['start'])
def send_mysnap(message):
   
    bot.send_message(message.chat.id,
    """بوت تيليجرام خاص بتحميل فيديوهات من سناب شات و إنستغرام وتيكتوك وتويتر يسمح للمستخدم بتحميل الفيديوهات بطريقة سهلة وسريعة من أشهر تطبيقات التواصل الاجتماعي دون الحاجة إلى تحميل أي تطبيقات إضافية
    
    للمزيد تابعني عبر قناتي https://t.me/false10

    أو عبر حسابي في السناب https://www.snapchat.com/add/rashed
    """) 
    bot.send_message(message.chat.id,
    """
    لتحميل فيديوهات يرجى إدخال الروابط من الشكل التالي 🤖

    <code>/instagram www.instagram.com/reel/xxxxxx</code> 📸

    <code>/twitter twitter.com/i/status/xxxxxxx</code> 🎞️

    <code>/tiktok www.tiktok.com/xxxxx/video/xxxxxxx</code> 🎬

    <code>/snapchat xxxxxxx</code> 🎉
    """,parse_mode="html")

@bot.message_handler(commands=['mychannel'])
def send_mysnap(message):
    bot.send_message(message.chat.id,
    """بوت تيليجرام خاص بتحميل فيديوهات من سناب شات و إنستغرام وتيكتوك وتويتر يسمح للمستخدم بتحميل الفيديوهات بطريقة سهلة وسريعة من أشهر تطبيقات التواصل الاجتماعي دون الحاجة إلى تحميل أي تطبيقات إضافية
    
    للمزيد تابعني عبر قناتي https://t.me/false10

    أو عبر حسابي في السناب https://www.snapchat.com/add/rashed
    """) 

          
@bot.message_handler(commands=['instagram'])
def instagram(message):
    request = message.text.split()
    chatId = message.chat.id
    user = message.chat.username 
    if len(request) == 1 :     
        bot.send_message(chatId, """للتحميل فيديو أو ريل من إنستغرام ضع أمر مع  الرابط بشكل التالي
        \n<code>/instagram www.instagram.com/reel/xxxxxx</code>""",parse_mode="html")
        bot.delete_message(chatId, message.id)
        return 

    url = request[1]
    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] instagram video to user {} started ".format( user ))
    link = getInstagramVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video') 
    bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
    bot.delete_message(chatId, message.id)

    logger.info("[✔] {} instagram video downloaded".format(user))



@bot.message_handler(commands=['twitter'])
def twitter(message):
    request = message.text.split()
    chatId = message.chat.id
    user = message.chat.username 
    if len(request) == 1 :        
        bot.send_message(chatId, """للتحميل فيديو تويتر ضع أمر مع الرابط بشكل التالي
        \n<code>/twitter twitter.com/i/status/xxxxxxx</code>""",parse_mode="html")
        bot.delete_message(chatId, message.id)
        return 

    url = request[1]
    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] twitter video to user {} started ".format( user ))
    link = getTwitterVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video')   
    bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
    bot.delete_message(chatId, message.id)
    logger.info("[✔] {} twitter video downloaded".format(user))


@bot.message_handler(commands=['tiktok'])
def tiktok(message):
    request = message.text.split()
    chatId = message.chat.id
    user = message.chat.username 
    if len(request) == 1 :   
        bot.send_message(chatId, """للتحميل فيديو تيك توك ضع أمر مع الرابط بشكل التالي
        \n<code>/tiktok www.tiktok.com/@wv.1l/video/xxxxxxx</code>""",parse_mode="html")
        bot.delete_message(chatId, message.id)
        return 

    url = request[1]
    bot.send_message(chatId,  "جاري التحميل يرجى إنتظار ⏳")    
    logger.info("[+] tiktok video to user {} started ".format( user ))
    link = getTikTokVideo(url)
    if type(link) is dict:
        bot.send_message(chatId,  "حدث خطأ يرجى التأكد من الرابط ⚠️") 
        return 
    bot.send_chat_action(chatId, 'upload_video') 
    bot.send_video(chatId,link,reply_markup=resultKeyboard(url=url))
    bot.delete_message(chatId, message.id)
    logger.info("[✔] {} tiktok video downloaded".format(user))


@bot.message_handler(commands=['snapchat'])
def snapchat(message):
    request = message.text.split()
    chatId = message.chat.id
    user = message.chat.username 
    if len(request) == 1 :   
        bot.send_message(chatId, """للتحميل سناب شات ستوريس ضع إسم المسخدم بشكل التالي
        \n<code>/snapchat xxxxxxx</code>""",parse_mode="html")
        bot.delete_message(chatId, message.id)
        return 

    snapuser = request[1]
     
    logger.info("[+] snapchat stories to user {} started ".format( user ))
    
    SnapchatDL().download(snapuser, chatId, bot)

    
    bot.delete_message(chatId, message.id)
    logger.info("[✔] {} snapchat stories downloaded".format(user))


@bot.message_handler()
def help(message):
    bot.send_message(message.chat.id,"""
    لتحميل فيديوهات يرجى إدخال الروابط من الشكل التالي 🤖

    <code>/instagram www.instagram.com/reel/xxxxxx</code> 📸

    <code>/twitter twitter.com/i/status/xxxxxxx</code> 🎞️

    <code>/tiktok www.tiktok.com/xxxxx/video/xxxxxxx</code> 🎬

    <code>/snapchat xxxxxxx</code> 🎉
    """,parse_mode="html") 

bot.infinity_polling(allowed_updates=telebot.util.update_types)



