import os
import time
from hashlib import sha256


def get_cloudinary_timestamp():
    t = int(time.time())
    return t


def get_cloudinary_signature():

    p = {
        'cloud_name': os.environ['CLOUD_NAME'],
        'timestamp': get_cloudinary_timestamp(),
        'username': os.environ['CLOUDINARY_USER'],
        'api_secret': os.environ['API_SECRET'],
    }

    params = f"cloud_name={p['cloud_name']}&timestamp={p['timestamp']}&username={p['username']}{p['api_secret']}"
    s = sha256(params.encode('utf-8')).hexdigest()

    return s
