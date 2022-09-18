import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot",intents=discord.Intents.all())

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print('My Ready is Body')
    #clist = []
    #cid = ""
    #for guild in bot.guilds:
    #    for channel in guild.text_channels:
    #        print (channel.id)
            #print (channel + channel.id)
    #        if channel ==  "bot-land":
    #            print ("found it")
    #            cid = channel.id    

def counter (cmd):
     f = open (cmd, "r")
     c = f.readline ()
     f.close() 
     c1 = int (c) + 1
     if cmd == "shaira" and c == 69:     
         c1 = 69
     
     c = str (c1) 
     f = open (cmd, "w") 
     f.write (c)
     f.close
     return c

def getKey ():
    f = open ("key","r")
    c = f.readline ()
    f.close ()
    return c



@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)
    elif "test-ch" in message.content.lower ():
        await message.channel.send (message.channel.id)
        await bot.process_commands(message)

    elif "!shaira" in message.content.lower ():
        cmd = "shaira"
        c = counter (cmd)
        
        await bot.process_commands(message)
        await message.channel.send ("ikaw ha " +  cmd + " nakaka 69 ka na (actually " +c+ ")")

    elif "!kuyael" in message.content.lower ():
        cmd = "kuyael"
        c = counter (cmd)
       
        await bot.process_commands(message) 
        await message.channel.send("ikaw ha " + cmd + " nakaka " + c + " ka na")

    elif "!bing" in message.content.lower ():
        cmd = "bing"  
        c = counter (cmd)
        await bot.process_commands(message)
        await message.channel.send ("ikaw ha " + cmd +" nakaka " + c + " ka na")

    elif "!raimi" in message.content.lower ():
        cmd = "raimi"   
        c = counter (cmd)
        await bot.process_commands(message)
        await message.channel.send ("ikaw ha " + cmd + " nakaka " + c + " ka na")

    elif "!dudong" in message.content.lower ():
        cmd = "dudong"  
        c = counter (cmd)
        await bot.process_commands(message)
        await message.channel.send ("you have been dudonged " + c  + " times")

    elif "!bonta" in message.content.lower ():
        cmd = "bonta"  
        c = counter (cmd)
        await bot.process_commands(message)
        await message.channel.send ("ikaw ha " + cmd + " nakaka " + c + " ka na")
    
    elif "!rotate" in message.content.lower ():
       await message.channel.send ("https://www.youtube.com/watch?v=eY52Zsg-KVI")
       await bot.process_commands(message)

    elif "!viper" in message.content.lower (): 
       cmd = "viper"
       c = counter (cmd)
       await message.channel.send (" AIR MANIII!!! " + c + " times <:kappa:965201460608516138>")
       await bot.process_commands (message)
    
    elif "!khuziee" in message.content.lower ():
       cmd = "khuziee"
       c = counter (cmd)
       await message.channel.send ("Khuziee being UwU " + c + " times")
       await bot.process_commands (message)
       
    elif "!test" in message.content.lower ():
       await message.channel.send ("yeah yeah im working")
       await bot.process_commands (message)

    elif "!boruto"  in message.content.lower ():
       await message.channel.send ("<:boruto:983704550047383583> <:boruto:983704550047383583> <:boruto:983704550047383583> <:boruto:983704550047383583> <:boruto:983704550047383583>")
       await bot.process_commands (message)

    elif "!metaldogs" in message.content.lower ():
        await message.channel.send('Set in a world after the destruction of humankind, the harsh battle of the combat dog "Pochi" begins. Explore dungeons that change every time you enter, get a wide variety of weapons, and power up your dog! Hunt the evil "WANTED"! Enjoy exhilarating battles casually in this shooting action game.')
        await bot.process_commands (message)

    elif "!monika" in message.content.lower():
        await message.channel.send('Just Monika. https://imgur.com/gallery/1dz3yOR')
        await bot.process_commands (message)
#bot.run(getKey())
bot.run("")