@Ghost.command(name="neko", description="Pictures or videos of nekos", usage=f"neko", aliases=["catgirl"])
async def neko(ctx):
    image = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
    await ctx.send(image)
