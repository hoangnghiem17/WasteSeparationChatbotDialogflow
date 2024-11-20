import logging

from flask import Flask, request, jsonify, render_template

from utils import get_entsorgungsinfo

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fulfillment', methods=['POST'])
def fulfillment():
    req = request.get_json()
    logging.debug(f"Incoming request: {req}")  # Log the entire request payload

    item_name = req['queryResult']['parameters'].get('EntsorgungsItem')  # Extract the item
    logging.debug(f"Extracted item name: {item_name}")  # Log the extracted item

    if item_name:
        entsorgungsinfo = get_entsorgungsinfo(item_name)
        if entsorgungsinfo:
            entsorgungsort, adresse, link = entsorgungsinfo
            response_text = f"Der Entsorgungsort für {item_name} ist {entsorgungsort} bei der folgenden Adresse: {adresse}. Du findest weitere Informationen zu der Adresse hier: {link}"
        else:
            response_text = f"Für {item_name} konnte ich leider keinen Entsorgungsort finden."
    else:
        response_text = "Bitte nenne mir das Item, welches du entsorgen möchtest."

    logging.debug(f"Response text: {response_text}")  # Log the response text
    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(debug=True)
