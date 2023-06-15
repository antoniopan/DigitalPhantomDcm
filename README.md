# DigitalPhantomDcm
A Tool to generate digital phantom test dicom files

目前已经完成的工作：

- 3D几何形状的接口定义及立方体、球体、椭球体、圆柱体的四个实现
- 离散化时超采样接口的定义，及均匀采样、随机采样的两种实现
- 根据给定的DICOM模板文件将空间采样生成的体数据保存为DICOM图像
- 目前只支持正方位的体数据及3D几何形状的定义
- 针对以上功能的xml schema定义及Python下的Data Binding实现

## 依赖库 ##

### pyxb ###
Python语言的xml data binding，用于配置文件的读取，每一次修改volume_phantom.xsd之后，需要从当前文件夹运行pyxbgen脚本更新相应模块。

### Geometry3D ###
3D几何库，完成3D空间下的变换

### lxml ###
用于xml schema校验

### numpy ###
用于数值计算

### pydicom ###
用于DICOM文件的读写