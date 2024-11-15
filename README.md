### 改进增强的DeepLabV3Plus网络模型
改进的DeepLabV3+模型源代码及自建数据集Sublane

### 所需环境
torch==2.2.2  
CUDA==11.8  
Python==3.18  

### 注意事项
代码中的预训练文件deeplab_mobilenetv2.pth是基于VOC拓展数据集训练的
训练和预测时注意修改backbone   

### 文件下载

SubLane数据集可在迅雷中下载:  
链接: https://pan.xunlei.com/s/VOBiDBpldbtFoH7C3J3BtTrDA1

VOC拓展数据集的百度网盘如下：  
链接: https://pan.baidu.com/s/1vkk3lMheUm6IjTXznlg7Ng 

### 程序
#### 训练
1、收集自己的数据集，数据集全部标注  
（数据集为.jpg格式，标签为.json格式，都放在一个文件夹里即可）  
2、利用step1_seg_image_gen.py将数据集进行转换  
（原始.jpg图像存在了JPEGImages中，分割好的.png格式图像存在SegmentationClass中）  
3、将VOCdevkit/VOC2007中的JPEGImages和SegmentationClass替换成datasets中的datasets中的JPEGImages和SegmentationClass（复制替换即可）  
4、利用step2_reset_tra_and_val.py将数据集随机按一定比例以.txt方式分成训练集和训练验证集存在Segmentation的train.txt、trainval.txt和val.txt中  
（假设数据集1000，训练验证为8:2，则trainval=1000、train=800、val=200）    
5、在train.py文件夹下面，选择自己要使用的主干模型和下采样因子。  
本文提供的主干模型有mobilenet。下采样因子可以在8和16中选择。需要注意的是，预训练模型需要和主干模型相对应     
6、注意修改train.py的num_classes为分类个数+1     
7、运行train.py即可开始训练  

#### 预测
预测的步骤较为简单，详细参考程序注释

### Reference
https://github.com/ggyyzm/pytorch_segmentation  
https://github.com/bonlime/keras-deeplab-v3-plus
https://github.com/bubbliiiing/deeplabv3-plus-pytorch
