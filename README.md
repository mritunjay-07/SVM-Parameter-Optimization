- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# SVM PARAMETER OPTIMIZATION
## OVERVIEW
This assignment is an implementation of SVM (Support Vector Machine) algorithm with parameter optimization using random search. The algorithm is applied on the 
"Room Occupancy Estimation" dataset which contains temperature, humidity, light, and CO2 sensor data for a room.

The python code uses the RandomizedSearchCV function of scikit-learn library to perform parameter optimization for SVM. The hyperparameters tuned in this algorithm include kernel, Nu, and epsilon.

Parameter optimization for SVM is an important step in tuning the performance of the algorithm. SVM is a machine learning algorithm that is used for classification and regression analysis. SVM tries to find a boundary that best separates the classes in the data. However, the performance of SVM is highly dependent on the values of its hyperparameters, such as Kernel type, Nu value, and Epsilon value. Therefore, the goal of parameter optimization is to find the best set of hyperparameters that maximize the performance of SVM on the given data.

In this code, a 10-fold cross-validation strategy is used to evaluate the performance of SVM with different sets of hyperparameters. The RandomizedSearchCV function randomly samples a set of hyperparameters from a predefined distribution and evaluates the performance of SVM with those hyperparameters. The best set of hyperparameters is selected based on the highest performance score obtained from the cross-validation. The process is repeated 10 times with different random seeds to ensure the robustness of the optimization results.

Finally, the code generates a table that shows the best hyperparameters and accuracy obtained for each sample.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


