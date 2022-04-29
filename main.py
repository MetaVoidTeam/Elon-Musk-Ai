from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import random
import json
import requests
import aiohttp
import asyncio

import os
import re



API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 

bot = Client(
    "Db" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)



bot_id = int(BOT_TOKEN.split(":")[0])




URL = "https://api-inference.huggingface.co/models/luca-martial/DialoGPT-Elon"

headers = {"Authorization": f"Bearer {os.environ['HUGGING_API']}"}



def elonai(payload):
  x = json.dumps(payload)
  resp = requests.request("POST", ELON_API_URL, headers=headers, data=URL)
  elonx = json.loads(response.content.decode("utf-8"))
  return elonx


@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def stats(client, message):
        await message.reply_text("hello there! I'm Elon Musk. Mechine Learning AI ChatBOT. I'm created by @MetaVoid.")




@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def elon(client: Client, message: Message):
   if message.reply_to_message:     
       msg = message.text
       getme = await bot.get_me()
       bot_id = getme.id
       if not message.reply_to_message.from_user.id == bot_id:
           return    
       resp = elonai({'text': msg})
       elon_response = resp.get('generated_text', None)
       res = elon_response
       if not elon_response:
         res = "No Idea Your Message"
       await message.reply_text(res)       
       


@bot.on_message(
    filters.text
    & ~filters.reply
    & filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def elon(client: Client, message: Message):
    msg = message.text
    resp = elonai({'text': msg})
    elon_response = resp.get('generated_text', None)
    res = elon_response
    if not elon_response:
      res = "No Idea Your Message"
    await message.reply_text(res)
    






bot.run()
