#CODE BY VIREN SACHDEV
print("TO convert txt file to pdf program, go to terminal or cmdPrompt, and type pip intall fpdf")
print("TO convert img file to pdf program, go to terminal or cmdPrompt, and type pip intall img2pdf")
from fpdf import FPDF
import img2pdf
from PIL import Image
import os

#conversion of text and Img to pdf format program.
def textToPdf(size_ofFont, txtFile, nameOfFile):
    #saving class into variable
    pdf = FPDF()
    #adding page
    pdf.add_page()
    #set style and size of font as requried in pdf
    pdf.set_font("Arial", size = size_ofFont)
    #opening the text file in read mode
    f = open("{0}".format(txtFile), "r")
    #insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    #save the .pdf file
    pdf.output("{0}.pdf".format(nameOfFile))
    #output
    print("Successfully made pdf file in current working dir")

#converting img files to pdf
def imgToPdf(pathImg, nameOffile):
    #storing image path
    img_path = pathImg
    #storing pdf path
    pdf_path = "{0}/{1}.pdf".format(os. getcwd(), nameOffile)
    #opening image
    image = Image.open(img_path)
    #converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    #opening or creating pdf file
    file = open(pdf_path, "wb")
    #writing pdf files with chunks
    file.write(pdf_bytes)
    #closing image file
    image.close()
    #closing pdf file
    file.close()
    #output
    print("Successfully made pdf file in current working dir")


def main():

    print("Welcome to file converter")
    print("choose option")
    print("1.convert txt file to pdf")
    print("2.convert image file to pdf")
    option = int(input("choose option (1 or 2) : "))


    if option == 1:
        #taking inputs
        size_ofFont = int(input("Enter size of font: "))
        txtFile = input("Enter the name and path of txt file: ")
        nameOfFile = input("Enter the name, by which you want to save your pdf file: ")
        print("PDF file will be saved where you ran the program")

        #calling function
        textToPdf(size_ofFont, txtFile, nameOfFile)


    elif option == 2:
        #taking inputs
        pathImg = input("Enter path of image: ")
        nameOffile = input("Enter the name you would like the pdf to be saved: ")

        #calling function
        imgToPdf(pathImg, nameOffile)




if __name__=="__main__":
    main()


