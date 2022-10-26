import os
import random
import asyncio
import discord
import scrapereddit as rs
import psycopg2

from settings import DISCORDBOT_TOKEN, DATABASE, HOST, USER, PASSWORD, PORT

subs = ['vinylreleases']
keywords = [['diamond']]

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  # await client.wait_until_ready()
  while True:
    conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    # Creating a cursor (a DB cursor is an abstraction, meant for data set traversal)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS redditpostalerts (post_id VARCHAR (50) UNIQUE)")
    for i in range(len(subs)):
      sub = subs[i]
      posts = rs.ScrapeReddit(sub, keywords[i])
      for p in posts:
        # Executing your PostgreSQL query
        cur.execute("SELECT EXISTS (SELECT 1 FROM redditpostalerts WHERE post_id = '" + str(p.id) + "');")
        post_id = cur.fetchone()[0]
        if post_id == False:
          # cur.execute("INSERT INTO redditpostalerts (post_id) VALUES ('" + p.id + "');")
          # In order to make the changes to the database permanent, we now commit our changes
          conn.commit()
          user = client.get_user(140965583528263681)
          print(user)
          await user.send("[" + sub + "] " + p.title + "\n" + p.url)
        if post_id == True:
          print("Post already notified")
    # We have committed the necessary changes and can now close out our connection
    cur.close()
    conn.close()
    await asyncio.sleep(300)


client.run(DISCORDBOT_TOKEN)
