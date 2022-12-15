from flask import Blueprint, request
import assignment1.logTextFile as logtextfile

logtextfile_api = Blueprint("logtextfile_api", __name__)


@logtextfile_api.route('/')
def hello_world():
    return 'Hello logtextfile!'


@logtextfile_api.route('/create', methods=["POST", "PUT"])
def create():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextfile.create_log(log_name)


@logtextfile_api.route('/read', methods=["GET"])
def read():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextfile.read_log(log_name)


@logtextfile_api.route('/update', methods=["PUT", "POST"])
def update():
    log_path = request.json.get('path')
    content = request.json.get('content')
    print(type(log_path))
    return logtextfile.write_log(log_path, content)


@logtextfile_api.route('/delete', methods=["DELETE"])
def delete():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextfile.delete_log(log_name)
