from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hi, I am [ANONYMOUS FILE SENDER BOT](https://telegra.ph/file/e4888d7e2d90d7d4e70da.png).\n\n"
                 "Just Forward me Some messages or\n"
                 "media and I will Anonymize the\n"
                 "sender.\n\n"
                 "MY Developer is [IsiraPiumAth](t.me/IsiRAPiumaTH) & Support him \n"
                 "By Joining the Support Group & Channel👇👇")


if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("🤖Deploy a clone🤖","https://heroku.com/deploy?template=https://github.com/masterisira/Anonymous-bot")],
                                         [Button.url("🔰⭕️Support Channel⭕️🔰","https://t.me/slpcgames")],
                                         [Button.url("💠Support Group💠","https://t.me/slpcgame")],
                                         [Button.url("💖Contact Developer💝","https://t.me/IsiRAPiumaTH")]])                                                                 
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
