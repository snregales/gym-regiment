release: flask db upgrade
web: gunicorn autoapp:APP -b 0.0.0.0:$PORT -w 3
