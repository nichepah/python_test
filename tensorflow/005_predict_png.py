from keras.models import load_model
from PIL import Image
import numpy as np
import glob


if __name__ == "__main__":
    """ Identifies a png image. 
    
    Images were created in GIMP, 100x100, grey scale, exported as png, no extra data saved.
    Its a bit tricky to get it identified, especially digits like 8 !
    """
    model = load_model('csi_training_handwritten.h5')
    # list of files
    pic_files = sorted([f for f in glob.glob("pics/*_1.png")])
    for my_file in pic_files:
        my_img = Image.open(my_file).convert("L")
        my_img = my_img.resize((28, 28))
        my_arr = np.array(my_img)
        my_arr = my_arr.reshape(1, 784)
        my_pred = model.predict(my_arr)
        print(my_file, my_pred)

