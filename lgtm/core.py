#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 09:41:39 2020

@author: TakahiroKurokawa
"""


import click

@click.command()
def cli():
    """LGTM画像生成ツール"""
    lgtm()
    click.echo("lgtm") #動作確認用

def lgtm():
    #ここにロジックを追加していく
    pass
