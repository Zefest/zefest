import telebot
import string
import random
import datetime
import requests
import json
from decimal import Decimal
import sqlite3
from config import *

bot = telebot.TeleBot(token)
print("bot initialized!")

def getValuesFromDB(cmd, arg):
	db = sqlite3.connect("bot.db")
	c = db.cursor()
	c.execute(cmd, arg)
	result = c.fetchall()
	c.close()
	return result

def setValuesToDB(cmd, arg):
	db = sqlite3.connect("bot.db")
	c = db.cursor()
	c.execute(cmd, arg)
	db.commit()
	c.close()
	return True

def getUsers():
	users = getValuesFromDB('SELECT * FROM users', tuple())
	return users

def getUser(userid):
	user = getValuesFromDB('SELECT * FROM users WHERE userid = ?', (userid,))
	try: 
		user = user[0]
		return user
	except IndexError: return False

def makeUser(userid):
	timestamp = int(datetime.datetime.utcnow().timestamp())
	setValuesToDB('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', (userid, 'register', timestamp, 0, 0, 0))

def getBillId(userid):
	return getValuesFromDB('SELECT billid FROM users WHERE userid = ?', (userid,))[0][0]

def setBillId(userid, billid):
	setValuesToDB('UPDATE users SET billid = ? WHERE userid = ?', (billid, userid))

def setGoodPrice(userid, goodprice):
	setValuesToDB('UPDATE users SET goodprice = ? WHERE userid = ?', (goodprice, userid))

def getGoodPrice(userid):
	return getValuesFromDB('SELECT goodprice FROM users WHERE userid = ?', (userid,))[0][0]

def getStats(time):
	timedict = {"час": 60*60, "день": 60*60*24, "неделя": 60*60*24*7, "месяц": 60*60*24*31}
	timestamp = int(datetime.datetime.utcnow().timestamp()) - timedict[time]
	registered = getValuesFromDB('SELECT * FROM users WHERE timestamp > ?', (timestamp,))
	return len(registered)

def setLastStep(userid, step):
	setValuesToDB('UPDATE users SET laststep = ? WHERE userid = ?', (step, userid))

def getLastStep(userid):
	return getValuesFromDB('SELECT laststep FROM users WHERE userid = ?', (userid,))[0][0]

def setLoh(userid, loh):
	setValuesToDB('UPDATE users SET loh = ? WHERE userid = ?', (loh, userid))

def getLoh(userid):
	return getValuesFromDB('SELECT loh FROM users WHERE userid = ?', (userid,))[0][0]

def createKb(rows):
	kb = telebot.types.ReplyKeyboardMarkup(True)
	for row in rows:
		kb.row(row)
	return kb

kbList = {}
for key, value in liList.items():
	kbList[key] = createKb(value)

def makeInvoice(amount):
	billId = random.randrange(1, 10000000000000000)
	dateNow = datetime.datetime.now() + datetime.timedelta(hours=3)
	expirationDateTime = dateNow.strftime('%Y-%m-%dT%H:%M:%S+03:00')
	amount = str(round(Decimal(float(amount)), 2)) #прости меня, господи
	data = {"amount": {"currency": "RUB", "value": amount}, "comment": "Оплата товара", "expirationDateTime": expirationDateTime, "customFields": {"themeCode": theme_code}}
	headers = {"Authorization": "Bearer " + secret_key, "Accept": "application/json", "Content-Type": "application/json"}
	req = requests.put("https://api.qiwi.com/partner/bill/v1/bills/{0}".format(str(billId)), data=json.dumps(data), headers = headers)
	if req.status_code == 200:
		req = req.json()
		return (req["payUrl"], req["billId"])
	if req.status_code == 500:
		return "NOPE"
	else:
		bot.send_message(admin, 'Увага! Ошибка при создании счета! Код запроса: {0}'.format(req.status_code))

def checkInvoice(billId):
	headers = {"Authorization": "Bearer " + secret_key, "Accept": "application/json", "Content-Type": "application/json"}
	req = requests.get("https://api.qiwi.com/partner/bill/v1/bills/{0}".format(billId), headers = headers)
	if req.status_code == 200:
		req = req.json()
		return req["status"]["value"]
	else:
		bot.send_message(admin, 'Увага! Ошибка при проверке счета! Код запроса: {0}'.format(req.status_code))

print("everything loaded!")

@bot.message_handler(commands=['mass_send'])
def mass_send(message):
    if message.from_user.id == admin:
        for user in getUsers():
            try: bot.send_message(user[0], message.text.replace('/mass_send ', ''))
            except: pass
        bot.send_message(admin, "Рассылка законечена")

