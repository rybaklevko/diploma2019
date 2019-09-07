from app import app


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/start_page', methods=['GET'])
def start_page():
    return "Hello world"
