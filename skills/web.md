# Web
子目录:
- [XSS](#xss)

## XSS

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-02:

> 匿名用户 提问：
你好，我看你在微博里面发的XSS,其中有一个 `<title><img src="</title><img src=x onerror=alert(1)//"\>` 其中的解释是title的解析高优先级造成的，能介绍下这方面的知识，或者指点要看的书籍吗？

没什么特别的书，虽然我们那本《Web前端黑客技术揭秘》也有相关介绍。

这方面的知识就是吃透浏览器 DOM，建议去读 Webkit 的源码，及浏览器 F12 去看看 DOM 的怪异解析。


---