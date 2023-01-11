# model-metrics-plot

![](./img/project_logo.png)

model-metrics-plot(mmp)

[English](README.md) | [简体中文](README.zh-CN.md)

---
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fatrox%2Fsync-dotenv%2Fbadge&style=flat)](https://github.com/isLinXu/model-metrics-plot)  ![img](https://badgen.net/badge/icon/learning?icon=deepscan&label)
![](https://badgen.net/github/stars/isLinXu/model-metrics-plot)![](https://badgen.net/github/forks/isLinXu/model-metrics-plot)![](https://badgen.net/github/prs/isLinXu/model-metrics-plot)![](https://badgen.net/github/releases/isLinXu/model-metrics-plot)![](https://badgen.net/github/license/isLinXu/model-metrics-plot)![img](https://hits.dwyl.com/isLinXu/model-metrics-plot.svg)



## 😎 介绍

本项目基于Pandas、Matplotlib等库开发，可用于绘制多个深度学习模型的算法精度、速度等多个指标参数的折线图。

---

## 🥰结果

### data review

![](./img/data_csv.png)

### 绘制结果

![](./img/plot_metrics.jpg)



---

## 🔨用法

### 依赖安装

```shell
pip install matplotlib
pip install pandas
```

### 运行

```shell
git clone git@github.com:isLinXu/model-metrics-plot.git
cd model-metrics-plot
```

```shell
python3 main.py
```

或者，你可以使用自定义数据。

```shell
 python3 main.py -c 'csv_path' -n 'figture_name'
```

```shell
 python3 main.py -c data/model_data.csv -n 'plot.jpg'
```