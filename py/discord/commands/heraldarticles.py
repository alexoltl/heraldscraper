import hikari
import lightbulb
import datetime
import requests
from bs4 import BeautifulSoup

plugin = lightbulb.Plugin("Articles")

@plugin.command
@lightbulb.option("link", "Link to the article")
@lightbulb.command("article", "Posts paywall-locked arcticle from The Herald.")
@lightbulb.implements(lightbulb.SlashCommand)
async def notices(context):
    counter = 0
    output_str = ""

    url = context.options.link

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for p in soup.find_all("p"):
        if "article__heading-caption hero" not in p["class"]:
            if counter < 4:
                counter += 1
                continue
            output_str += p.get_text() + "\n\n"

    embed = (
        hikari.Embed(
            title="Notices",
            description=output_str,
            timestamp=datetime.datetime.now().astimezone()
        )
    )
    await context.respond(embed)

def load(bot):
    bot.add_plugin(plugin)