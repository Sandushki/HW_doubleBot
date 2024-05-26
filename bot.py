import discord
from discord.ext import commands

from logic import *

import os, random

# Botumuzun ayrıcalıklarını depolayalım
intents = discord.Intents.default()
intents.message_content = True


# Bot adında bir değişken oluşturarak bot objesi ile bir bot oluştururuz, fakat işimiz bu sefer orada bitmez.
# commands sınıfındaki Bot objesini kullanırız

# Komutlarımızın prefixini command_prefix'ten ayarlarız.
# bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='?', intents=intents)

# Deklaratör, @ ile başlar, ve fonksiyonları otomatik olarak belirli koşullarda çalıştırılmasını sağlaırız.
@bot.event
async def on_ready():
    print(f"{bot.user} olarak Discord'a vardık!")


@bot.command()
async def troll(ctx):
    randomVideo = random.choice(os.listdir('vid'))

    with open(f'vid\{randomVideo}', 'rb') as f:
        video = discord.File(f)

    # Videomuzu göndertirken, bir metin çıktısı değil, o videoyu istediğimiz için başına "file=" koymamız gerekir.
    await ctx.send(file=video)

@bot.command()
async def kompozisyon(ctx):
    with open('komp.txt', 'r', encoding='utf-8') as m:
        metin = m.read()

    # Bu sefer göndereceğimizin başında "file=" koymayız çünkü zaten yazı göndermek istiyoruz.
    await ctx.send(metin)

@bot.command()
async def roll(ctx):
    sayi = str(zar(6))

    await ctx.send(f'Anlaşılan zar atmak istediniz.\n\nSONUCUNUZZ:\n\n\n{sayi}')
@bot.command()
async def kimim(ctx):
    user = ctx.author.name

    await ctx.send(f"Siz {user}'sınız!\nUnuttunuz mu?????")

@bot.command()
async def insult(ctx):
    soz = oldur()

    await ctx.send(f'Siz bir {soz}sunuz!')


bot.run('TOKEN HERE')