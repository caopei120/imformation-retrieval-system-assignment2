from flask import Blueprint, request
import assignment1.binaryFile as binaryfile

binaryfile_api = Blueprint("binaryfile_api", __name__)


@binaryfile_api.route('/')
def hello_world():
    return 'Hello binaryfile!'


@binaryfile_api.route('/create', methods=["POST", "PUT"])
def create():
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryfile.create_file(file_path)


@binaryfile_api.route('/read', methods=["GET"])
def read():
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryfile.read_file(file_path)


@binaryfile_api.route('/update', methods=["PUT", "POST"])
def update():
    file_name = request.json.get('path')
    content = request.json.get('content')
    print(type(file_name))
    return binaryfile.update_file(file_name, content)


@binaryfile_api.route('/delete', methods=["DELETE"])
def delete():
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryfile.delete_file(file_path)
