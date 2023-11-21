import subprocess
import os
from flask import Flask, request, jsonify
import openai
import subprocess
import os
from flask import Flask, request, jsonify
import openai

class SecureAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.route('/gpt4', methods=['POST'])(self.gpt4)
        self.app.route('/chat', methods=['POST'])(self.chat)
        self.model_name = "gpt-4.0-turbo"

    def run(self):
        try:
            self.app.run()
        except OSError as e:
            print(f"Failed to start the server: {e}")
            exit(1)

    def gpt4(self):
        try:
            data = request.get_json()
            # Your code here
        except Exception as e:
            error_response = {
                'error': str(e)
            }
            return jsonify(error_response), 500
        api_key = data['api_key']
        prompt = data['prompt']

        if not self.authenticate(api_key):
            return jsonify({'error': 'Invalid API key'}), 401

        response = self.generate_response(prompt)
        response_data = {
            'result': self.obscure_key(response)
        }
        return jsonify(response_data)

    def chat(self):
        try:
            data = request.get_json()
            api_key = data['api_key']
            messages = data['messages']

            if not self.authenticate(api_key):
                return jsonify({'error': 'Invalid API key'}), 401

            response = self.generate_response(messages)
            response_data = {
                'result': self.obscure_key(response)
            }
            return jsonify(response_data)
        except Exception as e:
            error_response = {
                'error': str(e)
            }
            return jsonify(error_response), 500

    def generate_response(self, input_data):
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        prompt = ""
        if isinstance(input_data, str):
            prompt = input_data
        elif isinstance(input_data, list):
            for message in input_data:
                role = message['role']
                content = message['content']
                prompt += f"{role}: {content}\n"

        response = openai.Completion.create(
            engine=self.model_name,
            prompt=prompt,
            max_tokens=100,
            n=3,
            stop=None,
            temperature=0.7
        )

        return [choice.text.strip() for choice in response.choices]

def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', 'flask', 'openai', 'python-dotenv'])
        os.makedirs('logs', exist_ok=True)
        os.makedirs('data', exist_ok=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install dependencies:", e)

class SecureAPI:
    def __init__(self):
        self.model_name = "gpt-4.0"

    def run(self):
        # Your code for running the API
        pass

    def gpt4(self):
        try:
            data = request.get_json()
            api_key = data['api_key']
            prompt = data['prompt']

            if not self.authenticate(api_key):
                return jsonify({'error': 'Invalid API key'}), 401

            response = self.generate_response(prompt)
            response_data = {
                'result': self.obscure_key(response)
            }
            return jsonify(response_data)

        except Exception as e:
            error_response = {
                'error': str(e)
            }
            return jsonify(error_response), 500

    def chat(self):
        # Your code for the chat endpoint
        pass

    def generate_response(self, input_data):
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        prompt = ""
        if isinstance(input_data, str):
            prompt = input_data
        elif isinstance(input_data, list):
            for message in input_data:
                role = message['role']
                content = message['content']
                prompt += f"{role}: {content}\n"

        response = openai.Completion.create(
            engine=self.model_name,
            prompt=prompt,
            max_tokens=100,
            n=3,
            stop=None,
            temperature=0.7
        )

        return [choice.text.strip() for choice in response.choices]

        response = openai.Completion.create(
            engine=self.model_name,
            prompt=prompt,
            max_tokens=100,
            n=3,
            stop=None,
            temperature=0.7
        )

        return [choice.text.strip() for choice in response.choices]


def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', 'flask', 'openai', 'python-dotenv'])
        os.makedirs('logs', exist_ok=True)
        os.makedirs('data', exist_ok=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install dependencies:", e)

if __name__ == '__main__':
    install_dependencies()
    api = SecureAPI()
    api.run()






