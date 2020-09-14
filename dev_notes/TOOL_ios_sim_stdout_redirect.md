...menustart

- [ios simulator stdout stderr redirect](#808223f71402e744750e77a2865d1277)

...menuend


<h2 id="808223f71402e744750e77a2865d1277"></h2>


# ios simulator stdout stderr redirect

目的: 当 iOS app 脱离xcode，在 simulator 上运行时， 我们希望可以查看到详细的日志

---
首先, 所有的功能都必须确保只在 模拟器环境下有效

```objective-c
#if TARGET_IPHONE_SIMULATOR
    ...
#endif
```

---
我们需要一个方法，来检测 app 是否 运行在 xcode debugger 下.

```objective-c
#if TARGET_IPHONE_SIMULATOR

#include <assert.h>
#include <stdbool.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/sysctl.h>

// There's a function from Apple to detect wether a Mac program is being debugged.
static bool AmIBeingDebugged(void)
// Returns true if the current process is being debugged (either
// running under the debugger or has a debugger attached post facto).
{
    int                 junk;
    int                 mib[4];
    struct kinfo_proc   info;
    size_t              size;
    
    // Initialize the flags so that, if sysctl fails for some bizarre
    // reason, we get a predictable result.
    
    info.kp_proc.p_flag = 0;
    
    // Initialize mib, which tells sysctl the info we want, in this case
    // we're looking for information about a specific process ID.
    
    mib[0] = CTL_KERN;
    mib[1] = KERN_PROC;
    mib[2] = KERN_PROC_PID;
    mib[3] = getpid();
    
    // Call sysctl.
    
    size = sizeof(info);
    junk = sysctl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);
    assert(junk == 0);
    
    // We're being debugged if the P_TRACED flag is set.
    
    return ( (info.kp_proc.p_flag & P_TRACED) != 0 );
}

#endif
```

---
如果 app 脱离了 debugger 环境运行,

在 [application: didFinishLaunchingWithOptions] 方法开始,  对输出做重定向。

```objective-c
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    
// redirect stdout , stderr to log file , if it is NOT attached to a debugger

#if TARGET_IPHONE_SIMULATOR
    if ( !AmIBeingDebugged() ) {
        NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,NSUserDomainMask, YES);
        NSString *documentsDirectory = [paths objectAtIndex:0];
        
        // get user name
        NSError* error = NULL;
        NSString* reg = @"^/Users/(\\w+)/.*?$";
        NSRegularExpression* regex = [NSRegularExpression regularExpressionWithPattern:reg
                                                                               options:0
                                                                                 error:&error];
        
        NSUInteger numberOfMatches = [regex numberOfMatchesInString:documentsDirectory options:0 range:NSMakeRange(0, documentsDirectory.length )];
        if (  numberOfMatches == 1) {
            
            NSString* result = [regex stringByReplacingMatchesInString:documentsDirectory
                                                                options:0
                                                                range:NSMakeRange(0, documentsDirectory.length)
                                                                withTemplate:@"$1"];
            
            NSString *logFilePath = [NSString stringWithFormat:@"/Users/%@/Documents/ios-simulator.log" , result ];
            NSLog( @"freopen to file:  %@" ,  logFilePath ) ;
            freopen([logFilePath cStringUsingEncoding:NSASCIIStringEncoding],"a+",stderr);
            freopen([logFilePath cStringUsingEncoding:NSASCIIStringEncoding],"a+",stdout);
        }

    }
#endif
    
    //other codes
    ...

```

**重定向到设备文件，并通过itunes浏览log**

1. write to device tile all.log

```objective-c
    if ( !AmIBeingDebugged() ) {
        NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,NSUserDomainMask, YES);
        NSString *documentsDirectory = [paths objectAtIndex:0];
        
        NSString *logFilePath = [NSString stringWithFormat:@"%@/%@" , documentsDirectory , @"app.log" ] ;
        freopen([logFilePath cStringUsingEncoding:NSASCIIStringEncoding],"a+",stderr);
        freopen([logFilePath cStringUsingEncoding:NSASCIIStringEncoding],"a+",stdout);
    }
```

2. enable file sharing with itunes

- add `UIFileSharingEnabled` to info.plist, and set "YES"
- the full name of `UIFileSharingEnabled` is `Application supports iTunes file sharing`
