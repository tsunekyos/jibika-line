from dotenv import load_dotenv
load_dotenv()

import os
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', '')
LINE_USER_ID = os.getenv('LINE_USER_ID', '')
WEBSITE_URL = os.getenv('WEBSITE_URL', '')
WEBSITE_CARD_ID = os.getenv('WEBSITE_CARD_ID', '')
WEBSITE_BIRTHDAY = os.getenv('WEBSITE_BIRTHDAY', '')
