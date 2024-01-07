[](...menustart)

- [OSX tcpdump](#45270fb7b9364718bc0d75359e96a603)
    - [Basic Usage](#23cb76671b38f735ce0e4ee4e7795897)
    - [Filters](#f3f43e30c8c7d78c6ac0173515e57a00)
        - [filter \[src/dst\] host](#d64d64a80cbd8dde0d09133aa3bc267d)
        - [filter \[src/dst\] port](#9db89898b6cc5692bbfdea625eeaee82)
        - [filter \[src/dst\] net  (network segment)](#f81c64c801ab8c51b518e78c5b22ad64)
        - [filter protocal](#d0f76edbff72d4bb6babc455e7cdcb6b)
        - [Combinations](#b9208b03bcc9eb4a336258dcdcb66207)
    - [Options](#dae8ace18bdcbcc6ae5aece263e14fe8)
    - [Tcpdump Flags](#667dc5257f1557114de086cdcb685c9e)
    - [Examples](#ff7c0fcd6a31e735a61c001f75426961)

[](...menuend)


<h2 id="45270fb7b9364718bc0d75359e96a603"></h2>

# OSX tcpdump


<h2 id="23cb76671b38f735ce0e4ee4e7795897"></h2>

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


<h2 id="f3f43e30c8c7d78c6ac0173515e57a00"></h2>

## Filters

<h2 id="d64d64a80cbd8dde0d09133aa3bc267d"></h2>

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

<h2 id="9db89898b6cc5692bbfdea625eeaee82"></h2>

### filter [src/dst] port

```bash
sudo tcpdump -i en0 -n host 10.192.89.36 and dst port 443 

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:50:37.251495 IP 10.192.89.36.62453 > 52.123.168.210.443: Flags [P.], seq 3437366920:3437366977, ack 3476488259, win 4096, length 57
11:50:37.321724 IP 10.192.89.36.62453 > 52.123.168.210.443: Flags [.], ack 47, win 4095, length 0
```

<h2 id="f81c64c801ab8c51b518e78c5b22ad64"></h2>

### filter [src/dst] net  (network segment)

```bash
$ sudo tcpdump -i en0 -n src net 10.192

listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
11:53:48.418515 IP 10.192.93.218.55204 > 239.255.255.250.1900: UDP, length 175
11:53:48.445103 IP 10.192.89.57.57849 > 239.255.255.250.1900: UDP, length 175
```

<h2 id="d0f76edbff72d4bb6babc455e7cdcb6b"></h2>

### filter protocal

```bash
$ sudo tcpdump -i en0 -n arp
$ sudo tcpdump -i en0 -n ip
$ sudo tcpdump -i en0 -n tcp
$ sudo tcpdump -i en0 -n udp
$ sudo tcpdump -i en0 -n icmp
```

<h2 id="b9208b03bcc9eb4a336258dcdcb66207"></h2>

### Combinations

- 与：`&&` 或 `and`
- 或：`||` 或 `or`
- 非：`!` 或 `not`


<h2 id="dae8ace18bdcbcc6ae5aece263e14fe8"></h2>

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


<h2 id="667dc5257f1557114de086cdcb685c9e"></h2>

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


<h2 id="ff7c0fcd6a31e735a61c001f75426961"></h2>

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


