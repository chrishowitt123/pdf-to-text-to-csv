import pdfplumber
import pandas as pd


with pdfplumber.open('eni.pdf') as pdf:
    page = pdf.pages[3]
    text = page.extract_text()
    print(text)
    
file1 = open("myfile.txt","w") 
file1.writelines(text)
file1.close() #to change file access modes 

data = pd.read_csv('myfile.txt', encoding= 'unicode_escape', header=None, error_bad_lines=False)
data.to_excel('myfile.xlsx')
data
