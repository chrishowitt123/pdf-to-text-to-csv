import pdfplumber
import pandas as pd

filename = 'eni.pdf'
fn = filename.split('.')[0]

with pdfplumber.open(filename) as pdf:
    page = pdf.pages[4]
    text = page.extract_text()
    print(text)
    
file1 = open(f"{fn}.txt","w") 
file1.writelines(text)
file1.close() #to change file access modes 

data = pd.read_csv('myfile.txt', encoding= 'unicode_escape', header=None, sep='delimiter', engine='python')
data.to_excel('myfile.xlsx')
data
