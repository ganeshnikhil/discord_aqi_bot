import os
import discord
import responses
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 

# intents.members = True
# intents.presences = True
# intents.messages = True

async def send_message(message, user_message, is_private):
   try:
      response = responses.handle_response(user_message , name = message.author)
      await message.author.send(response) if is_private else await message.channel.send(response)
   except Exception as e:
      print(e)


def run_discord_bot():
   # Load the token from an environment variable
   TOKEN = os.getenv("Token")
   
   if not TOKEN:
      print("DISCORD_TOKEN not found in environment variables.")
      return

   #intents = discord.Intents.all()
   client = discord.Client(intents=intents)

   @client.event
   async def on_ready():
      print(f"{client.user} is now running")
   
   @client.event
   async def on_member_join(member):
      await member.create_dm()
      await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
   
   @client.event
   async def on_message(message):
      if message.author == client.user:
         return

      username = str(message.author)
      user_message = str(message.content)
      channel = str(message.channel)

      print(f"{username} said: '{user_message}' ({channel})")

      if user_message.startswith('?'):
         user_message = user_message[1:]
         await send_message(message, user_message, is_private=True)
      else:
         await send_message(message, user_message, is_private=False)

   client.run(TOKEN)

