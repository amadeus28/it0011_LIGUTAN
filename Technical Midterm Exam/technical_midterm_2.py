from datetime import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")
date_obj = datetime.strptime(date_input, "%m/%d/%Y")
formatted_date = date_obj.strftime("%B %d, %Y")

print("Date Output:", formatted_date)
