# Defense


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> Sea0fStars 提问：
使用AppArmor或者SELinux加固系统，效果明显吗？然后，如何更好的加固Web服务器呢？


明显，其他可以参考安全技能树里防御那里的说明与资料。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦老师，请问您如何看待现在的入侵检测技术已经很成熟，也有很多检测web注入攻击的技术被提出，但web注入攻击的误报率、漏报率仍然很高的问题？


没感觉很成熟呀，在各种动态复杂场景下，所谓的“智能”、“自学习”、“下一代”都难以适应，别看宣传做得那么好，漏误报一直是很大的问题。但再深入思考下，其实这些防御或检测“智能”水平相当情况下，这种攻防平衡目的倒是达到了。

未来如果 AI 真能在这样的场景下发挥好，会是很大的机会，可是真的懂 AI 又懂安全的人有几个呢？🙂



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> 匿名用户 提问：
有一些账号密码，或者一些关键的信息。以前一直都是用的txt或者word保存，学习过sql sever。用什么保存这类文件，是数据库还是用其他的工具呢？若是数据库选择什么数据库比较合适且以后学习安全也适合的。希望解答~


1Password



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天看到这篇文章《论如何反击用AWVS的黑客》：


[论如何反击用AWVS的黑客 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/news/136476.html)



思路是经典的，本质是 AWVS 内置的浏览器解析引擎会执行我们自定义好的 JavaScript。然后大家可以再看看 BeEF 里的路由器攻击插件集：

`beef/modules/exploits/router/`

这里有一堆路由器的 CSRF 利用插件。

如果你在自己的页面（比如自己的博客）挂上这些插件利用，哪天有人不小心访问你的页面，那么他们用的路由器就可能被 CSRF 利用，然后中招，比如有命令执行的，可以反弹出 MSF 利用。

