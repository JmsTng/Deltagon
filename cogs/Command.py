class CommandPerms(commands.Cog):
	@commands.is_owner()
	@commands.command(aliases=["blk"])
	async def block(self, ctx, id, command):
		if command in commandlist:
			db["blocklist"][command].append(id)
			await ctx.send(f"<@{id}> was blocked from using `delta:{command}`.")
		else:
			await ctx.send("Are you sure that's a valid command?")
	
	@commands.is_owner()
	@commands.command(aliases=["ub", "ublk"])
	async def unblock(self, ctx, id, command):
		if command in commandlist:
			if id in db["blocklist"][command]:
				db["blocklist"][command].remove(id)
				await ctx.send(f"<@{id}> has been unblocked from using `delta:{command}`.")
			else:
				await ctx.send(f"<@{id}> was never blocked...")
		else:
			await ctx.send("Are you sure that's a valid command?")

	@commands.is_owner()
	@commands.command(aliases=["ba", "blka", "blkall"])
	async def blockall(self, ctx, id):
		for i in commandlist:
			if id not in db["blocklist"][i]:
				db["blocklist"][i].append(id)
		await ctx.send(f"<@{id}> has been blocked from using all commands.")

	@commands.is_owner()
	@commands.command(aliases=["uba", "ublka", "ublkall"])
	async def unblockall(self, ctx, id):
		for i in commandlist:
			if id in db["blocklist"][i]:
				db["blocklist"][i].remove(id)
		await ctx.send(f"<@{id}> has been unblocked from using all commands.")
