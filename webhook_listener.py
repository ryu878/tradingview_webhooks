# Ryuryu's TradingView Webhook Listener
# SQLite Edition (Production Mode #6973)
# -------------------------------------
# (c) 2023 Ryan Hayabusa 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: https://discord.gg/zSw58e9Uvf
# Telegram: https://t.me/aadresearch
# -------------------------------------
# openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
# {
# "command": "buy",
# "symbol": {{ticker}}
# }

from flask import Flask, request
from config import *
import sqlite3
import datetime
import threading
import time



ver = '1.0:110323.1329'

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    timestamp = str(datetime.datetime.now())
    status = 'new'
    data = request.get_json()
    conn = sqlite3.connect('webhooks.db')
    c = conn.cursor()
    c.execute("INSERT INTO webhook_data (data, timestamp, status) VALUES (?, ?, ?)", (str(data), timestamp, status))
    conn.commit()
    conn.close()
    return 'Webhook received and saved to database'


def create_table():
    conn = sqlite3.connect('webhooks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS webhook_data (
        data TEXT,
        timestamp TEXT, 
        status TEXT
        )
        ''')
    conn.commit()
    conn.close()


create_table()


def delete_old_records():
    while True:
        conn = sqlite3.connect('webhooks.db')
        c = conn.cursor()
        c.execute("DELETE from webhook_data WHERE timestamp <= date('now', '-1 day')")
        conn.commit()
        conn.close()
        time.sleep(3600) # repeat the task every hour


if __name__ == '__main__':
    delete_thread = threading.Thread(target=delete_old_records)
    delete_thread.start()
    app.run(debug=True, host=wh_host, port=wh_port, ssl_context=(crt, key))
