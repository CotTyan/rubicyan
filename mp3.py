import discord
import asyncio
import datetime
import random
import os
import time
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    global voich
    # voice = await join_voice_channel(client.get_channel())
    if message.content == ("///rubi start"):
        voich = await discord.VoiceChannel.connect(message.author.voice.channel)
        t = random.choice(('music.mp3','music2.mp3','music3.mp3'))
        print(t)
        voich.play(discord.FFmpegPCMAudio(t))
        sleep_time = 62
        await asyncio.sleep(sleep_time)
        await voich.disconnect()
    if t == ("music.mp3"):
        if message.content == ('春すぎて 夏来にけらし 白妙の 衣ほすてふ 天の香具山'):
            await message.channel.send("正解")
        await message.channel.send(t)
    if t == ('music2.mp3'):
        # if message.content == ('田子の浦に うち出でてみれば 真白にそ 富士の高嶺に 雪は降りつつ'):
        #     await message.channel.send("正解")
        await message.channel.send(t)
    if t == ('music3.mp3'):
        if message.content == ('憶良らは 今は罷らむ 子泣くらむ それその母も 我を待つらむそ'):
            await message.channel.send("正解")
        await message.channel.send(t)
client.run("")