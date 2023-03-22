## 1.1 welcome to the study of Machine Learning



## 1.2 What is Machine Learning

the two major types of ml alogrithms:

![image-20230129194352412](Andrew-Ng-machine-learning.assets/image-20230129194352412.png)



## 1.3 What is Supervised Learning

![image-20230129195327539](Andrew-Ng-machine-learning.assets/image-20230129195327539.png)



![image-20230129195506065](Andrew-Ng-machine-learning.assets/image-20230129195506065.png)

predict the sort of continuous values attribute

predict real_valued output



classification problem:

![image-20230129200534274](Andrew-Ng-machine-learning.assets/image-20230129200534274.png)



## 1.4 What is Unsupervised Learning?

clustering

just give the datas, let the algorithm automatically do something





## 2.1 Linear Regression with one variable——Model Representation

![image-20230201154018280](Andrew-Ng-machine-learning.assets/image-20230201154018280.png)



## 2.2 Linear Regression with one variable——Cost Function

![image-20230201154342472](Andrew-Ng-machine-learning.assets/image-20230201154342472.png)



square error cost function

![image-20230201171531140](Andrew-Ng-machine-learning.assets/image-20230201171531140.png)



## 2.3 Cost Function Intuition Ⅰ



## 2.4 Cost Function Intuition Ⅱ

contour plots



the same bowel shape as J(theta1)

![image-20230206085144359](Andrew-Ng-machine-learning.assets/image-20230206085144359.png)



![image-20230206085533090](Andrew-Ng-machine-learning.assets/image-20230206085533090.png)



## 2.5 Gradient descent

![image-20230206090447889](Andrew-Ng-machine-learning.assets/image-20230206090447889.png)

![image-20230206090428147](Andrew-Ng-machine-learning.assets/image-20230206090428147.png)



![image-20230209192300703](Andrew-Ng-machine-learning.assets/image-20230209192300703.png)



## 2.6 Gradient descent intuition



## 2.7 Gradient descent for linear regression

![image-20230209210424382](Andrew-Ng-machine-learning.assets/image-20230209210424382.png)



![image-20230210090514928](Andrew-Ng-machine-learning.assets/image-20230210090514928.png)



![image-20230213105352785](Andrew-Ng-machine-learning.assets/image-20230213105352785.png)



Gradient descent will scale better to larger data sets than that normal equations method



## 3.1 Matrices and vectors

 ![image-20230213112845116](Andrew-Ng-machine-learning.assets/image-20230213112845116.png)



## 3.2 Addition and scalar multiplication



## 3.3 Matrix-vector multiplication

![image-20230213113922027](Andrew-Ng-machine-learning.assets/image-20230213113922027.png)



## 3.4 Matrix-matrix multiplication 



## 3.5 Matrix multiplication properties

![image-20230213202234199](Andrew-Ng-machine-learning.assets/image-20230213202234199.png)



## 3.6 Inverse and transpose

![image-20230213203020140](Andrew-Ng-machine-learning.assets/image-20230213203020140.png)



![image-20230213203136618](Andrew-Ng-machine-learning.assets/image-20230213203136618.png)



## 4.1 Linear Regression with multiple variables——Multiple features

![image-20230216155953185](Andrew-Ng-machine-learning.assets/image-20230216155953185.png)



![image-20230216160427665](Andrew-Ng-machine-learning.assets/image-20230216160427665.png)



## 4.2 Linear Regression with multiple variables——Gradient d6escent for multiple variables

![image-20230222174035229](Andrew-Ng-machine-learning.assets/image-20230222174035229.png)



## 4.3 Linear Regression with multiple variables——Gradient descent in practice Ⅰ: Feature Scaling

gradient descents can converge more quickly

![image-20230222174456269](Andrew-Ng-machine-learning.assets/image-20230222174456269.png)



![image-20230222174717646](Andrew-Ng-machine-learning.assets/image-20230222174717646.png)



![image-20230228134323580](Andrew-Ng-machine-learning.assets/image-20230228134323580.png)



## 4.4 Linear Regression with multiple variables——Gradient descent in practice Ⅱ: Learning rate

the author tends to look at plots like the figure on the left rather than rely on an automatic convergence test

 ![image-20230228135427553](Andrew-Ng-machine-learning.assets/image-20230228135427553.png)



![image-20230228163918551](Andrew-Ng-machine-learning.assets/image-20230228163918551.png)



## 4.5 Linear Regression with multiple variables——Features and polynomial regression

sometimes by defining new features you might actually get a better model

