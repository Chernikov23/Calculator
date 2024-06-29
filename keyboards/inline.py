from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyb():
    keyboard = InlineKeyboardBuilder()
    
    buttons = [
        '1', '2', '3', '/',
        '4', '5', '6', 'x',
        '7', '8', '9', '-',
        '0', '.', '=', '+'
    ]
    
    for button in buttons:
        keyboard.button(text=button, callback_data=f"calc:{button}")
    keyboard.adjust(4)
    return keyboard.as_markup()
