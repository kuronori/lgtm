#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:18:41 2020

@author: TakahiroKurokawa
"""


import requests

class LocalImage:
    def __init__(self,path):
        self._path = path
    
    def get_image(self):
        return open(self._path,"rb")


from io import BytesIO

class RemoteImage:
    """URLから画像を取得する"""
    def __init__(self,path):
        self._url = path
    
    def get_image(self):
        data = requests.get(self._url)
        #バイトデータをファイルオブジェクトに変換
        return BytesIO(data.content)

class _LoremFlicker(RemoteImage):
    """キーワード検索で画像を取得する"""
    LOREM_FLICKER_URL = "https://loremflicker.com"
    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self,keyword):
        super().__init__(self._build_url(keyword))
    
    def _build_url(self,keyword):
        return (f"{self.LOREM_FLICKER_URL}/"
                f"{self.WIDTH}/{self.HEIGHT}/{keyword}")

KeywordImage = _LoremFlicker


from pathlib import Path

#コンストラクタとして利用するため
#単語を大文字始まりにしてクラスのように見せる
def ImageSource(keyword):
    """最適なイメージソースクラスを返す"""
    if keyword.startswith(("http://","https://")):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)

def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()