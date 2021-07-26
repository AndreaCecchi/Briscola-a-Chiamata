import cv2
import matplotlib.pyplot as plt
import numpy as np

# Source data

# reads image 'opencv-logo.png' as grayscale
img = cv2.imread('/briscola3/fotocarte/annotazioni/Mixcarte.png', 0) 
plt.imshow(img, cmap='gray')
cv2.imshow('my detection',img_file)
# create an openCV image
img = cv2.imread(img_file)
imgplot = plt.imshow(img)
cv2.imshow('my detection',img)
plt.show()
# pre trained Card classifiers
ori1_classifier = '1ori.xml'
ori2_classifier = '2ori.xml'
ori3_classifier = '3ori.xml'
ori4_classifier = '4ori.xml'
ori5_classifier = '5ori.xml'
ori6_classifier = '6ori.xml'
ori7_classifier = '7ori.xml'
ori8_classifier = '8ori.xml'
ori9_classifier = '9ori.xml',
ori10_classifier = '10ori.xml'
coppe1_classifier = '1coppe.xml'
coppe2_classifier = '2coppe.xml'
coppe3_classifier = '3coppe.xml'
coppe4_classifier = '4coppe.xml'
coppe5_classifier = '5coppe.xml'
coppe6_classifier = '6coppe.xml'
coppe7_classifier = '7coppe.xml'
coppe8_classifier = '8coppe.xml'
coppe9_classifier = '9coppe.xml'
coppe10_classifier = '10coppe.xml'
spade1_classifier = '1spade.xml'
spade2_classifier = '2spade.xml'
spade3_classifier = '3spade.xml'
spade4_classifier = '4spade.xml'
spade5_classifier = '5spade.xml'
spade6_classifier = '6spade.xml'
spade7_classifier = '7spade.xml'
spade8_classifier = '8spade.xml'
spade9_classifier = '9spade.xml'
spade10_classifier = '10spade.xml'
bastoni1_classifier = '1bastoni.xml'
bastoni2_classifier = '2bastoni.xml'
bastoni3_classifier = '3bastoni.xml'
bastoni4_classifier = '4bastoni.xml'
bastoni5_classifier = '5bastoni.xml'
bastoni6_classifier = '6bastoni.xml'
bastoni7_classifier = '7bastoni.xml'
bastoni8_classifier = '8bastoni.xml'
bastoni9_classifier = '9bastoni.xml'
bastoni1_classifier = '10bastoni.xml'

# convert color image to grey image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create trackers using classifiers using OpenCV

spade9_tracker = cv2.CascadeClassifier(spade9_classifier)

# detect cars
spade9 = spade9_tracker.detectMultiScale(gray_img)


# display the coordinates of different cars - multi dimensional array
print(spade9)


# draw rectangle around the cars
for (x,y,w,h) in spade9:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


# Finally display the image with the markings
cv2.imshow('my detection',img)

# wait for the keystroke to exit
cv2.waitKey()


print("I'm done")