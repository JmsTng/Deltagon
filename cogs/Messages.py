class Messages(commands.Cog):
	@commands.command()
	async def dump(self, ctx, channel, content=None):
		if channel.startswith("<#"):
			id = int(channel[2:-1])
			channel = discord.utils.get(bot.get_all_channels(), id=id)
			if content:
				f = []
				if len(ctx.message.attachments) > 0:
					for file in ctx.message.attachments:
						async with aiohttp.ClientSession() as ses:
							async with ses.get(file.url) as resp:
								respstr = str(resp)
								respstr = respstr.split(">")[0].split("[")[1][0:3]
								if respstr != "200":
									await ctx.send("There was a problem with the file.")
									return
								data = io.BytesIO(await resp.read())
								f.append(discord.File(data, file.filename))
				await channel.send(content, files=f)
			elif ctx.message.reference:
				await channel.send(ctx.message.reference.resolved.content)
		else:
			await ctx.send("Pass a channel (#channel) to send to."
		
	@commands.command(aliases=["bm"])
	async def bookmark(self, ctx):
		replies = ctx.message.reference
		if not replies:
			return await ctx.send("Reply to a message *then* run this command.")
		reply_id = replies.message_id
		link = f"https://discord.com/channel/{ctx.message.guild.id}/{ctx.message.channel.id}/{reply_id}"
		channel = await ctx.author.create_dm()
		await channel.send(link)
