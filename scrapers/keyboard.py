import telebot

def resultKeyboard(url ='', btn=''):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = " الرابط 🔗"
    markup.add(telebot.types.InlineKeyboardButton(text=btn1, url=url))
    return markup


def successKeyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    btn = " تابعني في تلغرام 📢 " 
    markup.add(telebot.types.InlineKeyboardButton(text=btn, url="https://t.me/false10"))
    return markup
