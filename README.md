# What is this?

This project shows a Pythonic version of

- plugin architecture
- fast data crunching pipeline
- process communication using a message queue in Redis

# Install

```
virtualenv --python=/usr/local/bin/python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d
```

# Running

```
source venv/bin/activate
python main.py publisher

# in as many separate terminals as you want
source venv/bin/activate
python main.py subscriber
```
![terminal](docs/queueing.png "Cool queuing example")


# References

https://medium.com/@johngrant/python-redis-pub-sub-6e26b483b3f7
http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html