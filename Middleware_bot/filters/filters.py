import logging

from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject



logger = logging.getLogger(__name__)

class TrueFilter(BaseFilter):
    async def __call__(self, event:TelegramObject) -> bool:
        logger.debug('Вы проникли внуть фильтра %s',__class__.__name__)
        return True
class FalseFilter(BaseFilter):
    async def __call__(self,event:TelegramObject)->bool:
        logger.debug('Вы проникли внутрь фильтра %s',__class__.__name__)
        return False
