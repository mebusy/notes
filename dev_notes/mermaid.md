
# Mermaid

[mermaid styling](https://mermaid-js.github.io/mermaid/#/flowchart?id=styling-and-classes)

[mermaid live](mermaid.live)

simple example: 

```
graph TD
    A["Sender: io.send(data)"] -->|data| E0{"Is data we are interested in"}
    E0-->|no| E(Default Encoder)
    E0-->|yes| E1("data'->protobuf")
    E1-->E

    E -->|"encoded data"| D0{"Is data customized?"}

    D0 -->|no| D(Default Decoder)
    D0 -->|yes| D1("protobuf->data'")
    D1 --> D

    D -->|"data"| R["Receiver: io.on('message',...)"]

    subgraph \n
        A
        subgraph DEFAULT-PARSER
            E
            D
        end
        R
    end


    style E0 fill:cyan
    style E1 fill:#00FFFF

    style D0 fill:lightgreen
    style D1 fill:lightgreen

    style DEFAULT-PARSER fill:yellow,color:red
```
