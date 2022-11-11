[](...menustart)


[](...menuend)


把下列代码 加入 View Controller 中

```objective-c
#if TARGET_IPHONE_SIMULATOR

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

#endif
```
