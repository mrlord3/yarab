import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("cr")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس cr \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓 ", url=f"https://t.me/Ng_103"),
                    InlineKeyboardButton(
                        "𝒅𝒊𝒗 𝒎𝒂𝒉𝒎𝒐𝒅 ", url=f"https://t.me/FM_3omda"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑  ⌝⚡", url=f"https://t.me/N_G_12"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓 ", url=f"https://t.me/Ng_103"),
             InlineKeyboardButton("𝒅𝒊𝒗 𝒎𝒂𝒉𝒎𝒐𝒅 ", url=f"https://t.me/FM_3omda")],
            [InlineKeyboardButton("★⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 ⌝⚡", url=f"https://t.me/N_G_12")],
        ]
    ))

