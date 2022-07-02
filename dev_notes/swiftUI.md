
# SwiftUI

## 5 Key Concepts

1. Only 3 Ways to Layout View
    - Vertically
        ```swift
        var body: some View {
            VStack {
                Text( "Hello world 1" )
                Text( "Hello world 2" )
                Text( "Hello world 3" )
            }
        }
        ```
    - Horizontally
        ```swift
            HStack {
                RoundedRectangle(cornerRadius: 30)
                RoundedRectangle(cornerRadius: 30)
            }
        ```
    - Depth Stack (ZStack)
        - everything inside is laid out one on top of another
        ```swift
            ZStack {
                Color.pink  // this color is bottom layer
                VStack {...}
            }
        ```

2. Everything is a View
    - VStack is a View, Text is a View, `Color.pink` is a View
    - Modifiers replace View
        ```swift
            Text( "Everything is a View!" )
                .font(.largeTitle)
        ```
        - Views are REPLACED when modified.
3. Parent-Child Relation
    - modifier on parent level will affect on all chindren
4. Views can Pull-In or Push-Out
    - there are 2 types of views or layout behaviors: 
        1. Pulling view 
            - for example, a Text, it's only using as much space as it needs. It doesn't stretch out doesn't push out doesn't try to take any more space.
        2. push out views
            - for example, `Color.pink`, `RoundedRectangle` , those are pushing out and computing for space. They're trying to use as much space as possible.
5. Change Views with DATA, not directly
    - you saw you can change views with modifiers and modifiers they don't actually change the existing object, they replace the existing object. Well what do you do during runtime when you want to change an object?
    ```swift
    struct AlterViewsWithData: View {
        @State private var circleColr = Color.red

        var body: some View {
            VStack {
                Text( "You change views with DATA." ).font(.largeTitle)
                Button("Change Color") {
                    // TODO: change circle's color
                }
                Circle().foregroundColor(circleColor)
            }
        }
    }
    ```
    - I have a button and when I click the button I want to change the color of that circle. How do I modify that color ?
    - **You can't reference views directly!**
        - I cannot create what you might know as an outlet from UIKit, I can create an outlet for a circle. I can't create a variable to represent that circle and change that variable.
    - What I have to do is anything I want to change on the screen, I have to change data, and my view reacts to that data, my view will respond to that data and change with it.
        ```swift
            // TODO: change circle's color
            self.circleColor = Color.green
        ```



