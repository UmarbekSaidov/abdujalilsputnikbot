from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import aiogram
from aiogram import Bot, types

b = Bot(token="5195439454:AAHzvSqBV5yfOT04UJubt5InF0H0FvcW8DI")
bot = Dispatcher(b)

@bot.message_handler(commands="start")
async def start(message):
    await message.reply(f'Salom <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b> men ishlayabman😉\n\n /help buyrug\'idan foydalanishingiz mumkin!', parse_mode='HTML')


@bot.message_handler(commands="author")
async def author(message):
    await message.reply('Meni kodimni <a href="tg://user?id=738052033">Asadbek</a> yozgan', parse_mode='HTML')


@bot.message_handler(commands="help")
async def help(message):
    await message.reply("<b>Mavjud buyruqlar:</b> \n\n /start - Botni qaytadan ishga tushirish \n /author - Bot kodini yozgan muallif haqida malumot \n /feedback - Bot bilan bog\'liq muammo chiqsa bog\'lanish uchun \n /help - Bot bo\'yicha yordam kerak bo\'lsa", parse_mode='HTML')


@bot.message_handler(commands="feedback")
async def feedback(message):
    await message.reply("Yordam kerak bo'lsa @AbdujalilQobulov ga yozing ")

@bot.channel_post_handler(content_types=["text"])
async def podpis(message):
    if message.chat.type == 'channel':
        t = message.text
        await message.edit_text(f'{t}\n\n👉 @uz_sputnik тезкор янгликлар', parse_mode='HTML', disable_web_page_preview=True)


@bot.channel_post_handler(content_types=["photo", "video", "animation", "voice", "audio", "document"])
async def photopodpis(message):
    if message.chat.type == 'channel':
        if message.caption is not None:
            await message.edit_caption(f'{message.caption}\n\n👉 @uz_sputnik тезкор янгликлар', parse_mode='HTML')
        else:
            await message.edit_caption(f'\n\n👉 @uz_sputnik тезкор янгликлар', parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)
