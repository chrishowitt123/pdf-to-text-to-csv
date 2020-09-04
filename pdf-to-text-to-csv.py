import pdfplumber
import pandas as pd

filename = 'annualfinancialsample.pdf'
fn = filename.split('.')[0] #seperate filename from extention for f-string output files

with pdfplumber.open(filename) as pdf: #extract text from desired page
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)
    
file1 = open(f"{fn}.txt","w") #output pdf text as .txt
file1.writelines(text)
file1.close() 

data = pd.read_csv(f"{fn}.txt", encoding= 'unicode_escape', header=None, sep='delimiter', engine='python') #read text file as csv and output
data.to_excel(f"{fn}.xlsx")
data
