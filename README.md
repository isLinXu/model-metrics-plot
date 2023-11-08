# model-metrics-plot

![](./img/project_logo.png)

model-metrics-plot(mmplot)

[English](README.md) | [简体中文](README.zh-CN.md)

---
![GitHub watchers](https://img.shields.io/github/watchers/isLinXu/model-metrics-plot.svg?style=social) ![GitHub stars](https://img.shields.io/github/stars/isLinXu/model-metrics-plot.svg?style=social) ![GitHub forks](https://img.shields.io/github/forks/isLinXu/model-metrics-plot.svg?style=social) ![GitHub followers](https://img.shields.io/github/followers/isLinXu.svg?style=social)
 [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fatrox%2Fsync-dotenv%2Fbadge&style=flat)](https://github.com/isLinXu/model-metrics-plot)  ![img](https://badgen.net/badge/icon/learning?icon=deepscan&label)![GitHub repo size](https://img.shields.io/github/repo-size/isLinXu/model-metrics-plot.svg?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/isLinXu/model-metrics-plot)  ![GitHub last commit](https://img.shields.io/github/last-commit/isLinXu/model-metrics-plot) ![GitHub](https://img.shields.io/github/license/isLinXu/model-metrics-plot.svg?style=flat-square)![img](https://hits.dwyl.com/isLinXu/model-metrics-plot.svg)

## 😎 About

This project is developed based on libraries such as Pandas and Matplotlib, and can be used to draw line graphs of multiple index parameters such as algorithm accuracy and speed of multiple deep learning models.

---

## 🥰Result

### plot

| <img src="./img/plot_metrics.jpg" style="zoom:33%;" />       | ![](./img/paddle_plot_metrics.jpg)                           | <img src="./img/bar_chart_plot.jpg" style="zoom: 25%;" />    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [data/Pytorch_models_data.csv](https://github.com/isLinXu/model-metrics-plot/blob/main/data/Pytorch_models_data.csv) | [data/PaddleYOLO_models_data.csv](https://github.com/isLinXu/model-metrics-plot/blob/main/data/PaddleYOLO_model_data.csv) | [data/MMYOLO_model_data.csv](https://github.com/isLinXu/model-metrics-plot/blob/main/data/MMYOLO_model_data.csv) |

| <img src="./img/plot_mult_chart.jpg" style="zoom:20%;" />                                                | <img src="./img/plot_mult_code_chart.jpg" style="zoom:20%;" />                                           | <img src="./img/mllm_chart_acc1.png" alt="mllm_chart_acc1" style="zoom:33%;" /> |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------| ------------------------------------------------------------ |
| [data/llm_eval_data.csv](https://github.com/isLinXu/model-metrics-plot/blob/main/data/llm_eval_data.csv) | [data/llm_eval_data.csv](https://github.com/isLinXu/model-metrics-plot/blob/main/data/llm_code_eval.csv) | |

---

## 🔨Usage

### requirement

```shell
pip install matplotlib
pip install pandas
```

### mmplot install

```shell
git clone git@github.com:isLinXu/model-metrics-plot.git
cd model-metrics-plot
```

```shell
pip install -e .
```

### run

```shell
python3 main.py
```

or use your custom data csv

```shell
 python3 main.py -c 'csv_path' -n 'figture_name' -p 'plot_type' -t 'title_name' -x 'xlabel_name' -y 'ylabel_name' -f font_size -g False -v 'value_type' -r 'colors' 
```

#### line

> python3 main.py -c data/model_data.csv -n 'plot.jpg' -p 'line' -t 'MS COCO Object Detection' -x 'PyTorch FP16 RTX3080(ms/img)' -y 'COCO Mask AP val' -f 10 -v 'mAP' -r '#0000FF'
>

```shell
python3 main.py -c data/PaddleYOLO_extra_model_data.csv -n 'plot.jpg' -p 'line' -t 'MS COCO Object Detection' -x 'PyTorch FP16 RTX3080(ms/img)' -y 'COCO Mask AP val' -f 10 -v 'mAP' -r '#0000FF'
```

<img width="639" alt="image" src="https://github.com/isLinXu/issues/assets/59380685/be3d7dca-e2b4-4408-9de1-0e04bd946ca4">

#### bar

```shell
python3 main.py -c data/MMYOLO_model_data.csv -p bar
```

<img width="640" alt="image" src="https://github.com/isLinXu/issues/assets/59380685/e6aae12f-e969-4df0-adb4-2a1f3f899094">

#### leida


```shell
python3 main.py -c data/mllm_acc_eval-csv1029.csv -p leida
```

![image](https://github.com/isLinXu/issues/assets/59380685/7fa2d90d-55bc-4fa9-8e0c-899726e22425)