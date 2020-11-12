import random

from flask import Flask, render_template, request
import twl

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return anagram(request.args.get('anagram', ''))


def anagram(a):
    l = list(twl.anagram(a))
    r = random.randint(0, len(l))
    return r


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
