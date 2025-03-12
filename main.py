from flask import Flask
import json

app = Flask(__name__)

@app.route("/zmena") # divi.votisek.dev/zmena
def change():
    # zde se bude menit url endpoint nfc tagu
    # budou tu potreba 2 udaje
    #   na co se to zmeni
    #   ID nfc tagu

@app.route("/redirect/<nfc_id>")
def redirect():
    with open("users.json", "w+t") as users:
        data = json.load(users)
        if nfc_id in data.keys():
            
app.run("0.0.0.0", 5001)
