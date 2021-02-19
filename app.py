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
    print(twl.anagram('asrtonomer'))
    return max(list(twl.anagram(a)), key=len)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
