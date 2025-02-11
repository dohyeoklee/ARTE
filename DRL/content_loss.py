import torch
from torchvision import models
import numpy as np
import cv2

from torchvision import transforms

LAST_VGG_LAYER = 17

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Images must be normalized and made 224x224 pixels before entering into the vgg model
normalize = transforms.Compose([transforms.ToPILImage(),
                         transforms.Resize((224,224)),
                         transforms.ToTensor(),
                         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])])

def extract_features(X):
    ''' Run X through the truncated VGG-16 model '''
    X.to('cpu')
    x_norm = torch.zeros((X.shape[0], 3, 224, 224)).to(device)
    for i in range(len(X)):
        x_norm[i,:,:,:] = normalize(X[i,:,:,:].cpu())
    return vgg((x_norm))

def get_l2_mask(targets):
    ''' Get a 0-1 weighted matrix of features extracted using vgg-16 '''
    width = targets.shape[-1]
    masks = np.empty(targets.shape)
    target_feats = extract_features(targets)
    for i in range(len(targets)):
        mask = target_feats[i,:,:,:]
        mask = cv2.resize(np.transpose(mask.cpu().numpy(), (1,2,0)), (width, width))
        mask = np.sum(mask, axis=-1)
        mask = (mask - np.min(mask))
        mask = mask / np.max(mask)
        mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

        masks[i,:,:,:] = np.transpose(mask, (2, 0, 1))
    
    #masks = 1.0 - masks # Incase you wanted to invert the mask to test it
    return torch.tensor(masks).to(device)

vgg_model = models.vgg16(pretrained=True)
vgg = torch.nn.Sequential(*list(vgg_model.features.children())[:LAST_VGG_LAYER])
for param in vgg.parameters():
    param.requires_grad = False
vgg.to(device)
