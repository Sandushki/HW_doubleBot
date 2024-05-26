import discord
import os, random

# Benim farklı bir Python belgemden istediğim fonsiyonu çekmek içim from fonksiyonu kullanılır.
# İmport anahtar kelimesinden sonra teker teker fonksiyonların adını yazabiliriz ama bütün fonksiyonları almak için * sembolünü kullanırız.
from logic import *
# Botun ayrıcalıklarını depolayacak bir değişken oluşturalm. --> intents = ayrıcalıklar
intents = discord.Intents.default()

# Mesajları okuma ayrıcalığını vermemiz gerekir.
intents.message_content = True

# İstemci(Client) değişkeni ile bot oluşturalım.
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Ben; {client.user} olarak Discord'a vardım bile!")


@client.event
async def on_message(message):
    if message.author == client.user:
        # Yanıtları geri döndürür.
        return
    
    elif message.content.startswith('£Troll'):
        randomVid = random.choice(os.listdir('vid'))

        with open(f'vid\{randomVid}', 'rb') as f:
            video = discord.File(f)

        # Videomuzu göndertirken, bir metin çıktısı değil, o videoyu istediğimiz için başına "file=" koymamız gerekir.
        await message.channel.send(file=video)


    elif message.content.startswith('£Kompozisyon'):
        with open('komp.txt', 'r', encoding='utf-8') as m:
            metin = m.read()

        # Bu sefer göndereceğimizin başında "file=" koymayız çünkü zaten yazı göndermek istiyoruz.
        await message.channel.send(metin)

    elif message.content.startswith('£Roll'):
        sayi = str(zar(6))

        await message.channel.send(f'Anlaşılan zar atmak istediniz.\n\nSONUCUNUZZ:\n\n\n{sayi}')

    elif message.content.startswith('£Kimim'):
        user = message.author

        await message.channel.send(f"Siz {user}'sınız!\nUnuttunuz mu?????")

    
    elif message.content.startswith('£Insult'):
        soz = oldur()

        await message.channel.send(f'Siz bir {soz}sunuz!')


client.run('TOKEN HERE')