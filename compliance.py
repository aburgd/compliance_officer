import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import discord
from discord.ext import commands

from settings import CLIENT_TOKEN
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
async def register(ctx):
    # alias the database
    staff = db.staff_members
    # alias the two values you need most
    staff_id = ctx.message.author.id
    staff_nick = (
        ctx.message.author.nick if ctx.message.author.nick else ctx.message.author.name
    )
    sel = staff.select()
    res = connection.execute(sel)
    selected_member = res.fetchone()
    stored_id = selected_member[0]
    if staff_id == stored_id:
        stored_nick = selected_member[1]
        if stored_nick != staff_nick:
            upd = (
                staff.update()
                .where(staff.c.snowflake == staff_id)
                .values(current_nick=staff_nick)
            )
            connection.execute(upd)
            await ctx.send("Nick updated. We'll be with you shortly.")
    else:
    ins = sa.insert(staff).values(snowflake=staff_id, current_nick=staff_nick)
        connection.execute(ins)
    await ctx.send("Number taken. Please take a seat.")



bot.run(CLIENT_TOKEN)
