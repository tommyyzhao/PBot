import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

MIN_CHARS = 100

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        welcome_message = await channel.send(f'Hey there {member.mention}! Welcome to the Principal Components Discord Server. Please tell us a little about you and how you got here (with at least {MIN_CHARS} characters, you have 5 minutes).')

        def check(message):
            return message.author == member and len(message.content) >= MIN_CHARS and message.channel == channel

        try:
            message = await client.wait_for('message', timeout=300.0, check=check)
        except:
            await member.kick(reason="Please send an introduction message.")
        else:
            role = discord.utils.get(member.guild.roles, name="member")
            await member.add_roles(role)

client.run('MTA4Mjg4MjYwNTYwMDQ3NzMxNA.GF5nSy.Hwe9MsZ-zLVDPEF06Twn9enmxUsnBIZ3KztRIs') 