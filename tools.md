# Tools
子目录:
- [合集](#合集)
- [getsploit](#getsploit)
- [Metasploit](#metasploit)
- [DVWA](#dvwa)
- [BeEF](#beef)
- [nmap](#nmap)
- [Kali](#kali)
- [OSINT](#osint)
- [Secure Headers](#secure-headers)
- [隐写](#隐写)
- [Cracking](#cracking)
- [zANTI](#zanti)

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
