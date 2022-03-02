import os
import speedtest
import wget
from Music.MusicUtilities.helpers.gets import bytes
from Music import app, SUDOERS, BOT_ID
from pyrogram import filters, Client
from Music.MusicUtilities.database.onoff import is_on_off, add_on, add_off
from pyrogram.types import Message


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def gstats(_, message):
    userid = message.from_user.id
    if await is_on_off(2) and userid not in SUDOERS:
        return
    m = await message.reply_text("Running Music's speed test")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("Running Download SpeedTest")
        test.download()
        m = await m.edit("Running Upload SpeedTest")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await message.err(text=e)
        return
    m = await m.edit("Sharing SpeedTest Results")
    path = wget.download(result["share"])
    output = f"""**Speedtest Results**
    
🔘 <u>**Client:**</u>
├-☉️⇝ **__ISP:__** {result['client']['isp']}
└-☉️⇝ **__Country:__** {result['client']['country']}
  
🔘 <u>**Server:**</u>
├-☉️⇝ **__Name:__** {result['server']['name']}
├-☉️⇝ **__Country:__** {result['server']['country']}, {result['server']['cc']}
├-☉️⇝ **__Sponsor:__** {result['server']['sponsor']}
└-☉️⇝ **__Latency:__** {result['server']['latency']}  

🔘 **__Ping:__** {result['ping']}"""
    msg = await app.send_photo(chat_id=message.chat.id, photo=path, caption=output)
    os.remove(path)
    await m.delete()
