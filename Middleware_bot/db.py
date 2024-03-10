# db:dict[int:str] = {}
# db[0] = 'ноль'
# db[1] = 'один'
# print(db)

# a:list[int] = [['0'],[1]]
# print(a)

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware,Dispatcher
from aiogram.types import TelegramObject, User
dp = Dispatcher
CACHE = {
    'banned': [254443334, 214454432, 112221212],
}


class ShadowBanMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        user: User = data.get('event_from_user')
        if user is not None:
            if user.id in CACHE.get('banned'):
                return

        return await handler(event, data)
# А подключение миддлвари происходит уже знакомым нам образом:

dp.update.middleware(ShadowBanMiddleware())

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from cachetools import TTLCache

CACHE = TTLCache(maxsize=10_000, ttl=5)  # Максимальный размер кэша - 10000 ключей, а время жизни ключа - 5 секунд

class ThrottlingMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')
        
        if user.id in CACHE:
            return

        CACHE[user.id] = True

        return await handler(event, data)