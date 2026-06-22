# Image Classification Using Convolutional Neural Network (CNN)

## Project Overview

This project was developed by following the tutorial:

**Image Classification Using CNN**

https://www.youtube.com/watch?v=Rmtr9SY-4VQ

The objective of this project is to implement an image classification system using Convolutional Neural Networks (CNN) and evaluate its performance on the CIFAR-10 dataset. In addition, an enhanced CNN architecture (new_CNN) was proposed to improve classification performance.

---

# 1. What is Image Classification?

Image classification is a computer vision task that involves assigning a predefined label or category to an image based on its visual content.

The goal is to enable computers to automatically recognize and categorize images similarly to human perception.

Examples include:

* Cat vs Dog Classification
* Face Recognition
* Medical Image Diagnosis
* Traffic Sign Recognition
* Product Classification

In this project, image classification was performed using the CIFAR-10 dataset.

---

# 2. What is CNN?

Convolutional Neural Network (CNN) is a deep learning architecture specifically designed for image processing and computer vision tasks.

CNN automatically learns important image features through multiple layers of processing.

## CNN Architecture

### Input Layer

Receives image pixels as input.

Example:

```text id="eh0i89"
32 × 32 × 3
```

RGB image

---

## Observations

The enhanced CNN achieved:

* Higher classification accuracy
* Lower loss
* Better generalization
* Reduced overfitting
* More stable training process

---

# Results and Discussion

The experimental results demonstrate that CNN is effective for image classification tasks.

The baseline CNN successfully learned image features and achieved satisfactory classification performance. However, the enhanced CNN outperformed the original model due to the introduction of:

* Data augmentation
* Batch normalization
* Additional convolution layers
* Dropout regularization

These improvements enabled the model to extract more meaningful image features while reducing overfitting.

The findings indicate that architectural enhancements significantly improve CNN performance on the CIFAR-10 dataset.

---

# Reflection

This project provided valuable experience in applying deep learning techniques for image classification. One of the main challenges encountered was understanding CNN architecture and selecting suitable hyperparameters. Additionally, monitoring training performance and identifying overfitting required careful analysis of accuracy and loss curves.

Through this project, I gained practical experience in:

* Deep Learning
* Convolutional Neural Networks
* Image Processing
* TensorFlow and Keras
* Model Evaluation
* Hyperparameter Tuning

The project also improved my understanding of how architectural design decisions influence model performance. Future work could explore transfer learning approaches such as VGG16, ResNet, and EfficientNet to achieve even higher classification accuracy.

---

# Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib

---

# Learning Outcomes

* Understand Image Classification Concepts
* Understand CNN Architecture
* Implement CNN Models in Python
* Evaluate Deep Learning Models
* Improve CNN Performance
* Compare Multiple CNN Architectures

