import pdfplumber
import pandas as pd


with pdfplumber.open('eni.pdf') as pdf:
    page = pdf.pages[4]
    text = page.extract_text()
    print(text)
    
file1 = open("myfile.txt","w") 
file1.writelines(text)
file1.close() #to change file access modes 

data = pd.read_csv('myfile.txt', encoding= 'unicode_escape', header=None, sep='delimiter', engine='python')
data.to_excel('myfile.xlsx')
data
