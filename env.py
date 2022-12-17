from dotenv import load_dotenv
load_dotenv()

import os
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_BEARER_TOKEN')
LINE_USER_ID=os.getenv('LINE_TO')
