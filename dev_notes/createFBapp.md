...menustart

 - [Create Instant Games](#009069c69b11caef6d75739ab207e856)
 - [Create Message Bot](#1b3b0682a7aea56937be67c5a729a846)
 - [debug messager bot with local server](#aceacf6ca899a80c0a70aa4f2522d77c)
     - [localtunnel](#627aea0b68e33e1e89d82f9b7303f7a1)
 - [Write GameBot server](#b0c374aec5250909fe4a1c18e6889ae0)
     - [verify webhook](#4a6ec9d128ee67c8fb62497859117c6c)
     - [gameplay POST ( when close instance game )](#dd8d4a0d714285457d9f4d8ded0d4284)

...menuend


<h2 id="009069c69b11caef6d75739ab207e856"></h2>


# Create Instant Games

 1. create a new app
 2. set as game 
    - /Setting / basic / Category
 3. 为应用添加管理员、开发者和测试员
    - Facebook 正在逐步面向更广泛的受众推广小游戏，您的游戏目前可能无法对所有用户开放。
    - 要确保游戏的所有发开者和测试员拥有访问权限，请在应用面板的**/Roles**选项卡中将他们添加为应用的管理员、开发者或测试员
 4. Enable Instant Games in the App Dashboard
    - PRODUCTS +  > instant game > Set up
    - Make sure to enable the the **Use Instant Games** toggle.
 5. Testing and Uploading
    - To upload the .zip file, click the **Web Hosting** tab in the App Dashboard
    - and click **+Upload Version**  to upload the .zip file to Facebook's hosting service 
    - After that, the build will process the file, which should only take a few seconds. When the state changes to "Standby", click the **"★"** button to push the build to production.
 6. Setting up a Game Bot
    - Step 1: Create a Page,  
        - it needs some some special properties:
            - The page's category needs to be **App Page**
            - The page's name needs to **contain the name** of the app.
            - The page **cannot be associated** with another app.
        - Instant Games/Details/App Page
    - Step 2: Activate your Bot 
        - first create a message bot ( see below )
        - Instant Games bots are only permitted to use standard messaging and the GAME_EVENT message tag but not pages_messaging_subscriptions.
    - Step 3: https://developers.facebook.com/docs/games/instant-games/guides/bots-and-server-communication/
 7. https://developers.facebook.com/docs/games/instant-games/guides/bots-and-server-communication/
    - 客户端发送 sessionData , 游戏关闭时，这个sessionData 会作为 `payload` property  of the game_play webhook.

```
FBInstant.setSessionData({
  scoutSent:true,
  scoutDurationInHours:24
});
```



<h2 id="1b3b0682a7aea56937be67c5a729a846"></h2>


# Create Message Bot

https://developers.facebook.com/docs/messenger-platform/getting-started


 1. Add the Messenger Platform to your Facebook app
    - 'PRODUCTS', click '+ Add Product' / 'Messenger'  /  'Set Up' 
 2. Configure the webhook for your app
    - In the 'Webhooks' section of the Messenger settings console , 'Setup Webhooks' 
    - 'Callback URL' : something like `https://domain/webhook`
    - 'Verify Token' : your custom token
    - 'Subscription Fields': `messages` and `messaging_postbacks`
 3. Subscribe your app to a Facebook Page
    - In the 'Token Generation' section , choose page, get the Page Access Token
        - 每选择 一次page，就会重新生成 token
    - then , in the 'Webhook' section ,  select the same page , Click the 'Subscribe' to  subscribe your app to receive webhook events for the Page.
 4. Test your app subscription
    - send a message to your Page from facebook.com or in Messenger. 
    - If your webhook receives a webhook event, you have fully set up your app!


<h2 id="aceacf6ca899a80c0a70aa4f2522d77c"></h2>


# debug messager bot with local server

 - localtunnel or ngrok
    - 使用 localtunnel 需要清理掉你本地的 代理服务器设置，不要设置 http-proxy , https-proxy, 否则会出现错误 Tunnel Server is offline 

<h2 id="627aea0b68e33e1e89d82f9b7303f7a1"></h2>


## localtunnel

 - create localtunnel server
    - https://github.com/localtunnel/server

 - or just use provided service
    - `lt -s mebusy -l 10.192.81.132 -p 5757`


 
<h2 id="b0c374aec5250909fe4a1c18e6889ae0"></h2>


# Write GameBot server 

<h2 id="4a6ec9d128ee67c8fb62497859117c6c"></h2>


## verify webhook

```
GET /stack?hub.mode=subscribe&hub.challenge=1709021033&hub.verify_token=TEST_VERIFY_TOKEN HTTP/1.1
```


<h2 id="dd8d4a0d714285457d9f4d8ded0d4284"></h2>


## gameplay POST ( when close instance game )

```
POST /stack HTTP/1.1

{"object":"page","entry":[{"id":"1163397087175417","time":1551091549707,"messaging":[{"recipient":{"id":"1163397087175417"},"timestamp":1551091549707,"sender":{"id":"2396781657060600"},"game_play":{"game_id":"2223523667903679","player_id":"1766087003495604"}}]}]}
```

```python
// more human readable
{
    "entry": [
        {
            "id": "1163397087175417",
            "messaging": [
                {
                    "game_play": {
                        "game_id": "2223523667903679",
                        "player_id": "1766087003495604"
                    },
                    "recipient": {
                        "id": "1163397087175417"
                    },
                    "sender": {
                        "id": "2396781657060600"
                    },
                    "timestamp": 1551091549707
                }
            ],
            "time": 1551091549707
        }
    ],
    "object": "page"
}
```

 - test data ,  single event 

```
curl -X POST http://127.0.0.1:3000/bot -d '{"object":"page","entry":[{"id":"821299701563322","time":1551944314225,"messaging":[{"recipient":{"id":"821299701563322"},"timestamp":1551944314225,"sender":{"id":"2058800797536806"},"game_play":{"game_id":"702997996724334","payload":"{\"timezone\":8,\"nickname\":\"Qi\",\"firstTime\":false,\"top1player\":\"2247834808562963\",\"randomFriendId\":\"2247834808562963\"}","player_id":"2074839315937481"}}]}]}'
```

 - test data , 两组 entry, 每个 entry 包含2个event; 
    - 有一个event 是 message 

```
curl -X POST http://127.0.0.1:3000/bot -d '{"object":"page","more":"more","entry":[{"id":"1163397087175417","time":1551091549707,"messaging":[{"recipient":{"id":"1163397087175417"},"timestamp":1551091549707,"sender":{"id":"2396781657060600"},"game_play":{"game_id":"2223523667903679","player_id":"1766087003495604"}},{"recipient":{"id":"1163397087175417"},"timestamp":1551091549708,"sender":{"id":"2396781657060600"},"game_play":{"game_id":"2223523667903679","player_id":"1766087003495604"}}]},{"id":"1163397087175418","time":1551091549707,"messaging":[{"recipient":{"id":"1163397087175417"},"timestamp":1551091549707,"sender":{"id":"2396781657060600"},"game_play":{"game_id":"2223523667903679","player_id":"1766087003495604"}},{"recipient":{"id":"1163397087175417"},"timestamp":1551091549708,"sender":{"id":"2396781657060600"},"message":{"game_id":"2223523667903679","player_id":"1766087003495604"}}]}]}'
```





