class script(object):
    START_TXT = """π§i {}, <b>π­ππΌπΎ ππ ππΎπΎπ πππ π</b>
<i>π¨'π ππππ πΊ ππππππΎ πππΎ - πΏπππΌπππππΎπ½ πΊππππΏππππΎπ π»ππ</i>

<i>iππ πΎπΊππ ππ πππΎ ππΎ; ππππ πΊπ½π½ ππΎ ππ ππππ πππππ πΊπ πΊπ½πππ, πππ /help πΏππ ππππΎ</i>
"""
    HELP_TXT = """<b>π§πΎππΎ ππ πππΎ π΄πππΊπ πΌππππΊππ½π:</b> 
/start - πΌππΎπΌπ πππΎπππΎπ ππ ππππππΎ 
/help - ππΎπ ππππ ππΎππ ππΎπππΊππΎ
/about - πΊπ»πππ ππΎ
"""
    GTRANS_TXT = """<b>π³ππΊππππΊπππ</b>
- π³ππΊππππΊππΎ ππΎπππ ππ πΊ πππΎπΌππΏππΌ ππΊππππΊππΎ!
<b>π’ππππΊππ½π πΊππ½ π΄ππΊππΎ:</b>
- /tr [language code][reply] - π³ππΊππππΊππΎ ππΎππππΎπ½ ππΎπππΊππΎ ππ πππΎπΌππΏππΌ ππΊππππΊππΎ.

π¬πΊπ½πΎ π»π @ADHOLOKAMHDCHANNEL β€οΈ
"""
    PASTE_TXT = """<b>π―πΊπππΎ</b>
- π―πΊπππΎ ππππΎ ππΎπππ ππ π½ππΌπππΎπππ ππ πΊ ππΎπ»ππππΎ!
<b>π’ππππΊππ½π πΊππ½ π΄ππΊππΎ:</b>
- /paste [text] - π―πΊπππΎ πππΎ ππππΎπ ππΎππ ππ ππΊπππ
- /paste [reply] - π―πΊπππΎ πππΎ ππΎππππΎπ½ ππΎππ ππ ππΊπππ

π¬πΊπ½πΎ π»π @ADHOLOKAMHDCHANNELβ€οΈβ€οΈ
"""
    STICK_TXT = """<b>π²πππΌππΎπ π¨π£</b>
- π³πππ πΌππππΊππ½ ππ πππΎπ½ ππ ππΎπ πΊ π¨π£ ππΏ πΊπ ππππΌππΎπ

<b>Command</b>
- /stickerid - π¦πΎπ π¨π£

π¬πΊπ½πΎ π»π @ADHOLOKAMHDCHANNEL β€οΈ
"""
    ABOUT_TXT = """
β π¬π π­πΊππΎ : <a href='https://t.me/Naruto_ahautofilterbot'>π¨π·αα©ααTO</a>
β π’ππΎπΊπππ : <a href='https://t.me/TEAM_KERALA'>α΄ααK Oα΄α΄π¨π·[π’πππππ‘π]</a>
β π«πΊππππΊππΎ : π―πππππ π₯ 
β π«ππ»ππΊππ : π―ππππππΊπ πΊππππΌππ π’.π£π©.π£ 
β π²πΎπππΎπ : <a href='https://www.heroku.com'>π§πΎππππ</a>
β π£πΊππΊπ»πΊππΎ : <a href='https://www.mongodb.com'>π¬πππππ£π‘ π₯ππΎπΎ π³ππΎπ</a>
β π‘ππππ½ π²ππΊπππ : π΅8.π© [π¬πΊπππ]
"""
    SOURCE_TXT = """<b>NOTE:</b>
- Sakura is a closed source project.   

<b>DEVS:</b>
- <a href='https://t.me/TEAM_KERALA'>α΄ααK Oα΄α΄π¨π·[π’πππππ‘π]</a>
- <a href='https://t.me/HAZARD_77'>Sha__</a>

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /index  - <code>to add files from a channel</code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """π³πππΊπ π₯πππΎπ: <code>{}</code>
π³πππΊπ π¬πΎππ»πΎππ: <code>{}</code>
π³πππΊπ π’ππΊππ: <code>{}</code>
π΄ππΎπ½ π²ππππΊππΎ: <code>{}</code> πΌππ±
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
