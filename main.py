

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>YOU ARE WELCOME</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5555)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
