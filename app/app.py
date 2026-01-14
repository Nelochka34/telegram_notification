from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/checkpoint_alerts', methods=['POST'])
def checkpoint_alerts():
    proxies = { "http" : "http://address:8080", "https" : "http://address:8080" }
    settings = {}
    settings['bot_token'] = "add_bot_token"
    settings['netsec_chat_id'] = "add_netsec_chat_id"
    request.get_data()
    msg = request.data.decode('utf-8')
    res = requests.post("https://api.telegram.org/bot" + settings['bot_token'] + "/sendMessage", data={'chat_id': settings['netsec_chat_id'], 'text': msg}, proxies = proxies)
    return("ok")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5002)
