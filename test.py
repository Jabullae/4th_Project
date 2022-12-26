import torch

# Model
model = torch.hub.load('C:/dev/MLDL/mini/yolov5/', 'custom', path='C:/dev/MLDL/mini/yolov5/runs/train/exp2/weights/best.pt', source='local') # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'C:/dev/MLDL/mini/upload/KakaoTalk_20221222_211411996.png'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.save()  # or .show(), .save(), .crop(), .pandas(), etc.