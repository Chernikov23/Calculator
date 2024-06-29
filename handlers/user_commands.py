from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline import *

router = Router()
@router.message(CommandStart())
async def start(msg: Message):
    
    
    await msg.answer("0", reply_markup=keyb())
