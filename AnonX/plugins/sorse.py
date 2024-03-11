
import asyncio

import os
import config
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "arnop"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒅𝒊𝒗 𝒏𝒂𝒅𝒆𝒓 ", url=f"https://t.me/Ng_103"), 
                
                    InlineKeyboardButton(
                        "𝒈𝒓𝒐𝒖𝒑 𖠨", url=f"https://t.me/Ng_333"),
                ],[
                    InlineKeyboardButton(
                        "⌞𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒓𝒏𝒐𝒑 𖠵 ⌝", url=f"https://t.me/N_G_12"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



