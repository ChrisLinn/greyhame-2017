# Web
子目录:
- [XSS](#xss)
- [CSRF](#csrf)
- [SSRF](#ssrf)
- [PHP](#php)
- [Apache](#apache)
- [Python](#python)
- [Socket](#socket)
- [协议](#协议)
- [杂](#杂)

## XSS

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:

> 匿名用户 提问：
你好，我看你在微博里面发的XSS,其中有一个 `<title><img src="</title><img src=x onerror=alert(1)//"\>` 其中的解释是title的解析高优先级造成的，能介绍下这方面的知识，或者指点要看的书籍吗？

没什么特别的书，虽然我们那本《Web前端黑客技术揭秘》也有相关介绍。

这方面的知识就是吃透浏览器 DOM，建议去读 Webkit 的源码，及浏览器 F12 去看看 DOM 的怪异解析。


---


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
在xss的时候，输出的内容在html中，这时候可以用html实体编码来替换< >;  如果把< > 事先转译了，浏览器就不会解析了，会把左右接括号原样输出到页面，这是html 自解码机制，能否详细说下自解码原理，原样输出尖括号而又不执行？ 多谢！


如果你买过我曾经的那本书，里面正好提到了自解码机制。但你的问题实在太模糊，我无从再深入回答。



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

<img src="https://images.xiaomiquan.com/FgJfCF8Zg1kR0gmlyQL4A83b03xk?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:UfJr0Kgahh1AO-a7-6875RhUis4=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 

<img src="https://images.xiaomiquan.com/FgddMI0uHCdwNJmjCO0Nr5A6X0lR?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:sft4roGlWzR3MnNl1PxVll3kj9I=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 

<img src="https://images.xiaomiquan.com/FvuVoquQw9ZhRMf0p1YyZxOEAjVR?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:VcUgR8lqT2WzVXsYN9gVxmcb6GY=" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 第一题，原封不动 `<script>alert()</script>`
第二题就是双引号和单引号括号urlencode输入
第三题 `\"`  可以变成  `"`

<img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: `',alert(),'`

<img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 被自己蠢哭了，第三题就因为没在抓包工具里url解码，抓狂了好久。。。

<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: `0');alert('`


<img src="https://images.xiaomiquan.com/FqBOss10t51xjQEn6KC6WNIGK_RN?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Wj7Y0JuWqsXq4gdG1jmDvkkxkdU=" width="50%" height="50%" align="middle"/>


<img src="https://file.xiaomiquan.com/c6/19/c619f2f8272cce087de22a13bf084787e929efee10e32381acfb833c8b9a7b3e.jpg" width="25px"/> __乌鸦__: `'onerror='alert()'`


<img src="https://images.xiaomiquan.com/Fkhh_Sx3PpFtfjImAY5ZyGuEGG0D?e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Jf3LBKlJLtjrlXf-zWbnl37JSp0=" width="50%" height="50%" align="middle"/>


<img src="https://file.xiaomiquan.com/02/c2/02c29c774c01e67904e2a54d7c47a07b32e73898a3e9863a47a26b93099e474e.jpg" width="25px"/> __桔多淇__: 想玩又不会的还不让看攻略😱

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/08/5f/085fb0537ae32a57afd19df88c738810e85c9250a3ec4bff1352a84fa871536e.jpg" width="25px"/> __samurai__: 什么意思，我在这被坑了好久，浏览器标签里的字符串都用的双引号，结果choosetab用的单引号😡

<img src="https://file.xiaomiquan.com/e0/1d/e01d033928215404410d8a95fcd0868cc1cde3f31609eb54f6048cc674ef5baa.jpg" width="25px"/> __一休__ replies to <img src="https://file.xiaomiquan.com/38/9c/389c2cf556f50cb75c0a5ec3a988e7841dfec3eb2a19634628a74b60eaeaf870.jpg" width="25px"/> __Crushmyr__: 我也被自己蠢哭了，我把它当做document.write一样去试各种编码了😂

<img src="https://file.xiaomiquan.com/60/64/60640ca1fb2dfb0131ee8573a60ad8d86961495d76e4d6f025927ab4ce652fcb.jpg" width="25px"/> __国勇@ATToT__ replies to <img src="https://file.xiaomiquan.com/c8/4d/c84d3b3fb2f71423e6a315e509f1918fe8d921e54c95e219cdb75c4083ed3acb.jpg" width="25px"/> __Loong__: 这个方法聪明


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
[IPB.zip](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/IPB.zip)


...

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 调试的都快晕了，能请问一下是哪里对$controller进行了输出么

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: convertutf8/System/Output/Browser/Template.php

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 能具体到行么。。。这个文件当然看过了

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 里面有个模板，输出了controller变量。这个变量直接从request获取没经过过滤。

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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-09:


__#科普#__

XSS 与 CSRF

以下转自我之前在「XSS'OR技能」圈子里的分享，因为正好有同学遇到这个困惑，科普供参考。

__XSS__

XSS(Cross Site Script，缩写为了区分 CSS，把 C 改为 X，X 本就有 Cross 十字的含义），中文称为“跨站脚本”。我们只要能把我们可控的 JavaScript 脚本内容注入到目标页面，那这个页面就存在 XSS 漏洞。而 JavaScript 就是 XSS 这个过程的核心魔法。

JavaScript 这个核心魔法能在哪里释放？你看看整个 DOM(Document Object Model) 树，能执行 JavaScript 的地方主要有：

1. `<script>` 标签内；
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

__CSRF__

CSRF(Cross Site Request Forgery)跨站请求伪造，这个核心点在于：

从目标用户浏览器发出的 HTTP 请求不是用户预期内的，那么都可以认为这是一种跨站请求伪造，关键不在“跨站”，而在“请求伪造”。

那么，通过怎样的机制可以去“请求伪造”，或者说简单点，“发出请求”？回答这个问题前，首先得区分下请求方式都有哪几种？

1. GET 请求，就是一个 URL 形式
2. POST 请求，需要提交表单
3. 其实还可以独立提一种请求方式，就是 AJAX 这种异步请求
4. 其实其实，如果涉及到跨域，就不是提 AJAX 了，而是提 CORS(Cross-Origin Resource Sharing)跨域资源共享。

注：AJAX 与 CORS 共同点在于都是基于 XMLHttpRequest。

区分这些请求方式后，我们就可以挖掘都有什么机制可以发出请求，比如：

1. GET 请求，一堆的标签都可以发出这个请求，如：`<img src="[目标 URL]">`
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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-26:

> Vesper 提问：
碰到一个伪静态站。XSS提交留言需审核，登录页点不出来，看了源码无奈学艺不精，有点焦灼，无头苍蝇。希望余弦大大能科普一下这方面的渗透技巧，给我指一下路。


可以用 XSS 盲打呀，可以拿 XSS'OR 去做盲打测试，如果不仅是测试，自己可以 fork XSS'OR，修改代码很容易，就可以打造一个自己的盲打平台。



---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-01:


__#姿势#__

 
分享一个最新的Safari XSS供大家把玩把玩，权当抛砖引玉

```
<script>location.href;'javascript:alert%281%29'</script>
```

<img src="https://images.xiaomiquan.com/FvEIJiOesyg3CW4IHSS8gbuIxwQK?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:PHR5k-Xs0LWwC3VBmRDJhOzVnxs=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 把;当成=

这类trick都可以通过简单的fuzzing找到。

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 大家可以拿起 Safari 浏览器，访问测试：

[http://xssor.io/s/safari.html](http://xssor.io/s/safari.html)



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: iPhone上的Safari也可以哦

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 通过 cos 这个例子发现了 Safari 重定向以后接下来的代码都不执行，而 Chrome 和JavaScript 伪协议似乎有 py 交易，重定向以后还从下一行执行到结束。😅


...

---

## CSRF

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-23:


__#姿势#__

Kaspersky Anti-Virus File Server Multiple Vulnerabilities


[Kaspersky Anti-Virus File Server Multiple Vulnerab...](https://www.coresecurity.com/advisories/Kaspersky-Anti-Virus-File-Server-Multiple-Vulnerabilities)



最近很忙，这篇早想分享，忘记了。

里面有个技巧：CSRF to RCE，很低级的漏洞，但威力很大，这种“跨”属于“跨应用”，这类漏洞其实不少。

Payload 如下：

```
"notifier": {"Actions": [{"Command": "touch /tmp/pepperoni", "EventName": 22, "Enable": true,
"__VersionInfo": "1 0"}]
```

攻击请求如图所示。攻击的是 9080 端口，利用时只需诱骗目标用户访问一个链接，触发这段攻击请求就可以成功。就是个典型的 CSRF 过程，只是这次“跨应用”了，搞掉了卡巴斯基的反病毒文件服务。

<img src="https://images.xiaomiquan.com/FkXnlZX2teScz5pXL2wXLJ9sut3A?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:tUAmQS9aEnm90U_bQmFSqBc9-yg=" width="50%" height="50%" align="middle"/>


---


## SSRF



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

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-24:


__#HITB#__

今天最后的一个议题，和 SSRF 有关的，也是很期待的一个，来自台湾的 Orange。

大家可以看之前他的这篇，一个很棒的 exploit 过程：

[【BlackHat 2017 议题剖析】连接的力量：GitHub 企业版漏洞攻击链构造之旅](http://paper.seebug.org/363/)



之前说了，SSRF 是新 Web 安全里非常重要的一项，之前在本圈也发过相关资料，大家可以自行搜索。

会后我们交流了一个多小时，很 nice。大家对 Red Team 有发自内心的激情。几个来自不同国家与区域的安全人员，交流甚欢。


__分享文件:__
[D1 - Orange Tsai - A New Era of SSRF – Exploiting URL Parsers in Trending Programming Languages.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

## XXE



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-04:


__#资源#__

 XXE 及 XXE OOB 攻击清单

XXE 全称：XML External Entity，XML 扩展实体。扩展了，攻击面就来了。

OOB 全称：Out of Band，带外数据，就是把数据传出去的方式，应用场景主要在无回显的场景，也就是所谓的盲打场景。

这里有一份清单，还不错，作为玩到这类攻击时的参考：


[https://gist.github.com/staaldraad/01415b990939494879b4](https://gist.github.com/staaldraad/01415b990939494879b4)



这里漏洞如何挖掘呢，自动化其实也不难，那些 Payloads 发出去，想办法接收判断就好。如果你在渗透时，发现有 XML 格式的数据传输（或 base64 等可逆加密后的），那么就可以顺手一试是否有 XXE 漏洞。

总会存在惊喜的。



---


## PHP



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

<img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 一开始不会php，多做ctf题😄php不会就百度 慢慢的就会了😂😂

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/b2/27/b2273c727cd42d41352bd2bb195a82e4d41270073f0e99e7e46ffb1a1566c21f.jpg" width="25px"/> __。__: 2333，我一开始也是这样的。不过建议还是能系统的把基础的php过一遍，让比赛是温故而知新。

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 在用xdebug来调试的时候我碰到了这种情况：遇到代码做过混淆或者加密的php，xdebug直接崩溃了，大大遇到过这种情况么，有解决的办法么？另外，能不能分享一波审计大牛的博客~😜

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 加密的没法调试，尝试去一些在线解密去混淆的站点试试看能不能还原。至于代码审计牛的博客我倒是有好些，等我抽时间整理出来分享给你们。

<img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 哦哦，好的好的

<img src="https://file.xiaomiquan.com/bd/87/bd872d6bf8f2e37a8687398bc1bc0af07f9b896fc43c3663a77f830db1ac4c5c.jpg" width="25px"/> __ken🐜__ replies to <img src="https://file.xiaomiquan.com/8d/e2/8de2de5d6a1eb3d448658bdd79d07593b0268ecf828399fd6d6a3a2912077290.jpg" width="25px"/> __Shutdown-r__: 法師的審計的好像開源了。可以去看下他的工具


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-08-16:


__#代码审计#__

  
__#姿势#__

  
之前发了两篇代码审计的文章，但是感觉大家没什么反应，可能是因为有很多圈友缺乏相应的基础，看起来很费力。因此我决定从零开始讲代码审计，还是那句话，希望各位能有所收获。

今天先来讲环境搭建。首先，你要有一台靶机和攻击机，靶机的操作系统随意，win或者Linux都可以。如果只想放在本地，那么服务器的ip地址不能是127.0.0.1，需要绑定其他ip地址，如192.168.1.100,这样才能使用burpsuite抓包。下面是搭建资料链接。(这一段经 @大宇 同学提醒，已更正)

__Linux:__

- [LAMP环境搭建 - Linux 入门教程 - 极客学院Wiki](http://wiki.jikexueyuan.com/project/linux/lamp.html)


- [ApacheMySQLPHP - Community Help Wiki](https://help.ubuntu.com/community/ApacheMySQLPHP)

（这个更简单，一键安装）

__Win:__

- [http://www.phpstudy.net/](http://www.phpstudy.net/)


一个集成环境的软件，非常方便，可以选择版本。

我自己是用Mac的本机当靶机的，然后拿kali虚拟机当攻击机的，环境搭建使用的是MAMP PRO，因为这个集成相当方便，可以快速切换服务器或者php版本。

接下来就是按照phpstorm以及对于代码审计最重要的功能Xdebug。phpstorm各个操作系统都有对应版本，网上都可以找的到。我就不说了。

xdebug的安装资料则如下：

- [Xdebug: Documentation](https://xdebug.org/docs/install)



安装之后的配置：

- [PhpStorm Xdebug远程调试环境搭建原理分析及问题排查](http://paper.seebug.org/308/)


- [PHP调试利器XDebug Mac下安装与使用 | funbox's Blog](https://ifunbox.top/mac_php_xdebug_phpstorm_install)



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

<img src="https://file.xiaomiquan.com/50/15/50154c902d647320df2ca5062d97714537e014cedca871845319cb445a4fc409.jpg" width="25px"/> __GoodLuck__: 很友好 支持。。。

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 请问一下有没有关于sublime做代码审计的配置？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__: 像sublime或者atom这种编辑器确实可以武装的很像ide一样，但是太麻烦了，ide更方便而且功能强大。

<img src="https://file.xiaomiquan.com/87/4a/874a9d7bc90aec06621571157ebc051fbde8f37747aa5c2d5a8ebb11163cbe88.jpg" width="25px"/> __风__ replies to <img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__: 好的，谢谢了


...

---

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-08-28:


__#姿势#__

 
__#代码审计#__

  
php的配置文件很重要，咱们先从搞懂配置文件开始吧。:)


__分享文件:__
[代码审计之php配置文件.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)


---

## Apache

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


## Pyhton



<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-10:

> 老七 提问：
django写的网站开启了debug，有没有漏洞啥可利用的，django版本是1.10.3


除了知道目标系统一些基本情况之外，我这没有，其他同学有好的利用思路可以说下。



...

<img src="https://file.xiaomiquan.com/77/94/7794a6fa7fe3127b708f61d481fc168de96e9be8d2484ddd20ab6edb9153c405.jpg" width="25px"/> __快看这是一只野生的自然卷__: 开启debug，如果是sql存储或查询出错会暴露models的字段信息（表名，列名），还有出错部分的源码，可以尝试利用，因为本身django提供了很多参数传递的功能，如进行sql查询时tb.objects.filter（id=1），很多常规的测试方法都会失效，只能指望开发人员比较喜欢用语句拼接什么的😰。现在各种cms做的越来越安全，而码农门槛越来越低，还是从逻辑上挖掘漏洞容易些。


...

---



## Socket


<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ on 2017-06-25:


__#姿势#__

 
__#python#__

 
今天我来给大家科普科普python当中socket的使用。socket可以说是网络安全编程领域当中，用的最广泛的库了。只要涉及到网络应用层，除非是web，不然都逃不开socket。所以今天我就来为大家介绍介绍socket的使用。


[python中socket模块的使用 | D_infinite的小站](http://dinfinite.cn/2017/06/25/python%E4%B8%ADsocket%E6%A8%A1%E5%9D%97%E7%9A%84%E4%BD%BF%E7%94%A8/)



以后，我会带来一系列跟python有关的分享。如果有什么问题或者建议的，欢迎在评论区留言指教。



...

<img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: 请问大神，关于http请求的库最喜欢或者最推荐哪个？为啥？

<img src="https://file.xiaomiquan.com/63/d0/63d0b05ed5938e543b17689ddc40ce30365485a71ed6a24d7a40768910845fec.jpg" width="25px"/> __D_infinite@ATToT__ replies to <img src="https://file.xiaomiquan.com/ed/8e/ed8e264a6c1b3e6acd2f7423ad6ccc19dfd5810cd3b64c1a1c58cc6e04010c56.jpg" width="25px"/> __bit4__: requests

...

---


## 协议



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

<img src="https://file.xiaomiquan.com/f7/9a/f79af1bde651a9dd2c989af5ff7daef5802563815d9456228954484c65760e60.jpg" width="25px"/> __岳锦文__: 配合wireshark一起食用，效果更佳😄

<img src="https://file.xiaomiquan.com/e1/0d/e10dbdcd9c404ec785f7ddf3e5ddf7f5402ee81bf46fbc34e92923c6551eb768.jpg" width="25px"/> __尹少爷__: 我买了这本书，看了第一章感觉又清楚了很多～书不错，以前读tcp/ip1，感觉没有串起来，这次把我看的http详解的感觉也都串起来了，感谢一下

...

---


## 杂

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-09:


__#资源#__

这篇漏洞及修复经验很有意思，其中第3个，居然也能重视，如果国内认这个，可以刷一波了：


[Flexport今年在hackerone被报告的6个有趣的漏洞 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/vuls/139171.html)





...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 厂家居然认为第3点：这是最令我们感到惊讶的一个问题。

<img src="https://file.xiaomiquan.com/64/90/649032a29005a37e93906d26f68a0492d5247ecf4cbfea97aa6b0e74a7a6b1b0.jpg" width="25px"/> __一个头两个大大大大大大大大大大大__: 早在去年，freebuf上就出现了关于target_blank的钓鱼分析

[http://www.freebuf.com/vuls/113634.html](http://www.freebuf.com/vuls/113634.html)


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

