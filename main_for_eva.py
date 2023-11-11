from pyrogram import Client, filters
from pyrogram.enums.parse_mode import ParseMode
from config import api_id, api_hash, api_hash_for_gorilla, api_id_for_gorilla, api_hash_for_valeria, api_id_for_valeria, api_hash_for_usa1, api_id_for_usa1
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
app = Client('my_account_eva', api_id=api_id_for_usa1, api_hash=api_hash_for_usa1)


async def distribute_other_chats(ids_of_chats):
    with app:
        messages_sent = 0
        while True:

            template = '''
    Привіт, дорогі друзі!
    
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
    
    📱 Телефонуйте або пишіть нам на телефон ||**+380951385528**|| або на наш Instagram: ||**charivna_fortetsya**||.
    
    Нехай ваше свято стане справжнім святом радості та сміху з Величезним Білим Ведмедиком! 🌟🐾
        '''
            for id_of_chat in ids_of_chats:
                try:
                    print(id_of_chat)
                    await app.send_message(chat_id=id_of_chat, text=template, parse_mode=ParseMode.MARKDOWN)
                    messages_sent += 1

                    await app.send_message(881704893, f'{messages_sent} Сообщение было отправлено в чат ')
                except Exception as ex:
                    print(ex)
                await asyncio.sleep(300)


if __name__ == '__main__':
    with app:
        ''
        # ids_of_chats = []
        #
        # for chat in session.query(ChatsForDistribution).all():
        #     ids_of_chats.append(chat.chat_telegram_id)
        #
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(distribute_other_chats(ids_of_chats))