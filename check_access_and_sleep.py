import os
from datetime import datetime, timedelta

HEROKU_APP_NAME = 'bmhien1'
HEROKU_API_KEY = 'your_heroku_api_key'

def get_last_access_time():
    try:
        with open('/tmp/last_access.txt', 'r') as f:
            last_access_time = f.read().strip()
            return datetime.strptime(last_access_time, '%Y-%m-%d %H:%M:%S.%f')
    except Exception as e:
        return None

def put_app_to_sleep():
    os.system(f"heroku ps:scale web=0 --app {HEROKU_APP_NAME} --api-key={HEROKU_API_KEY}")

def main():
    last_access_time = get_last_access_time()
    if last_access_time and datetime.now() - last_access_time > timedelta(minutes=10):
        put_app_to_sleep()

if __name__ == '__main__':
    main()
