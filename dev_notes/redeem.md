...menustart

 - [兑换码](#9bff7a874cd7d0dd3b7574a0917de15f)
     - [限制字符集](#d451326fd2b4c1b301f29a5ea7fe4e1e)
     - [兑换码设计，本身包含重要信息](#3f9352573d37d3ec177bc6496e4b13a4)
     - [CRC](#1a4b5d84a0328c4a33bd669c608a34c3)
     - [Base 58](#36e3a1ad5f706ac6414ea1c1bb708494)
     - [decode/verify redeemCode](#03174a9cd6c332b4ed1a3fe8d4b64c77)
     - [python script to generate RedeemCode](#2440b42391dd88dc32b14c0253b3a95a)

...menuend


<h2 id="9bff7a874cd7d0dd3b7574a0917de15f"></h2>


# 兑换码

<h2 id="d451326fd2b4c1b301f29a5ea7fe4e1e"></h2>


## 限制字符集

使用base58

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
  expireTime int NOT NULL ,
  updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (redeemID),
  UNIQUE KEY (redeemCode)
)
```

<h2 id="1a4b5d84a0328c4a33bd669c608a34c3"></h2>


## CRC 

[crc IEEE](python_tips_1.md#d86a76b0e9825d4420259cf836f9230a)

<h2 id="36e3a1ad5f706ac6414ea1c1bb708494"></h2>


## Base 58

[base58](python_tips_1.md#0f3fed443cef1a400f3ac44edebf896b)


<h2 id="03174a9cd6c332b4ed1a3fe8d4b64c77"></h2>


## decode/verify redeemCode


```go
// verify
import (
    "github.com/btcsuite/btcutil/base58"
    "encoding/binary"
)

    redeemcodeb58 := vars["redeemcode"]

    redeemCode := base58.Decode(redeemcodeb58)

    info_len := len( redeemCode ) -4
    redeemInfo := redeemCode[:info_len ]
    redeemCrc :=  binary.LittleEndian.Uint32(redeemCode[info_len: ])

    crc := crc32.ChecksumIEEE( redeemInfo  )
    crc = crc32.Update( crc, crc32.IEEETable, []byte("<your secret str>") )
    // log.Println( redeemCrc , crc )
    // 1. crc校验
    if crc != redeemCrc {
        response( w, emptyResData , myerrors.New( 6, "输入错兑换码：无效的兑换码，错误ID 003" )  , ""  )
        return
    }
    channelIdx := int(redeemCode[4])
    if channelIdx < 0 || channelIdx >= len(conf.AvailableChannles()) || conf.AvailableChannles()[channelIdx] != channel {
        response( w, emptyResData , myerrors.New( 7, "兑换码不是该渠道的：不符合使用条件" )  , ""  )
        return
    }
    giftCode := fmt.Sprintf( "gift_code_%02d_%02d", uint( redeemCode[5]), int(redeemCode[6] ) )


```


<h2 id="2440b42391dd88dc32b14c0253b3a95a"></h2>


## python script to generate RedeemCode

```python
#!/usr/local/bin/python3
import sys
import requests
import json
import struct
import binascii
import base58
import shutil
import os
from datetime import datetime
import re

# conf.txt example
# channel , gift_code,  number of redeem

"""txt
huawei  gift_code_01_06     10  202009211500
oppo    gift_code_03_01     5   202009211500
xiaomi  gift_code_03_06     5   202009211500
"""


hosts = {
    "local": "http://xxx",
    "sha" : "https://xxx" ,
    "dev"  : "https://xxx" ,
    "prod" : "https://xxx" ,
}

# 32bit redeemID + 8bit channel  + 8bit 产品序列1 + 8bit 产品序列2 + 32bit crc

Available_Channels = [ "channel6", "channel1","channel2" ]
Available_Channels.sort()

# bulk insert: If either of the value-pair fails, none of the data will be inserted.
templ_insert_sql = """
INSERT INTO tbl_redeem ( redeemID, redeemCode,expireTime )
VALUES
{}
;
"""

RE_GIFTCODE = re.compile( r"gift_code_(\d{2})_(\d{2})" )

if __name__ == '__main__':
    host_key = len(sys.argv) < 2 and "n/a" or sys.argv[1]
    if host_key not in hosts:
        print( "usage: redeemGen.py (local|dev|prod) [conf.txt] " )
        sys.exit(1)

    host = hosts[ host_key ]
    print ( "host:", host )

    # get max redeem id in database
    url = host + "/maxredeemid"
    r = requests.get(url)
    resp = json.loads( r.text )

    if resp['errcode'] != -1:
        print( resp[ "err" ] )
        sys.ext(1)

    maxRedeemID = resp["data"]["maxRedeemID"]
    startIdx = maxRedeemID + 1
    print( "start redeem index :", startIdx )
    print( "Available_Channels:", Available_Channels )

    # read config
    conf_file = "conf.txt"
    if len(sys.argv) >= 3:
        conf_file = sys.argv[2]

    with open( "conf.txt" ) as fp:
        lines = fp.readlines()

    output_dir = "{}-output-{}".format( host_key, startIdx )
    shutil.rmtree( output_dir, ignore_errors=True )
    os.makedirs( output_dir )

    sql_values = []

    for line in lines:
        items = line.split()
        if len(items) >= 4:
            channel, giftCode, number,expire8 = items
            print( "\tgenerating:", channel, giftCode, number, " from:", startIdx )
            expireTime = int(datetime.fromisoformat(expire8).timestamp())

            channel_idx = Available_Channels.index( channel )
            if channel_idx == -1:
                raise Exception( "error channel" )

            result = RE_GIFTCODE.match( giftCode )
            code1 = int(result.group(1))
            code2 = int(result.group(2))

            redeemCodes = []
            for i in range( int(number) ):
                info = struct.pack( "IBBB", startIdx + i, channel_idx, code1,code2  )
                crc = binascii.crc32(info + b'<your secret str>' )
                info_crc = info + struct.pack( "I", crc )
                # print(info_crc, len(info_crc))
                redeemCode = base58.b58encode( info_crc )
                # print( redeemCode )
                redeemCodes.append( str(redeemCode,'utf-8' ) )
                sql_values.append( '( {},"{}", {})'.format(  startIdx + i, str(redeemCode,'utf-8' ) , expireTime ) )
                pass

            # output
            with open( os.path.join( output_dir , "{}-{}-{}-{}.txt".format( host_key, channel, giftCode, number ) ), "w" ) as fp:
                fp.write( "\r\n".join( redeemCodes ) )

            startIdx += int(number)

    with open( os.path.join( output_dir , host_key + "-redeem.sql"), "w" ) as fp:
        fp.write( templ_insert_sql.format( ",\n".join( sql_values ) )   )

    print('done')
```


