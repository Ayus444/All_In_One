import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import logging
from pyrogram import Client, filters
from subprocess import getstatusoutput
import re
from pyrogram.types import User, Message
import os

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg",
    caption = "**Hi i am All in One Extractor Bot**.\n"
                            "Press **/pw** for **Physics Wallah**..\n\n"
                            "Press **/e1** for **E1 Coaching App**..\n\n"
                            "Press **/vidya** for **Vidya Bihar App**..\n\n"
                            "Press **/ocean** for **Ocean Gurukul App**..\n\n"
                            "Press **/winners** for **The Winners Institute**..\n\n"
                            "Press **/rgvikramjeet** for **Rgvikramjeet App**..\n\n"
                            "Press **/txt** for  **Ankit With Rojgar,**\n**The Mission Institute,**\n**The Last Exam App**..\n\n"
                            "Press **/cp** for **classplus appp**..\n\n"
                            "Press **/cw** for **careerwill app**..\n\n"
                            "Press **/khan** for **Khan Gs app**..\n\n"
                            "Press **/exampur** for ** Exampur app**..\n\n"
                            "Press **/samyak** for ** Samayak Ias**..\n\n"
                            "Press **/chandra** for ** Chandra app**..\n\n"
                            "Press **/mgconcept** for **Mgconcept app**..\n\n"
                            "Press **/down** for **For Downloading Url lists**..\n\n"
                            "Press **/forward** To **Forward from One channel to others**..\n\n"
                            "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝒞𝓇𝓎𝓅𝓉💞𝓈𝓉𝒶𝓇𝓀**")
           


@stark.on_message(filters.command(["restart"]) & ~filters.edited)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@stark.on_message(filters.command(["log"]) & ~filters.edited)
async def log_msg(bot: stark , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
