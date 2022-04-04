# coding: utf-8



import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.utils import get
import os, sys, json

Comment = {"en":"""
----> /---\ --+-- /---- /---\ 
|  /  |   |   |   |     |   | 
+-<   |   |   |   +---  +---/ 
|  \  |   |   |   |     |  \  
----> \---/   |   \---- |   \ 

if Discord has CLI version...
""",
"ja":"""
----> /---\ --+-- /---- /---\ 
|  /  |   |   |   |     |   | 
+-<   |   |   |   +---  +---/ 
|  \  |   |   |   |     |  \  
----> \---/   |   \---- |   \ 

もしDiscordにCLI版があったら..."""}

SETTING = json.load(open(f'setting.json', 'r'))

from discord.embeds import Embed
sys.setrecursionlimit(10000)#エラー回避
import pickle
import traceback
import datetime
import asyncio
import tl

message_commands = [
    "/help",
    "/exit",
    "/change",
    "/load"
    ]

bot = discord.Client()

stdio = tl.stdio(SETTING["language"])

@bot.event
async def on_ready():
    stdio.printf({
        "en":f"""\
Login user: {bot.user} ({bot.user.id})
Guilds: {len(bot.guilds)}
""",
        "ja":f"""\
ユーザー: {bot.user} ({bot.user.id})
サーバー数: {len(bot.guilds)}
"""
    })
    while True:
        stdio.printf({
            "en":"・Guild select",
            "ja":"・サーバー選択"
        })
        for i in range(len(bot.guilds)):
            print(f"{'{:<4d}'.format(i+1)}: {bot.guilds[i]}")
        guild = stdio.scanf({
            "en":"Select guild> ",
            "ja":"サーバー> "
        })
        try:
            GUILD = bot.guilds[int(guild)-1]
        except BaseException as err:
            stdio.printf({
                "en":f"{err}\nPlease reselect.",
                "ja":f"{err}\nもう一度選択しなおしてください。"
            })
            continue
        print(f"\n[{GUILD.name}]\n")
        stdio.printf({
            "en":"・Channel select",
            "ja":"・チャンネル選択"
        })
        for i in range(len(GUILD.text_channels)):
            print(f"{'{:<4d}'.format(i+1)}: {GUILD.text_channels[i]}")
        channel = stdio.scanf({
            "en":"Select channel> ",
            "ja":"チャンネル> "
        })
        try:
            CHANNEL = GUILD.text_channels[int(channel)-1]
        except BaseException as err:
            stdio.printf({
                "en":f"{err}\nPlease reselect.",
                "ja":f"{err}\nもう一度選択しなおしてください。"
            })
            continue
        messages = await CHANNEL.history(limit=SETTING["history_limit"]).flatten()
        messages.reverse()
        print(f"[{GUILD.name}/{CHANNEL.name}]")
        for i in messages:
            print(f"# {i.author.name} {i.created_at.month}/{i.created_at.day} {i.created_at.hour}:{i.created_at.minute}(UTC)\n{i.content}\n")

        while True:
            MESSAGE = stdio.scanf({
                "en":f"[/help - Show Help]\n・Send a message to #{CHANNEL.name} as {bot.user}\n",
                "ja":f"[/help - ヘルプ表示]\n・#{CHANNEL.name} に {bot.user}としてメッセージを送信\n"
            })
            if MESSAGE[:1] != "/":
                try:
                    await CHANNEL.send(MESSAGE)
                    print("Sended!\n")
                    continue
                except BaseException as err:
                    stdio.printf({
                        "en":f"\n・An error has occurred.\n{err}\n",
                        "ja":f"\n・エラーが発生しました。\n{err}\n"
                    })
                    continue
            else:
                if MESSAGE[:2] == "//":
                    try:
                        MSG = await CHANNEL.send(MESSAGE[1:])
                        print(f"# {MSG.author.name} {MSG.created_at.month}/{MSG.created_at.day} {MSG.created_at.hour}:{MSG.created_at.minute}(UTC)\n{MSG.content}\n")
                        continue
                    except BaseException as err:
                        stdio.printf({
                            "en":f"\n・An error has occurred.\n{err}\n",
                            "ja":f"\n・エラーが発生しました。\n{err}\n"
                        })
                        continue

                if MESSAGE not in message_commands:
                    stdio.printf({
                        "en":f"Unknown command: {MESSAGE}",
                        "ja":f"不明なコマンド: {MESSAGE}"
                    })
                    continue

                # HELP COMMAND
                if MESSAGE == message_commands[0]:
                    stdio.printf({
                        "en":"""\n
BOTER - Help

/help - Show this help
/exit - Logout client
/change - Change guild/channel
/load - Reload message history
""",
                        "ja":"""\n
BOTER - ヘルプ

/help - ヘルプを表示
/exit - ログアウトする
/change - サーバー/チャンネルを変更する
/load - 再度メッセージを読み込む
"""
                    })


                # LOGOUT COMMAND
                elif MESSAGE == message_commands[1]:
                    while True:
                        CONFIRM = stdio.scanf({
                            "en":f"Are you sure want to logout {bot.user}?[y/n]\n> ",
                            "ja":f"本当に{bot.user}からログアウトしてもよろしいですか？[y/n]\n> "
                        })
                        if CONFIRM not in ["y","n"]:
                            stdio.printf({
                                "en":"You have to enter [y] or [n].",
                                "ja":"[y]か[n]を入力してください。"
                            })
                            continue
                        else:
                            if CONFIRM == "y":
                                await bot.close()
                                stdio.printf({
                                    "en":"See you again...",
                                    "ja":"またね..."
                                })
                                os._exit(0)
                            else:
                                break

                # CHANGE GUILD/CHANNEL COMMAND
                elif MESSAGE == message_commands[2]:
                    break

                # RELOAD MESSAGES COMMAND
                elif MESSAGE == message_commands[3]:
                    messages = await CHANNEL.history(limit=SETTING["history_limit"]).flatten()
                    messages.reverse()
                    for i in messages:
                        print(f"# {i.author.name} {i.created_at.month}/{i.created_at.day} {i.created_at.hour}:{i.created_at.minute}(UTC)\n{i.content}\n")
                
            


