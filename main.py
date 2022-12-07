
from loging import *
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from controller import parse_data, calculate


bot = Bot(token='5829023283:AAE4tiD8ry2_sC0D01lRwnJnlyt0YkDzV-c')
updater = Updater(token='5829023283:AAE4tiD8ry2_sC0D01lRwnJnlyt0YkDzV-c')
dispatcher = updater.dispatcher

start_calculate = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Hi i ll calculate for you')
    context.bot.send_message(
        update.effective_chat.id, 'Hi i ll calculate for you, can do: +,-,*,/. Press /end once done')

    get_user_id(update.effective_chat.id)
    return start_calculate


def receive_data(update, context):
    data = update.message.text
    get_input_data(data)
    list_data = parse_data(data)
    result = calculate(list_data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id,
                             f'calculated results:{result}')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'see ya')
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(
    Filters.text & (~Filters.command), receive_data)

mes_data_handler = CommandHandler('end', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler], states={
                                   start_calculate: [receiving_data_handler]}, fallbacks=[mes_data_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
