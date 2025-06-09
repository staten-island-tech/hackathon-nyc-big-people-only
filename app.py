from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/park", methods=["POST"])
def park():
    data = request.json
    print(f"Received parking data: {data}")
    return jsonify({"status": "success", "message": "Parking recorded"})

if __name__ == "__main__":
    app.run(debug=True)