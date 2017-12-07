# Mobile/App

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
弦哥，能分析下前段时间引起iOS微信crash的天线宝宝gif图么


FreeBuf 上已经有分析：

[一张GIF引发的微信崩溃 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/terminal/135577.html)



这种畸形 gif 也是可以 fuzzing 出来的。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-29:

> Oliver 提问：
余大大，最近一个月从Web安全转到了App安全，感觉测重点还是业务和服务端，余大大怎么看待app安全测试呢


挺好的，Web 安全的技能还能延续。

App 安全分为几大块：

1. 本地安全，如：权限控制、数据安全、第三方接口安全、恶意代码执行、代码保护等

2. 通信安全，如：SSL 证书机制、一些加密算法等，主要对抗中间人劫持

3. 云端安全，由于很多是走 HTTP 这种轻量级协议，所以 Web 安全的技能在这可以复用起来

那么做 App 安全测试这些都需要覆盖。还有一般情况下除了网络安全外，企业还会考虑业务安全，比如风控有关的，对抗羊毛党。

App 安全审计推荐个不错的自动化平台 Janus(appscan.io)，看看，可以开眼。另外我昨天发的那个“渗透技能树之利器”，里面有 Android 安全审计相关的平台或工具，可以也顺便了解看看。

工欲善其事，必先利其器。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
目前来说，有没有可能利用web安全技术，在手机上实现非交互式(或者一次点击)的获取物理地址。
有什么方案吗？


暂无非交互。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-14:


__#资源#__

  Android 应用逆向入门

圈子有不少同学有问安卓安全/调试/逆向方面的知识，这里推荐这篇：


[https://www.evilsocket.net/2017/04/27/Android-Appl...](https://www.evilsocket.net/2017/04/27/Android-Applications-Reversing-101/)



这篇文章很不错，可以学到：

apk 基本知识，adb 基本命令，网络分析（用到了作者自己开发的 bettercap），静态分析，动态分析，动态注入等入门知识。

除了文中这些，我还有用到的如：Inspeckage、MobFS。

实战出真知。

<img src="https://images.xiaomiquan.com/FnpxBcd8M5Z8YfmmTHV_tusHlkbn?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lz2IwMYoeus_E09sqOHOl57X0Ys=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-16:


__#经验#__

想刷黑手的同学，重点推荐一加1代（淘宝买二手就好），一加2、3、3T也行，如果你钱多的话。现在一加最新是5（没有4），但是5还不建议去刷，官方没出兼容方案，如果你不怕，可以自己折腾。

黑手可刷机型完整清单可以看官方这个链接：


[Home · offensive-security/kali-nethunter Wiki · Gi...](https://github.com/offensive-security/kali-nethunter/wiki)

 

一旦有一加5可刷黑手的新消息，我会乘势好好跟进并分享黑手使用经验。



...

<img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: ZUK Z1也可以刷

...

---
