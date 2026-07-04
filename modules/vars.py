#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "36122517"))
API_HASH = environ.get("API_HASH", "82b458994092391d3e8ed1a32087c744")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "8902042822"))
CREDIT = environ.get("CREDIT", " @MR_Toxic_1")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8723278238,8480660521,7988815969,6660248311,8680968748,8745263057,8703802029').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8723278238,8902042822,8480660521,7988815969,6660248311,8680968748,8745263057,8703802029').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

