![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)

# CLAMP-ViT
CLAMP-ViT: Contrastive Data-Free Learning for Adaptive Post-Training Quantization of ViTs

Our repository is adapted from FQ-ViT([link](https://github.com/megvii-research/FQ-ViT/tree/main)) and Evol-Q([link](https://github.com/enyac-group/evol-q)).

Please follow these instructions to setup the code and evaluate MPQ results for different ViT models.

## Getting Started

### Install

Follow these steps to clone the repository and set up your environment.

1. **Clone the repository**

```bash
git clone https://github.com/ARamachandran2000/CLAMP-ViT.git
cd CLAMP-ViT
```

2. **Requirements**

- Packages
  - python>=3.8
  - pytorch>=1.5
  - matplotlib
  - pandas
  - timm

3. **Data Preparation**

To evaluate the models, you will need the standard ImageNet dataset. Please download and organize it as follows:

```
imagenet/
├── train/
├── val/
```

4. **Evaluation**

To run experiments on different quantized model run the following:

```
python test_clamp_vit.py --model <MODEL-NAME> --weight-path ./quantized/<MODEL-NAME>.pth --data PATH-TO-IMAGENET_2012
```
5. **Results for Image Classification**

| Model | Top-1 Accuracy  |
|-----------|-----------|
|DeiT-T (W4.9/A6.2) | 71.69 |
| DeiT-S (W4.7/A5.9) | 79.43 |
| Swin-T (W5.5/A6.9) | 81.78 |
| Swin-S (W5.1/A6.3) | 82.86 |


## Disclaimer
This “research quality code” is for Non-Commercial purposes and provided by the contributors “As Is” without any express or implied warranty of any kind. The organizations (Intel or georgia Tech) involved do not own the rights to this data set and do not confer any rights to it. The organizations (Intel or Georgia Tech) do not warrant or assume responsibility for the accuracy or completeness of any information, text, graphics, links or other items within the code. A thorough security review has not been performed on this code. Additionally, this repository may contain components that are out of date or contain known security vulnerabilities.


