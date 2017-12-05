# Tools
子目录:
- [综合](#综合)
- [Metasploit](#metasploit)
- [BeEF](#beef)
- [OSINT](#osint)

## 综合

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
[渗透技能树之利器 v1.pdf](https://github.com/ChrisLinn/sst-2017/blob/master/docs/%E6%B8%97%E9%80%8F%E6%8A%80%E8%83%BD%E6%A0%91%E4%B9%8B%E5%88%A9%E5%99%A8%20v1.pdf)

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

