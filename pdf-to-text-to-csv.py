import pdfplumber
import pandas as pd
 
pdf = pdfplumber.open('eni.pdf')
page = pdf.pages[1]
text = page.extract_text()
print(text)
pdf.close()

file1 = open("myfile.txt","w") 
file1.writelines(text)
file1.close() #to change file access modes 

data = pd.read_csv('myfile.txt', encoding= 'unicode_escape', header=None)
data
