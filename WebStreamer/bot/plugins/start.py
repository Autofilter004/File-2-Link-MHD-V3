# Β© @AvishkarPatil [ Telegram ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<b>π Hello Buddy {}

π Send Me Any File Or Media From Telegram..!!

π I Will Provide External Direct Download Link..!!

β Add Me In Your Channel For Direct Download Links In Button..!!

β»οΈ Generate Link Is Permanent 

β³ With Fastest Speed Like 37mb/s\n

π¨βπ¬ This Bot Owner Is : <a href="https://t.me/mhd_thanzeer"> π ππ_π§πππ‘π­πππ₯</a></b>"""

HELP_TEXT = """<b>π Send Me Any File Or Media From Telegram..!!\n\n
π I Will Provide External Direct Download Link..!!\n\n
β Add Me In Your Channel For Direct Download Links In Button..!!\n\n
β»οΈ Generate Link Is Permanent\n
β³ With Fastest Speed 37mb/s\n\n
π¨βπ¬ This Bot Owner Is : <a href='https://telegram.me/mhd_thanzeer'>π ππ_π§πππ‘π­πππ₯</a></b>"""

ABOUT_TEXT = """
<b>π Bot Name : File 2 Link Bot</b>\n
<b>πΈVersion : <a href='https://telegram.me/mhd_thanzeer'>3.6.8</a></b>\n
<b>πΉDeveloper : <a href='https://telegram.me/mhd_thanzeer'>π ππ_π§πππ‘π­πππ₯</a></b>\n
<b>πΈLast Update : <a href='https://telegram.me/mhd_thanzeer'> 26 - September - 2021 || 11:00 PM</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined π₯³:** \n\n__My New Friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Started Your Bot!!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sorry Sir, You Are Banned To Use Me. Contact The Developer\n\n @mhd_thanzeer **They Will Help You**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Join My Movies Group To Use Me  π</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("JOIN  NOW π", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Something Went Worng Contact My Owner </b> <b><a href='http://t.me/mhd_thanzeer'>π ππ_π§πππ‘π­πππ₯</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You Are Banned To Use Me. Contact The Developer\n\n @mhd_thanzeer **They Will Help You**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Please Join My Group To Use This Bot \n\n Dude To Overload, Only Join My Group You Can Use The Bot<\b>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("β‘οΈ  JOIN MY GROUP  β¬οΈ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Something Went Worng Contact My Owner </b> <b><a href='http://t.me/mhd_thanzeer'>π ππ_π§πππ‘π­πππ₯</a></b>",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
<b><u>π¬πΌππΏ ππΆπ»πΈ ππ²π»π²πΏπ?ππ²π± !</u></b>\n
<b>π File Name :</b> <b>{}</b>\n
<b>π¨ File Size :</b> <b>{}</b>\n
<b>π₯ Download :</b> <code>{}</code>\n
<b>β­οΈ Note : Link Expired in Bot Off Time </b>\n
<b>π¨βπ¬ Developer : <a href='http://t.me/mhd_thanzeer'>π ππ_π§πππ‘π­πππ₯</a></b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("π₯ Download Now π₯", url=stream_link)]])
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined **\n\n__My New Friend__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sorry Sir, You Are Banned To Use Me. Contact The Developer\n\n @mhd_thanzeer They Will Help You</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Join My Group To Use This Bot !**\n\n__Due To Overload, Only Join My Group To Use Me!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("β­οΈ JOIN MY GROUP β­οΈ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Something Went Worng..!! Contact Me __ [π ππ_π§πππ‘π­πππ₯](http://t.me/mhd_thanzeer)",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
