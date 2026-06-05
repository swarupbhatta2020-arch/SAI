from flask import Flask, render_template, request, jsonify
from google import genai
import warnings

warnings.simplefilter("ignore", UserWarning)

app = Flask(__name__)

client = genai.Client(api_key="API_KEY")

MODELS = [
    "gemini-2.5-flash-lite",  # Primary
    "gemini-2.5-flash",       # Fallback 1
    "gemini-2.0-flash",       # Fallback 2
    "gemini-1.5-flash",       # Fallback 3
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_message
            )

            return jsonify({
                "reply": response.text,
                "model_used": model
            })

        except Exception as e:
            print(f"{model} failed: {e}")
            continue

    return jsonify({
        "reply": "Sorry, all AI models are currently unavailable."
    }), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)0.0.0", port=5000,
    if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT",
    5000))
    )
