from discord.ext import commands
import os
import traceback
import discord
import random  # おみくじで使用

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "Good morning":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good morning")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "Good night":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Go to bed early♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "Hllo All":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "Good evening":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん　Good evening～☆" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "Hello!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention} ☆༺.Hello All.Everyone! Thank you!☆")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "こんこん":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんにちは☺️楽しんで！")  # f文字列（フォーマット済み文字列リテラル）


    if message.content == "HEY":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん HEY😃🎵")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはっ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん GoodMorning♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "そろそろ寝ます":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Have a good dream♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "sb/jpyn":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip JPYN 10 "f"{message.author.mention}　 🔑<:JPYNdisco:698471276498649168> ")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "sb/ben":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BEN 100 "f"{message.author.mention}　　🔑<:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>  Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/bgpt":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BGPT 1000 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    
    elif message.content == "b/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "b/RAIN":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 5.5 ActiveUserOnly ☔It Rains")
        [await q.add_reaction(i) for i in ('☂', '⛈')]  # for文の内包表記
        
    elif message.content == "language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "b/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

        
    elif message.content == "b/info":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben 残高")
        [await q.add_reaction(i) for i in ('↺', '↷')]  # for文の内包表記

        
    elif message.content == "b/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BEN 7.77 ActiveUserOnly ☔It Rains")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記
        
        
    elif message.content == "b/TIP":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" B/tip BGPT 5.14 "f"{message.author.mention}さん gave you a Tip＄")
        [await q.add_reaction(i) for i in ('💲', '☺')]  # for文の内包表記
  
        
    elif message.content == "b/tip":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip BGPT 2 "f"{message.author.mention}さん gave you a Tip＄")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記
        
           
    elif message.content == ".b/tip":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip BGPT 5 "f"{message.author.mention}さん gave you a Tip＄")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記
  

    elif message.content == "b/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 12 3 EquallyDistributed ☞/catchで受け取ってください⚾")
        [await q.add_reaction(i) for i in ('⚾', '✋')]  # for文の内包表記

        
    elif message.content == ".b/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 10 4 EquallyDistributed ☞/catchで受け取ってください⚾")
        [await q.add_reaction(i) for i in ('⚾', '✋')]  # for文の内包表記

        
    elif message.content == "+b/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 30 3 EquallyDistributed ☞/catchで受け取ってください⚾")
        [await q.add_reaction(i) for i in ('⚾', '✋')]  # for文の内包表記

        
    elif message.content == "/tip":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip BGPT 5 "f"{message.author.mention}さん gave you a Tip＄")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記


    elif message.content == "/info":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip BGPT 10 "f"{message.author.mention}さん gave you a Tip＄")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記


    elif message.content == "b/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain JPYN 6 ActiveUserOnly ☔It Rains")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記

        
    elif message.content == "+b/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 10 ActiveUserOnly ☔It Rains")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記
    
        
    elif message.content == "b/RAIN":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 50 ActiveUserOnly ☔It Rains")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記


    elif message.content == "balance":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ←Fill in this balance")
        [await q.add_reaction(i) for i in ('↺', '↷')]  # for文の内包表記


    elif message.content == "fack":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 931 "f"{message.author.mention}さん に💩Tip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '💩')]  # for文の内包表記


    elif message.content == "unko":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 931 "f"{message.author.mention}さん にunkoTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '💩')]  # for文の内包表記
        


client.run(token)
