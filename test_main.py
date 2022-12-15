import requests

# In assignment1, I used mac, here I used window11
dir_path = 'D:/test_caopei'


def test_create_dir():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/directory/create"
    payload = {
        "path": dir_path
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_read_dir():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/directory/read"
    payload = {
        "path": dir_path
    }
    response = requests.get(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_delete_dir():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/directory/delete"
    payload = {
        "path": dir_path
    }
    response = requests.delete(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


binary_file = '/cp.bin'


def test_create_binary():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/binaryfile/create"
    payload = {
        "path": dir_path + binary_file
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_update_binary():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/binaryfile/update"
    payload = {
        "path": dir_path + binary_file,
        "content": "this is new message!"
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_read_binary():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/binaryfile/read"
    payload = {
        "path": dir_path + binary_file
    }
    response = requests.get(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_delete_binary():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/binaryfile/delete"
    payload = {
        "path": dir_path + binary_file
    }
    response = requests.delete(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


log_text_file = '/cp.log'


def test_create_log():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/logtextfile/create"
    payload = {
        "path": dir_path + log_text_file
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_update_log():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/logtextfile/update"
    payload = {
        "path": dir_path + log_text_file,
        "content": "this is new log!"
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_read_log():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/logtextfile/read"
    payload = {
        "path": dir_path + log_text_file
    }
    response = requests.get(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_delete_log():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/logtextfile/delete"
    payload = {
        "path": dir_path + log_text_file
    }
    response = requests.delete(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


buffer_file = '/queue_cp'


def test_create_buffer():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/bufferfile/create"
    payload = {
        "path": dir_path + buffer_file,
        "size": 3
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_add_buffer():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/bufferfile/add"
    payload = {
        "path": dir_path + buffer_file,
        "element": "3"
    }
    response = requests.post(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_read_buffer():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/bufferfile/read"
    payload = {
        "path": dir_path + buffer_file
    }
    response = requests.get(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)


def test_delete_buffer():
    # 返回接口响应结果
    url = "http://127.0.0.1:5000/bufferfile/delete"
    payload = {
        "path": dir_path + buffer_file
    }
    response = requests.delete(url=url, json=payload)
    print("\nresponse------------------------>" + response.text)
