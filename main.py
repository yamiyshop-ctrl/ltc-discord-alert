import requests
import time
import os

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PRICE_TARGET = 72.0
alert_sent = False

if not WEBHOOK_URL:
    raise Exception("WEBHOOK_URL manquant")

def get_ltc_price():
    r = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "litecoin", "vs_currencies": "usd"},
        timeout=10
    )
    return r.json()["litecoin"]["usd"]

print("🚀 Bot LTC démarré")

while True:
    try:
        price = get_ltc_price()
        print("LTC:", price)

        if price >= PRICE_TARGET and not alert_sent:
            requests.post(WEBHOOK_URL, json={
                "content": f"🚨 **ALERTE LTC** 🚨\nLitecoin a atteint **{price}$**"
            })
            alert_sent = True

    except Exception as e:
        print("Erreur:", e)

    time.sleep(60)
