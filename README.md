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

## Result and Analysis
### Scenario
- We trained the model with relu and Adam until we find the highest possible validation accuracy.
- This combination model then further will be utilized with different combination of activation function and optimizer
- We utilizes these activation function : relu, swish and mish
- We utilizes these optimizer : SGD, RMSprop and adam
### Result
#### Result in Graph
- Note : The graph image title and y-axis is mistakenly rendered, the right title and y-axis is based on the table label.
- Below is the result of training click to dropdown.
<details markdown="1">
<summary>ReLU training graph result</summary>
</br>
<table style="width:100%">
  <tr> 
      <th> Loss SGD </th>
      <th> Accuracy SGD</th>
  </tr>
  <tr> 
      <td> <img src="https://user-images.githubusercontent.com/54882818/189628149-5a637d19-36c3-4225-9ce8-7fd3b49c2b2e.jpg"/> </td>
      <td> <img src="https://user-images.githubusercontent.com/54882818/189628162-826bffb9-37cb-4aff-8382-78bc79541ae3.jpg"/> </td>
  </tr>
  <tr> 
      <th> Loss RMSprop</th>
      <th> Accuracy RMSprop</th>
  </tr>
  <tr> 
      <td> <img src="https://user-images.githubusercontent.com/54882818/189627995-8d7902ba-de00-42e8-ab89-ef719e5fad10.jpg"/> </td>
      <td> <img src="https://user-images.githubusercontent.com/54882818/189628031-563df083-c24d-4e2a-8dbe-320af0ccff67.jpg"/> </td>
  </tr>
  <tr> 
      <th> Loss Adam</th>
      <th> Accuracy Adam</th>
  </tr>
  <tr> 
      <td> <img src="https://user-images.githubusercontent.com/54882818/189619093-74daec8a-294a-4d58-b6c9-e38e437fdd28.jpg"/> </td>
      <td> <img src="https://user-images.githubusercontent.com/54882818/189619122-55ffac46-c6f3-47b2-ada7-681ccd73500f.jpg"/> </td>
  </tr>
</table>
</details>

<details markdown="1">
<summary>SWISH training graph result</summary>
</br>
<table style="width:100%">
  <tr> 
    <th> Loss SGD </th>
    <th> Accuracy SGD</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629219-eb6d12ec-5d49-4371-988a-1f17c13121e6.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629234-7a93e31d-2693-477c-b9d1-53da5ca902d5.jpg"/> </td>
  </tr>
  <tr> 
    <th> Loss RMSprop</th>
    <th> Accuracy RMSprop</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629508-2f249a09-9c3c-4dc5-b9ad-a83acc3cfb30.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629522-3c7ee465-d7a5-4da2-9702-314bc8dab8a7.jpg"/> </td>
  </tr>
  <tr> 
    <th> Loss Adam</th>
    <th> Accuracy Adam</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629658-c801ea45-2efa-4df5-87e9-6d6754d2303a.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189629747-a24a3c66-017f-40e1-a34e-b67375b19c87.jpg"/> </td>
  </tr>
</table>
</details>

<details markdown="1">
<summary>MISH training graph result</summary>
</br>
<table style="width:100%">
  <tr> 
    <th> Loss SGD </th>
    <th> Accuracy SGD</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632597-42e6fbd5-85e3-4d58-b4c5-932035dadc22.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632608-94c68edd-53bf-4217-80e7-ec25ce2df4e4.jpg"/> </td>

  </tr>
  <tr> 
    <th> Loss RMSprop</th>
    <th> Accuracy RMSprop</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632710-947b33f7-1c2a-473a-9e97-983de45815b3.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632747-a4d32221-841d-451c-afc2-cce7069ef863.jpg"/> </td>
  </tr>

  <tr> 
    <th> Loss Adam</th>
    <th> Accuracy Adam</th>
  </tr>
  <tr> 
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632344-0a34a778-fefa-4c96-bddc-94a1114c6b8c.jpg"/> </td>
    <td> <img src="https://user-images.githubusercontent.com/54882818/189632357-1e58f28d-a9c1-496d-94fc-defeee0cdfc3.jpg"/> </td>
  </tr>
</table>
</details>

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

### Analysis

## Conclusion
