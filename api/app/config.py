import os
from dotenv import load_dotenv

load_dotenv()

S3_USER = os.environ.get("S3_USER") 
S3_PASSWORD = os.environ.get("S3_PASSWORD")
S3_NAME = os.environ.get("S3_NAME")
S3_HOST = os.environ.get("S3_HOST")
S3_PORT = os.environ.get("S3_PORT")
S3_URL = os.environ.get("S3_URL")
API_URL = os.environ.get("API_URL")