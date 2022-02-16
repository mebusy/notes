...menustart

- [Web FrontEnd Note](#4a5647bb8fe0a7a3f6eb3fe7e2d038d6)
    - [reactJS](#6f2631dbb72803960030d1912849b034)
    - [Ant.design](#2efb47900229246f126114d5446309c8)
    - [http request from JS](#b63638704f9953ca8cb4512dcf01b2a2)
    - [button click -> javascript](#8ee1ccd085896dae59d2585a43f6ad61)
    - [form submit -> javascript](#5746a56c4e47f39b4dbc05035350625c)
    - [get the content of a file](#14d95bde54c8e5595aeb776fe1cfc950)
    - [Html Number Input field, max/min length](#d2b729a11d72c4041af51d779b41cd05)
    - [Html Hidden Element](#e9475a1dc92ef25ff6490381ce108171)
    - [Html Drop List](#343ad9cb4bc1d4a4684f231e3a380be7)

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

<h2 id="8ee1ccd085896dae59d2585a43f6ad61"></h2>


## button click -> javascript

```html
const t_delete_page_html = `
<button onclick="deleteEvent()">删除当前活动</button>

<script>
function deleteEvent() {
    // submit form data to api
    fetch( window.location.origin + "/" + "deleteaccrecharge/" + {{.Game}}  ,  {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: "{}" , 
    })
      .then(res => res.json())
      .then(
        (result) => {
            if (result.err) {
                alert( result.err ); 
            } else {
                // to reset page
                window.location.reload(true);
            }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
            alert( error ) ;
        }
      )
}
</script>
`
```


<h2 id="5746a56c4e47f39b4dbc05035350625c"></h2>


## form submit -> javascript

```html
const t_add_page_html = `
<form name="form_event" onsubmit="addEvent(); return false;">
  <label>时间格式(北京时间): 2016010215</label><br>
  <label>活动开始时间</label><br>
  <input type="text" id="id_starttime" name="starttime" maxlength="10" placeholder="1970010208"><br>
  <label>统计截止时间</label><br>
  <input type="text" id="id_deadline" name="deadline" maxlength="10" placeholder="1970010214"> <br>
  <label>活动结束时间</label><br>
  <input type="text" id="id_endtime" name="endtime" maxlength="10" placeholder="1970010220"><br><br>

  <input type="submit" value="发布累冲活动">
</form> 


<script>
function isNumeric(num){
  return !isNaN(num)
}
function addEvent() {
    starttime =  document.form_event.elements["starttime"].value
    deadline =  document.form_event.elements["deadline"].value
    endtime =  document.form_event.elements["endtime"].value
    
    if ( starttime.length < 10 || deadline.length < 10 || endtime.length < 10   ) {
        alert( "请填写完整时间" ) ;
        return ;
    }
    if ( !isNumeric( starttime ) || !isNumeric( deadline ) ||  !isNumeric( endtime ) ) {
        alert( "时间不能包含非数字" ) ;
        return ;
    }

    let url =  window.location.origin + "/publishaccrecharge/" + {{.Game}} + "/"+starttime+"/"+deadline+"/"+endtime
    fetch( url ,  {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: "{}" , 
    })
      .then(res => res.json())
      .then(
        (result) => {
            if (result.err) {
                alert( result.err ); 
            } else {
                // to reset page
                window.location.reload(true);
            }
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
            alert( error ) ;
        }
      )
}
</script>
`
```

<h2 id="14d95bde54c8e5595aeb776fe1cfc950"></h2>


## get the content of a file

```html
<!DOCTYPE html>
<html>
<title>
get file content test
</title>
<body>

<p>Upload your file</p>

<script>
async function readText(event) {
  const file = event.target.files.item(0)
  const text = await file.text();

  console.log( text );

  // document.getElementById("output").innerText = text
}
</script>

<input type="file" onchange="readText(event)" />
<!-- <pre id="output"></pre> -->

</body>
</html>
```


<h2 id="d2b729a11d72c4041af51d779b41cd05"></h2>


## Html Number Input field, max/min length

```html
    <input type="number" id="id_starttime" name="starttime" minlength="10" maxlength="10" placeholder="1970010208" required oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);">
```

<h2 id="e9475a1dc92ef25ff6490381ce108171"></h2>


## Html Hidden Element

```html
    <form id="id_form_query">
        <!-- hideen filed -->
        <input type="hidden" name="action" value="query" />
        ...
        <button type="submit" form="id_form_query">Query</button>
    </form>
```


<h2 id="343ad9cb4bc1d4a4684f231e3a380be7"></h2>


## Html Drop List

```html
    <select name="game" id="id_game" form="id_form_create">
        {{ range $index, $gamename := .GameList }}
        <option value="{{$gamename}}">{{$gamename}}</option>
        {{ end }}
    </select>
```

