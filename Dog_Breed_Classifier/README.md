# Dog Breed Classifier

Build a pipeline that can be used within a web or mobile app to process real-world, user-supplied images. Given an image of a dog, the algorithm will identify an estimate of the canine’s breed. If supplied an image of a human, the code will identify the resembling dog breed.  

Sample Dog Output 1        |Sample Dog Output 2        |Sample Human Output                    
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/LuLi0077/AI/blob/master/Dog_Breed_Classifier/images/sample_dog_output.png" width="285" height="285">  |  <img src="https://github.com/LuLi0077/AI/blob/master/Dog_Breed_Classifier/images/sample_dog_output2.png" width="285" height="285">  |  <img src="https://github.com/LuLi0077/AI/blob/master/Dog_Breed_Classifier/images/sample_human_output.png" width="285" height="285">  


`dog_breed_classifier.ipynb` - 

* Step 0: Import datasets
* Step 1: Detect humans ([haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades))
* Step 2: Detect dogs ([ResNet-50](http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006))
* Step 3: Create a CNN to classify dog breeds (from scratch)
* Step 4: Use a CNN to classify dog breeds (using transfer learning)
* Step 5: Create a CNN to classify dog breeds (using transfer learning)
* Step 6: Write algorithm
* Step 7: Test algorithm
* Step 8: Overlay dog ears on detected human heads
* Step 9: Turn the algorithm into a web app


## Convolutional Neural Networks Workbooks

* `mnist_mlp.ipynb` - train an MLP to classify images from the MNIST database
* `cifar10_mlp.ipynb` - train an MLP to classify images from the CIFAR-10 database
* `cifar10_cnn.ipynb` - train a CNN to classify images from the CIFAR-10 database
* `cifar10_augmentation.ipynb` - train a CNN on augmented images from the CIFAR-10 database
* `conv_visualization.ipynb` - visualize four activation maps in a CNN layer
* `bottleneck_features.ipynb` - calculate VGG-16 bottleneck features on a toy dataset
* `transfer_learning.ipynb` - use transfer learning to train a CNN to classify dog breeds


## Resources

* [Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
* [How convolutional neural networks see the world](https://blog.keras.io/how-convolutional-neural-networks-see-the-world.html)
* [How to Grid Search Hyperparameters for Deep Learning Models in Python With Keras](http://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)
* [Image Augmentation for Deep Learning With Keras](http://machinelearningmastery.com/image-augmentation-deep-learning-keras/)
* [Keras_Cheat_Sheet_Python](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Keras_Cheat_Sheet_Python.pdf)
* [ImageNet: VGGNet, ResNet, Inception, and Xception with Keras](http://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/) - [classify_image.py](https://github.com/LuLi0077/Code_Snippets/blob/master/Python/classify_image.py)
* [Haar Cascade Object Detection Face & Eye OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/)
* [Object Recognition with Convolutional Neural Networks in the Keras Deep Learning Library](http://machinelearningmastery.com/object-recognition-convolutional-neural-networks-keras-deep-learning-library/)
