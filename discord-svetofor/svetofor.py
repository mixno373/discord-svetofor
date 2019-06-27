import discord, json, asyncio


DISCORD_BOT_TOKEN = input("Введите Discord token: ")

client = discord.Client()

async def svetofor():
    await client.wait_until_ready()
    sleep = 0.7
    print("Working...")
    while not client.is_closed():
        await client.change_presence(status=discord.Status.online)
        await asyncio.sleep(sleep)
        await client.change_presence(status=discord.Status.idle)
        await asyncio.sleep(sleep)
        await client.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(sleep)

@client.event
async def on_command_error(error, ctx):
	pass

@client.event
async def on_ready():
	client.loop.create_task(svetofor())

client.run(DISCORD_BOT_TOKEN, bot=False)