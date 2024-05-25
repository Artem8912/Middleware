import logging
from filters.filters import TrueFilter
from aiogram.types import Message
from aiogram import Router
from filters.filters import TrueFilter
from lexicon.lexicon import LEXICON_RU

other_router = Router()
logger = logging.getLogger(__name__)

@other_router.message(TrueFilter())
async def send_echo(message:Message):
    logger.debug('Вы вошли в эхо-хэндлер')
    
    try:
        await message.send_copy(chat_id=message.from_user.id)
    except TypeError:
        await message.answer(text=LEXICON_RU['no_echo'])
        logger.debug('Вышли из эхо-хэндлера')
