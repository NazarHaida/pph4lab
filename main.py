from flask import Flask
from waitress import serve
from db.aut import auth
from db.user import user
from db.audience import audience
from db.reservation import reservation


app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(audience)
app.register_blueprint(reservation)

@app.route('/api/v1/hello-world-7')
def pp4():
    return "Hello World 7"
if __name__ == '__main__':
    #serve(app, "0.0.0.0", 8080)
    app.run(debug=True)