from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")

"""
@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")

"""
@router.message()
async def message_handler(msg: Message):
    text = msg.text.lower()

    if text == "привет":
        await msg.answer("Привет!")
    elif text == "как тебя зовут?":
        await msg.answer("Меня зовут Бот. Чем я могу помочь?")
    elif text == "пока":
        await msg.answer("До свидания! Если у вас есть еще вопросы, обращайтесь.")
    elif "id" in text:
        await msg.answer(f"Твой ID: {msg.from_user.id}")
        # Здесь можно вызвать API для получения информации о погоде и отправить ответ
    elif "новости" in text:
        await msg.answer("Сейчас я узнаю для вас последние новости.")
        # Здесь можно вызвать API для получения последних новостей и отправить ответ
    else:
        await msg.answer("Извините, я не могу ответить на этот вопрос.")
"""
@router.message()
async def message_handler(msg: Message):
    if msg.text.lower() == "привет":
        await msg.answer("Привет! Как дела?")
    else:
        await msg.answer("Задай правильный вопрос, я ограничен в ответах")

       
@router.message()
async def message_handler(msg: Message):
    if msg.text.lower() == "мой id":
        await msg.answer(f"Твой ID: {msg.from_user.id}")
    else:
        await msg.answer("Задай правильный вопрос, я ограничен в ответах")

@router.message()
async def message_handler(msg: Message):
    if msg.text.lower() == "как тебя завут":
        await msg.answer("Antoine_Huarez_3_bot")
    else:
        await msg.answer("Задай правильный вопрос, я ограничен в ответах")        """