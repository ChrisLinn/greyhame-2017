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
[HID攻击简易上手.pdf](fileulrxxxxxxxxxxxxxxxxxxxfileulr)

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


