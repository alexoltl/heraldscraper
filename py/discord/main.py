import lightbulb
import json

config = json.load(open("config.json", "r"))

# Start the bot
bot = lightbulb.BotApp(
    token=config["token"]
)

# Load commands
bot.load_extensions_from("./commands")
bot.run()