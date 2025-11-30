import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.get("/")
def index():
    count = r.incr('hits')
    return f"Hello! I have been seen {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
