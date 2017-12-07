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
