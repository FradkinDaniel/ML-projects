# Ex1 – Linear Regression Model

> Introduction to Machine Learning course assignment implementing **linear regression** in Python.

---

## Table of Contents
- [About](#about)  
- [Model](#model)  
- [Dataset](#dataset)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Results](#results)  
- [Project Structure](#project-structure)  
- [License](#license)

---

## About
This project was developed as part of the **Introduction to Machine Learning** course.  
The assignment focuses on implementing and testing a **linear regression model** with gradient descent.

It demonstrates:
- Loading and visualizing data  
- Implementing linear regression with cost function minimization  
- Training with **gradient descent**  
- Plotting the regression line and cost convergence  

---

## Model
The linear regression hypothesis is:

\[
h_\theta(x) = \theta_0 + \theta_1 x
\]

Training is performed using **gradient descent** to minimize the cost function:

\[
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
\]

---

## Dataset
The dataset (e.g. `ex1data1.txt`) contains two columns:
- `x`: independent variable (feature)  
- `y`: dependent variable (target value)  

It is used to train the linear regression model and visualize the regression line.  

---

## Getting Started

### Prerequisites
- Python 3.8+  
- Required packages:
  ```bash
  pip install numpy matplotlib
