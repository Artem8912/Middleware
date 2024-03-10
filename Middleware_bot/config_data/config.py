from environs import Env
from dataclasses import dataclass

@dataclass
class Tg_bot:
    bot_token:int

@dataclass
class Config:
    tg_bot:Tg_bot

def load_env()->Config:
    env=Env()
    env.read_env()
    return Config(tg_bot=Tg_bot(bot_token=env('BOT_TOKEN')))

    