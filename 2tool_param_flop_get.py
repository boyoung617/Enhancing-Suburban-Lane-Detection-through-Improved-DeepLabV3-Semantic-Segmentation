import torch
import time
from thop import profile
from thop import clever_format
from nets.deeplabv3_plus import DeepLab

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('testing GPU'.center(100, '-'))
net1 = DeepLab(num_classes=2,pretrained=False,backbone='mobilenet').cuda()
net2 = DeepLab(num_classes=2,pretrained=False,backbone="xception").cuda()
input = torch.randn(1,3,640,360)
input = input.to(device)
start = time.time()
flops1,params1 = profile(net1,inputs=(input,))
flops2,params2 = profile(net2,inputs=(input,))
end = time.time()
flops1,params1 = clever_format([flops1,params1],"%.3f")
flops2,params2 = clever_format([flops2,params2],"%.3f")
#print('params',params1,'M','FLOPs',flops1,'G')
#print('params',params2,'M','FLOPs',flops2,'G')
print('---------------------------------------------------------------')
print('MobileNetV2-----Params:',params1,'       ','FLOPs:',flops1)
print('Xception-----Params:',params2,'       ','FLOPs:',flops2)
print('---------------------------------------------------------------')