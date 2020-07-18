#!/usr/bin/env python3

import os
import shutil
import requests
import re

BASE_DIR = os.path.dirname(os.path.abspath("__FILE__"))
DL_DIR = os.path.join(BASE_DIR, "Downloads")
try:
    os.makedirs(DL_DIR)
except FileExistsError:
    pass

def file_downloader(url=None, fname=None):
    pattern = r'^http.'
    if re.search(pattern, url) is None:
        print("Sorry, only http urls are supported. ")
        return
    else:
        print("Trying to fetch file..")

    if fname is None or fname.strip() == "": # if file name is not provided
        fname = os.path.basename(url)
    else:
        extension = url.split('.')[-1]
        fname = fname.strip()+'.'+extension.strip()

    fpath = os.path.join(DL_DIR, fname)

    try:
        with requests.get(url, stream=True) as response:
            with open(fpath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=128):
                    f.write(chunk)
    except:
        print("Couldn't fetch file please check URL..")
        return

    print("Fetched file {} successfully..".format(fname))

if __name__ == '__main__':
    print("=="*50)
    print("=="*50)
    url = input("Enter url: ")
    fname = input("Save as:")
    file_downloader(url, fname)
    print("=="*50)
    print("=="*50)
