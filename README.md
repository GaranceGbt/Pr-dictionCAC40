# Project: Crawler and Stock Market Analysis

Objective: Retrieve a table with data collected at regular intervals and analyze the stock market using the data table.

## 1. How to Use

The 'crawler' and 'Prediction' files can be used separately. Using 'Prediction' requires a table returned by the crawler or a table with the same structure.

## 2. Prerequisites

Python Version 8.2.0
Requires the following packages:
   - requests
   - bs4
   - pandas 
   - time
   - scikitLearn
   - matplotlib.pyplot

## Using the 'crawler' file

The arguments of the functions created in the crawler file are explained directly. To collect data over a desired period:
Go to Part 4 (line 140) and adjust the parameters according to your needs.

## Using the 'Prediction' file

Importing a data table in CSV format is necessary to run this program. If you want to use your own dataset, modify the file name in line 14. By default, we import data collected over a half-day on November 8th, named 08nov.csv. The analysis can be done on any company from CAC40; just change the company name appearing in line 17 to the desired one. The number of training values can be changed in line 30, and the total number of values in line 31. The number of variables within the moving averages can be changed:
- Line 76 for single moving average
- Lines 85 and 88 for the other two

## Using the 08nov.csv file

No modifications are needed for this file. It serves as the dataset for the 'Prediction' program.
