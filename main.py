import discord
from discord.ext import commands

# Intents কনফিগারেশন
intents = discord.Intents.default()
intents.message_content = True

# Bot ইনিশিয়ালাইজ করা
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("AYUMI🎀 is online and ready!")

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("হ্যালো! আমি AYUMI🎀, আপনার ডিসকর্ড বট। আমি এখন Render-এ ২৪/৭ অনলাইনে আছি! ✨")

# বটের সিক্রেট টোকেন দিয়ে রান করা
bot.run("MTU2OTI3NTg5OTM1Mjk3MzQxNQ.GCpm0t.8ZkDkh445CSa1fcMmzpCBWJYTuq0yarWMlvLVw")
