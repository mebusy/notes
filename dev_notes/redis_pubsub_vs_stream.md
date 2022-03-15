
# Redis Put/Sub vs. Stream

## Pub/Sub

messages **miss** if no subscriber.

![](../imgs/redis_pubsub_illustration.png)


## Stream 

message **won't miss** even if there's no subscriber.

![](../imgs/redis_stream_illustration.png)



