# Announcement: Discontinuation of Free Bots for Bybit 
I regret to inform that I will no longer be updating or maintaining my free trading bots for the Bybit exchange. This decision comes after a deeply disappointing experience with Bybit's unethical practices, particularly regarding their affiliate program and their handling of user earnings.

Despite fully complying with Bybit's rules, including completing KYC (Know Your Customer) requirements, my affiliate earnings were abruptly terminated without valid justification. Bybit cited "one IP address" as the reason, a claim that is both unreasonable and unfair, especially for users in shared living environments or using shared internet connections. This behavior demonstrates a lack of transparency and fairness, and it has eroded my trust in Bybit as a reliable platform.

I want to thank everyone who has supported my work and used my free bots for Bybit. Your trust and feedback have been invaluable, and I hope to continue providing value to the crypto community through my future projects. Stay tuned for updates, and feel free to reach out if you have any questions or need assistance during this transition.

Thank you for your understanding and support.

---

# Tradingview webhooks alerts listener (server)
Simple webhook listener written on Flask for saving tradingview signals (or any other) to the SQLite database.

## How to run
First you need a server.

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
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf

## Crypto Exchanges

😎 Register on BingX and get a 20% discount on fees: https://bingx.com/invite/HAJ8YQQAG/

👍 MEXC: https://promote.mexc.com/r/f3dtDLZK

🐀 Join Bybit: https://www.bybit.com/invite?ref=P11NJW

## VPS for bots and scripts
I prefer using DigitalOcean.
  
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
  
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
