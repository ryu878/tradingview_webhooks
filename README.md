# Tradingview webhooks alerts listener (server)
Simple webhook listener written on Flask for saving tradingview signals (or any other) to the SQLite database.

## How to run
First you need a server. I prefer using DigitalOcean. You can get 100$ rebate if use my referal link: https://m.do.co/c/3d7f6e57bc04

Next you need to create keys:

<code>openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt</code>

Then install Flask:

<code>pip install flask</code>

Change setting in the config.py file and run the webhook_listener.py using the command

<code>python3 webhook_listener.py</code>

Note, that by default it run in debug mode. Feel free to change it on the last line in the code.

This will run the webhook server. It will listen to any alerts that will come from your tradingview webhook (check their FAQ how to create them).
And it wil save all of them to the SQLine database in the same folder.

## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch

## VPS for bots and scripts
I prefer using DigitalOcean.\n
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
