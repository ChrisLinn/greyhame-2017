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