def main(token):
    stdio.printf({
        "en":"Launching bot.\nPlease wait...\n\n",
        "ja":"BOTを起動しています。\nしばらくお待ちください...\n\n"
    })
    bot.run(token)
    stdio.printf({
        "en":"\n\nExit.",
        "ja":"\n\n終了。"
    })



if __name__ == "__main__":
    stdio.printf(Comment)
    if len(SETTING["TOKENS"].keys()) == 0:
        stdio.printf({
            "en":"You have to enter bot tokens in to [setting.json] like [temp.setting.json]!!!\nYou can enter multiple tokens.",
            "ja":"[temp.setting.json]を参考にして[setting.json]にTOKENを入力する必要があります。\nTOKENは複数入力可能です。"
            })
        stdio.scanf({
            "en":"[Enter to exit]",
            "ja":"[エンターで終了]"
            })
        os._exit(0)
    for i in range(len(SETTING["TOKENS"].keys())):
        print(f"{'{:<4d}'.format(i+1)}: {list(SETTING['TOKENS'].keys())[i]}")
    stdio.printf({
            "en":"Which account do you want to login?",
            "ja":"どのアカウントでログインしますか？"
            })
    while True:
        token = stdio.scanf({
            "en":"",
            "ja":""
            })
        try:
            TOKEN = SETTING['TOKENS'][list(SETTING['TOKENS'].keys())[int(token)-1]]
            break
        except BaseException as err:
            stdio.printf({
            "en":f"{err}\nPlease reselect.\nWhich account do you want to login?",
            "ja":f"{err}\nもう一度入れなおしてください。\nどのアカウントでログインしますか？"
            })
            continue
    main(TOKEN)