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
