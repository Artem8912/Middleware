from aiogram import Dispatcher,Bot
from aiogram.types import Message,TelegramObject
from config_data.config import Config,load_env
import logging
import asyncio
from handlers.user import user_router
from handlers.other import other_router
from middlewares.inner import FirstInnerMiddleware,SecondInnerMiddleware,ThirdInnerMiddleware

from middlewares.outer import (
    FirstOuterMiddleware,
    SecondOuterMiddleware,
    ThirdOuterMiddleware,
)

from aiogram import Router

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s')

async def main() -> None:
    
    ENV =load_env()
    
    dp = Dispatcher()
    bot = Bot(token=ENV.tg_bot.bot_token)

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_router)
    dp.include_router(other_router)

    # Здесь будем регистрировать миддлвари
    dp.update.outer_middleware(FirstOuterMiddleware())
    
    # Запускаем polling
    await dp.start_polling(bot)


asyncio.run(main())



