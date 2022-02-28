import hashlib
import pandas as pd

def hash_params(timestamp, priv_key, pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def json_to_df(data):

    my_dict = {'id': [],
           'name': [],
           'picture_url': [] }

    for elem in data['data']['results']:
        my_dict['id'].append(elem.get('id', 'no_id'))
        my_dict['name'].append(elem.get('name', 'no_name'))
        url_pic = elem.get('thumbnail', 'no_thumbnail').get('path', 'no_path') + '.' + elem.get('thumbnail', 'no_thumbnail').get('extension', 'no_extension')
        my_dict['picture_url'].append(url_pic)
        
    df_results = pd.DataFrame(my_dict)
    return df_results