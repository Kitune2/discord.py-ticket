import discord
from discord.ext import commands
from discord_buttons_plugin import *
import requests
from discord.utils import get
bot = commands.Bot(command_prefix = "!")
buttons = ButtonsClient(bot)
カテゴリ = 1111111111111  #tickt置くカテゴリid
ロール = "admin"#チケット作った人以外にチケットを見れるロール名


@bot.event
async def on_ready():
    print("ready")

@buttons.click
async def infor(ctx):
    ch_name = "￤-{0}￤".format(ctx.member.name)
    guild = bot.get_guild(ctx.guild.id)
    category = guild.get_channel(カテゴリ)
    admin_role = get(guild.roles, name=ロール)
    permission = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    ch = await category.create_text_channel(name=ch_name, overwrites=permission)
    embed = discord.Embed(title="チケット",description="間違えて押した場合は消すを押してください", color=0x7fff00)
    await ctx.reply("チケットを作成しました", flags = MessageFlags().EPHEMERAL)
    await buttons.send(
        embed = embed,
        channel = ch.id,
        components = [
            ActionRow([
                Button(
                    label="消す", 
                    style=ButtonType().Danger, 
                    custom_id="jorkcr",
                    disabled = False
                )
            ])
        ]
    )
    

 

@bot.command()
async def ticket(ctx):
    await buttons.send(
        content = "チケット作成ボタンです", 
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    label="ticket作成", 
                    style=ButtonType().Danger, 
                    custom_id="infor"
                )
            ])
        ]
    )


bot.run(TOKEN)
