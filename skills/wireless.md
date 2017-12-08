# Wireless


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-09:

> 匿名用户 提问：
请问cos，用破解WIFI最高效的还是用彩虹表吗？另外如何防范彩虹表破解？


得看情况，如果是 WPA2 且无一键 WPS 这个缺陷情况下，是彩虹表。密码12位，再加几个特殊字符，很难很难破了。



---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-09-13:


__#漏洞#__

BlueBorne 蓝牙攻击


[http://go.armis.com/hubfs/BlueBorne%20Technical%20White%20Paper.pdf](http://go.armis.com/hubfs/BlueBorne%20Technical%20White%20Paper.pdf)



又是个有 Logo 的漏洞，细节如上，下面这个演示视频好屌：


[BlueBorne接管Android系统的演示](https://m.v.qq.com/play.html?vid=r054937flzf)



<img src="https://images.xiaomiquan.com/FgukHfLYbLlnnRDZxVNCYYblTYtj?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:I3WYOHabMgYTTirzkS3Hin0k3Rw=" width="50%" height="50%" align="middle"/>
<img src="https://images.xiaomiquan.com/FhnnCiK4PqdKcP7iWs0_4Qdra62r?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:o8DBpm-wMyR8tFubEk4wniqnFuY=" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-10-16:

拭目以待

[KRACK Attacks: Breaking WPA2](https://www.krackattacks.com/)





...

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 细节已放出

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__: 还有演示视频
[https://www.youtube.com/watch?v=Oh4WURZoR98](https://www.youtube.com/watch?v=Oh4WURZoR98)

...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-16:


__#漏洞#__

关于 WPA2 这个 KRACK 攻击


[https://www.krackattacks.com/](https://www.krackattacks.com/)



今天炒的火热，很多文章标题党也是正常现象，毕竟这是个专业话题...

由于白天都很忙，这里简单转几句我们后来的交流，供大家理解。

Longas杨叔：“花时间仔细看了视频和说明文档，这个 KRACK ATTACK 攻击应该是目前最取巧的针对 WPA/WPA2 的中间人攻击方法。并不针对 WPA 加密本身，而是通过多次重播四次握手的消息3来强制复位本地保存的 WPA 密钥，即把原来正确真实的 WPA 密码替换掉，不破解直接替换，这样就可以将受害者连到伪造的 AP 上，无需任何提示，再配合 SSLStrip 之类的工具做中间人就圆满地实现了基于 Wi-Fi 的无缝中间人攻击。”

余弦：“这个戏法最终是对 Client，视频演示很明显。这种攻击作者也偷懒了，没提这个 MITM（SSLStrip）没法对 Google 进行，大家知道为什么吗？原因是：HSTS。”

目前来看，这个漏洞实战意义还是不错的，要修复应该也不是什么难事。那些乱喊 WPA2 要死的文章，笑笑就罢了。

更多细节等后续再看值得补充就再补充吧。

<img src="https://file.xiaomiquan.com/05/07/05079510f9e4c0efbf78f55d9373d5d790d0be05d794132df47b309ba3476eb1.png" width="50%" height="50%" align="middle"/>
<img src="https://file.xiaomiquan.com/c4/d9/c4d9438fb65e0c25a109b77130c9021a79472a8bb4d494b375f37b612ef88465.png" width="50%" height="50%" align="middle"/>


---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-18:


__#姿势#__

WPA2 这个 KRACK 攻击，推荐看 Longas杨叔 这篇文章，清晰明了：


[WPA2被攻破？全球WiFi瘫痪？WiFi末日到来？能再夸张点不](http://mp.weixin.qq.com/s/nEfwjrE3AOORVC89TJHBtg)


---

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ on 2017-10-18:

WPA2密码重装攻击的POC，python脚本写的附带原理论文PDF，www.github.com/jiansiting/wpa2-krack

<img src="https://file.xiaomiquan.com/ee/87/ee87523c7470f1d20a91683c1f6b842296024c2335095132e43a6b01a64bf3b8.jpg" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 效果如何

<img src="https://file.xiaomiquan.com/c3/ff/c3ff7b7a3452ad4f7a0a6d1eb752f9b3a7e5bceeafff53d1372943527450dde0.jpg" width="25px"/> __唐古拉老山羊__: 像我这样英文渣，文献根本看不懂啊

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 源头在这:
[krack - Pastebin.com](https://pastebin.com/aZyyS16w)



<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 效果可以，就是严格按照pdf可以走下来，创建了一个同名AP获取数据包。

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/c3/ff/c3ff7b7a3452ad4f7a0a6d1eb752f9b3a7e5bceeafff53d1372943527450dde0.jpg" width="25px"/> __唐古拉老山羊__: 可以参考部分中文

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 我这个是一个github上的朋友发给我的研究和测试的，看开来你提供这个连接应该是最早的poc代码了

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 只是FT，貌似的支持802.11r 才可以

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 没错，你看得很仔细，程序的一开始就用文本说明了这个地方

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 
[GitHub - vanhoefm/krackattacks-test-ap-ft](https://github.com/vanhoefm/krackattacks-test-ap-ft)



<img src="https://file.xiaomiquan.com/7e/6e/7e6e47b51f5a9733c99849a1458f703fdb6abecf319d98a1500d009c1f02b46a.jpg" width="25px"/> __Sunset__: 所以，只能针对FT协议的WiFi？并不能wpa2吗？


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-10-19:

我还能说什么：斯诺登2010年泄漏NSA机密文档介绍的BADDECISION项目，疑似就是KRACK攻击，所以该漏洞被exploit至少7年了。


[07-Introduction-to-BADDECISION-Redacted](https://www.documentcloud.org/documents/3031639-07-Introduction-to-BADDECISION-Redacted.html)





...

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 想想协议也服役13年了

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 那这些老毛子到底还有多少不为人知的东西。😂😂

<img src="https://file.xiaomiquan.com/74/ab/74abebf3530d1f6750d72fe7669a6d76f77779d6c66552a6a545521b66fee4fc.jpg" width="25px"/> __I0ck_me__: 挖洞这种事早就该上升为国家战略了[悠闲]

<img src="https://file.xiaomiquan.com/3f/16/3f163367e182ea761220cbd7bda16b9ee6d325dbbb31156bc1175ebabafe7747.jpg" width="25px"/> __***__: 怪不得祖国要自己搞WAPI...不过也不了解其是否也有漏洞。。。😂

<img src="https://file.xiaomiquan.com/41/b3/41b36482e50df589c1aab96bf02cc26f84715aecfb4ab94cff73436a248938a7.jpg" width="25px"/> __剑思庭__: 原来如此，看上去很像呀

<img src="https://file.xiaomiquan.com/e1/00/e100c6649e7211ae83de05a72bebc940db70ce033ea11ee32bf5971ed6568bf8.jpg" width="25px"/> __眠熊__ replies to <img src="https://file.xiaomiquan.com/3f/16/3f163367e182ea761220cbd7bda16b9ee6d325dbbb31156bc1175ebabafe7747.jpg" width="25px"/> __***__: 国内搞WAPI跟这个没关系的

<img src="https://file.xiaomiquan.com/31/25/31254abb1de0594857f57786f9915393792db057f35056a77039e9d273cab5f5.jpeg" width="25px"/> __天天向上__: 这还是知道的已如此恐惧了，还有多少隐匿的


...

---

<img src="https://file.xiaomiquan.com/53/93/5393f85d981fdca80d89f411c1db56b464ad0512f3e49b0e88bfc2ce40916a62.jpg" width="25px"/> __RAY__ on 2017-10-31:

scapy加了个Krack AP module ：）


[Krack AP module by commial · Pull Request #928 · s...](https://github.com/secdev/scapy/pull/928)





---

