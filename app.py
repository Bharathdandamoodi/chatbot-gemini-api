from flask import Flask, render_template, request, jsonify
from configparser import ConfigParser
from chatbot import ChatBot

app = Flask(__name__)

# Load API key from credentials.ini
config = ConfigParser()
config.read('credentials.ini')
api_key = config['gemini_ai']['API_KEY']

# Initialize chatbot
chatbot = ChatBot(api_key=api_key)
chatbot.start_conversation()

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('chatbot_gui.html')

# Route to handle user input and return bot response
@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']

    try:
        response = chatbot.send_prompt(user_input)
        return jsonify({'bot_response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
