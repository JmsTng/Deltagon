from discord.ext import commands
import discord, os, time

class Moderation(commands.Cog):
	@commands.has_permissions(kick_members=True)
	@commands.command(pass_context = True)
	async def kick(ctx, member: commands.MemberConverter, *, why=None):
		if why == None:
			await ctx.channel.send("Please specify a reason!")
		else:
			try:
				await member.kick(reason=why)
			except:
				await ctx.channel.send("There was an issue")

	@commands.has_permissions(ban_members=True)
	@commands.command(pass_context = True)
	async def ban(ctx, member: commands.MemberConverter, *, why=None):
		if why == None:
			await ctx.channel.send("Please specify a reason!")
		else:
			try:
				await member.ban(reason=why)
			except:
				await ctx.channel.send("There was an issue")
