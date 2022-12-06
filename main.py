from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5829023283:AAE4tiD8ry2_sC0D01lRwnJnlyt0YkDzV-c')
updater = Updater(token='5829023283:AAE4tiD8ry2_sC0D01lRwnJnlyt0YkDzV-c')
dispatcher = updater.dispatcher


# def start(update, context):
#    context.bot.send_message(update.effective_chat.id, 'This is Kate_Bot')


# def voice(update, context):
#    context.bot.send_message(update.effective_chat.id,
#                             'Я не умею обрабатывать голосовые сообщения')


def delete_letters(update, context):
    text = update.message.text.split()
    list = []
    for elem in text:
        if 'абв' not in elem:
            list.append(elem)
            context.bot.send_message(update.effective_chat.id, ' '.join(list))


#start_handler = CommandHandler('start', start)
#message_handler = MessageHandler(Filters.voice, voice)
message_handler = MessageHandler(Filters.text, delete_letters)

# dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
