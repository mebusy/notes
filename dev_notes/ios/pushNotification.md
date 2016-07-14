...menustart

 - [APNS 服务器证书制作，客户端部分代码](#1294a83ff96c5c0ee3c4b9620dd74edf)
   - [准备文件](#105dbfd27d203f637ce0d3c08eb78878)
   - [制作](#8cdf041fee866eecab95555346b07394)
   - [证书测试](#81f55b42ec661d67d432330fd47cd07c)
   - [客户端修改](#0c64cd168e7b43ebccec68a62f1d85e7)

...menuend



<h2 id="1294a83ff96c5c0ee3c4b9620dd74edf"></h2>
# APNS 服务器证书制作，客户端部分代码

<h2 id="105dbfd27d203f637ce0d3c08eb78878"></h2>
## 准备文件

 1. 开发者证书导出 .p12 文件, 比如 `PushChatKey.p12`
 2. Apple ID 配置 开启 push notification 功能后， 并下载证书 `aps_development.cer`

<h2 id="8cdf041fee866eecab95555346b07394"></h2>
## 制作

 - 转换证书 .cer 文件到 .pem 文件格式：
 	- `openssl x509 -in aps_developer_identity.cer -inform der -out PushChatCert.pem`
 - 转换私钥 .p12 文件 到 .pem 文件格式:
 	- 如果需要设置密码:
 		- `openssl pkcs12 -nocerts -out PushChatKey.pem -in PushChatKey.p12`
 	- 如果不想设置密码: 
		- `$openssl pkcs12 -in key.p12 -out key.pem  -nodes`
 - 最后，如果需要，我们把这两个文件合并成一个 .pem 文件：	
 	- `cat PushChatCert.pem PushChatKey.pem > ck.pem`


<h2 id="81f55b42ec661d67d432330fd47cd07c"></h2>
## 证书测试

 - 首先确认网络是否可以 正确连接到 苹果推送服务器

```
telnet gateway.sandbox.push.apple.com 2195
Trying 17.172.232.226...
Connected to gateway.sandbox.push-apple.com.akadns.net.
Escape character is '^]'.
```

 - 试一试用私钥和证书进行SSL加密连接：

```
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert PushChatCert.pem -key PushChatKey.pem
Enter pass phrase for PushChatKey.pem:
```

<h2 id="0c64cd168e7b43ebccec68a62f1d85e7"></h2>
## 客户端修改

 - applicationDidFinishLaunching  方法里，加上3句代码

```Objective-C
// 注册 APNS 服务
[[UIApplication sharedApplication] registerForRemoteNotificationTypes:
     (UIRemoteNotificationTypeAlert |   UIRemoteNotificationTypeBadge | UIRemoteNotificationTypeSound)];   
    
// push message 的数量标志清0
[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0]; 
```


 - AppDelegate 类中加入两个方法 ， 这两个是注册APNS的系统回调方法

```Objective-C
- (void)application:(UIApplication *)app didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {        
    NSString *str = [NSString stringWithFormat:@"Device Token=%@",deviceToken];     
       
    
    
    str = [str stringByReplacingOccurrencesOfString:@" " withString:@""];
    
    int startIndex =  [str rangeOfString:@"<"].location ;
    int endIndex =  [str rangeOfString:@">"].location ;
    
    str = [str substringWithRange:(NSRange){ startIndex+1 , endIndex-startIndex -1 }];
    
    NSLog(@"token %@ , %d %d",str , startIndex, endIndex);

    // TODO 
    // send your device token to server 

	//    
	//    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"register" message:str delegate:nil cancelButtonTitle:@"ok" otherButtonTitles: nil];
	//    [alert show];
	//    [alert release];

}   

- (void)application:(UIApplication *)app didFailToRegisterForRemoteNotificationsWithError:(NSError *)err {        
    NSString *str = [NSString stringWithFormat: @"Error: %@", err];     
    NSLog(@"%@",str);       
}
```








