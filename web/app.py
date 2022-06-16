# flask
from flask import *
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', test1=int(time.time()))


if __name__ == '__main__':
    app.run(
        port=5702,
        debug=True
    )
