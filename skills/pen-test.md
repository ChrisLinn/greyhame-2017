# Penetration Testing
子目录:
- [webshell扫描](#webshell扫描)
- [域渗透](#域渗透)
- [Exchange](#exchange)

## webshell扫描

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
使用字典远程扫描webshell，脚本发现疑似webshell后如何更好的进一步自动化甄别与判断。（假设密码已知，webshell包括大小马和一句话）


以前我们做过这个研究，这种远程扫描来准确识别并不容易，对于已知 Webshell，我们可以加精准特征（比如：HTML 里的内容、代码执行的返回内容、特别的文件名等），想通过什么好算法来处理，其实很难。


---

## 域渗透

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-06-06:

> 匿名用户 提问：
想学习有关域渗透的一些资料，windows域 08/12/WIN10安全检测及bypass，挺说还有linux域，感觉在这方面很欠补，毕竟环境接触的少，网上说的都模棱两可，大多不可行，弄的晕头转向，想权威体质的学习一下


安全技能树里推荐了不少，如果你真想感受，首先得“坏”。



---

## Exchange

<img src="https://file.xiaomiquan.com/96/86/9686aeac0faa9aa0efc8cc53e1617273dd5e53e7a0425b9f06b68f806f03ca15.jpg" width="25px"/> __余弦@ATToT__ on 2017-05-26:

> 匿名用户 提问：
内网中域控权限 Exchange服务器可控 如何在命令行获取所有邮箱列表及单个邮箱邮件打包 或按时间段打包


好吧，还是公开回复吧，你可以参考这个项目：


[GitHub - sensepost/ruler: A tool to abuse Exchange services](https://github.com/sensepost/ruler)



"Ruler is a tool that allows you to interact with Exchange servers remotely, through either the MAPI/HTTP or RPC/HTTP protocol. The main aim is abuse the client-side Outlook features and gain a shell remotely."

通过 MAPI/HTTP 与 RPC/HTTP 协议。



...

<img src="https://file.xiaomiquan.com/89/da/89dac2fbbada82afb3c1152dd4f88d703c91d5f5cbd238debe3f749b98c36f68.jpg" width="25px"/> __Twi1ight__: 用powershell在exchange服务器上也可以直接导出pst文件，支持按时间段导出，这是官方自带的


...

---
