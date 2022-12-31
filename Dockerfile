FROM python:3

WORKDIR /Users/ycc/Documents/pythontest/test

COPY . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]