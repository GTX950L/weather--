# 🌤️ 天气查询小工具

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Level](https://img.shields.io/badge/练习-初学者-blue?style=flat-square)

</div>

一个用 Python 写的实时天气查询工具，输入城市名即可查看天气，无需注册或 API Key。

## 🚀 运行方式

```bash
python weather.py
```

## 📖 使用说明

```
     🌤️  天气查询小工具
     输入城市名查天气
     输入 quit 退出

常用城市：北京 | 上海 | 广州 | 深圳 | 杭州 | 成都 | 武汉 | 南京

请输入城市名：深圳

╔══════════════════════════════╗
║  🌤️  深圳 实时天气
╠══════════════════════════════╣
║  天气：晴
║  温度：28°C（体感 30°C）
║  湿度：65%
║  风速：12 km/h（东南）
║  能见度：10 km
║  紫外线指数：5
╚══════════════════════════════╝
```

## 🛠️ 用到的知识点

- 网络请求（urllib）
- JSON 数据解析
- 异常处理
- 字符串格式化
- 用户交互循环

## 🔌 接口说明

使用 [wttr.in](https://wttr.in) 提供的免费天气 API，无需注册、无需 API Key，查询次数无限制。

支持中英文城市名，也支持拼音（如 `shenzhen`）。

## 📝 后续可以增强的功能

- [ ] 查询未来几天的天气预报
- [ ] 保存查询历史
- [ ] 多城市对比
- [ ] 图形界面版本

---

*出门前看一眼，再也不用纠结穿什么。*
