from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    response = {
        'data': None,
        'error': None,
        'request_args': None,
        'extra_data': {}
    }
    try:
        response['data'] = 'Success'
    except Exception as e:
        response['error'] = e
    return response


if __name__ == '__main__':
    app.run(debug=True)