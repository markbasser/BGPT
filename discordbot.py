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

    if message.content == "Hello All":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "/tip bgpt 500 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip ben 50 {message.author.mention}  \n Swapped from BGPT500<:BGPT02:698471366004965406> to BEN500<:BENKEICOIN04:698471407650209832> .　" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "/tip bgpt 1000 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip ben 100 {message.author.mention}   \n Swapped from BGPT1000<:BGPT02:698471366004965406> to BEN100<:BENKEICOIN04:698471407650209832>")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "/tip ben 100 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip bgpt 1000 {message.author.mention}   \n Swapped from BEN100<:BENKEICOIN04:698471407650209832> to BGPT1000<:BGPT02:698471366004965406> ")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "/tip ben 500 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip bgpt 5000 {message.author.mention}  \n Swapped from BEN100<:BENKEICOIN04:698471407650209832> to BGPT1000<:BGPT02:698471366004965406> ")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "/tip BGPT 500 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip ben 50 {message.author.mention}   \n Swapped from BGPT500<:BGPT02:698471366004965406> to BEN500<:BENKEICOIN04:698471407650209832> .　" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "/tip BGPT 1000 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip ben 100 {message.author.mention}   \n Swapped from BGPT1000<:BGPT02:698471366004965406> to BEN100<:BENKEICOIN04:698471407650209832>")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "/tip BEN 100 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip bgpt 1000 {message.author.mention}  \n Swapped from BEN100<:BENKEICOIN04:698471407650209832> to BGPT1000<:BGPT02:698471366004965406> ")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "/tip BEN 500 <@700134903311761460>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip bgpt 5000 {message.author.mention}   \n Swapped from BEN100<:BENKEICOIN04:698471407650209832> to BGPT1000<:BGPT02:698471366004965406> ")  # f文字列（フォーマット済み文字列リテラル）


    if message.content == "sb/jpyn":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip JPYN 10 "f"{message.author.mention}　 🔑<:JPYNdisco:698471276498649168> ")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "sb/ben":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BEN 100 "f"{message.author.mention}　　🔑<:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>  Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/bgpt":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BGPT 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/kenj":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip KENJ 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/sprts":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip SPRTS 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    
    elif message.content == "b/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "b/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "b/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記   
     
    
    elif message.content == "b/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 60 ActiveUserOnly  <:BGPT02:698471366004965406><:good01:699581068285706301>🌈☔It Rains")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '🌈')]  # for文の内包表記
         
            
    elif message.content == "b/Rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send("  /rain BEN 30 ActiveUserOnly  <:benkeicoinsl:698471387064696833>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:benkeicoinsl:698471387064696833>')]  # for文の内包表記

        
    elif message.content == "b/RAIN":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain JPNY 10 ActiveUserOnly  <:JPYNdisco:698471276498649168>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '🌈')]  # for文の内包表記
        
   
    elif message.content == "b/RAin":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain KENJ 100 ActiveUserOnly  <:kenj:700136543003607101> 🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:sangras01:699579409220370514>')]  # for文の内包表記
      
    
    elif message.content == "b/RAIn":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain SPRTS 1000 ActiveUserOnly  <:sprts:699076413931782146> 🌈☔It Rains🌱")
        [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '🌱')]  # for文の内包表記
        
        
   
    elif message.content == "b/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 200 4 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "b/THROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 80 4 EquallyDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "b/THrow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 40 4 EquallyDistributed  <:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "b/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 400 4 EquallyDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記


    elif message.content == "b/THROw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 777 5 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記


    elif message.content == "b/thunder":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /thunder BGPT 777 ActiveUserOnly  <:good:699580636448423936><:BGPT02:698471366004965406>thunder")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPT02:698471366004965406>')]  # for文の内包表記

        
    elif message.content == "b/tHROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 777 4 AttenuationDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:jhlo:700932650944299098>')]  # for文の内包表記
    
    
    elif message.content == "b/thROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 100 4 AttenuationDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記
 
    
    elif message.content == "b/thrOW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 80 4 AttenuationDistributed  <:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "b/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 1000 4 AttenuationDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記



    elif message.content == "fack":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}  !😡🚫:warning:💩")
        [await q.add_reaction(i) for i in ('💩', '💩')]  # for文の内包表記


    elif message.content == "unko":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}  !😡🚫:warning:💩")
        [await q.add_reaction(i) for i in ('💩', '💩')]  # for文の内包表記
        
    
    elif message.content == "BAKA":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}   !😡🚫:warning:💩")
        [await q.add_reaction(i) for i in ('💩', '💩')]  # for文の内包表記

   
    elif message.content == "baka":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}  !😡🚫:warning:💩")
        [await q.add_reaction(i) for i in ('💩', '💩')]  # for文の内包表記   
        
        

client.run(token)
