...menustart

 * [ios simulator stdout stderr redirect](#808223f71402e744750e77a2865d1277)

 * [if TARGET_IPHONE_SIMULATOR](#74ab1a2b1d81a278d3beb1f85be3a145)

 * [endif](#e96d8afc259593a20838480dfb84400b)

 * [if TARGET_IPHONE_SIMULATOR](#74ab1a2b1d81a278d3beb1f85be3a145)

 * [include <assert.h>](#ebc0698cf05d2d8bbf78c2089a5dd7e4)

 * [include <stdbool.h>](#093848d6b19f265b15f0124d33f45079)

 * [include <sys/types.h>](#32614ed8861386b4ee97f921788d04fe)

 * [include <unistd.h>](#72500b52c1addad1fb042b9944382803)

 * [include <sys/sysctl.h>](#4cd69413490417afabba01a5f27fc38c)

 * [endif](#e96d8afc259593a20838480dfb84400b)

 * [if TARGET_IPHONE_SIMULATOR](#74ab1a2b1d81a278d3beb1f85be3a145)

 * [endif](#e96d8afc259593a20838480dfb84400b)


...menuend


<h2 id="808223f71402e744750e77a2865d1277"></h2>
# ios simulator stdout stderr redirect

目的: 当 iOS app 脱离xcode，在 simulator 上运行时， 我们希望可以查看到详细的日志

---
首先, 所有的功能都必须确保只在 模拟器环境下有效

```objective-c
<h2 id="74ab1a2b1d81a278d3beb1f85be3a145"></h2>
#if TARGET_IPHONE_SIMULATOR
    ...
<h2 id="e96d8afc259593a20838480dfb84400b"></h2>
#endif
```

---
我们需要一个方法，来检测 app 是否 运行在 xcode debugger 下.

```objective-c
<h2 id="74ab1a2b1d81a278d3beb1f85be3a145"></h2>
#if TARGET_IPHONE_SIMULATOR

<h2 id="ebc0698cf05d2d8bbf78c2089a5dd7e4"></h2>
#include <assert.h>
<h2 id="093848d6b19f265b15f0124d33f45079"></h2>
#include <stdbool.h>
<h2 id="32614ed8861386b4ee97f921788d04fe"></h2>
#include <sys/types.h>
<h2 id="72500b52c1addad1fb042b9944382803"></h2>
#include <unistd.h>
<h2 id="4cd69413490417afabba01a5f27fc38c"></h2>
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

<h2 id="e96d8afc259593a20838480dfb84400b"></h2>
#endif
```

---
如果 app 脱离了 debugger 环境运行,

在 [application: didFinishLaunchingWithOptions] 方法开始,  对输出做重定向。

```objective-c
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    
// redirect stdout , stderr to log file , if it is NOT attached to a debugger

<h2 id="74ab1a2b1d81a278d3beb1f85be3a145"></h2>
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
<h2 id="e96d8afc259593a20838480dfb84400b"></h2>
#endif
    
    //other codes
    ...

```


