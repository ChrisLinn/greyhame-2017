# Penetration Testing
子目录:
- [webshell扫描](#webshell扫描)
- [域渗透](#域渗透)
- [MSF](#msf)
- [Exchange](#exchange)
- [边界设备安全](#边界设备安全)

## webshell扫描

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
使用字典远程扫描webshell，脚本发现疑似webshell后如何更好的进一步自动化甄别与判断。（假设密码已知，webshell包括大小马和一句话）


以前我们做过这个研究，这种远程扫描来准确识别并不容易，对于已知 Webshell，我们可以加精准特征（比如：HTML 里的内容、代码执行的返回内容、特别的文件名等），想通过什么好算法来处理，其实很难。


---

## 域渗透

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
想学习有关域渗透的一些资料，windows域 08/12/WIN10安全检测及bypass，挺说还有linux域，感觉在这方面很欠补，毕竟环境接触的少，网上说的都模棱两可，大多不可行，弄的晕头转向，想权威体质的学习一下


安全技能树里推荐了不少，如果你真想感受，首先得“坏”。


---


## MSF


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天再转篇 FreeBuf 的文章《MSF外网持久控制Android手机并渗透测试局域网》：


[MSF外网持久控制Android手机并渗透测试局域网 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/sectool/136574.html)



这个大三学生动手能力不错，哪家相关安全公司需要，可以考虑收了。

年轻人应该多折腾，守正出奇。把握好度就行，一定要把握好度，否则，违法犯罪你迟早跑不掉。

BTW：今天转的 FreeBuf 另一篇文章作者据说只是个高中生。



...

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 我也看了，感觉好像有办法实验一次，不过有很多点疑问，试试再来请教可好，现在就有个问题，我用dns欺骗在家里能骗局域网内一台机（共8台只能骗一台），在办公室一台都骗不了，一执行还把人弄死你了，大侠请赐教

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 你怎么做dns欺骗的？

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 说到守正出奇，今晚突然想起之前看过的一个贴，[tieba.baidu.com/p/4963716287?see_lz=1&pn=1](tieba.baidu.com/p/4963716287?see_lz=1&pn=1)  这位大兄弟的SE也是六到没谁了

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: kali下用ettercap,,扫描主机经常扫不全，中间人经常无效……

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比看看 bettercap

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 所以啊有高手快速指导反馈才能进步，半年前就这个问题折腾的半死，最后都停止玩了，两台电脑一台没问题，一台win10下虚拟机能nat联网，可是不能桥接，网上都查遍了也没解决

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 对比结果可以再反馈下

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这种远程问就是很难弄明白，各种小问题非常繁琐，每一个小坑都要折腾半死，烦的自己都不好意思一直问

<img src="https://file.xiaomiquan.com/e6/16/e616b63d215ace23913e168c6b8d4f4b20eeab9eb71886ecabb3bd60cd4f07fe.jpg" width="25px"/> __萝卜__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: ettercap跟bettercap都试过 感觉都是时灵时不灵 cos哥有没有更稳定的中间人工具推荐？


...

---

## Exchange

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
内网中域控权限 Exchange服务器可控 如何在命令行获取所有邮箱列表及单个邮箱邮件打包 或按时间段打包


好吧，还是公开回复吧，你可以参考这个项目：


[GitHub - sensepost/ruler: A tool to abuse Exchange services](https://github.com/sensepost/ruler)



"Ruler is a tool that allows you to interact with Exchange servers remotely, through either the MAPI/HTTP or RPC/HTTP protocol. The main aim is abuse the client-side Outlook features and gain a shell remotely."

通过 MAPI/HTTP 与 RPC/HTTP 协议。



...

<img src="https://file.xiaomiquan.com/89/da/89dac2fbbada82afb3c1152dd4f88d703c91d5f5cbd238debe3f749b98c36f68.jpg" width="25px"/> __Twi1ight__: 用powershell在exchange服务器上也可以直接导出pst文件，支持按时间段导出，这是官方自带的


...

---


## 边界设备安全



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
你好，能不能分享一些关于边界设备安全的资料，例如路由器，防火墙这类设备的安全，以及如何基于这类设备进行渗透测试，谢谢


之前分享的知道创宇研发技能表里有列不少。渗透测试高姿势可以参考 NSA 方程式被泄露的那批防火墙 Exploits。



---