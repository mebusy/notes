

# OSX tcpdump


## Basic Usage

record packets on the default Ethernet-like interface `en0`

```bash
$ sudo tcpdump -i en0 -n

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:44:20.388596 IP 10.192.91.189.53150 > 230.0.0.1.6666: UDP, length 50
11:44:20.390271 00:9e:1e:13:f6:80 > ff:ff:ff:ff:ff:ff, RRCP-0x23 reply
...
```

The `-n` option tells tcpdump not to attempt to use reverse DNS to map IP addresses to names; such mapping is rarely useful on the modern Internet and it radically slows things down.


## Filters

### filter [src/dst] host

```bash
$ sudo tcpdump -i en0 -n host 10.192.89.36

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:46:04.285959 IP 10.192.89.36.62418 > 52.123.168.210.443: Flags [P.], seq 882599011:882599069, ack 2140293774, win 4096, length 58
11:46:04.357163 IP 52.123.168.210.443 > 10.192.89.36.62418: Flags [P.], seq 1:48, ack 58, win 2048, length 47
11:46:04.357213 IP 10.192.89.36.62418 > 52.123.168.210.443: Flags [.], ack 48, win 4095, length 0
```

src filter

```bash
$ sudo tcpdump -i en0 -n src host 10.192.89.36

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:47:48.716107 IP 10.192.89.36.53613 > 52.98.68.178.443: Flags [.], ack 3559659975, win 2048, options [nop,nop,TS val 1783658578 ecr 49101428], length 0
11:47:48.716361 IP 10.192.89.36.53613 > 52.98.68.178.443: Flags [.], ack 1133, win 2048, options [nop,nop,TS val 1783658578 ecr 49101428], length 0
```

dst filter

```bash
$ sudo tcpdump -i en0 -n dst host 10.192.89.36

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:48:44.361376 IP 52.123.168.210.443 > 10.192.89.36.62418: Flags [P.], seq 2140293962:2140294009, ack 882599301, win 2048, length 47
11:48:52.186808 IP 10.192.0.200.3128 > 10.192.89.36.49517: Flags [.], ack 184043614, win 165, options [nop,nop,TS val 1285380514 ecr 1944732644], length 0
```

### filter [src/dst] port

```bash
sudo tcpdump -i en0 -n host 10.192.89.36 and dst port 443 

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:50:37.251495 IP 10.192.89.36.62453 > 52.123.168.210.443: Flags [P.], seq 3437366920:3437366977, ack 3476488259, win 4096, length 57
11:50:37.321724 IP 10.192.89.36.62453 > 52.123.168.210.443: Flags [.], ack 47, win 4095, length 0
```

### filter [src/dst] net  (network segment)

```bash
$ sudo tcpdump -i en0 -n src net 10.192

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:53:48.418515 IP 10.192.93.218.55204 > 239.255.255.250.1900: UDP, length 175
11:53:48.445103 IP 10.192.89.57.57849 > 239.255.255.250.1900: UDP, length 175
```

### filter protocal

```bash
$ sudo tcpdump -i en0 -n arp
$ sudo tcpdump -i en0 -n ip
$ sudo tcpdump -i en0 -n tcp
$ sudo tcpdump -i en0 -n udp
$ sudo tcpdump -i en0 -n icmp
```

### Combinations

- 与：`&&` 或 `and`
- 或：`||` 或 `or`
- 非：`!` 或 `not`


## Options

- `-X` display package by both ASCII and HEX
    ```bash
    $ sudo tcpdump -i en0 arp -n -X 
    12:12:51.166726 ARP, Request who-has 10.192.94.140 tell 10.192.94.115, length 46
        0x0000:  0001 0800 0604 0001 60a4 4c50 c118 0ac0  ........`.LP....
        0x0010:  5e73 0000 0000 0000 0ac0 5e8c 0000 0000  ^s........^.....
        0x0020:  0000 0000 0000 0000 0000 0000 0000       ............
    ```
- `-XX` display Ethernet header as well
    ```bash
    $ sudo tcpdump -i en0 arp -n -XX
    12:12:48.311278 ARP, Request who-has 10.192.94.43 tell 10.192.94.150, length 46
        0x0000:  ffff ffff ffff 6c0b 84e2 2a1e 0806 0001  ......l...*.....
        0x0010:  0800 0604 0001 6c0b 84e2 2a1e 0ac0 5e96  ......l...*...^.
        0x0020:  0000 0000 0000 0ac0 5e2b 0000 0000 0000  ........^+......
        0x0030:  0000 0000 0000 0000 0000 0000            ....
    ```
- `-A` display package only by ASCII
    ```bash
    sudo tcpdump -i en0 arp -n -A
    listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
    12:18:58.833332 ARP, Request who-has 10.192.93.124 tell 10.192.94.186, length 46
    ..........>d.5
    .^.......
    .]|..................
    ```
- `S` Print absolute, rather than relative, TCP sequence numbers.
- `-i any` listen all interfaces
- `-v, -vv, -vvv` more details


## Tcpdump Flags

TCP Flag | tcpdump Flag | Meaning
--- | --- | ---
SYN | [S] | Syn packet, a session establishment request.
ACK | [A] | Ack packet, acknowledge sender’s data.
FIN | [F] | Finish flag, indication of termination.
RESET | [R] | Reset, indication of immediate abort of conn.
PUSH | [P] | Push, immediate push of data from sender.
URGENT | [U] | Urgent, takes precedence over other data.
NONE | [.] | Placeholder, usually used for ACK.


## Examples

1. Capture all TCP data passing through en0, the destination address is 192.168.1.254 or 192.168.1.200, the port is 80
    ```bash
    $ sudo tcpdump -i en0 '((tcp) and (port 80) and ((dst host 192.168.1.254) or (dst host 192.168.1.200)))'
    ```
2. Capture all ICMP data passing through en0 and the target MAC address is 00:01:02:03:04:05
    ```bash
    $ sudo tcpdump -i en0 '((icmp) and ((ether dst host 00:01:02:03:04:05)))'
    ```
3. Capture all TCP data passing through en0, the destination network is 192.168, but the destination host is not 192.168.1.200
    ```bash
    $ sudo tcpdump -i en0 '((tcp) and ((dst net 192.168) and (not dst host 192.168.1.200)))'
    ```
4. Only capture SYN packets
    ```bash
    $ sudo tcpdump -i en0 'tcp[tcpflags] = tcp-syn'
    ```
5. Catch SYN, ACK
    ```bash
    $ sudo tcpdump -i en0 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack != 0' 
    ```
6. Capture SMTP data. Capture packets whose data area starts with MAIL. The hexadecimal value of MAIL is 0x4d41494c.
    ```bash
    $ sudo tcpdump -i en0 '((port 25) and (tcp[(tcp[12]>>2):4] = 0x4d41494c))'
    ```
7. Capture SSH return
    ```bash
    $ sudo tcpdump -i en0 'tcp[(tcp[12]>>2):4] = 0x5353482D'
    ```
8. Capture DNS request data
    ```bash
    $ sudo tcpdump -i en0 udp dst port 53
    ```
9. Capture the GET packet of port number 8000 in real time, and then write it to GET.log
    ```bash
    $ sudo tcpdump -i en0 '((port 8000) and (tcp[(tcp[12]>>2):4]=0x47455420))' -nnAl -w /tmp/GET.log
    ```


