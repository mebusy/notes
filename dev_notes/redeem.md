
# 兑换码

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

## CRC 


## Base X







