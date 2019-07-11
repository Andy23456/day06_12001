from selenium.webdriver.common.by import By

loc1 = By.ID,"id1"

loc2 = "id","id1"
print(loc1[0],loc1[1])
print("*"*30)
print(loc2[0],loc2[1])
