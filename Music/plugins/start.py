import yt_dlp
from pyrogram import filters
from pyrogram import Client
from Music import app, SUDOERS, BOT_ID, BOT_USERNAME, OWNER
from Music import dbb, app, BOT_USERNAME, BOT_ID, ASSID, ASSNAME, ASSUSERNAME
from Music.MusicUtilities.helpers.inline import start_keyboard, personal_markup
from Music.MusicUtilities.helpers.thumbnails import down_thumb
from Music.MusicUtilities.helpers.ytdl import ytdl_opts
from Music.MusicUtilities.helpers.filters import command
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Music.MusicUtilities.database.chats import (
    get_served_chats,
    is_served_chat,
    add_served_chat,
    get_served_chats,
)
from Music.MusicUtilities.database.queue import (
    is_active_chat,
    add_active_chat,
    remove_active_chat,
    music_on,
    is_music_playing,
    music_off,
)
from Music.MusicUtilities.database.sudo import get_sudoers, get_sudoers, remove_sudo


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = f"[{user_name}](tg://user?id={str(user_id)})"
        await app.send_message(
            message.chat.id,
            parse_mode="markdown",
            reply_to_message_id=message.message_id,
        )
    elif len(message.command) == 2:
        query = message.text.split(None, 1)[1]
        f1 = query[0]
        f2 = query[1]
        f3 = query[2]
        finxx = f"{f1}{f2}{f3}"
        if str(finxx) == "inf":
            query = (str(query)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = x["thumbnail"]
            searched_text = f"""
🔍__**Video Track Information**__

🔘 {x["title"]}   
├-☉️⇝ ⏳**Duration:** {round(x["duration"] / 60)} Mins
├-☉️⇝ 👀**Views:** `{x["view_count"]}`
├-☉️⇝ 👍**Likes:** `{x["like_count"]}`
├-☉️⇝ 👎**Dislikes:** `{x["dislike_count"]}`
├-☉️⇝ ⭐️**Average Ratings:** {x["average_rating"]}
├-☉️⇝ 🎥**Channel Name:** {x["uploader"]}
├-☉️⇝ 📎**Channel Link:** [Visit From Here]({x["channel_url"]})
└-☉️⇝ 🔗**Link:** [Link]({x["webpage_url"]})

⚡️ __Searched Powered By Aries Music Bot__"""
            link = x["webpage_url"]
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(
                message.chat.id,
                photo=thumb,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**__Sudo Users List Of Aries Music:-__**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue
                text += f"➤ {user}\n"
            if not text:
                await message.reply_text("No Sudo Users")
            else:
                await message.reply_text(text)
