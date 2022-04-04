# coding: utf-8


import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.utils import get
import os, sys

Comment = """
----> /---\ --+-- /---- /---\ 
|  /  |   |   |   |     |   | 
+-<   |   |   |   +---  +---/ 
|  \  |   |   |   |     |  \  
----> \---/   |   \---- |   \ 

if Discord has CLI version...
"""



from discord.embeds import Embed
sys.setrecursionlimit(10000)#エラー回避
import pickle
import traceback
import datetime
import asyncio

message_commands = [
    "!help",
    "!exit",
    "!change",
    "!load"
    ]

bot = discord.Client()


@bot.event
async def on_ready():
    print(f"""\
Login: {bot.user} ({bot.user.id})
Guilds: {len(bot.guilds)}
""")
    while True:
        print("・Guild select")
        for i in range(len(bot.guilds)):
            print(f"{'{:<4d}'.format(i+1)}: {bot.guilds[i]}")
        guild = input("Select guild> ")
        try:
            GUILD = bot.guilds[int(guild)-1]
        except BaseException as err:
            print(f"{err}\nPlease reselect.")
            continue
        print(f"\n[{GUILD.name}]\n")
        print("・Channel select")
        for i in range(len(GUILD.text_channels)):
            print(f"{'{:<4d}'.format(i+1)}: {GUILD.text_channels[i]}")
        channel = input("Select channel> ")
        try:
            CHANNEL = GUILD.text_channels[int(channel)-1]
        except BaseException as err:
            print(f"{err}\nPlease reselect.")
            continue
        messages = await CHANNEL.history(limit=20).flatten()
        messages.reverse()
        for i in messages:
            print(f"# {i.author.name} {i.created_at.month}/{i.created_at.day} {i.created_at.hour}:{i.created_at.minute}\n{i.content}\n")

        while True:
            MESSAGE = input(f"[!help - Show Help]\n・Send a message to #{CHANNEL.name} as {bot.user}\n")
            if MESSAGE[:1] != "!":
                try:
                    await CHANNEL.send(MESSAGE)
                    print("Sended!\n")
                    continue
                except BaseException as err:
                    print(f"\n・An error has occurred.\n{err}\n")
                    continue
            else:
                if MESSAGE not in message_commands:
                    print(f"Unknown command: {MESSAGE}")
                    continue

                # HELP COMMAND
                if MESSAGE == message_commands[0]:
                    print("""\n
BOTER - Help

!help - Show this help
!exit - Logout client
!change - Change guild/channel
!load
""")

                # LOGOUT COMMAND
                elif MESSAGE == message_commands[1]:
                    while True:
                        CONFIRM = input(f"Are you sure want to logout {bot.user}?[y/n]\n> ")
                        if CONFIRM not in ["y","n"]:
                            print("You have to enter [y] or [n].")
                            continue
                        else:
                            if CONFIRM == "y":
                                bot.close()
                                print("See you again...")
                                os._exit(0)
                            else:
                                break

                # CHANGE GUILD/CHANNEL COMMAND
                elif MESSAGE == message_commands[2]:
                    break

                # RELOAD MESSAGES COMMAND
                elif MESSAGE == message_commands[3]:
                    messages = await CHANNEL.history(limit=20).flatten()
                    messages.reverse()
                    for i in messages:
                        print(f"# {i.author.name} {i.created_at.month}/{i.created_at.day} {i.created_at.hour}:{i.created_at.minute}\n{i.content}\n")
                
            


def main(token):
    # BOT起動
    print("Launching bot.\nPlease wait...\n\n")
    bot.run(token)
    print("\n\nSee you!")

if __name__ == "__main__":
    print(f"""\
{Comment}


Please insert BOT Token.""")
    token = input("BOT TOKEN> ")
    if token == "":
        print("")
    main(token)