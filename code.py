import discord
import asyncio
import time
import random
from discord.ext import commands

TOKEN = 'NDg4MTMxMTY0NzIxMjUwMzEy.DnXwcA.ls0zYFPA7kM5Kl0A0Q6xQRoFACc'

client = commands.Bot(command_prefix='?')
client.remove_command('help')

@client.event
async def on_ready():
    print ('Logged in as:')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - ?help"))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.kick_members:
        if user is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to kick!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            await client.kick(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Kick Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.ban_members:
        if user is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to ban!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            await client.kick(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)

    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Ban Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to mute!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.add_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to unmute!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.remove_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name='Unmute - Information', value='You have been unmuted!', inline=False)
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Unmute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def nick(ctx, member:discord.User=None, *, newnick=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.manage_nicknames:
        if member is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to change the nickname of!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.change_nickname(member, newnick)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='**{}** Nickname has been changed.'.format(member.name))
            embed.add_field(name='Changed:', value='You have changed the nickname to: **{}**'.format(newnick), inline=True)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Nicknames``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=None):
    if ctx.message.author.server_permissions.manage_messages:
        if amount is None:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the amount of messages you want me to delete!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            channel = ctx.message.channel
            author = ctx.message.author
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Clear - Information')
            embed.add_field(name='Amount:', value='**I have deleted {} messages**'.format(amount), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Messages``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def timer(ctx, time=None):
    if time is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the seconds you want me to set for you!', inline=False)
        embed.set_footer(text='Please set a timer ?timer <amount>')
        await client.say(embed=embed)
    channel = ctx.message.channel
    author = ctx.message.author
    message = []
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name=':stopwatch: Timer Set:', value='Timer set for **{}** seconds'.format(int(time), inline=True))
    await client.say(embed=embed)
    await asyncio.sleep(int(time))
    msg=await client.say('{}'.format(author.mention))
    await client.delete_message(msg)
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name=':stopwatch: Timer Up:', value='Timer is up **{}**'.format(author.name), inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def welcome(ctx):
    if ctx.message.author.server_permissions.administrator:
        server = ctx.message.server
        author = ctx.message.author
        await client.create_channel(server=server, name="Welcome")
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='**Welcome Setup!**', value='I have created a welcome and goodbye channel! ``Please make the permissions for the channel!``', inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Administrator``', inline=False)
        await client.say(embed=embed)

@client.command()
async def invite():
    embed = discord.Embed(color=0x36393E)
    embed.set_author(name='Mr. M Invatation')
    embed.title = '**You can invite Mr. Monarch RN!!**'
    embed.url = 'https://discordapp.com/api/oauth2/authorize?client_id=488131164721250312&permissions=8&scope=bot'
    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=0x36393E)
    embed.set_author(name='Help Center - Information')
    embed.add_field(name='Moderation commands:', value='**?ban** \n **?kick** \n **?mute** \n **?unmute** \n **?nick** \n **?welcome** \n **?clear**', inline=False)
    embed.add_field(name='Fun Commands:', value='**?ping** \n **?timer** \n **?roast**', inline=False)
    embed.add_field(name='Calculation Commands:', value='**?add <num> <num>** \n **?sub <num> <num>** \n **?mul <num> <num>** \n **?div <num> <num>**', inline=False)
    embed.add_field(name='Regular Commands:', value='**?info <user>** \n **?serverinfo**', inline=False)
    await client.send_message(author, embed=embed)
    embed = discord.Embed(color=0x36393E)
    embed.title = ':mailbox_with_mail:  You have mail! **Check your DMs**'
    await client.say(embed=embed)

@client.command(pass_context=True)
async def roast(ctx, user: discord.User=None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to roast!', inline=False)
        embed.set_footer(text='Remember: ?roast @user')
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        choices = [
            'Your Mamma Fat **Roast 1**',
            'You like McDonalds? Slap them cheeks reall good daddy **Roast 2**',
            'Your Moms asshole is so smelly that when rick and morty came out they couldnt decide what was worse, there attitude or your moms asshole **Roast 3**',
            'Your dick is smaller than a homless mans Rent **Roast 4**',
            'You should stand in a chineese resteraunt and say ***This is America*** **Roast 5**',
            'Your mom is so gay that she grabbed your dogs dick **Roast 6**',
            'Your sister is lesbian **Roast 7**',
            'You gave head to Spongebob and then got wet, so you got sponged! **Roast 8**',
            'Fuck me harder David! **Roast 9**',
            'Daddys Home! Bruh i am your dad! **Roast 9**',
            
            
        ]
        embed.add_field(name='**{} Roasted :wink:**'.format(user), value=(random.choice(choices)), inline=True)
        await client.say(embed=embed)

@client.event
async def on_member_join(member: discord.Member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - ?help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')  
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Welcome **{}** , welcome to **{}** :envelope_with_arrow:'.format(member.name, server.name), value='Please read the rules of this server and follow corretly. Also type ?help for more commands of this bot!', inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)

# Calculations
@client.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Math Equations!', value='**{} + {} = {}**'.format(left, right, left + right), inline=True)
    await client.say(embed=embed)

@client.command()
async def sub(left : int, right : int):
    """Adds two numbers together."""
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Math Equations!', value='**{} - {} = {}**'.format(left, right, left - right), inline=True)
    await client.say(embed=embed)

@client.command()
async def mul(left : int, right : int):
    """Adds two numbers together."""
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Math Equations!', value='**{} x {} = {}**'.format(left, right, left * right), inline=True)
    await client.say(embed=embed)

@client.command()
async def div(left : int, right : int):
    """Adds two numbers together."""
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Math Equations!', value='**{} / {} = {}**'.format(left, right, left / right), inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title=":hourglass_flowing_sand:  Ping has been summoned:", description='**Latency: {}ms**'.format(round((t2-t1)*1000)), color=0x36393E)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server info")
    embed.add_field(name="**Name**", value=ctx.message.server.name, inline=True)
    embed.add_field(name="**ID**", value=ctx.message.server.id, inline=True)
    embed.add_field(name="**Roles**", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="**Members**", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user for me to give info about!', inline=False)
        await client.say(embed=embed)
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x36393E)
    embed=discord.Embed(color=0x36393E)
    embed.add_field(name="**Users Name Is:**", value="{}".format(user.name), inline=False)
    embed.add_field(name="**Highest Role Is:**", value="{}".format(user.top_role), inline=False)
    embed.add_field(name="**Users ID Is:**", value="{}".format(user.id), inline=False)
    embed.add_field(name="**Users Nickname Is:**", value="{}".format(user.nick), inline=False)
    embed.add_field(name="**Users Status Is:**", value="{}".format(user.status), inline=False)
    embed.add_field(name="**Users Game Is:**", value="{}".format(user.game), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def stats(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=0x36393E)
    embed.set_author(name='Bot Stats - Information'.format(author.name))
    embed.add_field(name='Prefix', value='Current Prefix ``?``', inline=True)
    embed.add_field(name='Bot Creator', value='**SaVaGe;_;#5185**', inline=False)
    await client.say(embed=embed)






        
    
        
            
        
        

client.run(TOKEN)
