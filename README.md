# ARTE : ARTificial Expressions

Yejin Kim and Dohyek Lee
<br />Sponsored by ZER01NE<br />

### TASK LIST
- [ ] train actors and critics using CLIP based loss functions using a target image
- [ ] train actors and critics using CLIP based loss functions using a target text
- [ ] inference; stroke based rendering and painting using a real robot



### 1. Introduction
#### 1.1  ARTE Skecher: Reinforcement Learning
#### 1.2. ARTE SKetcher: Objectives
- l2
- clip_conv_loss
- clip_fc_loss
- text



### 2. Run in Simulation
#### 2.1. Installation
install clip and stable diffusion

```
    virtualenv venv -p python3.8
    pip install torch==1.13.1+cu117 scipy==1.5 einops pytorch_lightning
    pip install git+https://github.com/openai/CLIP.git
    mv CLIP CLIP_
```

#### 2.2 Train Brush Strokes Renderer
#### 2.3 Train ARTE Sketcher
```
    python train.py --loss_fcn clip 
```

To monitor the training progress,
```
    tensorboard --logdir train_log_deleteme/
```

Table of tried hyperparameters


| Dataset   | LR                                 | Loss  | Loss Weights                     | Seed  | BS | Max Step | Warmup | Replay |
|-----------|------------------------------------|-------|----------------------------------|-------|----|----------|--------|--------|
| MNIST     |(9e-4,3e-3),(3e-4,9e-4),(3e-7,1e-6) | clip2 |x10 reward,[0.3,0.3,1,1,1.0],[0.1]| 1321  | 8  | 10       | 200    | 400    |
| Sketchy   |(3e-4,9e-4),(3e-4,9e-4),(3e-7,1e-6) | clip2 |x16 reward,[0.3,0.3,1,1,1.0],[0.1]| 1321  | 8  | 10       | 200    | 400    |
| CelebA    |(9e-5,3e-4),(3e-6,1e-5),(3e-7,1e-6) | clip2 |x100reward,[0.3,0.3,1,1,1.0],[0.1]| 1321  | 32 | 40       | 1000   | 400    | 
| Pascal    |(3e-7,1e-6)                         | clip2 |x160reward,[0.3,0.3,1,1,1.0],[0.1]| 1321  | 32 | 40       | 1000   | 400    |




#### 2.4 Paint by Inferences




### 3. Run With Robot
#### 3.1 Installation
#### 3.2 Robot-Camera Calibration
#### 3.3 Collecting Brush Strokes Data
#### 3.4 Paint by Inferences



### References
1. Learning to Paint [https://github.com/megvii-research/ICCV2019-LearningToPaint]
2. *Content Masked Loss [https://github.com/pschaldenbrand/ContentMaskedLoss]
3. *CLIPPasso [https://github.com/yael-vinker/CLIPasso]
4. **FRIDA [https://github.com/cmubig/Frida/tree/master]<br />
**Heavily influenced Sim* <br />
***Heavily influenced the robot code*

### Acknowledgements
ZER01NE


