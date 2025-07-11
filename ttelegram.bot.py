import os
import time
import feedparser
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("tel:7420283992")
CHAT_ID = os.getenv("https://t.me/agbarsin_test")  # اینم از env بخون بهتره

RSS_URL = 'https://www.farsnews.ir/rss/politics'
sent_links = set()
bot = Bot(token=TELEGRAM_TOKEN)

def check_rss():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        if entry.link not in sent_links:
            message = f"📰 {entry.title}\n{entry.link}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            sent_links.add(entry.link)

if __name__ == "__main__":
    while True:
        check_rss()
        time.sleep(60 * 5)
