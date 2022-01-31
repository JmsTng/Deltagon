class Miscellaneous(commands.Cog):
  @bot.command()
  async def say(ctx, *, arg):
	  if str(ctx.author.id) in db["blocklist"]["say"]:
		  await ctx.send("You've been blocked from using this command!")
  		return
	  await ctx.channel.purge(limit=1)
	  await ctx.send(f"{arg} - {ctx.author.mention}")

  @commands.has_permissions(manage_messages=True)
  @bot.command(aliases=["clear"])
  async def delete(ctx, amount):
	  if str(ctx.author.id) in db["blocklist"]["delete"]:
		  await ctx.send("You've been blocked from using this command!")
		  return
  	try:
	  	if "-" in amount:
		  	ctx.send("Invalid parameters!")
  		elif amount == None:
	  		await ctx.channel.purge(limit=1)
		  elif amount == "all" or amount == "max":
			  await ctx.channel.purge()
  		else:
	  		await ctx.channel.purge(limit=int(amount) + 1)
	  except commands.errors.MissingPermissions:
		  await ctx.send("You're missing some permissions.")
  	except:
	    await ctx.send("There was an issue.")


  @bot.command()
  async def membercount(ctx):
	  if str(ctx.author.id) in db["blocklist"]["membercount"]:
		  await ctx.send("You've been blocked from using this command!")
		  return
  	members = ctx.guild.member_count
	  await ctx.send(f"There are {members} members.")

  @bot.command()
  async def invite(ctx):
	  if str(ctx.author.id) in db["blocklist"]["invite"]:
		  await ctx.send("You've been blocked from using this command!")
		  return
  	await ctx.send("Add me to other servers: https://discord.com/api/oauth2/authorize?client_id=798221863620575244&permissions=141318&scope=bot")
