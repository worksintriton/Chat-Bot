from wand.image import Image as wi
pdf = wi(filename='C:/Users/Triton/Desktop/image/Gowtham00.pdf', resolution=300)

pdfimage = pdf.convert('jpeg')

i=1
for img in pdfimage.sequence:
    page = wi(image=img)
   # page.save(filename=str(i)+'.jpg')
    pdf.save(filename="C:/Users/Triton/Desktop/image/img/gowthampdfimage.jpg")

    i +=1
print('ok')
