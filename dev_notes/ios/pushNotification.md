...menustart

 - [APNS 服务器证书制作，客户端部分代码](#1294a83ff96c5c0ee3c4b9620dd74edf)
     - [准备文件](#105dbfd27d203f637ce0d3c08eb78878)
     - [证书测试](#81f55b42ec661d67d432330fd47cd07c)
     - [客户端修改](#0c64cd168e7b43ebccec68a62f1d85e7)

...menuend


<h2 id="1294a83ff96c5c0ee3c4b9620dd74edf"></h2>


# APNS 服务器证书制作，客户端部分代码

<h2 id="105dbfd27d203f637ce0d3c08eb78878"></h2>


## 准备文件

做苹果推送服务器，很重要的一步，就是生成与苹果APNS连接的证书，一般是.pem文件；

 1. 首先在苹果开发者中心 生成 aps_devlopment.cer文件；然后下载；双击导入钥匙串；
 2. 打开钥匙串 -选择登录--证书--找到 Apple Development iOS Push Server证书右键导出--生成apns_dev_cert.p12文件 不要设置密码
 3. 然后 选择 密钥 -- 找到 User下面的--Apple Development iOS Push Server密钥---右键---生成 apns_dev_key.p12文件 不要设置密码
 3. 打开终端，把上面的p12文件生成 .pem文件
    - openssl pkcs12 -clcerts -nokeys -out apns-dev-cert.pem -in apns_dev_cert.p12  
        - 生成apns-dev-cert.pem
    - openssl pkcs12 -nocerts -out apns-dev-key.pem -in apns_dev_key.p12   
        - 生成apns-dev-key.pem 
        - 这个要输入密码，记住输入的密码；
    - openssl rsa -in apns-dev-key.pem -out apns-dev-key-noenc.pem  
        - 生成 apns-dev-key-noenc.pem 
        - 因为上面的 apns-dev-key.pem有密码，这一步生成的就是把密码取消的文件；
    - cat apns-dev-cert.pem apns-dev-key-noenc.pem > apns-dev.pem 
        - 合并 apns-dev-cert.pem apns-dev-key-nonec.pem 为单个文件 apns-dev-cert.pem ;

最后在服务器端使用apns-dev-cert.pem就可以了；


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
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert apns-dev-cert.pem -key apns-dev-key-noenc.pem 
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








