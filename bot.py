import discord
import nacl
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '*')


@client.event 
async def on_ready():
	print('yo.')	

@client.command()
async def NODDERS(ctx):
	
	embed = discord.Embed(
		title = 'NODDERS'
		)
	embed.set_image(url = 'https://media.tenor.com/images/11c4ccb861ac402119e5d9b5e8392786/tenor.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\NODDERS.mp3")

@client.command()
async def pepeD(ctx):
	embed = discord.Embed(
		title = 'pepeD'
		)
	embed.set_image(url = 'https://media.tenor.com/images/e598ca7dc89620bd6b45f331083df584/tenor.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\pepeD.mp3")

@client.command()
async def catJAM(ctx):
	embed = discord.Embed(
		title = 'catJAM'
		)
	embed.set_image(url = 'https://media.tenor.com/images/5905a3c909f1cf1189773fef3876dffe/tenor.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\catJAM.mp3")

@client.command()
async def triDance(ctx):
	embed = discord.Embed(
		title = 'triDance'
		)
	embed.set_image(url = 'https://media1.tenor.com/images/f170020b9dc48d1d1c984be2ce2b61b6/tenor.gif?itemid=14672352')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\tridance.mp3")

@client.command()
async def Korone(ctx):
	embed = discord.Embed(
		title = 'EEKUM BOKUM'
		)
	embed.set_image(url = 'https://i.pinimg.com/originals/98/17/a6/9817a6fcaa9eb5008532e9de40451428.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\Korone.mp3")

@client.command()
async def poppingCat(ctx):
	embed = discord.Embed(
		title = 'POP POP POP POP POP POP POP '
		)
	embed.set_image(url = 'https://i.kym-cdn.com/photos/images/newsfeed/001/931/959/2e4.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\poppingCat.mp3")

@client.command()
async def juice(ctx):
	embed = discord.Embed(
		title = '( ͡° ͜ʖ ͡°) '
		)
	embed.set_image(url = 'https://cdn.shopify.com/s/files/1/0254/4363/1188/files/1533292611_1525003588_large.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\juice.mp3")

@client.command()
async def shampoo(ctx):
	embed = discord.Embed(
		title = 'shampoo '
		)
	embed.set_image(url = 'https://media.giphy.com/media/uKWMiEue0XcdyL029Q/giphy.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\shampoo.mp3")

@client.command()
async def milos(ctx):
	embed = discord.Embed(
		title = 'Ricardo Milos GANGGG '
		)
	embed.set_image(url = 'https://media1.tenor.com/images/2122258092f51309876ec76f80b7ddb5/tenor.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\milos.mp3")

@client.command()
async def dedo(ctx):
	embed = discord.Embed(
		title = 'DEDO ON DEDO ON DEDO ON DEDO '
		)
	embed.set_image(url = 'https://im2.ezgif.com/tmp/ezgif-2-5ed399092e0a.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\dedo.mp3")

@client.command()
async def free(ctx):
	embed = discord.Embed(
		title = 'Nuff said.'
		)
	embed.set_image(url = 'https://media1.tenor.com/images/41c0c2139f99146740aa20ea2d6f4ade/tenor.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\yourfree.mp3")

@client.command()
async def carti(ctx):
	embed = discord.Embed(
		title = 'They tryna be cray'
		)
	embed.set_image(url = 'https://media4.giphy.com/media/Bap9PFewF20es/giphy.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\carti.mp3")
	
@client.command()
async def sus(ctx):
	embed = discord.Embed(
		title = 'When the impostor is Sus!'
		)
	embed.set_image(url = 'https://i.kym-cdn.com/photos/images/newsfeed/001/966/661/fb8')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\sus.mp3")

@client.command()
async def pump(ctx):
	embed = discord.Embed(
		title = 'Thats Mafia City!!!'
		)
	embed.set_image(url = 'https://media2.giphy.com/media/MCizNlpCAf16imOCPF/200.gif')

	await ctx.send(embed= embed)
	await playAudio(ctx, "E:\\JAMBOTMUSIC\\pump.mp3")
	
	

@client.command()
async def logs(ctx):
	embed = discord.Embed(
		title = 'Update Logs'
		)
	embed.set_thumbnail(url = 'https://i.kym-cdn.com/entries/icons/mobile/000/031/066/cover2.jpg')
	embed.set_author(name = 'JamBot', icon_url = 'https://i.kym-cdn.com/entries/icons/mobile/000/031/066/cover2.jpg')
	embed.add_field(name = 'Version 1.0', value = 'Bot First made. Introduced pepeD, NODDERS, and catJAM', inline = True)
	embed.add_field(name = 'Version 1.1', value = 'Bot able to join calls. Added songs to each command', inline = True)
	embed.add_field(name = 'Version 1.2', value = '.leave command added', inline = True)
	embed.add_field(name = 'Version 1.3', value = 'Added Korone and corresponding sound', inline = True)
	embed.add_field(name = 'Version 1.3.1', value = 'Added triDance and corresponding sound', inline = True)
	embed.add_field(name = 'Version 1.3.2', value = 'Added poppingCat and corresponding sound', inline = True)
	embed.add_field(name = 'Version 1.3.3', value = 'JUICE, shampoo, Milos, dedo, free added', inline = True)

	await ctx.send(embed= embed)




async def playAudio(ctx, filepath):
        audioObject = await discord.FFmpegOpusAudio.from_probe(filepath)
        voiceStatus = ctx.author.voice
        voiceCall = voiceStatus.channel
        try:
            client = await voiceCall.connect()
        except discord.errors.ClientException:
            return
        try:
            client.play(audioObject)
            while(client.is_playing()):
                await asyncio.sleep(0.01)
            await client.disconnect()
        except TimeoutError:
            await client.disconnect()

@client.command(pass_context = True)
async def leave(ctx):
	await ctx.voice_client.disconnect()



client.run('')
#API key goes inbetween parens
