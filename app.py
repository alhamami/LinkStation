from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
        return render_template('home/about-us.html')


if __name__ == '__main__':
    app.run( port=80, debug=True)
