# Forensic


<img src="https://file.xiaomiquan.com/f2/18/f2187aaef0629494fb3ab1ab45faea17ed9021d9408eb286db2694c418ae7acf.jpg" width="25px"/> __ENI__ on 2017-06-08:

> Lion💬💬💬 提问：
做计算机终端安全检查时，怎么检查一台终端是否共享过热点？(PS:不是连接过的WIFI，是查是否有过共享热点事件）


好问题，这个估计玩取证的人更懂得，因为这些动作应该会在终端系统上留下痕迹。

我们没试过，但给你一个建议：比如 Windows 下，你用 Process Monitor 来监控下你自己的共享过程，看看是否会在注册表或什么位置留下信息。



...

<img src="https://file.xiaomiquan.com/7c/6a/7c6aab8c36f994d131ccd6b8365a3be2917ab22cf639a3e0ac140729b1cba2dd.jpg" width="25px"/> __M1k3__: 每个版本系统都设置热点，找个记录注册表更改的工具记录下就有特征了…可以依据特征写个检查脚本了


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-07-18:


__#姿势#__

使用橡皮鸭 U 盘偷取电脑里的文件


[Stealing Files with the USB Rubber Ducky – USB Exf...](https://hakshop.com/blogs/news/stealing-files-with-the-usb-rubber-ducky-usb-exfiltration-explained)



USB Rubber Ducky 这个 U 盘设备我玩了很久（不仅这个，我有全套），也叫橡皮鸭，来自 Hak5。攻击的本质原理就是 HID 攻击，U 盘会模拟成键盘，发出所有的触发指令都和键盘操作有关。

比如插入 U 盘，不需要任何其他手动操作，就可以植入木马。但是由于是模拟键盘操作，所以会发现打开了一些窗口（比如运行窗口、CMD 等），但是有办法能让这个过程做到尽可能隐蔽。

可以一键植入木马，当然也可以一键偷取目标电脑上的文件，上面分享的那个链接要达到的就是这个目的。

引导完毕，具体过程自己看吧。

顺便说一句，Hak5 的相关安全设备被美国禁止对中国销售，我有渠道可以买，但是没什么必要我懒得去做这个中间人。

再顺便说一句，黑手里的 HID 攻击也可以达到这类效果，我们玩安全得多脑洞、多扩展、多发散...😏

<img src="https://images.xiaomiquan.com/Fo6hCZWyBjpnyV4CAmyUPI0HS54n?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:Yn0sOlDk2uxqDL1J77jkWH-uiy8=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/FqflhBrfnOgsZ7O3EQh3PGMcbORG?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:uf2-OgIemafMszYssoSeZbM3MOg=" width="50%" height="50%" align="middle"/>

<img src="https://images.xiaomiquan.com/Fi0yA_3vqbpX3QPLPPpY1RxD_NU1?imageMogr2/auto-orient/thumbnail/800x/format/jpg/blur/1x0/quality/75&e=1843200000&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:ImTrBI7ZjXJTD7P07RbdAzQjRfA=" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 淘宝上有卖的

<img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: 可以在某宝购买MJMCU Digispark 微型arduino开发版自己diy一个hid设备。几块钱就可以了

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/b2/3c/b23c795737adee8dc13ad0c866f32f05b6b4bdd374a2cd62d6fa8eee0396f1a4.jpg" width="25px"/> __K3vi__: 可以呀

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 贵不少

<img src="https://file.xiaomiquan.com/d9/8d/d98d18950409c1a21557e81ea5b11addd5d8e0929702f32011454f6efb1c5892.jpg" width="25px"/> __GEASS__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 太贵了，888一个……

<img src="https://file.xiaomiquan.com/cf/7f/cf7f43f7239631b851f38b8930349bafd8287ac9930c0996b2316197f5245971.jpg" width="25px"/> __breadjun__: 链接看了，突然又向导余弦大大的这句话：（不仅这个，我有全套）

<img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 我也想买，从官网买399.9的套装卡在海关清单上，淘宝贵的有些离谱了

<img src="https://file.xiaomiquan.com/01/90/01903e0646f6df0fa017076ab2935b1104ade470b8eb8d28e3f2c3bb5b44e3d9.jpg" width="25px"/> __熟人不宜__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 这个应该是被US海关拦了吧？

<img src="https://file.xiaomiquan.com/e5/ed/e5ed19dec8b178c84d2b6dc707210d763fca1a37f8d64bf6776df8d5d2f9f6ae.jpg" width="25px"/> __Hi__ replies to <img src="https://file.xiaomiquan.com/67/6d/676dce5cc274939c3aff999a5a33001505c937dcf2325728952b4e67f9efb3e6.jpg" width="25px"/> __KevinShan__: 请问是海淘被海关扣下了吗？US扣的？

...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-08-07:

HID攻击是badusb攻击中成本最低，门槛最低的一类，通过模拟键盘向目标机器执行代码，本次分享以上手为主，带路三种从简易到实战的HID攻击姿势，每种都附有具体的how to链接。至于具体的payload大伙儿可以随自己喜欢，反正我是喜欢empire😂


__分享文件:__
[HID攻击简易上手.pdf](https://github.com/ChrisLinn/greyhame-2017/blob/master/shared-files/HID攻击简易上手.pdf)

---


<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-08-20:


__#姿势#__

利用 Safari 浏览器获取 macOS 敏感文件

分享来自@嘀嗒的钟  

成功利用这个bug需要满足两个条件，一是通过Safari浏览器访问本地文件，二是需要知道本地文件的绝对路径。

首先，第一个条件如何通过Safari浏览器访问本地文件，一般我们通过file://来访问本地文件，但是像Safari以及Chrome这些浏览器都对访问本地文件作了限制，大部分从Internet上下载的文件也是无法访问本地文件的。但是作者通过测试发现，Safari浏览器会对某些Internet上下载的文件放宽验证机制，从而导致可以访问本地文件（作者在文章中通过Mac桌面版的telegram传播恶意的xhtm可以突破safari浏览器的验证机制）

其次，如何获取本地文件的绝对路径，在macos系统的，如果用户有权访问某个文件夹并且访问过，通常会在该文件夹下生成一个隐藏文件 .DS_Store ，.DS_Store 的作用类似于windows系统下的Thumbs.db，但是所不同的是，.DS_Store 文件包含了文件夹以及该文件夹下所有文件的名称，我们通过解析 .DS_Store 就可以获取该文件夹下所有文件和文件夹的名称，这样就可以拼接出文件的绝对路径（理论上可以遍历系统上所有的文件）

因为很多敏感的文件都存在于当前用户文件夹下，例如.ssh文件下的登录凭证，各类浏览器的cookies，对于如何获取当前用户名称，文章提供了一种方法，通过获取系统日志（/var/log/system.log 和 /var/log/install.log）来查找当前用户的名称。

参考链接：

[https://lab.wallarm.com/hunting-the-files-34caa0c1496](https://lab.wallarm.com/hunting-the-files-34caa0c1496)


[如何通过简单的网页文件从macOS中盗取文件？ - 嘶吼 RoarTalk – 回归最本质的信息安全...](http://www.4hou.com/system/7012.html)


PoC: 
[GitHub - Bo0oM/Safiler: Safari local file reader](https://github.com/Bo0oM/Safiler)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 这个技巧针对 Mac 的攻击，很不错，有实战意义。

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: 不只是safari吧 同样是输入file://c:/ IE Edge 会直接弹出进入到c盘根目录的窗口 firefox直接会在页面上现实文件 之前leader让我尝试能否关掉这个 查询了很多资料 只是隐约提及了和内核里的文件搜索有关 具体的并没有说出来 然后就产生了一个这样的想法 能否在存在xss的地方插入一段js 让他直接访问受害者file:///c:/Windows/System32/cmd.exe (本地测试 可以打开)然后不在用户处回显 而且像beef一样 回显在攻击者的机子上

<img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: 我这边Chrome不会打开cmd，而是先下载，下载完提示“此文件可能会损害您的计算机”

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ replies to <img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__: Firefox 可行?我这测试好像不行

<img src="https://file.xiaomiquan.com/05/26/052606bee1b5e45844ab8e982107696c26c933506b311222774cbe70dda755c6.jpg" width="25px"/> __GeekaLeo__: 不错😘

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/aa/a5/aaa5edc50f15df8cf529bd4360fedbfada616c8ebc63bd72efe67ba9773f4b02.jpg" width="25px"/> __踏歌行千山__: 我刚重新试了一下 发现更新过后(不知道是浏览器更新还是系统更新 我这是win10)的确不行了 粗略查了查 可能是与'默认打开文件类型'的配置有关 我找个时间再仔细研究下 不过可以确定的是 有可能利用这个查看受害者电脑文件的方法吧

<img src="https://file.xiaomiquan.com/ff/f2/fff2d2a9cf8d31dde8b21cde5a1c3c387080fc4711e6039d58a4b571c9811449.jpg" width="25px"/> __别说话吻我头像__ replies to <img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__: 说的是直接打开cmd？ 我这里现在也不能复现了 不知道是更新系统 还是我调整了ie配置的问题 我再研究下吧(›´ω`‹ )


...

---

<img src="https://file.xiaomiquan.com/0a/bd/0abddfca718a9f30c1e29e53617f76be9cc86b9fe12b387e9899e75a3427aeec.jpg" width="25px"/> __豆@ATToT__ on 2017-09-13:

汉邦高科IP摄像头任意密码重置
__#漏洞#__

 
[SSD Advisory – Hanbanggaoke IP Camera Arbitrary Password Change – SecuriTeam Blogs](https://blogs.securiteam.com/index.php/archives/3420)


---

<img src="https://file.xiaomiquan.com/31/56/3156e285d9e9e4cc076ba99da0f33a9a0a1571a7ab9aba0050dbcbf5dae54503.jpg" width="25px"/> __嘀嗒的钟__ on 2017-09-14:


__#资讯#__

最近Talos公布了一个浏览器漏洞细节，讲的是利用绕过服务器设置的内容安全策略(CSP)，导致隐私信息泄露。

这个跟我之前分享的 “通过Safari浏览器获取MacOS系统的敏感信息”，都是利用内容安全策略这个安全机制。不过，这个这个漏洞覆盖的范围更广，Edge、Chrome、Safari都受影响。

相关链接:

[【技术分享】如何绕过Edge、Chrome和Safari的内容安全策略 - 安全客 - 有思想的安全新媒体](https://m.bobao.360.cn/learning/appdetail/4406.html)


...

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__: about:blank 是一个神奇魔法点


...

---

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ on 2017-10-24:


__#姿势#__

 BadUsb+Empire 让目标持久怀孕
胡乱写的，莫怪莫怪！[难过]
密码:alone

[http://hackerwing.com/2017/10/24/BadUsb-Empire-%E8%AE%A9%E7%9B%AE%E6%A0%87%E6%8C%81%E4%B9%85%E6%80%80%E5%AD%95/](http://hackerwing.com/2017/10/24/BadUsb-Empire-%E8%AE%A9%E7%9B%AE%E6%A0%87%E6%8C%81%E4%B9%85%E6%80%80%E5%AD%95/)





...

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 哈哈，手机上这个密码没用。只要把js禁用就行了。静态站点。QAQ

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: Badusb不管payload怎么改,调小调隐藏窗口，当插入别人电脑的时候终还是会有东西弹出来让别人察觉。然后taobao买了800多的橡皮鸭除了官方提供的payload比较全面之外也没有什么特别的地方，这些东西真的只能自己玩，然后以为做的隐藏比较完全，结果连客户鸟都不鸟这种东西。


<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 因为人家是甲方！滑稽。

<img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__ replies to <img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__: 不是 是某部门具体要实战用

<img src="https://file.xiaomiquan.com/8f/26/8f2660b040646e83a9094de27a4d4fd60e90a8488b576af28da8e08b90484ab4.jpg" width="25px"/> __Wing__ replies to <img src="https://file.xiaomiquan.com/1b/56/1b5688b7f998d36743d8be15316cbca7c8257f305fef2e7e01daa043d827db35.jpg" width="25px"/> __DarkEvil__: 学生狗不懂，😢😢😢


...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-10-31:

GoCrack是FireEye的ICE团队发布的一款工具，是基于Web的高效地管理多个GPU服务器上的密码破解任务，如创建，查看和管理。

[GitHub - fireeye/gocrack](https://github.com/fireeye/gocrack)





---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-04:

> sungrass 提问：
求问，忘了加密密钥，有办法逆向求出来么？已知DES加密，有大量明文和密文可以匹配。


非职业选手，看看圈里有谁可以搞定喽。



...

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: DES在密码学上已经属于高强度加密了，它的加强版就是大名鼎鼎的AES对称加密。除了穷举暴破之外，有几种数学的方式，但我只在paper看到过没试过。建议你google下 微分密码分析技术

<img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 但可能需要你的明密文对达到一定的数量。

<img src="https://file.xiaomiquan.com/39/24/3924e2a2664c8432b9924d965a04e82190b7db97c2bfcc1e2e36f47bb275d6b0.jpg" width="25px"/> __sungrass__ replies to <img src="https://file.xiaomiquan.com/58/e0/58e0e911c15f99cfb8994d9f484be21c5966b3c50e4241e5e2617599f157c67c.jpg" width="25px"/> __5u9ar__: 以前用kali试过破解wifi密码，感觉原理也是用密码字典暴力破解。能用相同的方法么？明文密文对数量没问题，估计能有三千个吧。


...

---

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-11-14:


__#姿势#__

 用一点对抗技巧来优雅地激活 Windows 10

上一篇分享的是 IDA Pro 7.0 在 Ubuntu 上的安装 hack 过程，这里给大家分享激活 Windows 10 的取巧过程。

我分享的这些更多是“渔”，请仔细吸收。

过程是这样的，我拿到个万能激活工具（MicroKMS 15.08.29.exe），不仅 Windows，Office 的也可以激活，但是对我来说谨慎很必要，万一这个小工具有个什么猫腻，那就不好了。

所以在激活之前，我安装了微软自家的 Sysmon 来做完整的日志记录，在管理员权限的 cmd 里安装如下：

```
sysmon -accepteula –i –h md5,sha256 –n
```

然后就可以在系统日志里找到 Sysmon 的所有记录。

这个小技巧是我们拿来做日志完备审计时用到的，当时的对抗出发点是恶意 PowerShell 的行为发现，用在这，其实一样:)

准备好后，双击 MicroKMS 15.08.29.exe 进行激活操作，很快就完成。然后我们就可以去 Sysmon 的日志里寻找痕迹了，发现两行命令：

```
cscript C:\Windows\System32\slmgr.vbs /skms kms-win.msdn123.com
cscript C:\Windows\System32\slmgr.vbs /ipk 7BNRX-D7ABG-3D4RQ-4WPJ4-YADFV
```

激活的本质就这两行，这两行什么意思自己试就知道了:)

提取出这两行后，准备干净的 Windows 10，直接在管理员权限下的 cmd 里执行就可以优雅地完成激活操作了。

这是个小技巧，在我们面对未知程序时多了份放心。



...

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 网上搜激活工具，一下出来好多乱七八糟的，肯定不放心，有时候直接拿 IDA 看一下，甚至 strings 一下也能发现好玩的

<img src="https://file.xiaomiquan.com/93/c0/93c0afcee1823a8215ad5307e444fe8d8eb054e940fd1f4a94b6d99df4d2b9c2.jpg" width="25px"/> __心态决定人生__: 从日志提取命令，学习了

...

---

<img src="https://file.xiaomiquan.com/fe/71/fe71de437c5674d403f6c4d6476c754511998d5ede4151feaaec7c7c2fa6001d.jpg" width="25px"/> __Sanr__ on 2017-12-07:


__#tools#__

 LogViewer:用于查看和搜索大型文本文件

[GitHub - woanware/LogViewer: LogViewer for viewing...](https://github.com/woanware/LogViewer)


glogg:快速浏览，搜索日志(优点：1.可以读取正在写入的日志 2. 支持Mac os、Linux、window)，正常情况下，如果日志正处于时时写入状态，会提示日志文件已被占用。

[GitHub - nickbnf/glogg: A fast, advanced log explo...](https://github.com/nickbnf/glogg)




<img src="https://file.xiaomiquan.com/160/50/6050c9b2e9289fb151b5836b1944acb17581e577fc57b8cd8137533e970e62a6.png" width="50%" height="50%" align="middle"/>

<img src="https://file.xiaomiquan.com/1a5/b9/a5b9376faf81e8d026d06c3efe32e8ff85f7372c72aa8267a2884b76581b64fe.png" width="50%" height="50%" align="middle"/>


...

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 大文件一般也只会用ue，涨姿势了

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 试了LogViewer，个人还是喜欢ue、notepad++这种，打开大文件也没多大问题，搜索支持结果汇总列表的，体验更方便些。[呲牙]

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 不知道大佬说的“大文件”一般是多大？平时我都用 Gvim for Windows 发现也够用[尴尬]

<img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__ replies to <img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__: 小弟使用一般也就是几十近百兆居多。顶多小几百兆而已。没到那么“大”其实。😂

<img src="https://file.xiaomiquan.com/d7/70/d770925d03a48166661a8101018a4f33a3ee1cf3922d704d4330cbdc5b28b58a.jpg" width="25px"/> __jiayu__ replies to <img src="https://file.xiaomiquan.com/8d/f6/8df6a4c90a9ec9e3b7d237bdd5b1798141a4dd962c04c0534de4fbe048cd1bc4.jpg" width="25px"/> __Y叔也叫段子手__: 不算小了[呲牙]

<img src="https://file.xiaomiquan.com/db/46/db463944dcee6d691b616604fe9fd3f08d518d7ae3ffd289fb5cd79f682e7b7b.jpg" width="25px"/> __sharecast__: 一般还是用Linux文本处理命令居多，一般的日志都是几十G，过滤出来用这个看还是比较方便的，感谢分享！


...

---


