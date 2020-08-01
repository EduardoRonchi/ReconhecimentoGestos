from keras.models import load_model
import cv2
import numpy as np
import sys
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import fnmatch
import os

CATEGORY_MAP = {
    0: "up",
    1: "down"
}

# Answer vector. It contains the correct results
actual = [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

# Predict vector. It contains the predicted results
predict = []

# This function returns the gesture name from its numeric equivalent 
def mapper(val):
    return CATEGORY_MAP[val]

#Load the saved model file
model = load_model("gesture-model05_20.h5", compile=False)

# Count the number of pictures
dir = 'C:/Users/Eduardo/LearnPython/Reconhecimento de Gestos/Untitled Folder/test_images/test_images/'
count_of_img = len(fnmatch.filter(os.listdir(dir), '*.jpg'))

#for i in range(41):
for i in range(count_of_img):
    #filepath = sys.argv[1]
    filepath = 'C:/Users/Eduardo/LearnPython/Reconhecimento de Gestos/Untitled Folder/test_images/test_images/{}.jpg'.format(i)

    # Ensuring the input image has same dimensions that is used during training. 
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (225, 225))

    # Predict the gesture from the input image
    prediction = model.predict(np.array([img]))

    gesture_numeric = np.argmax(prediction[0])
    gesture_name = mapper(gesture_numeric)
    predict.append(gesture_numeric)

    #print("Predicted Gesture: {}".format(gesture_name))

print("Done Testing!")    

# Plot the Classificasion Report
report = classification_report(actual, predict)
print("\n")
print("Test Report:")
print(report)

# Plot the confusion matrix
confusion_matrix(actual, predict)
data = confusion_matrix(actual, predict)
df_cm = pd.DataFrame(data, columns=np.unique(actual), index = np.unique(actual))
df_cm.index.name = 'Actual'
df_cm.columns.name = 'Predicted'
plt.figure(figsize = (5,3))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, cmap="Blues", annot=True,annot_kws={"size": 16})# font size
plt.show