去年我办的 TOBEAHACKER 培训，我分享了一个国产路由器 0day 利用，也是此道理。未来会考虑公布完整的挖掘与分析利用全过程。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 本圈特别补上 BeEF 里路由器攻击插件集合的链接：
[beef/modules/exploits/router at master · beefproje...](https://github.com/beefproject/beef/tree/master/modules/exploits/router)


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-10:

> 匿名用户 提问：
iPhone保持不越狱，及时更新，同时不让其他人碰到，既然生活离不开手机，如何保护好自己手机上的隐私安全？


已经很安全，如果还中招你就遇到百万价值的0day，或者无力抵抗的黑灰产业。

在密码方面 1Password 值得用，云服务谨慎用，陌生 Wi-Fi 更需谨慎。



...

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 
[隐私大爆炸，你得学几招保护自己](http://mp.weixin.qq.com/s/Kxe8OzmxCTxYjvjq3rTtlw)


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-09:

这周开始网络流量分析的系列分享
简单来说，攻击行为都会产生网络流量(侧信道攻击另谈，以后分享)，许多从主机防护层面看起来再隐蔽的攻击行为，从网络流量层面上来看都非常明显，举个比较极端的栗子：某黑客拿0day打下一台服务器种了个免杀马。这个场景下大部分安防设备都无效，但是如果上了网络流量分析，你会发现那个免杀马发出的心跳包是多么明显，0day利用的过程每一条指令都在数据包中显露无遗。很容易就定位到问题机器，然后走常规流程处理。

工欲善其事，必先利其器。推我日常用的神器之一，科来网络分析系统
[下载科来网络分析系统技术交流版 - 科来](http://www.colasoft.com.cn/download/capsa.php)


技术交流版是免费的

一个国内厂商做的，数据包的分类和展示都要比Wireshark直观，可以实时抓包分析也可以导入数据包回放分析，大伙儿先下来玩玩熟悉一下功能，官网也有非常详细的模块说明和几个案例，后续我会分享用如何通过网络流量分析发现常见的攻击行为

<img src="https://images.xiaomiquan.com/Fg38m8_XtJpyVgWEpgmp9lAoRWLV?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:TCJ9nLtevA2WLDs3PzWZ3_YWHI8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrI_KHfmNXcTZOFR9_2az9eU1zHA?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:pvVUPPjEyMwGK4RdgiLktUUnf3E=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 记得大学时老师推荐了三个软件，wireshark fiddler 科来，科来官网有一副网络协议的导图，能否推荐一下哪些协议值得学

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: TCP/IP详解永远是经典😄

...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-16:

网络流量安全分析第二弹—发现端口扫描

许多入侵都是从端口扫描开始的，发现扫描行为是网络安全流量分析里重要的一环，本次分享如何从网络流量分析中发现端口扫描行为

(由于小密圈不支持图文混排，我写了个PDF)


__分享文件:__
[网络流量分析发现端口扫描-ATTOT.豆.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-12:


__#工具#__

基础工具之 防火墙管理软件iptables

很多人知道iptables却不知道netfilter,实际上iptables只是linux防火墙的管理工具，真正实现防火墙功能的是netfilter，它集成在linux内核中。

我以前也和大多数人一样，对iptables只会一些简单的操作，编写简单的规则进行网络安全防护，最近几天由于工作需求，对它系统性的研究了一下，才发现原来对它的认识是那么的浅薄。据我所知有一些小型企业，是直接架起一台pc将iptables当成硬件防火墙来用的。

iptables 不仅可以进行常规的规则限制，还可以用来做端口转发、关键字过滤、时间段控制、连接数控制、速率控制，可以通过对recent模块的各个参数进行组合来匹配各种各样的特征包，然后根据匹配规则来执行各种动作，自由度非常大。
一个有趣的例子是当你的ssh不准许外部任何IP进行连接，但是自己有时候又有管理需求，可以定制一个暗号，来使你的ip可以接入ssh。
实例：

```
(1):iptables -P INPUT DROP
(2):iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
(3):iptables -A INPUT -p icmp --icmp-type 8 -m length --length 128 -m recent --set --name SSHOPEN --rsource -j ACCEPT
(4):iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT
(5):iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --rcheck --seconds 15 --name SSHOPEN --rsource -j ACCEPT
```

解释：

```
(1):先将INPUT 默认所有流量全部DROP
(2):-m --state 意思为引用状态匹配扩展，将其中RELATED，ESTABLISHED状态的数据包设置为准许
(3):--icmp-type 8 为ping的请求数据包类型，-m length --length 128，引用length匹配扩展，并且匹配长度为128，icmp包本身包头大小为28，这里填写大小128，实际ping 大小为100的包就可以匹配到，-m recent 为引用recent模块，并设置一个记录的名字为 SSHOPEN，设置完成后，触发一下这个规则，可以在 /proc/net/xt_revent/SSHOPEN 看到相关的记录。--rsource 为记录源IP
(4):这条意思为准许ping的请求包。
(5):增加一条准许连接到22端口，并且状态为新建立，在SSHOPEN 
```

列表有记录源IP，在15秒内，匹配通过这些条件后就准许放行ssh连接了。
配置完后，你再去连ssh是连不通的
你用windows，ping -l 100 IP ，之后再用ssh就可以连接了，相当于一个暗号。

这个例子只是想表达iptables非常自由，脑洞够大的话可以想到各种条件搭配去执行各种动作，有兴趣的话也可以看看我发的第二篇中的，利用iptables进行端口复用的例子，那个作者真是个高手。值得学习！

最后贴一张我做的比较粗糙的关于iptables的思维导图，就是推荐大家在学习一个东西的时候，最好边做笔记并且能把核心的要点都整理出来，这样对学习的效率会是一个很大的提升，并且日后自己回头看，也很容易回忆起来。


[http://www.zsythink.net/archives/1199](http://www.zsythink.net/archives/1199)

iptables快速入门系列，超爱这种把一个技术工具写的浅显易懂连载十几篇，我真的是非常敬佩这种分享精神的人！

<img src="https://images.xiaomiquan.com/FiJUyuJtGJhraCliPwgk-IzorA6a?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nCPig9yhFVK-Cs6skNsWE9vNEGQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__: 通过思维导图能更好地把知识内化为自己的东西，顺便问一下这种图是用什么软件做的？

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__ replies to <img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__: XMind8


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-08-21:

今天分享文件加密

出于各种各样的原因，我们都有一些文件需要加密，万一文件被盗对方也无法恢复，加密工具多如牛毛，我尽量推荐可信的工具


__Truecrypt__
    
平台：windows/Linux/MacOS

斯诺登曾推荐过这款加密工具，图形化界面，由于其加密严格，难以破解，作者一直保持神秘，但在其官网遭到入侵后据传其作者被NSA请去喝茶，在2014年停止更新，官网请大伙移驾微软的BitLocker，公开的理由是truecrypt被曝光存在提权漏洞，不过这个比较牵强，毕竟truecrypt源码经过两次代码审计，并没有发现明显的后门。目前不建议使用最后一版7.2（喝茶后的版本），建议使用7.1.a或更早的版本。

官网已死，下载请去
[TCnext - Site dedicated to the development of the ...](https://truecrypt.ch/)


使用上的howto请google，很多

__dm-crypt__

平台：Linux
    
Linux内核提供的磁盘加密工具，“dm-crypt”是 Linux 内核提供的一个磁盘加密功能，而“cryptsetup”是一个命令行的前端，通过它来操作“dm-crypt”。

使用dm-crypt首先你要先安装cryptsetup，在ubuntu中：apt-get install cryptsetup

dm-crypt既可以加密整块物理磁盘也可以加密一个虚拟磁盘，这里我给出一个方便简易的使用方法，需要深入的可以看官方文档
[cryptsetup / cryptsetup · GitLab](https://gitlab.com/cryptsetup/cryptsetup)



首先要创建一个容器文件，通过 fallocate 创建一个 10GB 容器文件。

`fallocate -l 10G /root/luks.vol`

接下来使用cryptsetup加密这个文件容器得到一个虚拟加密盘

```
cryptsetup --cipher aes-xts-plain64 --key-size 512 --hash sha512 --iter-time 10000 luksFormat /root/luks.vol
```

参数含义：

```
--cipher    加密方式
--key-size  密钥长度
--hash  散列算法
--iter-time 迭代时间
```

使用如下命令打开上述的文件容器，使用的映射名是 xxx（你也可以改用其它单词）。

```
cryptsetup luksOpen /root/luks.vol xxx
```
　
打开之后，该虚拟盘会被映射到 /dev/mapper/xxx

你可以用如下命令看到：

```
ls /dev/mapper/
```

由于加密盘已经打开并映射到 /dev/mapper/xxx 你可以在 /dev/mapper/xxx 之上创建文件系统。命令如下（文件系统类型以 ext4 为例）

```
mkfs.ext4 /dev/mapper/xxx
```

创建完文件系统之后，你还需要挂载该文件系统，才能使用它。挂载的步骤如下。
　　

首先，你要先创建一个目录，作为【挂载点】。俺把“挂载点”的目录设定为 /mnt/xxx（当然，你可以用其它目录作为挂载点）。

```
mkdir /mnt/xxx
```

创建好“挂载点”对应的目录，下面就可以进行文件系统的挂载。

```
mount /dev/mapper/xxx /mnt/xxx
```

挂载好文件系统，用如下命令查看，就可以看到你刚才挂载的文件系统。

```
df -hT
```

接下来，你就可以通过 /mnt/xxx 目录去访问该文件系统。当你往 /mnt/xxx 下面创建下级目录或下级文件，这些东东将被存储到该虚拟加密盘上。

当你使用完，要记得退出。包括下面两步：

+　卸载文件系统 `umount /mnt/xxx` 
+ 关闭加密盘 `cryptsetup close xxx` 

之后你需要再次使用这个加密盘的时候只需要

```
cryptsetup luksOpen /root/luks.vol xxx
mount /dev/mapper/xxx /mnt/xxx
```


使用完后

```
umount /mnt/xxx
cryptsetup close xxx
```

(附图，两种加密工具的对比)

<img src="https://images.xiaomiquan.com/FtUcF_H1D7ntUc5xgSt1DtU6uGd6?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:__vxJ0s3BpiVd-U5wVIlLWsMSfQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 还可以考虑用 TrueCrypt 后的一个分支版本 VeraCrypt

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 是的 Truecrypt官网已经用醒目红色字体警告:Using TrueCrypt is not secure，而且Truecrypt幕后的捐赠者也是很敏感😷

<img src="https://file.xiaomiquan.com/bf/f8/bff8ac74efe0ea61b12ec062defb01cf36b89beb446bf4cfec4a5a9a3130820d.jpg" width="25px"/> __Charles__: 想起当年大学时电脑里的岛国姐姐都是用truecrypt来守护的，舍友曾翻遍我电脑都找不到😂


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-05:

嗯，最近写了些脚本自动采开源情报，定时分享一些，大家可以添进各自的规则里


__分享文件:__
[IOC_20170904.txt](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 你应该顺便科普下😄

<img src="https://file.xiaomiquan.com/37/43/374310d6c0d10abd44b2dbd539c133fde6ac46f958196b2b642747858dc0af82.jpg" width="25px"/> __大宇__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: +1

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 其实这个很简单呀，把情报爬下来处理一下字符串就可以输出了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 处理好说，关键是应用场景、应用背景什么的

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我一般是添到回溯设备里，有相关报警就可以回溯流量，记录源IP、A地址，然后再挖源IP的流量找出出样本，A地址又可以扔进去回溯，挖所有通信过的客户端记录一下，上报处理


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-05:

嗯。。。科普一下自动爬取开源情报
比如
[http://osint.bambenekconsulting.com/feeds/c2-domma...](http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt)

这个源经常更新很多c2域名，那我们只需要写个简单的小脚本每小时自动化爬下来然后每天整合一下
以下是脚本示例

```
#!bin/bash
#获取当前系统时间精确到时
date=$(date +%Y%m%d%H)
#文件名变量
filename=baddomains_${date}.txt
#用wget把情报爬下来
wget http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt
```


作个简单字符串处理后保存
```
cut c2-dommasterlist-high.txt -f 1,2 -d , | sed -e '/#/d' > $filename
rm c2-dommasterlist-high.txt
```

脚本2,每天把拿到的情报去除重复项整合一下

```
#!/bin/bash
#获取昨天的日期
date=$(date -d yesterday +%Y%m%d)
filename=IOC_${date}.txt
#把昨天所有文件排序整合
cat baddomains_${date}*|sort|uniq|sort -t , +1 -2 > $filename
rm baddomains_${date}*
```

最后把以上脚本加入到crontab里面定时运行就OK了



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好😄

<img src="https://file.xiaomiquan.com/c1/72/c172abf7cb79b6e84958c7e46d643c1c4e9dd14a106f35b3bcf1dd251c753a00.jpg" width="25px"/> __ohblackmagic__: 清晰明了，赞

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 有兴趣也可以看看这个（推荐PC浏览器打开）😄

[FireHOL IP Lists | IP Blacklists | IP Blocklists |...](http://iplists.firehol.org/)



更新脚本比较复杂，不过看懂之后再写类似的脚本就不在话下了： 

[firehol/update-ipsets at master · firehol/firehol ...](https://github.com/firehol/firehol/blob/master/sbin/update-ipsets)



<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 脚本可以直接套脚本😂，不过这个IP列表没有对应威胁信息，无从归类😅

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: IP库来源有介绍，有一部分是有针对性威胁信息的，比如某个家族Malwr的C2


...

---

