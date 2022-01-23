from curses.ascii import isdigit
import PyPDF2
import re
from tika import parser 
    
def main():
    raw = parser.from_file('MAT_1.pdf')
    file = raw['content']
    #print(file)

    #split file by assignment
    file_split_by_assignment = file_split_by_word(file, "assignment")
    len_assignment = len(file_split_by_assignment);
    for x in range (0, len_assignment):
        date = date_finder(file_split_by_assignment[x])
        print(date)

    #print(file_split_by_assignment[len_assignment - 2])
    print(date_finder(file_split_by_assignment[len_assignment - 2]))
    

def file_split_by_word(file, word):
    return re.split(word, file, flags = re.IGNORECASE)

def assignment_name(file):
    next_word = file.split()[0]
    
    if next_word.isdigit():
        return "Assignment" + next_word
    else:
        return "Assignment"
    
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
                if list_all_words[list_all_words_index+1].isdigit():
                    found_date = int(list_all_words[list_all_words_index+1])
                return [found_month, found_date]

    return [found_month, found_date]

if __name__ == "__main__":
    main() 
