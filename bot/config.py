token = "1381133523:AAGdwDG81Dp0SRJif2VctkgJuvky7f6fzEQ" # Токен бота из @botfather
admin = 1269750865 # ID администратора бота, можно получить через бота @userinfobot
adminUsername = "@afcydore" # Юзернейм администратора бота
forward_channel_id = 0 # ID канала, в который нужно пересылать сообщения. Если не хотите пересылать сообщения в отдельный канал, оставьте 0. Получить можно через @userinfobot. Не забудьте минус в начале!
secret_key = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjF0cWhvNS0wMCIsInVzZXJfaWQiOiI3OTUzMzc4MDQzMSIsInNlY3JldCI6IjEyY2M2OTQ4MzFiZTc5NGQ5YzYwZDVkOTE3NTU0ODJjYWJiNDgwMDQ1M2UyZjUxODc2ZTUyZGEwMTJkNmVjZmQifX0=" # СЕКРЕТНЫЙ p2p-ключ Qiwi, получается на p2p.qiwi.com
theme_code = "MYLANA-A-Xpf6FuZi" # Код темы, получается на p2p.qiwi.com

startText = """
**Привет!** Добро пожаловать в магазин промокодов Яндекса!
Нажми на одну из кнопок снизу (список можно пролистывать)
"""

startKb = ['🍔 Яндекс.Еда', '🚕 Яндекс.Такси', '🔥 Акции', "🕵️ Реферальная программа", "👨‍💻 Контакты", "ℹ️ Информация"]

foodBtn = "Выберите нужный вам промокод Яндекс.Еды"

foodKb = ["🍔 Промо-код на 1000р", "🍔 Промо-код на 2000р", "🍔 Промо-код на 5000р", "◀️ В главное меню"]

taxiBtn = "Выберите нужный вам промокод Яндекс.Такси"

taxiKb = ["🚕 Промо-код на 2000р", "🚕 Промо-код на 5000р", "◀️ В главное меню"]

goodBtn = "Наличие: **есть!** Нажмите на одну из кнопок снизу"

goodKb = ["💸 Купить", "◀️ В главное меню"]

payBtn = """
➖➖➖➖
<b>Для оплаты перейдите по указанной ссылке:</b>
{0}

💾 Стоимость Вашего заказа составляет <b>{1} рублей!</b>
1️⃣  Обязательно оплатите заказ в течение срока действия ссылки!

3️⃣ После оплаты нажмите кнопку "💎 Я оплатил"👇
Бот автоматически выдаст вам промокод
➖➖➖➖
"""

payKb = ["💎 Я оплатил", "◀️ В главное меню"]

paidBtn = "⏰ Ожидайте, ваш платеж находится в обработке или не найден"

promoactions = """
**Здесь вы увидите все доступные акции, в нашем магазине:**

1. Реферальная система
Как она работает? Всё просто. Вы приглашаете своего знакомого/друга,
через ссылку, которую вам выдаст бот в разделе: "Реферальная программа"
После того, как ваш реферал купит у нас промокод, вы получите скидку 5%
на покупки промокодов в нашем магазине. Чем больше рефералов, тем больше скидка!
Скидка отобразится в разделе "Мой профиль", в пункте: "Ваша скидка"

**2. Купив 10 любых промокодов, вы получите скидку в 100% на следующую покупку.**

**3. Получи скидку за отзыв**
После совершения заказа напишите нам свой отзыв на: {0}
И получите скидку на следующий заказ от 5 до 20% ! Скидка зависит от вашего отзыва.
""".format(adminUsername)

info = """
**Если ты попал в этот раздел, значит тебя заинтерисовала информация по нашему сервису. 🤔**

**Начнём с того, как появляются эти промокоды. 📃**

Сразу хотим подметить, что промокоды получены
абсолютно легальным способом👮🏼‍
Никакого криминала нет, а соответственно и исключены проблемы с их использованием.

У сервиса Яндекс еды и Яндекс такси были акции, благодаря которым можно было получить промокоды.
Сейчас же существует и другой способ, который Вы можете у нас приобрести за **15.000 рублей**. по контактам ниже:

{0} 👤

**Как же их использовать? 💡**
После покупке промокода, допустим на 5000р, перейдите в приложение "Яндекс.Еда" 🍔
Затем приступите к сборке вашего заказа. После того, как вы собрали заказ, перейдите к оплате,
и вставьте купленный вами промокод в поле "Промокод". Это поле находится ниже адреса заказа.
И оплата за ваш заказ составит 0р. 👈

Как использовать промокод на 5000? 💡
Данный промокод делится на 5 частей, по 1000р.
Т.е вы можете его использовать 5 раз, и на каждый ваш заказ будет скидка 1000р. **( Можете сразу сделать 5 заказов )**

Далее переходим к Я.Такси: 🚖

Тут всё намного проще, как оказалось. При покупке промокода на 2000р,перейдите в приложение Я.Такси.
Далее откройте меню, и найдите кнопку "Скидки", далее перейдите по ней.

**Вам высветится 2 предложения:**

**"Ввести промокод" и "Получить скидку", выбирайте 1 вариант, ввод промокода. 💬**

Затем просто вставьте в поле ввода промокода, купленный в нашем магазине промокод. Всё.

В случае с Я.Такси, промокод не будет разбиваться на части, как в Яндекс.Еде, тут **он - одно целое.** 👨‍👩‍👧‍👧
Т.е вы получаете скидку в 2000р на целую поездку, либо много мелких. Как пожелает ваша душа.

**Наши контакты поддержки: {0} 👤**

**Желаем вам вкусно и дешево покушать, и покататься с друзьями в элитном классе такси, за низкую цену. 🍔 🚖**
""".format(adminUsername)

contacts = """
Наши контакты:

📝 Telegram: {0}
""".format(adminUsername)

refBtn = """
<b>Приглашайте новых пользователей и получайте скидки на последующие покупки!</b>
Например: ваш реферал покупает промокод в нашем магазине за 500р, вам моментально приходит скидка в 5% на ваши покупки.
Т.е тот же самый промокод, который он купил за 500р, вам обойдётся в 475р.
Реферальная программа бессрочна, не имеет лимита приглашений и начинает действовать моментально.
Для достижения высоких результатов, внимательно подходите к поиску целевой аудитории: привлекайте только тех,
кто будет покупать промокоды на постоянной основе.

Используйте уникальную реферальную ссылку для приглашения пользователей: https://t.me/YandexSale_bot?start={0}
"""

rejected = "Этот счет уже истек, пройдите процесс покупки заново"

rejectedKb = ["◀️ В главное меню"]

liList = {'startKb': startKb, 'foodKb': foodKb, 'taxiKb': taxiKb, 'goodKb': goodKb, 'payKb': payKb, 'rejectedKb': rejectedKb}

goods = {"food": {"🍔 Промо-код на 1000р": {"price":500, "image":"images/food1000.jpg"},
				  "🍔 Промо-код на 2000р": {"price":1000, "image":"images/food2000.jpg"},
				  "🍔 Промо-код на 5000р": {"price":2400, "image":"images/food5000.jpg"}},
		 "taxi": {"🚕 Промо-код на 2000р": {"price":1000, "image":"images/taxi2000.jpg"},
		 		  "🚕 Промо-код на 5000р": {"price":2400, "image":"images/taxi5000.jpg"}}}