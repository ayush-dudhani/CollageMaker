from PIL import Image
import os

def collage_maker(image1, image2, image3, image4, image5, image6, image7, image8,name):
    collage = Image.new("RGBA", (2000,1000))
    
    img1 = Image.open(image1)
    img1 = img1.resize((500,500))
    
    img2 = Image.open(image2)
    img2 = img2.resize((500,500))
    
    img3 = Image.open(image3)
    img3 = img3.resize((500,500))
    
    img4 = Image.open(image4)
    img4 = img4.resize((500,500))
    
    img5 = Image.open(image5)
    img5 = img5.resize((500,500))
    
    img6 = Image.open(image6)
    img6 = img6.resize((500,500))
    
    img7 = Image.open(image7)
    img7 = img7.resize((500,500))
    
    img8 = Image.open(image8)
    img8 = img8.resize((500,500))
    
    
    collage.paste(img1, (0,0))
    collage.paste(img3, (500,0))
    collage.paste(img5, (1000,0))
    collage.paste(img7, (1500,0))
    collage.paste(img2, (0,500))
    collage.paste(img4, (500,500))
    collage.paste(img6, (1000,500))
    collage.paste(img8, (1500,500))
    
    collage.save(name)
