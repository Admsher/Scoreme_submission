import pypdf
import os
import pandas as pd

filepath="test3.pdf"
file= os.path.basename(filepath)
pdfread=pypdf.PdfReader(filepath)
dataframe=pd.DataFrame()

for pages in pdfread.pages:
    text=pages.extract_text()
    
    row=text.split("\n")
    for i in range(len(row)):
        row[i] = ' '.join(row[i].split())
        columns=row[i].split(" ")

        dataframe = pd.concat([dataframe, pd.DataFrame([columns])], ignore_index=True)
    
dataframe.to_excel(file.split(".")[0]+".xlsx")






    