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

