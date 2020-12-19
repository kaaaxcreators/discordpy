from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')

def main():
    return "<h1 style=\"text-align: center;\">kaaaxBOT#2292</h1><h2 style=\"text-align: center;\">Offical Discord Bot for kaaaxcreators Community</h2><iframe src=\"https://discord.com/widget?id=739612214201286758&theme=dark\" width=\"350\" height=\"500\" allowtransparency=\"true\" frameborder=\"0\" sandbox=\"allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts\" style=\"margin:auto;display:block;\"></iframe><p style=\" position: absolute; bottom: 0; left: 0; width: 100%; text-align: center;\">COPYRIGHT @ kaaaxcreators 2020</p>"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()