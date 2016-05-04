from selenium import webdriver
driver = webdriver.Firefox()
from bs4 import BeautifulSoup
import sys

url = raw_input("Enter the URL of your BottleNose User Authentication Page: ")

driver.get(str(url))
driver.find_element_by_link_text("Go To Courses").click()
driver.find_element_by_partial_link_text("COMP.3010").click()
page = BeautifulSoup(driver.page_source, "lxml")
table = page.find("table")
data = []
rows = table.find_all("tr")

for row in rows:
  cols = row.find_all("td")
  data.append(cols)

values = []
for i in range(1, 9):
  values.append(data[i][1].text)

seperated_vals = map(lambda x: x.split(" / ") , values)

total_numerator = 0
total_denominator = 0
for numer in seperated_vals:
  total_numerator = total_numerator + float(numer[0])
  total_denominator = total_denominator + float(numer[1])

print "Your average for homeworks is: " + str(100 * total_numerator/total_denominator)
