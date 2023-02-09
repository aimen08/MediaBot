import telebot

def resultKeyboard(url ='', btn=''):
    markup = telebot.types.InlineKeyboardMarkup()

    btn1 = " الرابط 🔗"
    btn2 = "قناتي 📢"
    markup.add(telebot.types.InlineKeyboardButton(text=btn1, url=url),telebot.types.InlineKeyboardButton(text=btn2, url="https://t.me/false10"))
    return markup