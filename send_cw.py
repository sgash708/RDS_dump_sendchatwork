# -*- coding: utf-8 -*-
import os
import time
import sys
import requests
import ConfigParser
import datetime
import subprocess

sys.stderr.write('処理開始')

# ------------------
# 定数呼び出し
# ------------------
conf = ConfigParser.SafeConfigParser()
conf.read('./config.ini')

# ------------------
# シェルスクリプト実行
# ------------------
subprocess.call(['sudo', 'sh', conf.get('fileinfo', 'shell_path')])
sys.stderr.write('シェルスクリプト実行中です。5秒待ちます。')
time.sleep(5)

# ------------------
# ファイル情報呼び出し
# ------------------
today = datetime.date.today()
file_name = today.strftime('%Y%m%d') + conf.get('fileinfo', 'after_path')
file_path = conf.get('fileinfo', 'before_path') + file_name

if os.path.exists(file_path) == False :
    sys.stderr.write("ファイルは存在しません。\r処理を終了します。")

# ------------------
# チャットワーク通知
# ------------------
file_data = open(file_path, 'rb').read()
post_files = {
    'file': (file_name, file_data, 'text/plain')
}
post_data = {
    "message": conf.get('chatwork', 'HEAD')
}

url = conf.get('chatwork', 'URL')
post_url = url
post_headers = {'X-ChatWorkToken': conf.get('chatwork', 'TOKEN')}
requests.post(
    post_url,
    headers=post_headers,
    files=post_files,
    data=post_data,
)


