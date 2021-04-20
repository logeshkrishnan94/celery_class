## Activate virtualenv

```virtualenv venv3 --python=python3```\
```source venv3/bin/activate```\
```pip install -r requirements.txt```


## To run the example

* Start redis server for backend and broker using docker

```docker run -d -p 6379:6379 redis```

```redis-cli```

```ping``` -> PONG

* Run the following command from the root folder to start the celery worker

```celery -A celery_proj worker --loglevel=INFO --pool threads```

* Run the following command from the root folder to get the predictions

```python celery_test.py```





