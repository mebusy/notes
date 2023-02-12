[](...menustart)

- [Python Logging: How to Write Logs Like a Pro!](#272190d0f7628eae810eb386862457b9)
    - [Basic](#972e73b7a882d0802a4e3a16946a2f94)
    - [Config Logging](#a880c8bc5cc63affc1304be842655c5d)
    - [Integration with logging services](#eb18ed283b3da74c80fbf23a4551c1bf)

[](...menuend)


<h2 id="272190d0f7628eae810eb386862457b9"></h2>

# Python Logging: How to Write Logs Like a Pro!

<h2 id="972e73b7a882d0802a4e3a16946a2f94"></h2>

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

<h2 id="a880c8bc5cc63affc1304be842655c5d"></h2>

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

<h2 id="eb18ed283b3da74c80fbf23a4551c1bf"></h2>

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

