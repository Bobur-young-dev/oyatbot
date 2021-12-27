from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import requests
def start(update,context):
    text = f'Salom {update.message.from_user.name} <b>Sura</b> va <b>Oyat</b> raqamini ketma-ketlikda jo\'nating:\n1-sura,2-oyat: <b>1,4</b>'
    update.message.reply_html(text)
def search(update,context):
    try:
        if update.message.text=='/creator' or update.message.text=='/developer' or update.message.text=='/dev':
            update.message.reply_html("<b>Developer</b>: @bobur_khamzayev")
        else:
            tafsir = 'uzb-muhammadsodikmu'
            msg = update.message.text.split(',')
            sura = int(msg[0])
            oyat = int(msg[1])
            url_sura = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json'
            url_oyat = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json'
            r = requests.get(url_oyat)
            res=r.json()['text']
            update.message.reply_html(f'<b>{sura}-sura,{oyat}-oyat</b> :\n <i>{res}</i>')
    except:
        update.message.reply_text("Bunday oyat va sura topilmadi!")
updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, search))
updater.start_polling()
updater.idle()
