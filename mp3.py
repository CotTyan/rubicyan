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
    if message.content == ("///rubi help"):
        help = random.choice(('ほととぎす　鳴きつる方を　ながむれば　ただ有明の　月ぞ残れる','ひさかたの　光のどけき　春の日に　静心なく　花の散るらむ','天の原　ふりさけ見れば　春日なる　三笠の山に　出でし月かも'))
        embed = discord.Embed(title="ヘルプ", description="このヘルプを表示 `///rubi help`\nVCに接続する `///rubi start`\n※この機能はVCに接続しないと使えません　なお、音が大きい場合があるので注意してください\n機能追加はまだまだこれからですので気を長くしてお待ちください", color=0x00ccff)
        embed = embed.set_author(name="RubiTyan V by laminne", url="https://github.com/laminne", icon_url="")
        embed = embed.set_footer(text=help)
        await message.channel.send(embed=embed)
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