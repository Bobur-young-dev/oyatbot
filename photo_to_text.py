from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext,CallbackQueryHandler, MessageHandler, Filters


import pytesseract 
from PIL import Image

def start(update,context):
    
    update.message.reply_text("Send photo: ")
def search(update,context):
    
    msg = update.message.photo[-1].get_file()
    msg.download("user.jpg")
    
    try:
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
        img = Image.open('user.jpg')
        text = pytesseract.image_to_string(img)
    
   
        update.message.reply_text(text)
    except:
        update.message.reply_text("Sorry, I can not detect any text")
    
    


updater = Updater('1722542460:AAGGMLZ2kTGrH95_CjqNzY5HPsJDJR9VhZI')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo,search))
updater.start_polling()
updater.idle()