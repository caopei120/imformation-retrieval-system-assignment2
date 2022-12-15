from flask import Blueprint, request
import assignment1.bufferFile as bufferfile

bufferfile_api = Blueprint("bufferfile_api", __name__)


@bufferfile_api.route('/')
def hello_world():
    return 'Hello bufferfile!'


@bufferfile_api.route('/create', methods=["POST", "PUT"])
def create():
    file_name = request.json.get('path')
    size = request.json.get('size')
    print(type(file_name))
    return bufferfile.create_file(file_name, size)


@bufferfile_api.route('/read', methods=["GET"])
def read():
    file_name = request.json.get('path')
    print(type(file_name))
    return bufferfile.consume_element(file_name)


@bufferfile_api.route('/add', methods=["PUT", "POST"])
def add():
    file_name = request.json.get('path')
    element = request.json.get('element')
    print(type(file_name))
    return bufferfile.push_element(file_name, element)


@bufferfile_api.route('/delete', methods=["DELETE"])
def delete():
    file_name = request.json.get('path')
    print(type(file_name))
    return bufferfile.delete_file(file_name)
