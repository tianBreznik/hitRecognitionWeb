import hitRecognition
import numpy as np
#da bo np delal moras install-at novejso verzijo pythona kot python 2.7
#ampak matlab package-i ne supportajo python 3.7, 3.6 takda se probaj 3.5 64 version
myAudio = hitRecognition.initialize()
returned = myAudio.audioRecognition()
returned = np.asrray(returned)
binOut = returned.astype(int)
#for i in range(0, len(returned)):
#    if returned[i] == True:
#        returned[i] = 1 
#    else:
#        returned[i] = 0
print(returned)
#print acc
#print len(returned)
myAudio.terminate()
