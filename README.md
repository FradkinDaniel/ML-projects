# MLEX2 – Sigmoid Classification Model

> Introduction to Machine Learning course assignment implementing a **logistic regression model** (sigmoid-based classification) in Python.

---

## Table of Contents
- [About](#about)  
- [Model](#model)  
- [Dataset](#dataset)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Tests](#tests)  
- [Results](#results)  
- [Project Structure](#project-structure)  
- [License](#license)

---

## About
This project was developed as part of the **Introduction to Machine Learning** course.  
The goal of the assignment is to implement and test a **binary classification model** using logistic regression with the sigmoid activation function.

It demonstrates:
- Loading and preprocessing a dataset  
- Implementing the sigmoid hypothesis function  
- Training the model with gradient descent  
- Evaluating predictions on unseen data  
- Visualizing the decision boundary  

---

## Model
The model uses the **sigmoid function**:

\[
h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}
\]

- Produces outputs between **0 and 1**  
- Applies a threshold (0.5) to classify examples into class `0` or `1`  
- Learns decision boundaries by minimizing the cost function with gradient descent  

---

## Dataset
The dataset is provided in `ex2data1.txt`.  
- Format: `[feature1, feature2, label]`  
- Labels: binary (`0` or `1`) representing the decision outcome  
- Used to train and evaluate the classifier  

---

## Getting Started

### Prerequisites
- Python 3.8+  
- Install dependencies:
  ```bash
  pip install numpy matplotlib
