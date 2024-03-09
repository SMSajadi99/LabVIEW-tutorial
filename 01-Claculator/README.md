# Nerual-Network

# Assignment 
+ HomeWork 01
  
    + HomeWork 01 (optional)
+ HomeWork 02


## Home Work 04 (Image compression and reconstruction with Neural Network)
In this exercise, we want to try to compress a photo with 3 methods and reconstruct it with a neural network :)

1. [Photo compression by framing the photo and subtracting the average of each frame (using sklearn library)](https://github.com/SMSajadi99/Nerual-Network/blob/main/README.md#photo-compression-by-framing-the-photo-and-subtracting-the-average-of-each-frame-using-sklearn-library)
2. [Photo compression by framing the photo and subtracting the average from the total (using tensorflow library)](https://github.com/SMSajadi99/Nerual-Network/blob/main/README.md#photo-compression-by-framing-the-photo-and-subtracting-the-average-from-the-total-using-tensorflow-library)
3. [Standard PCA method (this method is without neural network)](https://github.com/SMSajadi99/Nerual-Network/blob/main/README.md#standard-pca-method-this-method-is-without-neural-network)

 ### Photo compression by framing the photo and subtracting the average of each frame (using sklearn library)

In this method, we try to create boxes in the shape and in the same box, we create boxes whose average is placed instead of the matrix of the same box, and Sklearn library tries to reconstruct it.

The main photo is as follows:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/face.jpg)

The Gray photo is as follows:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/bw_face.jpg)


In the table below, the parameters that should be required for training the network are given:

Max Iter | Hidden Layer Sizes | Test Size | Random State
--- | --- | --- | ---
5000 | 400,200 | 0.05 | 42

Now we try to display the results and outputs with 3 different boxes:

Framing | 8 x 8 | 16 x 16 | 32 x 32
--- | --- | --- | ---
Smaller Framing | 4 x 4 | 4 x 4 | 8 x 8
Samples Number | 4000 | 2000 | 1000
`PSNR (dB)` | 33.97 | 33.87  | 32.22

The results of each are listed separately:

* 8 x 8

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/8x8-3000/combined_image.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/8x8-3000/combined_image_com.png)

**Result:**

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/8x8-3000/combined_image_results.png)

  
* 16 x16

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/combined_image.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/combined_image_com.png)

**Result:**

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/combined_image_results.png)

* 32 x 32

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/32x32-750/combined_image.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/32x32-750/combined_image_com.png)


**Result:**

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/32x32-750/combined_image_results.png)




 ### Photo compression by framing the photo and subtracting the average from the total (using tensorflow library)
 
In this method, the entire image has been subtracted from each frame, and we have tried to reconstruct the image by moving it:

The main photo is as follows:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/face.jpg)

The Gray photo is as follows:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method01/16x16-1500/bw_face.jpg)

The Gray photo, from which the average is subtracted is as follows:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/16x16/reconstructed_com_image.jpg)


In the table below, the parameters that should be required for training the network are given:

Epoch |  Test Size | Random State
--- | --- | ---
50 |  0.2 | 42

Now we try to display the results and outputs with 3 different boxes:

Framing | 2 x 2 | 8 x 8 | 16 x 16
--- | --- | --- | ---
Samples Number | 39000 | 8000 | 4000
Weight | [Weight 2x2](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/2x2/image_translation_model_2x2.h5) | [Weight 8x8](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/8x8/image_translation_model_8x8.h5) | [Weight 16x16](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/16x16/image_translation_model_16x16.h5)
`PSNR (dB)` | 19.72 | 18.23  | 17.43


* 2 x 2


![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/2x2/bw_face.jpg)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/2x2/reconstructed_final_2x2.jpg)


* 8 x 8


![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/8x8/bw_face.jpg)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/8x8/reconstructed_final_image_8x8.jpg)



* 16 x 16


![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/8x8/bw_face.jpg)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method02/16x16/reconstructed_final_image_16x16.jpg)

 
 

 ### Standard PCA method (this method is without neural network)
 
In this method, we tried to compress the photo with the PCA method, and then reconstruct it with its basic components:

![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method03/bw_face.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method03/PCA_face.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method03/Recom_150_PCA_fac.png)
![Image Collage](https://github.com/SMSajadi99/Nerual-Network/blob/main/assinments/4/Method03/Recom_all_PCA_fac.png)


Be happy :)
 
