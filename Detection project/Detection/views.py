import requests
from django.shortcuts import render

# Create your views here.

import pytesseract
from pytesseract import Output
import re
import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread

from Detection.models import DataBase

len(os.listdir('/home/user/Desktop/CV_project/project/Helmet data'))

catpath = os.path.join('/home/user/Desktop/CV_project/project/Helmet data', 'Helmet')
for img in os.listdir(catpath):
    print(img)

flat_data_arr = []
target_arr = []
Categories = ['Helmet', 'No helm']

datadir = '/home/user/Desktop/CV_project/project/Helmet data'
for i in Categories:
    # print("loading.......",i)
    path = os.path.join(datadir, i)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path, img))
        img_resized = resize(img_array, (150, 150, 3))
        flat_data_arr.append(img_resized.flatten())
        target_arr.append(Categories.index(i))
    # print("loaded",i)

df = pd.DataFrame(flat_data_arr)
df['target'] = target_arr

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.svm import SVC

model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


def getPath(request):
    global final
    loc = request.GET['loc']
    getPath.final = loc
    return final


# helm and num = '/home/user/Desktop/CV_project/project/test/Helm&Number.png'
# Helm = '/home/user/Desktop/CV_project/project/test/Helmet only.png'
# zero = '/home/user/Desktop/CV_project/project/test/Nothing.png
# Num = '/home/user/Desktop/CV_project/project/test/Number only.png

path = '/home/user/Desktop/CV_project/project/test/Helmet only.png'

text = pytesseract.image_to_string(path)
data = pytesseract.image_to_data(path, output_type=Output.DICT)
n_boxes = len(data['text'])
data_pattern = '(KL\d{2}[a-zA-Z]{2}\d{4})'
for i in range(n_boxes):
    if data['conf'][i] > 60:
        if re.match(data_pattern, data['text'][i]):
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

    Vehicle_number = re.findall(data_pattern, data['text'][i])


def home(request):
    global text
    img_array = imread(path)
    img_resize = resize(img_array, (150, 150, 3)).flatten().reshape(1, -1)
    y_pred = model.predict(img_resize)

    if y_pred != 0:
        text = "This person wear helmet"
    else:
        text = "This person is not wearing helmet"

    content = {
        't1': text,
        'number': Vehicle_number,
        'pic': path
    }
    return render(request, 'home.html', content)

# def saveToDb(request):
#     if request.method == "POST":
#         Image = request.POST['Image']
#         Number = request.POST['Number']
#         Status = request.POST['Status']
#         datas = DataBase(Image = Image , Number = Number , Status=Status)
#         datas = DataBase.save()
#     return render(request,'home.html')
