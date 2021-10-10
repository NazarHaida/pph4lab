from flask import Flask
from waitress import serve



app = Flask(__name__)


@app.route('/api/v1/hello-world-7')
def pp4():
    return "Hello World 7"
if __name__ == '__main__':
    serve(app, "0.0.0.0", 8080)
    #app.run(debug=True)