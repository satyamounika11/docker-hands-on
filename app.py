# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello from Docker! 🚀"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask
import redis

app = Flask(__name__)
counter = redis.Redis(host="redis", port=6379)

@app.route('/')
def home():
    count = counter.incr('hits')
    return f"Page visited {count} times! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)