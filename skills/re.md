# 逆向


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 5u9ar 提问：
余大大，想请教一下，对于二进制类的漏洞挖掘，这类技术公开的学习资料少，能找到的也只是一些nday和fuzz payload去间接的学习，想问的是这类技术应该如何入门比较好呢？


《有趣的二进制》



...

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 这本书买来看了下，很不错，谢谢余神推荐。想追问一句  win平台的process monitor在mac linux有类似的工具吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 一下没想起来，也许可以了解下 OSSEC


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

厉害厉害，蠕虫传播会这样加强的，这次 Petya 还是老方式

<img src="https://images.xiaomiquan.com/FqGGq5Gc4xBJ5LggtzPlva6a-EdH?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:rJAvFUfme2O5tn_Dm-93YpPZCQc=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

怪不得内网感染那么凶？通过 WMIC、PSEXEC 这些经典内网渗透技巧来传播感染内网...即使内网那些机器补丁了之前的补丁(WannaCry 的 MS- 17010)也没用

<img src="https://images.xiaomiquan.com/FgnO9E-NSnxwTIZ669Wwq2EBWRmF?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:yRyW7mwEVquJ9XgkS_lgwYACBTc=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-28:


__#Petya#__

蠕虫样本分析各家应该加强两点，只是建议啊：1. 加密解密的清晰流程；2. 内网渗透部分的技巧，恐怕这块需要这方面职业人士才能一眼道破了...

什么系统、文件、注册表、网络等行为这个各家分析都很成熟，真的挑战职业的至少包括上述两点。

补充：

还有第3点：清晰靠谱的解决方案，像关闭 445 这么粗暴的就不用再提了...企业内网架构里，你说关就关啊



...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 比较全的#Petya#信息:
[https://gist.github.com/vulnersCom](https://gist.github.com/vulnersCom)



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

  卡巴斯基这篇分析不错：


[Schroedinger's Pet(ya) - Securelist](https://securelist.com/schroedingers-petya/78870/)

 

最关键是点名了 139、445 这两个端口，上下文可以知道为什么是这两个端口。

报告昨天的:-)



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 附微软的报告：
[New ransomware, old techniques: Petya adds worm ca...](https://blogs.technet.microsoft.com/mmpc/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/)




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

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 目前， marketplace已经下架这款恶意插件，所以链接一已经失效，但是插件官网和github目前还可以访问。但是官网和github下下载的插件源代码已经删除了恶意代码部分，不过github上release出的安装包，我看了一下依然包含恶意代码，有兴趣的同学可以研究一下，安装包下载的链接：
[https://github.com/cnfree/Eclipse-Class-Decompiler...](https://github.com/cnfree/Eclipse-Class-Decompiler/releases/download/v2.10.0/eclipse-class-decompiler-update_v2.10.0.zip)


PS：难道这个跟xshell一样，被入侵后恶意添加的？😂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 不知道多少人中招，而且这个后门还好危害不是那么直接

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 从marketplace的下载量以及github上源码的更新时间，估计还是很可观的


...

---


