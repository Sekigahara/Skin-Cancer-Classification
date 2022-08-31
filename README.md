# Skin Cancer Classification CNN based
This repository is based on my competition group repository [here](https://github.com/Sekigahara/skin-cancer-classification-skinconnect).

## Abstract
This repositories is associated to Bangkit academy group project. The main concern of our project is to create an telemedics application that helps people which suffer from skin cancers. Our application also considering False Negative diagnose by contacting the doctors for a second validation whether the taken photo had potential of being skin cancers.

## Dataset
1. The Dataset is taken and downloaded from Kaggle.
2. [Skin Cancer classesisic](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)
3. [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)

## Development and Installation
### Scenario
- The scenarios are splitted into two scenario, the first scenario is trained with 7 labels based on HAM10000 classes. The last scenario is utilized all of the classes into 3 classes(benigh, semi and malign)
- The semi class is a skin cancer in the verge of either benigh or could turn into malign(potentially malign).
#### 7 Classes scenario
- With merge script, we could merge HAM10000 and utilize a few classes from ISIC into one dataset.
- Based on HAM10000, we merge these classes ```actinic keratosis(akiec), basal cell carcinoma(bcc), Pigmented benign keratosis(bkl), dermatofibroma(df), melanoma(mel), melanocytic nevus(nv)m vascular lesion(vasc)```
#### 3 Classes scenario
- In this cases we merge this manually with details below.
- The malign class utilizing basal cell carcinomas, squamous cell carcinomas and melanoma
- The semi class utilizing actinic keratosis, basal cell carcinoma, vascular lesion
- The benign class utilizing melanoma, squamous cell carcinoma
### Installation
- The project runs on Python 3.8 and developed with Jupyter notebook(.ipynb) extension.
- In order to run this project install this requirements
```
pip install -r requirements.txt
```
- Most of the scripts are .ipynb, make sure to install jupyter notebook or using visual studio code notebook extension.
### 


[Agile Daily Report](https://github.com/users/SophrosyneEunoia/projects/3)
