# -*- coding: utf8 -*-

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def main():
    return '<div style="display:flex; justify-content:center; align-items:center; height:100%">__________ CØIN __________</div>'


@app.errorhandler(404)
def page_not_found(e):
    return 'sorry, nothing to see here ¯\_(ツ)_/¯', 404

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
if __name__ == "__main__":
    app.run()
    