from flask import Flask

from binaryfile_api import binaryfile_api
from bufferfile_api import bufferfile_api
from directory_api import directory_api
from logtextfile_api import logtextfile_api

app = Flask(__name__)

app.register_blueprint(directory_api, url_prefix="/directory")
app.register_blueprint(binaryfile_api, url_prefix="/binaryfile")
app.register_blueprint(logtextfile_api, url_prefix="/logtextfile")
app.register_blueprint(bufferfile_api, url_prefix="/bufferfile")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
