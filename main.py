import time

import telebot

from tools import printer

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

hi_command = 'hi'
time_command = 'time'
help_command = 'help'
sum_command = 'sum'

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand(hi_command, "приветствие"),
        telebot.types.BotCommand(time_command, "показать время"),
        telebot.types.BotCommand(help_command, "помощь"),
        telebot.types.BotCommand(sum_command, "просуммировать"),
    ],
    scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)



@bot.message_handler(commands=['hi'])
def hi_command(message):
    print(message.from_user.id)
    bot.reply_to(message, f"""\
hi, {message.from_user.username}\
""")


@bot.message_handler(commands=['help'])
def hi_command(message):
    print(message)
    bot.reply_to(message, f"""\
/hi\n/help\n/time\n/sum\
""")


@bot.message_handler(commands=['time'])
def hi_command(message):
    print(message)
    bot.reply_to(message, f"""\
{time.time()}
""")


@bot.message_handler(commands=['sum'])
def hi_command(message):
    print(message)
    bot.reply_to(message, f"""\
not implemented(((
""")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# здесь обрабатываются все текстовые сообщения от человека к боту
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'hello')
    printer(message)


bot.infinity_polling()
