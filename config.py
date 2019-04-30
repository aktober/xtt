import dotenv
import os

dotenv.load_dotenv()

# Note: set False for production
DEBUG = True


def get_key(key):
    val = os.environ[key] if key in os.environ else os.getenv(key)
    if not val:
        print(f'Error: <{key}> missed. Check instance env variables')
    return val


OER_API_KEY = get_key('OER_API_KEY')

# DATABASE
DB_HOST = get_key('DB_HOST')
DB_PORT = get_key('DB_PORT')
DB_NAME = get_key('DB_NAME')
DB_USER = get_key('DB_USER')
DB_PASSWORD = get_key('DB_PASSWORD')

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
