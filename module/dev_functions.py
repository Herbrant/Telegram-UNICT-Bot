import yaml
import telegram
from telegram import Update
from telegram.ext import CallbackContext

with open('config/settings.yaml', 'r') as yaml_config:
    config_map = yaml.load(yaml_config, Loader=yaml.SafeLoader)

def logging_message(update: Update, context: CallbackContext):
	try:
		message_id = update.message.message_id #ID MESSAGGI\O
		user = update.message.from_user # Restituisce un oggetto Telegram.User
		chat = update.message.chat # Restituisce un oggetto Telegram.Chat
		text = update.message.text #Restituisce il testo del messaggio
		date = update.message.date #Restituisce la data dell'invio del messaggio
		message = "\n___ID MESSAGE: " 	+ str(message_id) + "____\n" + \
					"___INFO USER___\n" + \
					"user_id:" 			+ str(user.id) + "\n" + \
					"user_name:" 			+ str(user.username) + "\n" + \
					"user_firstlastname:" + str(user.first_name) + " " + str(user.last_name) + "\n" + \
					"___INFO CHAT___\n" + \
					"chat_id:" 			+ str(chat.id) + "\n" + \
					"chat_type:" 			+ str(chat.type)+"\n" + "chat_title:" + str(chat.title) + "\n" + \
					"___TESTO___\n" + \
					"text:" 				+ str(text) + \
					"date:" 				+ str(date) + \
					"\n_____________\n"

		log_tmp = open("logs/logs.txt","a+")
		log_tmp.write("\n"+message)
	except:
		pass

# Devs Commands
def give_chat_id(update:Update, context:CallbackContext):
    update.message.reply_text(str(update.message.chat_id))

def send_log(update:Update, context:CallbackContext):
    if(config_map['dev_group_chatid'] != 0 and update.message.chat_id == config_map['dev_group_chatid']):
        context.bot.sendDocument(chat_id=config_map['dev_group_chatid'], document=open('logs/logs.txt', 'rb'))

def send_errors(update: Update, context: CallbackContext):
    if(config_map['dev_group_chatid'] != 0 and update.message.chat_id == config_map['dev_group_chatid']):
        context.bot.sendDocument(chat_id=config_map['dev_group_chatid'], document=open('logs/errors.txt', 'rb'))
