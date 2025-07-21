# Waste Separation Chatbot - Dialogflow Implementation

A conversational AI chatbot built with **Dialogflow** and **Flask** that helps users in Frankfurt am Main with waste separation and disposal information. The chatbot provides accurate disposal instructions for various waste items based on data from the Frankfurt Recycling Center.

## Features

- **Waste Classification**: Uses Dialogflow's natural language processing to understand user queries about waste disposal
- **Database**: Contains disposal information for hundreds of waste items from Frankfurt's recycling center
- **Fuzzy Matching**: Implements intelligent matching to handle variations in item names and spelling

## Architecture

```
WasteSeparationChatbotDialogflow/
├── app.py                 # Main Flask application
├── services/
│   ├── answer.py         # Response generation logic
│   ├── database.py       # Database query operations
│   └── request.py        # Dialogflow request parsing
├── data/
│   ├── create_db.py      # Database creation script
│   └── AbfallABC_RecyclingZentrumFrankfurt.xlsx  # Source data
├── templates/
│   └── index.html        # Web interface
├── static/               # Static assets (logos)
└── abfallABC_entsorgung.db  # SQLite database
```

## Data Source

The chatbot uses data from the [Frankfurt Recycling Center's Waste ABC](https://www.recyclingzentrum-frankfurt.de/abfall-abc), which contains comprehensive information about:
- Waste item names (Abfallart)
- Disposal methods (Entsorgungsweg)
- Disposal locations and addresses
- Additional information links

## Configuration

### Dialogflow Setup

1. **Create Intent**: Set up an intent for waste disposal queries
2. **Add Parameters**: Include `EntsorgungsItem` as a required parameter
3. **Configure Webhook**: Point to your Flask endpoint `/process-waste-item-query`
4. **Training Phrases**: Add example phrases like:
   - "Wie entsorge ich [item]?"
   - "Wo kann ich [item] wegwerfen?"
   - "Wohin mit [item]?"

### Environment Variables

Create a `.env` file (optional):
```env
FLASK_ENV=development
DIALOGFLOW_PROJECT_ID=your-project-id
```

## 🛠️ API Endpoints

### POST `/process-waste-item-query`

Processes waste disposal queries from Dialogflow.

**Request Body:**
```json
{
  "queryResult": {
    "parameters": {
      "EntsorgungsItem": "Batterien"
    }
  }
}
```

**Response:**
```json
{
  "fulfillmentText": "Der Entsorgungsort für Batterien ist Recyclingzentrum bei der folgenden Adresse: Adresse hier. Du findest weitere Informationen hier: https://link.com"
}
```

## How It Works

1. **User Input**: User asks about disposing of a specific item
2. **Dialogflow Processing**: Dialogflow extracts the item name using NLP
3. **Webhook Call**: Dialogflow sends the request to Flask app
4. **Database Query**: App searches the database using fuzzy matching
5. **Response Generation**: App constructs a natural language response
6. **User Feedback**: Response is sent back to the user

### Example curl command:
```bash
curl -X POST http://localhost:5000/process-waste-item-query \
  -H "Content-Type: application/json" \
  -d '{"queryResult":{"parameters":{"EntsorgungsItem":"Batterien"}}}'
```
## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Dialogflow account and project
- Basic knowledge of Flask and web development

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/WasteSeparationChatbotDialogflow.git
   cd WasteSeparationChatbotDialogflow
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   cd data
   python create_db.py
   cd ..
   ```

4. **Configure Dialogflow**
   - Create a new Dialogflow project
   - Set up an intent for waste disposal queries
   - Configure the webhook URL to point to your Flask app
   - Add the `EntsorgungsItem` parameter to capture the waste item name

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the chatbot**
   - Open your browser and go to `http://localhost:5000`
   - Or integrate the Dialogflow agent into your preferred platform
   
## 🙏 Acknowledgments

- [Frankfurt Recycling Center](https://www.recyclingzentrum-frankfurt.de/) for providing the waste disposal data
- [Dialogflow](https://dialogflow.com/) for the conversational AI platform
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) for fuzzy string matching
