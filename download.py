import random

import requests
import os


def downloadImage(url: str):
    try:
        filename = f'{random.randint(0, 10000)}{random.randint(0, 10000)}{random.randint(0, 10000)}.jpg'
        print(filename)
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(url)
        print(r.status_code)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename, 'wb') as f:
                f.write(r.content)

            print('Image successfully Downloaded: ', filename)
            return filename
    except:
        raise Exception("Could not download image")

def deleteImage(path: str):
    os.remove(path)
