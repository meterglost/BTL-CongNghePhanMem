import secrets

env = f'''
COMPOSE_PROJECT_NAME=BTL-CNPM
TZ=Asia/Ho_Chi_Minh

MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD={secrets.token_urlsafe(16)}
'''

try:
    with open('.env', 'xt') as f:
        f.write(env.lstrip('\n'))
except FileExistsError:
    print('.env file existed! Aborting...')
