from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/find_sneakers', methods=['POST'])
def find_sneakers():
    return jsonify({"status": "success", "message": "Sneakers found!"})
if __name__ == "__main__":
    app.run(debug=True)
