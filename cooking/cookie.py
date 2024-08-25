import browser_cookie3
import requests

url = [
    "gmail.com",       # Google
    "yahoo.com",        # Yahoo
    "outlook.com",      # Microsoft
    "hotmail.com",      # Microsoft
    "aol.com",          # AOL
    "mail.com",         # 1&1 Mail
    "icloud.com",       # Apple
    "zoho.com",         # Zoho
    "protonmail.com",   # ProtonMail
    "tutanota.com",     # Tutanota
    "yandex.com",       # Yandex
    "mail.ru",          # Mail.ru
    "gmx.com",          # GMX
    "inbox.com",        # Inbox
    "fastmail.com",     # FastMail
    "hushmail.com",     # Hushmail
    "runbox.com",       # Runbox
    "posteo.de",        # Posteo
    "lavabit.com",      # Lavabit
    "countermail.com",  # CounterMail
    "mailfence.com",    # Mailfence
    "startmail.com",    # StartMail
    "ukr.net",          # UkrNet
    "126.com",          # 126 Mail
    "163.com",          # 163 Mail
    "qq.com",           # QQ Mail
    "sina.com",         # Sina Mail
    "sohu.com",         # Sohu Mail
    "webmail.co.za",    # Webmail.co.za
    "broadband.com",    # Broadband Mail
    "blueyonder.co.uk", # Blueyonder
    "sky.com",          # Sky Mail
    "virginmedia.com"   # Virgin Media
]


for link in url:
    try:
        response = requests.get(f"https://{link}")
        cookies = response.cookies
        for cookie in cookies:
            print(f"Cookie for {link}\nName: {cookie.name}\nValue: {cookie.value}\n=============================================")
    except:
        print("connection timedout or invalid url")