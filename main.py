from curses.ascii import isdigit
import PyPDF2
import re
from tika import parser 
import datetime
import csv

def main():
    today = datetime.datetime.now()
    date = today.date()
    current_month = date.month
    current_year = date.year
            
    raw = parser.from_file('SAMPLE-Course-Syllabus.pdf')
    file = raw['content']
    #print(file)

    #split file by assignment
    file_split_by_assignment = file_split_by_word(file, "assignment")
    file_split_by_midterm = file_split_by_word(file, "midterm")
    len_assignment = len(file_split_by_assignment)
    main_list  = []
    
    for x in range (0, len_assignment):
        list = []
        date = date_finder(file_split_by_assignment[x])
        name = evaluation_name(file_split_by_assignment[x], "Assignment")
        
        if "nil" not in date:    
            list.append(name)
            date = date_to_num(date, current_month, current_year)
            list.append(date)
            main_list.append(list)
            
    for x in range (0, len(file_split_by_midterm)):
        list = []
        date = date_finder(file_split_by_midterm[x])
        name = evaluation_name(file_split_by_midterm[x], "Midterm")
        
        if "nil" not in date:
            list.append(name)
            date = date_to_num(date, current_month, current_year)
            list.append(date)
            main_list.append(list)
        
    for x in range (0, len(main_list)):
         print(main_list[x])
         
    content = main_list
    header = ['Subject', "Start Date"]
    
    with open('calendar.csv', 'w', encoding = 'UTF8', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(content)
            
        
            
def date_to_num(date, current_month, current_year):
    month = month_to_number(date[0])
    day = date[1]
    year = current_year
    
    if month>=1 and month<current_month: year = str(current_year + 1)
    if month<10: month = "0" + str(month)
    if day<10: day = "0" + str(day)
    
    year = str(year)
    day = str(day)
    month = str(month)
    
    return month + "/" + day + "/" + year
    
def month_to_number(month):
    return {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9, 
        "October": 10,
        'November': 11,
        'December': 12
    } [month]   

def file_split_by_word(file, word):
    return re.split(word, file, flags = re.IGNORECASE)

def evaluation_name(file, evaluation_type):
    next_word = file.split()[0]
    
    if next_word.isdigit():
        return evaluation_type + " " + next_word
    else:
        return evaluation_type
    
def date_finder(file):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    months_full = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]         
    list_all_words = file.split()[0:9]
        
    found_month = "nil"
    found_date = "nil"
    
    for months_index in range (0, len(months)):
        month = months[months_index]
        for list_all_words_index in range (0,len(list_all_words)):
            word = list_all_words[list_all_words_index]
            if month.lower() in word.lower():
                found_month = months_full[months_index]
                if list_all_words[list_all_words_index+1].replace(",", "").replace("st", "").replace("rd", "").replace("th", "").isdigit():
                    found_date = int(re.sub("[^0-9]", "", list_all_words[list_all_words_index+1]))
                return [found_month, found_date]

    return [found_month, found_date]

if __name__ == "__main__":
    main() 
