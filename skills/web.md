# Web
子目录:
- [XSS](#xss)
- [SSRF](#ssrf)
- [后端](#后端)
- [Socket](#socket)

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


## 后端


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-21:


__#资源#__

  2017年，Web 后端出现了哪些新的思想和技术？推荐这篇回答：


[2017年，Web 后端出现了哪些新的思想和技术？ - 知乎](https://www.zhihu.com/question/61085805/answer/186718190)

 

一位我一直觉得功力深厚的工程师好友。他这种底子如果想搞安全，那简直不敢想象的黑。😄

大家看他的回答，不懂的词汇可以自己搜索，算是了解下在优秀工程师眼里，Web 后端的门门道道吧，对我们搞安全的人来说，知己知彼，你懂得。


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

