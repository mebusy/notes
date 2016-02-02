...menustart

 * [if TARGET_IPHONE_SIMULATOR](#74ab1a2b1d81a278d3beb1f85be3a145)
 * [pragma mark 1.快捷键](#4f0e488340c72ec9bf7c87d4cce4703d)
 * [endif](#e96d8afc259593a20838480dfb84400b)

...menuend



把下列代码 加入 View Controller 中

```objective-c
<h2 id="74ab1a2b1d81a278d3beb1f85be3a145"></h2>
#if TARGET_IPHONE_SIMULATOR

<h2 id="4f0e488340c72ec9bf7c87d4cce4703d"></h2>
#pragma mark 1.快捷键

- (NSArray *)keyCommands
{
    return @[  [UIKeyCommand keyCommandWithInput:@"r"
                                 modifierFlags:UIKeyModifierCommand
                                        action:@selector(searchKeyPressed:)]   ];
}

- (void)searchKeyPressed:(UIKeyCommand *)keyCommand
{
    // Respond to the event
    //NSLog( @"input %@, %d" ,  keyCommand.input , keyCommand.modifierFlags ) ;
    
    if ( [keyCommand.input  isEqual: @"r"] &&  keyCommand.modifierFlags == UIKeyModifierCommand ) {
        NSLog(@"cmd + R pressed " ) ;
    }
}

<h2 id="e96d8afc259593a20838480dfb84400b"></h2>
#endif
```
