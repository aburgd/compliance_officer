import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import discord
from discord.ext import commands

import settings
import db

description = """Compliance Officer of the Nine

a bot to log community engagement and staff member absences for Community of Xur"""

command_prefix = "."

bot = commands.Bot(command_prefix=command_prefix, description=description)

connection = db.eng.connect()


@bot.event
async def on_ready():
    print("logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("--------------------")


@bot.command()
async def activity(ctx, message):
    return


@bot.command()
async def register(ctx, message):
    staff = db.staff_members
    staff_id = message.author.id
    staff_nick = message.author.name
    ins = sa.insert(staff).values(snowflake=staff_id, current_nick=staff_nick)
    await ctx.send("Number taken. Please take a seat.")


bot.run(settings.CLIENT_TOKEN)
