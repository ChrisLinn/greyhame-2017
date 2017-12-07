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

