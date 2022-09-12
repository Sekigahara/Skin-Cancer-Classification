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
- Order to run this scenario respectively : ```Run merge_main_dataset -> Run preprocess_main_dataset -> training_main_dataset```
#### 3 Classes scenario
- In this cases we merge this manually with details below.
- The malign class utilizing ```basal cell carcinomas, squamous cell carcinomas and melanoma```
- The semi class utilizing ```actinic keratosis, basal cell carcinoma, vascular lesion```
- The benign class utilizing ```melanoma, squamous cell carcinoma```
- Order to run this scenario respectively : ```Create and copy every file based on the above format -> Run preprocess_three_dataset -> training_three_dataset```
### Installation
- The project runs on Python 3.8 and developed with Jupyter notebook(.ipynb) extension.
- In order to run this project install this requirements
```
pip install -r requirements.txt
```
- Most of the scripts are .ipynb, make sure to install jupyter notebook or using visual studio code notebook extension to edit and read the scripts.
- The requirements that has been installed include the Flask for API.
### Endpoint
- The endpoint can be accessed with http://ip:port/api/v1/classify
- The request can be done by sending the image file directly
- The response is tested with Postman and can be seen below <br> ![image](https://user-images.githubusercontent.com/54882818/187690697-b9c695dc-7767-4944-9ced-45006467e432.png)

## Analysis
### Scenario
- We trained the model with relu and Adam until we find the highest possible validation accuracy.
- This combination model then further will be utilized with different combination of activation function and optimizer
- We utilizes these activation function : relu, swish and mish
- We utilizes these optimizer : SGD, RMSprop and adam
### Result
#### Result in Graph
- relu
<table style="width:100%">
  <tr> 
    <th> Loss SGD </th>
    <th> Accuracy SGD</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189619093-74daec8a-294a-4d58-b6c9-e38e437fdd28.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189619122-55ffac46-c6f3-47b2-ada7-681ccd73500f.jpg"/> </td>
  </tr>
  <tr> 
    <th> Loss RMSprop</th>
    <th> Accuracy RMSprop</th>
  </tr>
  <tr> 
    <td> <img src=""/> </td>
    <td> <img src=""/> </td>
  </tr>
  <tr> 
    <th> Loss Adam</th>
    <th> Accuracy Adam</th>
  </tr>
  <tr> 
    <td> <img src=""/> </td>
    <td> <img src=""/> </td>
  </tr>
</table>

#### Result Table
- Result in Accuracy
<table>
  <tr>
    <td> </td>
    <td colspan="3"> <b> Activation Functions </b> </td>
  </tr>
  <tr> 
    <td> <b> Optimizers </b> </td>
    <td> relu </td>
    <td> swish </td>
    <td> mish </td>
  </tr>
  <tr>
    <td> SGD </td>
    <td> 60.17% </td>
    <td> 36.34% </td>
    <td> 50.13% </td>
  </tr>
  <tr>
    <td> RMSprop </td>
    <td> 95.13% </td>
    <td> 99.50% </td>
    <td> 98.69% </td>
  </tr>
  <tr>
    <td> Adam </td>
    <td> 96.69% </td>
    <td> 98.42% </td>
    <td> 98.24% </td>
  </tr>
</table>

- Result in Validation Accuracy
<table>
  <tr>
    <td> </td>
    <td colspan="3"> <b> Activation Functions </b> </td>
  </tr>
  <tr> 
    <td> <b> Optimizers </b> </td>
    <td> relu </td>
    <td> swish </td>
    <td> mish </td>
  </tr>
  <tr>
    <td> SGD </td>
    <td> 51.95% </td>
    <td> 20.71% </td>
    <td> 49.12% </td>
  </tr>
  <tr>
    <td> RMSprop </td>
    <td> 70.68% </td>
    <td> 70.03% </td>
    <td> 71.75% </td>
  </tr>
  <tr>
    <td> Adam </td>
    <td> 71.22% </td>
    <td> 71.10% </td>
    <td> 71.75% </td>
  </tr>
</table>
