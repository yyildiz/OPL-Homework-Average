# OPL-Homework-Average
You'd think that there would be an average of our grades displayed on Bottlenose... WRONG!    
This script simply scrapes the page and adds up your grades to find the total average.    
The average is based on total points per assignment so some assignments worth 200 points    
are weighed more than those out of 100.   
![Bottlenose Preview]
(http://i.imgur.com/DRoAOpM.png?1)

# How to use:

## 1. Make sure that you have the following libraries installed on your Computer:
### 1. Python - [Instructions](https://www.python.org/downloads/)
### 2. BeautifulSoup - [Instructions](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
### 3. Selenium - [Instructions](http://selenium-python.readthedocs.io/installation.html)

## 2. Run the program using the following command:
If you're on python3 use 
```
python2 get_opl_average.py
```
or just use the following for python2
```
python get_opl_average.py
```

## 3. When prompted enter your authentication URL for Bottlenose.
### It should be in the following format:
```url 
https://grader.cs.uml.edu/main/auth?email=FIRSTNAME_LASTNAME%40student.uml.edu&key=YOUR_USER_SPECIFIC_KEY
```
