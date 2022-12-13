#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>📕 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ,\n\n○ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/bots_infinity'>ᴄᴏʟʟᴇᴄᴛᴏʀ ʟᴋ | ∞™</a>\n\n○ ʟᴀɴɢᴜᴀɢᴇ: <code>ᴘʏᴛʜᴏɴ</code> \n\n○ ғʀᴀᴍᴇᴡᴏʀᴋ: <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>\n\n ○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n○ ᴠᴇʀsɪᴏɴ : 2.0\n\n○ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/bots_infinity'>ɪɴғɪɴɪᴛʏ ʙᴏᴛs</a></b>\n\n<b><a href=https://t.me/bots_infinity>©️ ɪɴғɪɴɪᴛʏ ʙᴏᴛs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔻 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
