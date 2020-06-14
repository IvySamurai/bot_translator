from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import Updater

from crawler import Crawler
from config import TOKEN


class Bot:
    def send_message(self, update: Update, context: CallbackContext):
        """ Send messages to user """
        word = update.message.text
        translation = Crawler().get_translation(word)
        update.message.reply_text(
            text=translation
        )

    def start(self):
        """ Launches a bot """
        updater = Updater(
            token=TOKEN,
            use_context=True
        )

        updater.dispatcher.add_handler(
            MessageHandler(
                filters=Filters.text,
                callback=self.send_message
            )
        )

        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    Bot().start()