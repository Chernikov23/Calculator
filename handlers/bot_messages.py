from aiogram import Router, F, Bot
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline import *
from aiogram.types.audio import Audio


router = Router()

def calculate(expression: str) -> str:
    try:
        expression = expression.replace('x', '*')
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Ошибка: {e}"
    

@router.callback_query(F.data.startswith('calc:'))
async def call_query(callback_query: CallbackQuery):
    expression = callback_query.message.text
    button = callback_query.data.split(':')[1]
    
    if button == '=':
        result = calculate(expression)
        await callback_query.message.edit_text(f"{expression} = {result}", reply_markup=keyb())
    else:
        if ' = ' in expression or expression == '0':
            expression = button
        else:
            expression += button
        await callback_query.message.edit_text(expression, reply_markup=keyb())
    await callback_query.answer()
    
    
    
@router.inline_query()
async def inline_query_handler(query: InlineQuery): 
    expression = query.query or '0'
    result = calculate(expression)
    
    articles = [
        InlineQueryResultArticle(
            id='1',
            title='Result',
            input_message_content=InputTextMessageContent(message_text=f"{expression} = {result}")
        )
    ]
    await query.answer(results=articles, cache_time=1)
