- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# SVM PARAMETER OPTIMIZATION
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## OVERVIEW
This assignment is an implementation of SVM (Support Vector Machine) algorithm with parameter optimization using random search. The algorithm is applied on the 
"Room Occupancy Estimation" dataset which contains temperature, humidity, light, and CO2 sensor data for a room.

The python code uses the RandomizedSearchCV function of scikit-learn library to perform parameter optimization for SVM. The hyperparameters tuned in this algorithm include Kernel, Nu, and Epsilon.

Parameter optimization for SVM is an important step in tuning the performance of the algorithm. SVM is a machine learning algorithm that is used for classification and regression analysis. SVM tries to find a boundary that best separates the classes in the data. However, the performance of SVM is highly dependent on the values of its hyperparameters, such as Kernel type, Nu value, and Epsilon value. Therefore, the goal of parameter optimization is to find the best set of hyperparameters that maximize the performance of SVM on the given data.

In this code, a 10-fold cross-validation strategy is used to evaluate the performance of SVM with different sets of hyperparameters. The RandomizedSearchCV function randomly samples a set of hyperparameters from a predefined distribution and evaluates the performance of SVM with those hyperparameters. The best set of hyperparameters is selected based on the highest performance score obtained from the cross-validation. The process is repeated 10 times with different random seeds to ensure the robustness of the optimization results.

Finally, the code generates a table that shows the best hyperparameters and accuracy obtained for each sample.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## DATASET
* The "Room Occupancy Estimation" dataset available on the UCI Machine Learning Repository contains data collected from a wireless sensor network deployed in an office building for the purpose of occupancy detection. 
* The dataset can be downloaded from the given link: [Link](https://archive.ics.uci.edu/ml/datasets/Room+Occupancy+Estimation)
* The dataset consists of a total of 20,560 instances, with 16,928 instances in the training set and 3,632 instances in the test set. Each instance contains seven   attributes:
  * Date and time
  * Temperature, in degrees Celsius
  * Relative humidity, as a percentage
  * Light, measured in Lux units
  * CO2 concentration, measured in parts per million (ppm)
  * Humidity ratio, which is derived from the temperature and relative humidity values
  * Occupancy status, which is either 1 (occupied) or 0 (not occupied)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

![image](https://user-images.githubusercontent.com/104979974/233455715-245824f3-9dd6-45c1-80ee-9ba8037b060f.png)

