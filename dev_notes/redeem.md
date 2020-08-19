...menustart

 - [兑换码](#9bff7a874cd7d0dd3b7574a0917de15f)
     - [限制字符集](#d451326fd2b4c1b301f29a5ea7fe4e1e)
     - [兑换码设计，本身包含重要信息](#3f9352573d37d3ec177bc6496e4b13a4)
     - [CRC](#1a4b5d84a0328c4a33bd669c608a34c3)
     - [Base X](#325d83b8f57ce9fbb4071f7bdfaf2a74)

...menuend


<h2 id="9bff7a874cd7d0dd3b7574a0917de15f"></h2>


# 兑换码

<h2 id="d451326fd2b4c1b301f29a5ea7fe4e1e"></h2>


## 限制字符集

剔除大写字母 O , 以及 I , 共60个字符

```python
abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXZY0123456789
```

或 使用base58

```python
# base58
123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz
```

<h2 id="3f9352573d37d3ec177bc6496e4b13a4"></h2>


## 兑换码设计，本身包含重要信息

32bit redeemID + 8bit channel  + 8bit 产品序列1 + 8bit 产品序列2 + 32bit crc

```sql
CREATE TABLE if not exists tbl_redeem (
  redeemID int NOT NULL  ,
  redeemCode varchar(20) NOT NULL,
  status enum('unused','used','disabled','destroyed') NOT NULL DEFAULT 'unused',
  uuid  varchar(64) NOT NULL DEFAULT '',
  updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (redeemID),
  UNIQUE KEY (redeemCode)
)
```

<h2 id="1a4b5d84a0328c4a33bd669c608a34c3"></h2>


## CRC 


<h2 id="325d83b8f57ce9fbb4071f7bdfaf2a74"></h2>


## Base X


```go
// verify
import (
    "github.com/btcsuite/btcutil/base58"
    "encoding/binary"
)


```




