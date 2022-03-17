import discord
from discord.ext import commands
import os
import datetime
import pyfiglet
import urllib.request
import keep_alive
import time
import sys
from flask import Flask
app = Flask(__name__)
token = os.environ['token']
bot = commands.Bot(command_prefix='ui.', self_bot=True, help_command=None)

class Clientim:
    status = "dnd"
    help_list = """```IUserBot Komutları

Prefix : ui.

ui.help / ui.yardım [Bu Komut]
ui.alive
ui.userbilgi
ui.ascii [yazı]
ui.festak
ui.update```"""

cs = Clientim()

@bot.event
async def on_ready():
    keep_alive.keep_alive()

@bot.command()
async def alive(ctx):
    if ctx.message.author == bot.user:
        await ctx.message.edit(content=f'`☔ IUserBot Aktif !`')
        if cs.status == "dnd":
            await bot.change_presence(status=discord.Status.dnd)

@bot.command()
async def help(ctx):
    if ctx.message.author == bot.user:
        await ctx.message.edit(content=cs.help_list)

@bot.command()
async def yardım(ctx):
    if ctx.message.author == bot.user:
        await ctx.message.edit(content=cs.help_list)

@bot.command()
async def userbilgi(ctx):
    if ctx.message.author == bot.user:
        await ctx.message.edit(content=f"""`Kullanıcımın Bilgileri!
İsmi: {bot.user.name}
Hashtag'i: #{bot.user.discriminator}
Tam İsmi: {bot.user}
Hesap Kurulma Tarihi: {bot.user.created_at.day}.{bot.user.created_at.month}.{bot.user.created_at.year}`""")

@bot.command()
async def ascii(ctx):
    if ctx.message.author == bot.user:
        text = ctx.message.content[9:len(ctx.message.content)]
        ascii_banner = pyfiglet.figlet_format(text)
        await ctx.message.edit(content=f'```{ascii_banner}```')

@bot.command()
async def festak(ctx):
    if ctx.message.author == bot.user:
        await ctx.message.edit(content="`🎩 Fes Taktın!`")

@bot.command()
async def update(ctx):
    url = "https://iuserbotsite.henryoffline.repl.co/versiyon.html"
    html = urllib.request.urlopen(url)
    versionnow = str(html.read())
    versiontxt = open('version.txt')
    version = versiontxt.read()

    if version == versionnow[2:len(versionnow)-1]:
        await ctx.message.edit(content=f'`🍻 Versionunuz Güncel! Versiyonunuz {version}`')
    
    elif version == "":
        with open('version.txt', 'w') as f:
            f.writelines(versionnow[2:len(versionnow)-1])
        await ctx.message.edit(content='`🚩 Versiyon Dosyanız Bulunamadı. Oluşturuyorum`')
            
    elif versionnow[2:len(versionnow)-1] != version:
        await ctx.message.edit(content="`⏬ Update Bulundu! İndiriliyor!`")
        if os.path.exists("bot.py"):
            os.remove("bot.py")
        urllib.request.urlretrieve("https://iuserbotsite.henryoffline.repl.co/bot.py", "bot.py")
        with open('version.txt', 'w') as f:
            f.writelines(versionnow[2:len(versionnow)-1])
        time.sleep(5)
        await ctx.message.edit(content="`✅ Update Yapıldı! Yeniden Başlatılıyor!`")
        os.system("python3 bot.py")
        sys.exit()

@bot.command()
async def admin_alive(ctx):
    versiontxt = open('version.txt')
    version = versiontxt.read()
    if ctx.message.author.id == 932962111934586901:
        if ctx.message.author == bot.user:
            await ctx.message.edit(content=f'`🥂 Aktif olan botlara komut gönderildi {ctx.message.author.name}! Ayrıca versiyonum {version}`')
        else:
            await ctx.send(f'`🐱 Merhaba admin! Sürümüm {version}`')

@bot.command()
async def updatenow(ctx):
    url = "https://iuserbotsite.henryoffline.repl.co/versiyon.html"
    html = urllib.request.urlopen(url)
    versionnow = str(html.read())
    versiontxt = open('version.txt')
    version = versiontxt.read()
    
    await ctx.message.edit(content="`⏬ Update İndiriliyor!`")
    if os.path.exists("bot.py"):
        os.remove("bot.py")
    urllib.request.urlretrieve("https://iuserbotsite.henryoffline.repl.co/bot.py", "bot.py")
    with open('version.txt', 'w') as f:
        f.writelines(versionnow[2:len(versionnow)-1])
    time.sleep(5)
    await ctx.message.edit(content="`✅ Update Yapıldı! Yeniden Başlatılıyor!`")
    os.system("python3 bot.py")
    sys.exit()

bot.run(token)