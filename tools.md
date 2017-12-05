# Tools
子目录:
- [合集](#合集)
- [Metasploit](#metasploit)
- [BeEF](#beef)
- [OSINT](#osint)
- [Secure Headers](#secure-headers)
- [隐写](#隐写)
- [Cracking](#cracking)

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大，我可以不可以把beef理解为一个网络探针，并顺便有着浏览器漏洞利用工具的一个框架


可以。



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