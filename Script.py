import os
class script(object):
    
    START_TXT = """<b>Hi, I am {} {}

 ➠ I'm Only Work For <a href=https://t.me/M2LMOVIEZ>M➋LMOVIEZ</a>

 ➠ Join Our Group For More Movies & Series Working 24/7></b>"""
    
    HELP_TXT = """<b><i>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</i></b>"""
    
    CODEXBOTS = """<b><i>/upload - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴘᴍ</i></b>"""
 
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    IMDB_TEMPLATE_TXT = """<b>📻 ᴛɪᴛʟᴇ - <a href={url}>{title}</a>
🎭 ɢᴇɴʀᴇs - {genres}
🎖 ʀᴀᴛɪɴɢ - <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)
📆 ʏᴇᴀʀ - {release_date}
❗️ ʟᴀɴɢᴜᴀɢᴇ - {languages}</b>
"""

    FILE_CAPTION = """<b>{filename}
    ━═━═━═━═━═━═━═━═━═
ɢʀᴏᴜᴘ    ➧ @M2LGROUPz1
ᴄʜᴀɴɴᴇʟ ➧ @M2L_Backup
ᴄʜᴀɴɴᴇʟ ➧ @M2LMOVIEZ

<i>ᴘʟᴇᴀsᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪs ꜰɪʟᴇs ᴛᴏ ᴛʜᴇ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴄʟᴏsᴇ ᴛʜɪs ᴍᴇssᴀɢᴇ</i></b>"""

    RESTART_TXT = """<b>
📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """❌ 𝗧𝗵𝗮𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 𝘀𝗶𝗿 ⛔️"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""

    NO_RESULT_TXT = """🗳 𝗧𝗵𝗶𝘀 𝗠𝗼𝘃𝗶𝗲 𝗶𝘀 𝗻𝗼𝘁 𝘆𝗲𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱 𝗼𝗿 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 🗳"""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗻𝗮𝗺𝗲.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 😞... 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

I couldn't find anything related to that. Did you mean any one of these movies? 👇

நான் அதற்கு தொடர்புடைய எதையும் கண்டுபிடிக்க முடியவில்லை. இதில் எந்த ஒரு திரைப்படத்தை நீங்கள் குறிப்பிடுகிறீர்களா? 👇"""
    
    FONT_TXT= """<b><i>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ.</i></b>

<code>/font hi how are you</code>"""

    PREMIUM_TEXT = """<b><i><blockquote>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs  ♻️</blockquote>

• 𝟷 ᴡᴇᴇᴋ  -  ₹𝟹𝟶
ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴠᴇʀsɪᴏɴ.</i></b>"""

    EARN_TEXT = """<b><i><blockquote>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴛʜɪs ʙᴏᴛ  🤑</blockquote>

›› sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 𝟹𝟶𝟶 ᴍᴇᴍʙᴇʀs.

›› sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ <a href=https://telegram.me/{}</a> ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

›› sᴛᴇᴘ 𝟹 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href='https://tnshort.net/ref/devilofficial'>ᴛɴʟɪɴᴋ</a> ᴏʀ <a href='https://onepagelink.in/ref/Nobita'>ᴏɴᴇᴘᴀɢᴇʟɪɴᴋ</a>. [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

›› sᴛᴇᴘ 𝟺 : ɴᴏᴡ ꜱᴇᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ, ᴛᴜᴛᴏʀɪᴀʟ, ꜰꜱᴜʙ ᴀɴᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.

›› sᴛᴇᴘ 𝟻 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href='https://github.com/TechifyBots/Auto-Filter-Bot/blob/main/README.md'>ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ</a>.

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴠᴀʟᴜᴇꜱ ʙʏ /ginfo ᴄᴏᴍᴍᴀɴᴅ.

💯 ɴᴏᴛᴇ - ᴛʜɪs ʙᴏᴛ ɪs ꜰʀᴇᴇ ᴛᴏ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ᴇᴀʀɴ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏɴᴇʏ.</i></b>"""

    VERIFICATION_TEXT = """<b>ʜi {} {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ 😐
ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ. (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote>

ᴄʜᴇᴄᴋ /plan ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ...</b>"""

    VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 𝟷sᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ...

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ❤️‍🔥

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😁</b>"""

    SECOND_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ 😐
ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ. (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 𝟸ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ...

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ❤️‍🔥

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😁</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ‼️
ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛᴏᴅᴀʏ 😇

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ. (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>ʜʏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪꜰɪᴇᴅ ꜰᴏʀ ᴛᴏᴅᴀʏ ☺️

ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ ᴏʀ ᴀɴɪᴍᴇ 💥

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😁</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verification_{}_completed"""

    CUSTOM_TEXT = """<b><i>😊 <u>ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ</u> 😊
    
/shortlink - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ
/shortlink2 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰᴏʀ 𝟸ɴᴅ ᴠᴇʀɪꜰʏ
/shortlink3 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰᴏʀ 𝟹ʀᴅ ᴠᴇʀɪꜰʏ
/time2 - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ
/time3 - ᴛᴏ ꜱᴇᴛ 𝟹ʀᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ
/log - ᴛᴏ ꜱᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴜꜱᴇʀꜱ ᴅᴀᴛᴀ
/tutorial - ᴛᴏ ꜱᴇᴛ 𝟷ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/tutorial2 - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/tutorial3 - ᴛᴏ ꜱᴇᴛ 𝟹ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/caption - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰɪʟᴇ ᴄᴀᴘᴛɪᴏɴ
/template - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ
/fsub - ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ
/nofsub - ᴛᴏ ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ
/ginfo - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟꜱ</i></b>

😘 𝑰𝒇 𝒚𝒐𝒖 𝒅𝒐 𝒂𝒍𝒍 𝒕𝒉𝒊𝒔 𝒕𝒉𝒆𝒏 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑 𝒘𝒊𝒍𝒍 𝒃𝒆 𝒗𝒆𝒓𝒚 𝑪𝒐𝒐𝒍..."""

    FSUB_TXT = """{},

<i><b>🙁 ꜰɪʀꜱᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴍᴏᴠɪᴇ, ᴏᴛʜᴇʀᴡɪꜱᴇ ʏᴏᴜ ᴡɪʟʟ ɴᴏᴛ ɢᴇᴛ ɪᴛ.

ᴄʟɪᴄᴋ ᴊᴏɪɴ ɴᴏᴡ ʙᴜᴛᴛᴏɴ 👇</b></i>"""

    DONATE_TXT = """<blockquote>❤️‍🔥 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</blockquote>

<b><i>💞</code>
"""
    
