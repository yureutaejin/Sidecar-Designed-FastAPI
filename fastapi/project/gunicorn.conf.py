# gunicorn.conf.py
bind = "0.0.0.0:22222"
workers = 2
worker_class = "uvicorn.workers.UvicornWorker"
loglevel = "debug"