CS 4375 Assignment 1

disclaimer: I did use the help of AI to make the gradient descent program and the graphing at the end of part1.py to plot G1 vs G3 and then G2 vs G3

Purpose:  comparing two lienar regression models using the UCI Student Performance dataset


Files:

part1.py - implementing manual gradient descent
part2.py - implementing scikit-learn's SGDRegressor for


Dataset:

The dataset is for Student Performance, with the target variable being G3, the student's final grade. 
URL for dataset in public https://raw.githubusercontent.com/Santosh-1845/CS-4375---Assignment1/refs/heads/main/student-mat.csv


Requirements:

-Python 3
-NumPy
-pandas
-scikit-learn
-Matplotlib

Install packages: python -m pip install numpy pandas scikit-learn matplotlib


How to Run:

Run the commands below

python part1.py
python part2.py



Best Parameters

Part 1:

Learning Rate: 0.20
Iterations: 500
Testing MSE: 5.656643

Part 2:

Learning Rate: 0.0065
Iterations: 1000
Testing MSE: 5.483105