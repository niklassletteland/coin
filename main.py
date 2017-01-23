from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    return '__________ CØIN __________'


@app.errorhandler(404)
def page_not_found(e):
    return 'sorry, nothing to see here ¯\_(ツ)_/¯', 404
