# Defense


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-05:

> Sea0fStars 提问：
使用AppArmor或者SELinux加固系统，效果明显吗？然后，如何更好的加固Web服务器呢？


明显，其他可以参考安全技能树里防御那里的说明与资料。


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
余弦老师，请问您如何看待现在的入侵检测技术已经很成熟，也有很多检测web注入攻击的技术被提出，但web注入攻击的误报率、漏报率仍然很高的问题？


没感觉很成熟呀，在各种动态复杂场景下，所谓的“智能”、“自学习”、“下一代”都难以适应，别看宣传做得那么好，漏误报一直是很大的问题。但再深入思考下，其实这些防御或检测“智能”水平相当情况下，这种攻防平衡目的倒是达到了。

未来如果 AI 真能在这样的场景下发挥好，会是很大的机会，可是真的懂 AI 又懂安全的人有几个呢？🙂



---

<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> 匿名用户 提问：
有一些账号密码，或者一些关键的信息。以前一直都是用的txt或者word保存，学习过sql sever。用什么保存这类文件，是数据库还是用其他的工具呢？若是数据库选择什么数据库比较合适且以后学习安全也适合的。希望解答~


1Password



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:


__#姿势#__

  今天看到这篇文章《论如何反击用AWVS的黑客》：


[论如何反击用AWVS的黑客 - FreeBuf.COM | 关注黑客与极客](http://www.freebuf.com/news/136476.html)



思路是经典的，本质是 AWVS 内置的浏览器解析引擎会执行我们自定义好的 JavaScript。然后大家可以再看看 BeEF 里的路由器攻击插件集：

`beef/modules/exploits/router/`

这里有一堆路由器的 CSRF 利用插件。

如果你在自己的页面（比如自己的博客）挂上这些插件利用，哪天有人不小心访问你的页面，那么他们用的路由器就可能被 CSRF 利用，然后中招，比如有命令执行的，可以反弹出 MSF 利用。

去年我办的 TOBEAHACKER 培训，我分享了一个国产路由器 0day 利用，也是此道理。未来会考虑公布完整的挖掘与分析利用全过程。



...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 本圈特别补上 BeEF 里路由器攻击插件集合的链接：
[beef/modules/exploits/router at master · beefproje...](https://github.com/beefproject/beef/tree/master/modules/exploits/router)


...

---

