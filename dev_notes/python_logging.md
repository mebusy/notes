
# Python Logging: How to Write Logs Like a Pro!

## Basic

```python
import logging

def test():
    logging.basicConfig(level=logging.INFO)

    logging.debug("this is debug")
    logging.info("this is info")
    logging.warning("this is warning")
    logging.error("this is error")
    logging.critical("this is critical")


if __name__ == "__main__":
    test()
```

```bash
INFO:root:this is info
WARNING:root:this is warning
ERROR:root:this is error
CRITICAL:root:this is critical
```

## Config Logging

```python
import logging

def test():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        # filename='test.log', # write to file if you want
        )

    logging.debug("this is debug")
    logging.info("this is info")
    logging.warning("this is warning")
    logging.error("this is error")
    logging.critical("this is critical")

```

```bash
2023-02-10 22:02:13 INFO test.py:12 this is info
2023-02-10 22:02:13 WARNING test.py:13 this is warning
2023-02-10 22:02:13 ERROR test.py:14 this is error
2023-02-10 22:02:13 CRITICAL test.py:15 this is critical
```

## Integration with logging services

```python
import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = "logs.papertrailapp.com"
PAPERTRAIL_PORT = 12345

def test():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)


    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)
    # you can add multiple handlers to the same logger, e.g. a file handler

    logging.error("this is error")
    logging.critical("this is critical")
```

