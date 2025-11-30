from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice", "active_since": "2023-01-01"},
        {"id": 2, "name": "Bob", "active_since": "2023-06-15"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
