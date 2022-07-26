# importing required modules 
import PyPDF2

while True:
    # creating a pdf file object, opening it in binary mode (rb)
    pdfFileObj = open('yourfile.pdf', 'rb') #replace this with your file
        
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
    # printing number of pages in pdf file
    page_number = pdfReader.numPages
    print('There are {} pages in this file!'.format(page_number)) 
        
    # creating a page object 
    page_num = int(input('Which page do you want to convert?')) - 1 #pages are from 0 to page_num -1 but the user doesn't know that! user's page 1 is the computer's page 0.
    try:
        pageObj = pdfReader.getPage(page_num) 
    except:
        print('Out of range! There aren\'nt as many pages!')
        continue

    # extracting text from page 
    resultpage = pageObj.extractText()

    # closing the pdf file
    pdfFileObj.close()

    print ('Your File is ready!')

    # Saving the final file
    output = 'location/'+'page{}.txt'.format(page_num + 1) #replace 'location' with where you want to save the file
    f = open(output, 'w', encoding='utf-8') # encoding to avoid errors
    f.write(resultpage)
    f.close()

    break 
