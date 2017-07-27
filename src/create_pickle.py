import cPickle
import numpy as np
import Image

f = file('../data/smile_detection/train/image_names', 'r')

trainImage = []
trainResult=[]
for line in f:
    line=line.strip()
    line = "../data/smile_detection/train/" + line
    trainImage.append(line)
    if "b" not in line:
        trainResult.append(0)
    else:
        trainResult.append(1)
trainImageNumpy = [np.array(Image.open(fname))/255.0 for fname in trainImage]
trainFinal = []
trainFinal.append(trainImageNumpy)
trainFinal.append(trainResult)
f.close()
# # f = file('../data/smile_detection/train/train.pkl', 'wb')
# # cPickle.dump(train_data, f, protocol=cPickle.HIGHEST_PROTOCOL)
# # f.close()
#
# f = file('../data/smile_detection/test/image_names', 'r')
#
# test_data = []
# for line in f:
#     line =line.strip()
#     line = "../data/smile_detection/test/"+line
#     image = open(line,'r')
#     numpyImage = array(image)
#     if "a" in line:
#         test_data.append((numpyImage,0))
#     else:
#         test_data.append((numpyImage, 1))
# f.close
# # f = file('../data/smile_detection/test/test.pkl', 'wb')
# # cPickle.dump(test_data, f, protocol=cPickle.HIGHEST_PROTOCOL)
# # f.close()
#
# f = file('../data/smile_detection/validate/image_names', 'r')
#
# validate_data = []
# for line in f:
#     line =line.strip()
#     line = "../data/smile_detection/validate/" + line
#     image = open(line,'r')
#     numpyImage = array(image)
#     if "a" in line:
#         validate_data.append((numpyImage,0))
#     else:
#         validate_data.append((numpyImage, 1))
# f.close

f = file('../data/smile_detection/test/image_names', 'r')

testImage = []
testResult=[]
for line in f:
    line=line.strip()
    line = "../data/smile_detection/test/" + line
    testImage.append(line)
    if "b" not in line:
        testResult.append(0)
    else:
        testResult.append(1)
testImageNumpy = [np.array(Image.open(fname))/255.0 for fname in testImage]
testFinal = []
testFinal.append(testImageNumpy)
testFinal.append(testResult)
f.close()

f = file('../data/smile_detection/validate/image_names', 'r')

validateImage = []
validateResult=[]
for line in f:
    line=line.strip()
    line = "../data/smile_detection/validate/" + line
    validateImage.append(line)
    if "b" not in line:
        validateResult.append(0)
    else:
        validateResult.append(1)
validateImageNumpy = [np.array(Image.open(fname))/255.0 for fname in validateImage]
validateFinal = []
validateFinal.append(validateImageNumpy)
validateFinal.append(validateResult)

f.close()

f = file('../data/smile_detection/smile.pkl', 'wb')
cPickle.dump((trainFinal, validateFinal, testFinal), f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()

print "done"