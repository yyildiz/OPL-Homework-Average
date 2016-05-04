from selenium import webdriver
from bs4 import BeautifulSoup
import sys

def get_grades(url):
  driver = webdriver.Firefox()
  driver.get(str(url))
  driver.get("https://grader.cs.uml.edu/courses/22")
  page = BeautifulSoup(driver.page_source, "lxml")
  driver.close()
  table = page.find("table")
  data = []
  rows = table.find_all("tr")

  for row in rows:
    cols = row.find_all("td")
    data.append(cols)

  values = []
  for i in range(1, 9):
    values.append(data[i][1].text)

  return values

def get_grades_average(values):
  # get_grades returns a list of strings in the format "200 / 200" which need to be converted to floats.

  seperated_vals = map(lambda x: x.split(" / ") , values)
  total_numerator = 0
  total_denominator = 0
  for numer in seperated_vals:
    total_numerator = total_numerator + float(numer[0])
    total_denominator = total_denominator + float(numer[1])
  
  average = 100 * total_numerator/total_denominator
  return average


def main():
  url = raw_input("Enter the URL of your BottleNose User Authentication Page: ")
  # unformatted list in the form of "200 / 200" string values.
  grade_list = get_grades(url)
  average = get_grades_average(grade_list)
  print "Your homework average is: " + str(average)

if __name__ == '__main__':
  main()