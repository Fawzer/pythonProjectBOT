import telebot

bot = telebot.TeleBot("5562936941:AAHDpv7M92fSNk-XwR2gVGmUnteqrbVN2v8")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Hello, I'm a Fawzer bot if you want to know what this bot can do, then write "
                                      "the command [ /help ]</b>", parse_mode="html")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "<b>This bot provides access to all my networks"
                                      "To provide you with links to my networks, write a command [ /give ]</b>",
                     parse_mode="html")


@bot.message_handler(commands=['give'])
def give(message):
    bot.send_message(message.chat.id, "<b>Telegram chat link - t.me/+v5ax5E1d-t1hMjRi \n VK account link - vk.com/violente1</b>", parse_mode="html")


bot.polling(none_stop=True)
