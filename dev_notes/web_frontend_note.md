...menustart

 - [Web FrontEnd Note](#4a5647bb8fe0a7a3f6eb3fe7e2d038d6)
     - [reactJS](#6f2631dbb72803960030d1912849b034)
     - [Ant.design](#2efb47900229246f126114d5446309c8)
     - [http request from JS](#b63638704f9953ca8cb4512dcf01b2a2)

...menuend


<h2 id="4a5647bb8fe0a7a3f6eb3fe7e2d038d6"></h2>


# Web FrontEnd Note

<h2 id="6f2631dbb72803960030d1912849b034"></h2>


## reactJS

 - create project

```
npm install -g create-react-app
create-react-app my-app
```

 - run project

```
npm start
http://localhost:3000
```

<h2 id="2efb47900229246f126114d5446309c8"></h2>


## Ant.design

 - after you create reactJS app, `cd ` to project folder, then  run :

```
yarn add antd
```

 - use antd
    - - 修改 src/App.css，在文件顶部引入 antd/dist/antd.css。

```
@import '~antd/dist/antd.css';
```

<h2 id="b63638704f9953ca8cb4512dcf01b2a2"></h2>


## http request from JS

```javascript
    // submit form data to api
    fetch( "http://10.192.83.42:9000/announcementPublish" ,  {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify( values)
    })
      .then(res => res.json())
      .then(
        (result) => {
            if (result.err) {
                alert( "有错误发生,发布失败!!" ); 
            } else {
                alert( "公告发布成功" );
                this.props.form.resetFields() ;
            }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
            alert( error ) ;
        }
      )
```

