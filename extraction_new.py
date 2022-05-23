from curses.ascii import isdigit
import re
from sqlalchemy import null
from tika import parser 
import datetime
import csv

def main():
    today = datetime.datetime.now()
    date = today.date()
    current_month = date.month
    current_year = date.year

    raw = parser.from_file("user_upload.pdf")
    file = raw['content'].lower()
    #print(file)

    file_split_by_assignment = file_split_by_word(file, "assignment")
    file_split_by_assessment = file_split_by_word(file, "assessment")
    file_split_by_midterm = file_split_by_word(file, "midterm")
    file_split_by_final = file_split_by_word(file, "final")

    main_list  = []

    for check_assignment_date_block in file_split_by_assignment:
        [assignment_number, month, date] = date_finder(check_assignment_date_block)

        if month!=None and date!=None:
            if assignment_number == None:
                main_list.append(["Assignment", date_to_num(month, date, current_month, current_year)])
            else:
                main_list.append(["Assignment " + assignment_number, date_to_num(month, date, current_month, current_year)])      
    
    for check_assessment_date_block in file_split_by_assessment:
        [assessment_number, month, date] = date_finder(check_assessment_date_block)

        if month!=None and date!=None:
            if assessment_number == None:
                main_list.append(["Assessment", date_to_num(month, date, current_month, current_year)])
            else:
                main_list.append(["Assessment " + assessment_number, date_to_num(month, date, current_month, current_year)]) 

    for check_midterm_date_block in file_split_by_midterm:
        [midterm_number, month, date] = date_finder(check_midterm_date_block)

        if month!=None and date!=None:
            if midterm_number == None:
                main_list.append(["Midterm", date_to_num(month, date, current_month, current_year)])
            else:
                main_list.append(["Midterm " + midterm_number, date_to_num(month, date, current_month, current_year)]) 

    for check_final_date_block in file_split_by_final:
        [final_number, month, date] = date_finder(check_final_date_block)

        if month!=None and date!=None:
            if final_number == None:
                main_list.append(["Final", date_to_num(month, date, current_month, current_year)])
            else:
                main_list.append(["Final " + midterm_number, date_to_num(month, date, current_month, current_year)]) 

    print(main_list)

    header = ['Subject', "Start Date"]
    with open('calendar.csv', 'w', encoding = 'UTF8', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(main_list)
    return


def date_to_num(eval_month, eval_date, current_month, current_year):

    if current_month>=9 and current_month<=12:
        if eval_month>=1 and eval_month<=8: current_year = str(current_year + 1)
    
    if eval_month<10: eval_month = "0" + str(eval_month)
    if int(eval_date)<10: eval_date = "0" + str(eval_date)
        
    return str(eval_month) + "/" + str(eval_date) + "/" + str(current_year)

def file_split_by_word(file, word):
    return re.split(word, file, flags = re.IGNORECASE)

def month_to_number(month):
    return {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9, 
        "oct": 10,
        'nov': 11,
        'dec': 12,
        None: None
    } [month]  

def date_finder(date_block):

    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        
    found_month = None
    found_date = None
    evaluation_number = None

    #print("########################################################################")
    words_array = date_block.split(" ")[0:7]
    words_combined = " ".join(words_array).strip()
    words_array = words_combined.split(" ")
    #print(words_array)
    if words_array[0].isdigit(): evaluation_number = words_array[0]

    for word in words_array:
        month_in_array = next((month for month in months if month in word), None)
        if month_in_array:
            found_month = month_in_array
            break

    if found_month:
        test = words_combined.split(found_month)[1].strip().split(" ")
        potential_date = next((date.split("\n")[0].replace(",", "").replace("st", "").replace("rd", "").replace("th", "") for date in test if date.split("\n")[0].replace(",", "").replace("st", "").replace("rd", "").replace("th", "").isdigit()), None)
        if potential_date and int(potential_date)<=31:
            found_date = potential_date

    #print(evaluation_number, month_to_number(found_month), found_date)

    return [evaluation_number, month_to_number(found_month), found_date]

if __name__ == "__main__":
    main() 