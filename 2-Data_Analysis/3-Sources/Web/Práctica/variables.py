import datetime
from funciones import hash_params

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

# Rellenar con tus claves!
pub_key = ''
priv_key = ''

params = {'ts': timestamp, 
        'apikey': pub_key, 
        'hash': hash_params(timestamp, priv_key, pub_key)};

url = 'http://gateway.marvel.com/v1/public/characters'