![image-20230228172655376](Andrew-Ng-machine-learning.assets/image-20230228172655376.png)



## 4.6 Linear Regression with multiple variables——Normal equation

![image-20230307162143244](Andrew-Ng-machine-learning.assets/image-20230307162143244.png)



![image-20230307162627154](Andrew-Ng-machine-learning.assets/image-20230307162627154.png)



if you are using this normal equation method, then feature scaling isn't actually necessary

 ![image-20230307164542899](Andrew-Ng-machine-learning.assets/image-20230307164542899.png)

For this specific model of linear regression, the normal equation can give you an alternative that can be much faster than gradient descent. So, depending on the detail of your algorithm, depending on the detail of the problem and how many features that you have, both of these algorithms are well worth knowing about.



## 4.7 Linear Regression with multiple variables——Normal equation and non-invertibility (optional)

non-invertibility happens pretty rarely anyway so this should not be a problem for most implementations of linear regression



## 4.8 Octave Tutorial——Working on and submitting programming exercises



## 5.1 Octave Tutorial——Basic operations



## 5.9 Octave Tutorial——Vectorization



## 6.1 Logistic Regression——Classification



## 6.2 Logistic Regression——Hypothesis Representation

![image-20230308112438593](Andrew-Ng-machine-learning.assets/image-20230308112438593.png)

the term logistic function, that's what gives rise to the name logistic regression



## 6.3 Logistic Regression——Decision boundary

![image-20230308141715591](Andrew-Ng-machine-learning.assets/image-20230308141715591.png)



this decision boundary and a region where we predict Y equals 1 versus Y equals 0 are properties of the hypothesis and of the parameters of the hypothesis and not properties of the data set

![image-20230308140855353](Andrew-Ng-machine-learning.assets/image-20230308140855353.png)

the training set is not what we use to define the decision boundary but to fit the parameters theta



## 6.4 Logistic Regression——Cost function

![image-20230308160653039](Andrew-Ng-machine-learning.assets/image-20230308160653039.png)

if we use the same form of cost function as the Linear Regression's, we'll get a non-convex function, to which the gradient descent is not useful

![image-20230308161647672](Andrew-Ng-machine-learning.assets/image-20230308161647672.png)

![image-20230308161843991](Andrew-Ng-machine-learning.assets/image-20230308161843991.png)



## 6.5 Logistic Regression——Simplified cost function and gradient descent

![image-20230308201615192](Andrew-Ng-machine-learning.assets/image-20230308201615192.png)

![image-20230308202530877](Andrew-Ng-machine-learning.assets/image-20230308202530877.png)



## 6.6 Logistic Regression——Advanced optimization

![image-20230309084116420](Andrew-Ng-machine-learning.assets/image-20230309084116420.png)

it is actually entirely possible to use these algorithms successfully and apply to lots of different learning problems without actually understanding the inner-loop of what these algorithms do



## 6.7 Logistic Regression——Multi-class classification: One-vs-all

![image-20230309154154620](Andrew-Ng-machine-learning.assets/image-20230309154154620.png)

"one vs all" is also called "one vs rest"



![image-20230309154709844](Andrew-Ng-machine-learning.assets/image-20230309154709844.png)



![image-20230309162706198](Andrew-Ng-machine-learning.assets/image-20230309162706198.png)



## 7.1 Regularization——The problem of overfitting

underfitting, high bias

overfitting, high variance

![image-20230309163449260](Andrew-Ng-machine-learning.assets/image-20230309163449260.png)



![image-20230309163703173](Andrew-Ng-machine-learning.assets/image-20230309163703173.png)

![image-20230309164234935](Andrew-Ng-machine-learning.assets/image-20230309164234935.png)



## 7.2 Regularization——Cost function

![image-20230310085155229](Andrew-Ng-machine-learning.assets/image-20230310085155229.png)

if theta3 or theta4 are big nummbers, the value of the cost function will be big as well because there are plus 1000theta3 and 1000theta4, therefore, to decrease the value of the cost function, the value of theta3 and theta4 should be small, then the second hypothesis will change itself to a quadratic function



![image-20230310090112651](Andrew-Ng-machine-learning.assets/image-20230310090112651.png)



## 7.3 Regularization——Regularized linear regression

First situation: regularization used in gradient descent

![image-20230310091252739](Andrew-Ng-machine-learning.assets/image-20230310091252739.png)



Second situation: regularization used in Normal equation

![image-20230310171947495](Andrew-Ng-machine-learning.assets/image-20230310171947495.png)



## 7.4 Regularization——Regularized logistic regression





































