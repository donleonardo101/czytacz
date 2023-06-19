import pytesseract
from pdf2image import convert_from_path
import glob

# from PIL import Image
# from googletrans import Translator
# from PyPDF2 import PdfFileReader

pdfs = glob.glob(r"./rosliny.pdf")
# output_folder = glob.glob(r"./")

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)

    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='pol')

        with open(f'{pdf_path[:-4]}_page{pageNum}.txt', 'w') as the_file:
            the_file.write(text)

print("conversion complete")

# https://stackoverflow.com/questions/66995340/pdf-to-text-convert-using-python-pytesseract


        # with open(doc_file, mode='w') as the_file: 
        #     the_file.write(text) 


# cd /tmp
# # curl https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh --output anaconda.sh
# curl https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh --output anaconda.sh
# bash anaconda.sh
# source ~/.bashrc
# conda search "^python$"
# conda create --name czytacz python=3.10.11
# conda activate czytacz
# python --version
# conda deactivate


# conda install -c conda-forge pytesseract
# conda install -c conda-forge tesseract
# pip install pdf2image
# python czytacz.py