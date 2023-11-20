import subprocess
import os
import subprocess
import os

# Install required packages
try:
    subprocess.check_call(['pip', 'install', 'openai', 'flask'])
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    print("Failed to install dependencies:", e)

import openai
from flask import Flask, request, jsonify

class GPT4API:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.route('/gpt4', methods=['POST'])(self.gpt4)
        self.api_key = os.environ.get('OPENAI_API_KEY')  # Get the API key from environment variable
        self.model_name = "gpt-4.0-turbo"  # Replace with the desired GPT 4.0 model name

    def run(self):
        self.app.run()

    def gpt4(self):
        try:
            data = request.get_json()
            prompt = data['prompt']
            
            # Perform GPT 4.0 processing here
            response = self.generate_response(prompt)
            
            response_data = {
                'result': response
            }
            return jsonify(response_data)
        except Exception as e:
            error_response = {
                'error': str(e)
            }
            return jsonify(error_response), 500

    def generate_response(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine=self.model_name,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()

if __name__ == '__main__':
    api = GPT4API()
    api.run()

def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', 'flask', 'openai', 'python-dotenv'])
        # Add any other dependencies you need to install here
        # Example: subprocess.check_call(['pip', 'install', 'dependency_name'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install dependencies:", e)

if __name__ == '__main__':
    install_dependencies()
