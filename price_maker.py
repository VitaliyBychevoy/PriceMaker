import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename='DB.xlsx', data_only=True)

print(wb.sheetnames)

# 1. Chose machine

# 2. Chose system

# 3. Chose part (punch, die or stripper). 

# 3.1 Punch.  
#Chose shape and input dimentions.
#Option_one: flat, wisper, rooftop. Option_two coationg. Option_three subzerro.

# 3.2 If die.
#Chose shape and input dimentions.
#Option_one gap.

# 3.3 If stripper.
#Chose shape and input dimentions.

# 4. Press "+" to add part or "=" to check order

# 4.1 (If pressed "+") go back to 3.

# 4.2 (If pressed "=") press number of part to change / remove from the list or 
#press "=" once againg to sumbmit order.

# 4.3 (If press any number form list order) go to 3.
