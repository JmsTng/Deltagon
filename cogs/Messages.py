class Messages(commands.Cog):
	@commands.command()
	async def dump(self, ctx):
		if "<#" in ctx.message.content:
			channel = ctx.message.content.split("<#")[1]
			channel = channel.split(">")[0]
			sendable = discord.utils.get(bot.get_all_channels(), id=int(channel))
			if len(ctx.message.attachments) > 0:
				attachment = ctx.message.attachments[0]
				e = discord.Embed(description=ctx.message.content.split(f"delta:dump <#{channel}>")[1] + f" - {ctx.message.author.mention}")
				e.set_image(url=str(attachment).split("url='")[1].split("'>")[0])
				await sendable.send(embed=e)
			else:
				await sendable.send(ctx.message.content.split(f"delta:dump <#{channel}>")[1] + f" - {ctx.message.author.mention}")
		else:
			await ctx.channel.send("Pass a channel (#channel) to send to.")
		
	@commands.command(aliases=["bm"])
	async def bookmark(self, ctx):
		replies = ctx.message.reference
		reply_id = replies.message_id
		link = f"https://discord.com/channel/{ctx.message.guild.id}/{ctx.message.channel.id}/{reply_id}"
		channel = await ctx.author.create_dm()
		await channel.send(link)
