from flask import Flask, render_template, request, jsonify
from google import genai
import warnings
warnings.simplefilter("ignore", UserWarning)

app = Flask(__name__)

# Put your Gemini API key here
client = genai.Client(
    api_key="API_KEY"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
            contents=user_message
    )

    return jsonify({
        "reply": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,
    debug=True)