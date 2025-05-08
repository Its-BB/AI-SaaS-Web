from flask import Flask, request, Response, send_file
from flask_cors import CORS
from llama_cpp import Llama
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Load the GGUF model
model_path = "models/phi-2.Q5_0.gguf"
try:
    llm = Llama(
        model_path=model_path,
        n_ctx=1024,  # Context length
        n_threads=2,  # Reduced for stability
        temperature=0.7,
        top_p=0.9,
        max_tokens=256  # Max tokens per response
    )
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise

# Simple conversation history (last interaction only)
conversation_history = []

@app.route('/')
def serve_frontend():
    logger.debug("Serving frontend")
    return send_file('static/index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    logger.debug(f"Received user message: {user_message}")

    def generate_response():
        try:
            # Update conversation history (keep only last interaction)
            if len(conversation_history) > 2:  # Keep user + assistant pair
                conversation_history.pop(0)
            conversation_history.append({"role": "user", "content": user_message})

            # Build prompt with history
            prompt = "You are a highly intelligent AI assistant, designed to provide helpful and accurate responses. Respond to the user's query in a clear, concise, and engaging manner.\n\n"
            for msg in conversation_history:
                if msg["role"] == "user":
                    prompt += f"User: {msg['content']}\n"
                else:
                    prompt += f"Assistant: {msg['content']}\n"
            prompt += "Assistant: "
            logger.debug(f"Prompt sent to model: {prompt[:100]}...")

            # Estimate token count (rough: 1 token ~ 4 chars)
            if len(prompt) / 4 > 900:  # Leave room for response
                logger.warning("Prompt too long, truncating history")
                conversation_history.pop(0)
                # Rebuild prompt
                prompt = "You are a highly intelligent AI assistant, designed to provide helpful and accurate responses. Respond to the user's query in a clear, concise, and engaging manner.\n\n"
                for msg in conversation_history:
                    if msg["role"] == "user":
                        prompt += f"User: {msg['content']}\n"
                    else:
                        prompt += f"Assistant: {msg['content']}\n"
                prompt += "Assistant: "

            response = llm(
                prompt,
                max_tokens=256,
                temperature=0.7,
                top_p=0.9,
                stream=True,
                stop=["User:"]  # Prevent generating user-like inputs
            )

            bot_response = ""
            for output in response:
                text = output['choices'][0]['text'].strip()  # Remove extra spaces/newlines
                if text:  # Only yield non-empty text
                    logger.debug(f"Model output chunk: {text}")
                    bot_response += text
                    yield text + " "  # Add space for readability
                else:
                    logger.debug("Empty chunk received, skipping")

            if not bot_response:
                logger.warning("Model returned empty response")
                bot_response = "Sorry, I couldn't generate a response. Please try again."
                yield bot_response

            # Append AI response to history
            conversation_history.append({"role": "assistant", "content": bot_response})

        except Exception as e:
            logger.error(f"Error during inference: {str(e)}")
            error_msg = "Error: Unable to generate response. Please try again."
            yield error_msg
            conversation_history.append({"role": "assistant", "content": error_msg})

    return Response(generate_response(), content_type='text/plain', headers={
        'X-Accel-Buffering': 'no',  # Disable buffering for streaming
        'Cache-Control': 'no-cache'
    })

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug mode