import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "14263311"))
API_HASH = getenv("API_HASH", "c66911c3000c82abc7f41566520ae42c")
BOT_TOKEN = getenv("BOT_TOKEN", "7137416573:AAFod4gwCI86uEI3QG5jOM-1n46nr0UoJFQ")
STRING_SESSION = getenv("STRING_SESSION", "BAA0AS7NHigoB-so-ceRFOzmrdYJzsVtwTstFd8-_k-8SRJdvDgE0QCRa7wJ1RtoGJCdv8VY0Utiuf942RB_EPTKssh7sP1L5_lUXFMgQrVYiM3VMIiAH-FvX5Td3pXHrzbBZ1XAqPBqSr8YCDthiwzFhso9G6C8ZYztQCB70ax4NkZajApg1b0paHT2i0E3wJXEadNqpXJcDHvFVU0LYlCOhnpnVDQyC27wSHJn8YTi7LgpA8QFxs1oz0uXOF6A6a1LtM36DRWKY4FRVls8Q7o4g4ciQFuJY5rj3KZLJZvLccv3Mn0m2BHsx1nqEDcJBf463nhpRZM6wiqXmVGQp3RKAAAAAUXSSGkA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://yalay58680:yalay58680@cluster0.9y14h7v.mongodb.net/")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5466376297").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001828820002"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5466376297").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XdityaHalder/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
