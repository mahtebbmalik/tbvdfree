import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Free Telegram Config
API_ID = 21946338  # Default public ID
API_HASH = "b4aa485805562725e173be8bf332c021"
BOT_TOKEN = "8716205774:AAGSHOhTnD1TF13BH9Fn9fEoZ5TLnT-rngU" # BotFather wala token yahan paste karein

app = Client("terabox_free_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("👋 **Assalam-o-Alaikum!**\nMujhe TeraBox video link bhejein, mein aapko direct video send karunga. Sab kuch free hai!")

@app.on_message(filters.text & ~filters.command(["start"]))
async def download_terabox(client, message: Message):
    url = message.text
    if "terabox" not in url and "nephobox" not in url and "4shared" not in url:
        await message.reply_text("❌ Ye valid TeraBox link nahi hai.")
        return

    status = await message.reply_text("🔎 **Video link bypass ho raha hai...**")

    try:
        # Free Open-Source API to bypass Terabox
        api_url = f"https://workers.dev{url}"
        response = requests.get(api_url).json()

        if "download_link" not in response:
            await status.edit("❌ TeraBox ne is link ko block kiya hua hai ya server down hai.")
            return

        direct_link = response["download_link"]
        video_title = response.get("title", "Video.mp4")

        await status.edit("📤 **Telegram par direct forward ho rahi hai...**")
        
        # Link direct telegram ko de rahe hain taake hosting space full na ho
        await message.reply_video(video=direct_link, caption=f"🎬 **{video_title}**")
        await status.delete()

    except Exception as e:
        await status.edit(f"⚠️ **Error:** {str(e)}")

if __name__ == "__main__":
    app.run()
