# ProtectionEvaluX

## 框架梳理

### 前端页面梳理

#### 漏洞规则

![image-20240426161239263](./ProtectionEvaluX.assets/image-20240426161239263.png) 

支持根据启用状态和影响类型筛选  支持模糊查询

POC详情

![image-20240426161327465](./ProtectionEvaluX.assets/image-20240426161327465.png) 

![image-20240426161601716](./ProtectionEvaluX.assets/image-20240426161601716.png) 

规则设置处支持设置变量并在后续的参数中使用

![image-20240426162047757](./ProtectionEvaluX.assets/image-20240426162047757.png) 

注意防止代码注入



单条规则靶机测试

![image-20240426163758539](./ProtectionEvaluX.assets/image-20240426163758539.png) 

支持导入Xray的yml规则

![image-20240426164254500](./ProtectionEvaluX.assets/image-20240426164254500.png) 



> 表达式语法

```clike
response.status == 200 && response.body.bcontains(b"extensions") && response.body.bcontains(b"for 16-bit app support")
```

这里需要注意代码注入





#### 漏洞描述

![image-20240426162436993](./ProtectionEvaluX.assets/image-20240426162436993.png) 

#### 任务列表

![image-20240426162454570](./ProtectionEvaluX.assets/image-20240426162454570.png)

#### 扫描结果

![image-20240426162510844](./ProtectionEvaluX.assets/image-20240426162510844.png) 

#### 影响组件

![image-20240426162518579](./ProtectionEvaluX.assets/image-20240426162518579.png) 

这里影响组件和漏洞描述没有和漏洞规则联系起来 无法做到信息同步

### 后端逻辑梳理



## 功能修改

#### 增加功能 将规则转换成raw格式或hex格式的http请求

方便修改raw或hex格式的数据  从而在字节流进行修改实现攻击绕过

添加按钮支持将验证POC转换成

![image-20240426182002695](./ProtectionEvaluX.assets/image-20240426182002695.png) 

或者Hex格式

![image-20240426182019484](./ProtectionEvaluX.assets/image-20240426182019484.png) 

#### 增加对其他请求类型(tcp)的支持

某些漏洞POC是直接使用tcp协议发包或其他协议发包 而不仅仅是HTTP报文

#### 增加对多请求的漏洞复现的支持

有些漏洞的利用需要多步骤

即需要发送多个包

#### 漏洞描述和影响组件对接漏洞规则

![image-20240426160045228](./ProtectionEvaluX.assets/image-20240426160045228.png) 



![image-20240426160107451](./ProtectionEvaluX.assets/image-20240426160107451.png) 

漏洞描述详情里没有验证POC的链接，建议增加一个选项可以链接到复现报文处



## 功能新增

#### 新增实验室漏洞复现情况

需要管理员权限可以查看和编辑(此功能建议增加鉴权后添加)

为了对接实验室的改进建议表格，建议增加如下描述：

【分类】：检测能力提升、分析取证增强、配置易用性、安全框架支撑、基础能力增强

【方案分类】：编码绕过、缺少规则、打破规则匹配、冗余检测点、检测点不全、协议解析改进、大小写绕过规则检测、脏数据绕过、误报、易用性增强、功能缺失

【问题和痛点】

【需求/改进建议】

【参考文档】

【实施产品】

【需求提出人】

【需求review状态】

【处理责任人】

【接受状态】

【说明】

【备注】

![企业微信截图_17141188815892](./ProtectionEvaluX.assets/企业微信截图_17141188815892.png)

#### 新增端口探测



#### 新增弱口令爆破

支持多种应用的弱口令爆破

如：mysql、rdp、ssh、ftp等

#### 新增Web页面密码爆破(模仿客户端登陆操作)

实现对登陆页面截图，以及对纯js、js架构前端登陆页面进行检测

有些密码是在前端使用js加密的，这种情况下爆破需要前端js事先进行加密，传统的发包工具无法实现，需要内嵌浏览器的支持

#### 新增路径Fuzz

路径探测和相关应用的路径Fuzz

如：探测wordpress相关路径可以检测/wp/xx

#### 新增Web指纹探测

根据页面的返回信息判断web服务

如：响应中有weblogic相关信息则可以确定前端是weblogic

#### 新增域名探测和子域名爆破

根据输入的ip或域名探测可能存在的所有域名

#### 对接钟馗之眼

支持全网漏洞探测

#### 联动Sqlmap

对目标进行sql注入点检测