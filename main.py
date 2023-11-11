from pyrogram import Client, filters
from pyrogram.enums.parse_mode import ParseMode
from config import api_id, api_hash, api_hash_for_gorilla, api_id_for_gorilla, api_hash_for_valeria, api_id_for_valeria
import asyncio
import logging
import time
import asyncio
import threading
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, DateTime, Boolean, ForeignKey,ARRAY
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()



class ChatsForDistribution(Base):
    __tablename__ = 'chats_for_distribution'
    chat_telegram_id = Column(Integer, primary_key=True)

engine = create_engine('sqlite:///mydatabase.db')


Base.metadata.create_all(engine)
# Создаем сессию SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

logging.basicConfig(level=logging.INFO)
app = Client('my_account', api_id=api_id, api_hash=api_hash)

chat_id = 6032759612
ids = set()
async def send_message():
    while True:
        await app.send_message(chat_id, "Ебать зацени рассылку")
        await asyncio.sleep(0.25)

async def process_favorite_messages():
    # Получаем избранные сообщения


    # Проходимся по каждому сообщению
    async for message in app.get_chat_history(chat_id=chat_id):

        id = (f"Text: {message.text.split('id: -')[1].split('Text:')[0]}")
        id = (-int(id.replace('Text: ', '')))
        ids.add(id)


async def process_sergey():

    async for message in app.get_chat_history(chat_id=782266258):
        try:
            id = message.text.split('id: -')[1]
            id = -int(id)
            ids.add(id)
        except:
            'ok'
def get_members_of_chat(chat_id, quantity=50):
    members = []
    with app:
        for message in (app.get_chat_history(chat_id)):
            if len(members)>quantity:
                break
            members.append(message.from_user.id)
        return members

async def distribute_black_cats():

    while True:
        try:
            template = '''
**😩ЗАЕБАЛСЯ СИДЕТЬ БЕЗ ДЕНЕГ?😩

💵💸💲ХОЧЕШЬ ЗАРАБОТАТЬ БЕЗ ВЛОЖЕНИЙ НЕ ВЫХОДЯ ИЗ ДОМА?💲💸💵

ТЕБЕ КО МНЕ😏

🤥🦣САМЫЙ ДЕШЕВЫЙ БОТ ДЛЯ СКАМА МАММОНТОВ🦣🤥

РАБОТАЕТ ПО ВСЕМУ СНГ🇷🇺🇺🇦🇰🇿🇧🇾🇲🇩🇺🇿🇹🇲🇰🇬🇹🇯

БОТ🤖 ВКЛЮЧАЕТ В СЕБЯ АДМИН ПАНЕЛЬ⌨️, ТРЕЙДИНГ БОТА💱💹, ЭСКОРТ БОТА💦🔞 и БОТА ДЛЯ ВЫПЛАТ

УСПЕЙ ЗАКАЗАТЬ ПО СКИДОЧНОЙ ЦЕНЕ**

__1 месяц - 100$
3 месяца - 250$
неограниченное время - 500$

ПИШИ В ЛС⬇__️
||@Karina_PR_manager||
    '''
            await app.send_message(chat_id=-1001348448051, text=template, parse_mode=ParseMode.MARKDOWN)
            await asyncio.sleep(60)
        except Exception as ex:
            print(ex)


async def distribute_other_chats(ids_of_chats):
    messages_sent = 0
    while True:

        template = '''
**📬PACCЫЛKA ВAШEГО ОБЬЯВЛЕНИЯ ПО 700 ЧAТАМ КAЖДУЮ МИНУTУ**

__📚12 часов paccылки - 5$
📚1 День paccылки - 7$
📚3 Дня paccылки - 18$
📚7 Дней paccылки + ПРЕМИУМ(РАССЫЛКА ПО ЛС) - 60$__

``🔔Рекламируем:
🔺Каналы
🔺Объявления о работе
🔺Реферальные ссылки
🔺Боты
🔺Сайты
И многое другое!``

**🔥Огромный приход!
🔥Классное оформление вашего постa, советы от настоящих профи!

🔻По поводу рассылки сюда:**
||@Karina_PR_manager||
    '''
        template = '''
**Привіт, дорогі друзі!**

🌈 Шукаєте незрівнянний спосіб зробити ваше свято незвичайно казковим та незабутнім? Наш Величезний Білий Ведмедик - саме те, що вам потрібно! 🌟

**🐻 20 хвилин за 1300 грн:**

🎵 Музичний супровід
💃 Танці та забави
🤗 Обійми від Ведмедика

**🎉 20 хвилин за 1500 грн:**

🎤 Ведучий для ще більш незабутніх вражень
🎵 Музичний супровід
💃 Танці та забави
🤗 Обійми від Ведмедика
🏡 Велетенський Білий Ведмедик може завітати до вашого будинку, квартири, магазину, кафе чи ресторану, щоб подарувати незабутні хвилини радості.

🎶 Ми також зіграємо пісню на ваш вибір під час привітання. Ви можете вибрати свою улюблену пісню для ще більшого насолодження!

💬 Для отримання додаткової інформації та бронювання зателефонуйте або надішліть особисте повідомлення.

📱 Телефонуйте або пишіть нам на телефон ||+380951385528|| або на наш Instagram: ||charivna_fortetsya|| та Telegram: ||@Fluiitov||

Нехай ваше свято стане справжнім святом радості та сміху з Величезним Білим Ведмедиком! 🌟🐾
        
        '''
        for id_of_chat in ids_of_chats:
            try:
                print(id_of_chat)
                await app.send_message(chat_id=id_of_chat, text=template, parse_mode=ParseMode.MARKDOWN)
                messages_sent += 1
                await asyncio.sleep(300)
                await app.send_message(881704893, f'{messages_sent} Сообщение было отправлено в чат ')

            except Exception as ex:
                print(ex)
                await app.send_message(881704893, f'{ex}')


async def main(ids):
    # Запускаем две асинхронные функции в бесконечном цикле
    await asyncio.gather(distribute_other_chats(ids), distribute_black_cats())

def get_chats_2():
        chats = set()
        with app:
            for message in app.get_chat_history(-1002031389938):
                try:
                    if message.forward_from.id == 850434834 and 'Chat id' not in message.text:

                        chats.add('@'+message.text.split('@')[1].split('\n')[0])
                        print(chats)
                except:
                    'ok'
        return list(chats)
def get_chats():
    with app:
        chats = set()
        for message in app.get_chat_history(-1002031389938):
            try:
                if '@' in message.text:

                    if message.forward_from.id == 6032759612:
                        for strin in message.text.split(' '):
                            if '@' in strin:
                                chats.add(strin.replace('🕑', '').replace('\n',''))
            except:
                'ok'

        chats = list(chats)
        return chats

if __name__ == "__main__":
    with app:
        ids_of_chats = []

        for chat in session.query(ChatsForDistribution).all():
            ids_of_chats.append(chat.chat_telegram_id)

        loop = asyncio.get_event_loop()
        #loop.run_until_complete(get_chats_2())
        loop.run_until_complete(distribute_other_chats(ids_of_chats))
        #loop.run_until_complete(process_sergey())
        # loop.run_until_complete(process_favorite_messages())
        # ids = list(ids)
        #
        # #loop.run_until_complete(main(ids))




