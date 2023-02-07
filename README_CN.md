# bin2rbt 转换工具

## 介绍

本工具是用于将二进制文件转换为RBT格式的文本文件的脚本。

## 背景

使用LPC11U35FHI33作为下载工具为ICE40UP5k上传数据时，只支持RBT格式的文件，但是使用apio等开源FPGA工具生成的文件是bin格式的，无法直接上传。通过与moo大佬分析RBT文件格式，最终完成了这个工具的开发。

## 运行环境

- Python3
- click
- datetime

## 用法

通过命令行运行脚本并使用以下参数：

```
cssCopy code
python bin2rbt.py --binfile <BIN文件> --rbtfile <RBT文件>
```

参数说明：

- --binfile: 原始二进制文件的文件名，默认为binfile.bin
- --rbtfile: 转换后的RBT文件的文件名，默认为rbtfile.txt

## 原作者

moo

## 参与修改者

John Huang