@bot.message_handler(commands=['stats'])
def stats(message):
	if not message.from_user.id == admin:
		return
	arg = message.text.lower().replace('/stats ', '')
	if arg not in ["час", "месяц", "день", "неделя"]:
		bot.send_message(message.chat.id, "Неправильный аргумент команды")
		return
	count = getregistered(arg)
	bot.send_message(message.chat.id, "К-во зарегистрированных за выбранный промежуток времени: {0}".format(str(count)))


@bot.message_handler(commands=['start'])
def start(message):
	if not getUser(message.from_user.id):
		makeUser(message.from_user.id)
		print("registered user {0}".format(str(message.from_user.id)))
	bot.send_message(message.from_user.id, startText, parse_mode="markdown", reply_markup = kbList["startKb"])
	setLastStep(message.from_user.id, 'start')
	setLoh(message.from_user.id, 0)
	print("got start msg from id {0}".format(str(message.from_user.id)))

@bot.message_handler(content_types=['text'])
def send_text(message):
	if forward_channel_id: bot.forward_message(forward_channel_id, message.from_user.id, message.message_id)
	text = message.text
	if text == "◀️ В главное меню":
		start(message)
		return
	if text == "🍔 Яндекс.Еда":
		bot.send_message(message.from_user.id, foodBtn, parse_mode="markdown", reply_markup = kbList["foodKb"])
		setLastStep(message.from_user.id, 'food')
		return
	if text == "🚕 Яндекс.Такси":
		bot.send_message(message.from_user.id, taxiBtn, parse_mode="markdown", reply_markup = kbList["taxiKb"])
		setLastStep(message.from_user.id, 'taxi')
		return
	if text == "🔥 Акции":
		bot.send_message(message.from_user.id, promoactions, parse_mode="markdown")
		setLastStep(message.from_user.id, 'actions')
		return
	if text == "ℹ️ Информация":
		bot.send_message(message.from_user.id, info, parse_mode="markdown")
		setLastStep(message.from_user.id, 'info')
		return
	if text == "🕵️ Реферальная программа":
		bot.send_message(message.from_user.id, refBtn.format(message.from_user.id), parse_mode="HTML")
		setLastStep(message.from_user.id, 'ref')
		return
	if text == "👨‍💻 Контакты":
		bot.send_message(message.from_user.id, contacts, parse_mode="markdown")
		setLastStep(message.from_user.id, 'contacts')
		return
	laststep = getLastStep(message.from_user.id)
	if laststep in goods:
		if message.text in goods[laststep]:
			good = goods[laststep][message.text]
			setGoodPrice(message.from_user.id, good['price'])
			photo = open(good['image'], 'rb')
			bot.send_photo(message.from_user.id, photo)
			bot.send_message(message.from_user.id, goodBtn, parse_mode="markdown", reply_markup=kbList["goodKb"])
			setLastStep(message.from_user.id, 'good')
			return
	if laststep == "good" and text == "💸 Купить":
		goodPrice = getGoodPrice(message.from_user.id)
		invoice = makeInvoice(goodPrice)
		if invoice == "NOPE":
			bot.send_message(message.from_user.id, "Произошла ошибка при создании счета, попробуйте позже")
			return
		setBillId(message.from_user.id, invoice[1])
		payText = payBtn.format(invoice[0], goodPrice)
		bot.send_message(message.from_user.id, payText, parse_mode="HTML", reply_markup=kbList["payKb"])
		setLastStep(message.from_user.id, 'buy')
		return
	if laststep == "buy" and text == "💎 Я оплатил":
		if getLoh(message.from_user.id) == 1: pass
		else:
			billId = getBillId(message.from_user.id)
			checked = checkInvoice(billId)
			if checked in ["EXPIRED",'REJECTED']:
				bot.send_message(message.from_user.id, rejected, parse_mode="markdown", reply_markup=kbList["rejectedKb"])
				return
			elif checked == "PAID":
				setLoh(message.from_user.id, 1)
				bot.send_message(admin, "Лох оплатил! Сумма: {0} Айди лоха: {1}".format(getGoodPrice(message.from_user.id), message.from_user.id))
		bot.send_message(message.from_user.id, paidBtn, parse_mode="markdown")
		return



try:
	bot.polling()
except Exception as exc:
	bot.send_message(admin, "ВНИМАНИЕ!!! Бот упал, произошла ошибка! Тип ошибки: {0} Текст ошибки: {1}".format(str(type(exc)), str(exc)))