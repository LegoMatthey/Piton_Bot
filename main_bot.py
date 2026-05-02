import telebot
from randompass_func import gen_pass
from coin_giver import givecoin
token = "8646285454:AAHLRqpoZktLC2m2UFM5Mk6_d9-57iFQ1Fg"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Im your nice bot, write something")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['random'])
def send_bye(message):
    bot.reply_to(message, f"Your random password is: {gen_pass(10)}")

@bot.message_handler(commands=['give_coin'])
def send_bye(message):
    bot.reply_to(message, f"Here, have a coin with a value of: {givecoin()}")

@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.send_photo(message.chat.id,'https://mf.b37mrtl.ru/rbthmedia/images/2021.11/article/618e838a15e9f94113006d83.jpg')



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
