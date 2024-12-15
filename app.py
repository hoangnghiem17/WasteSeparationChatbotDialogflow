import logging

from flask import Flask, request, jsonify, render_template

from services.answer import generate_response
from services.request import extract_parameter

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG to capture all logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Format the log messages
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-waste-item-query', methods=['POST'])
def process_waste_item_query():
    req = request.get_json()  # Get the JSON request from Dialogflow
    item_name = extract_parameter(req, 'EntsorgungsItem')  # Extract the 'EntsorgungsItem' parameter
    
    if item_name:
        response_text = generate_response(item_name)
    else:
        response_text = "Bitte nenne mir das Item, welches du entsorgen möchtest."
    
    logging.debug(f"Response text: {response_text}")
    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(debug=True)
