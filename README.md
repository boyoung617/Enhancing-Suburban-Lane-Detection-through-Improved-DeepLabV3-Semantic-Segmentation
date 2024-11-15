### 改进增强的DeepLabV3Plus网络模型
改进的DeepLabV3+模型源代码及自建数据集Sublane

### 所需环境
Torch==2.2.2  
CUDA==11.8  
Python==3.18   

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
3、将VOCdevkit/VOC2007中的JPEGImages和SegmentationClass  
替换成datasets中的datasets中的JPEGImages和SegmentationClass（复制替换即可）  
4、利用step2_reset_tra_and_val.py将数据集随机按一定比例以.txt方式  
分成训练集和训练验证集存在Segmentation的train.txt、trainval.txt和val.txt中  
（假设数据集1000，训练验证为8:2，则trainval=1000、train=800、val=200）    
5、在train.py文件夹下面，选择自己要使用的主干模型和下采样因子。  
本文提供的主干模型有mobilenet。下采样因子可以在8和16中选择。  
需要注意的是，预训练模型需要和主干模型相对应     
6、注意修改train.py的num_classes为分类个数+1，运行train.py即可开始训练  

#### 预测
预测的步骤较为简单，详细参考程序注释
##### 1tool_miou_mpa_get.py  
进行指标评估需要注意以下几点：
1、该文件生成的图为灰度图，因为值比较小，按照PNG形式的图看是没有显示效果的，所以看到近似全黑的图是正常的。  
2、该文件计算的是验证集的miou，当前该库将测试集当作验证集使用，不单独划分测试集  
##### 3tool_Image_video_test.py  
单张图片预测，如果想对预测过程进行修改，如保存图片，截取对象等，可以先看详细的注释  
视频检测，可调用摄像头或者视频进行检测，详情查看注释。  
测试fps，使用的图片是img里面的xxx.jpg，详情查看注释。  
#### 注意事项  
1.训练前仔细检查自己的格式是否满足要求，该库要求数据集格式为VOC格式，  
需要准备好的内容有输入图片和标签输入图片为.jpg图片，无需固定大小，传入训练前会自动进行resize。  
2.如果格式有误，参考：https://github.com/bubbliiiing/segmentation-format-fix  
3.训练好的权值文件保存在logs文件夹中，每个训练世代（Epoch）包含若干训练步长（Step），每个训练步长（Step）进行一次梯度下降。  
4.训练分为两个阶段，分别是冻结阶段和解冻阶段。设置冻结阶段是为了满足机器性能不足的训练需求。

### Reference
https://github.com/ggyyzm/pytorch_segmentation  
https://github.com/bonlime/keras-deeplab-v3-plus  
https://github.com/bubbliiiing/deeplabv3-plus-pytorch
