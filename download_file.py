#!/usr/bin/env python3
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")
    with open(file_name[-1] ,"wb") as out_file:
        out_file.write(get_response.contents)

download("https://i.ytimg.com/vi/RcAWuwXjR2M/maxresdefault.jpg")