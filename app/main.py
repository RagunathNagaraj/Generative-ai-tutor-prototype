from flask import Flask, render_template, request, jsonify
import os

# Configuration
USE_MOCK = os.environ.get("USE_MOCK", "true").lower() in ("1", "true", "yes")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

if not USE_MOCK:
    import openai
    openai.api_key = OPENAI_API_KEY

app = Flask(__name__, template_folder="templates")


def mock_response(code, mode):
    if mode == "explain":
        return (
            "This program prints a sequence of numbers using a for loop. "
            "The range() function defines the loop count, and print() outputs each value."
        )
    else:
        return (
            "Debugging hint: check indentation, ensure correct variable names, "
            "and verify the range boundaries."
        )


def call_model(code, mode):
    prompt = (
        f"Explain this Python code for a beginner:\n{code}"
        if mode == "explain"
        else f"Find likely bugs and give step-by-step hints for this code:\n{code}"
    )

    if USE_MOCK:
        return mock_response(code, mode)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5,
    )
    return response["choices"][0]["message"]["content"].strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    code = request.form.get("code", "")
    mode = request.form.get("mode", "explain")

    if not code.strip():
        return jsonify({"result": "Please paste some Python code first."})

    try:
        output = call_model(code, mode)
        return jsonify({"result": output})
    except Exception as e:
        return jsonify({"result": f"Error: {e}"})


if __name__ == "__main__":
    app.run(debug=True)
