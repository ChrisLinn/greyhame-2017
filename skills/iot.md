# IoT/工控


<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-09:

> 剑思庭 提问：
如何看待工控安全这个行业？


没出事时，这个窄圈子自己热闹，出事了，都热闹了。

工控安全以前是不要出现场生产事故，现在是怕因为接入互联网或间接被感染导致工控网过于脆弱。这要出事确实是大事，会影响国计民生，所以重要度可以想象。

市场空间依赖工控的市场空间，安全的强需求会比其他的安全领域普遍来得高。但是，工控网有个特点，就是稳定运行优先，这导致如果没真出事，要去为了网络安全而去暂停运行，那不现实。还有，各种检测、防御方案也要求更高，第一要紧是别导致这些安全策略上了，影响工控网运转的稳定性。

所以，工控安全很迫切，但真想做好会更难。



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

