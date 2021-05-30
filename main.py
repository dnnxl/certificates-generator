from PIL import Image, ImageDraw, ImageFont

import os
import pandas as pd
import argparse

def generate_certificates(pFile, pTemplate, pOutformat, pNamecol, pIdentcol, pXlocation, pYlocation, pFontSize):

    df = None
    if(".csv" in pFile):
        df = pd.read_csv(pFile)
    elif(".xlsx" in pFile):
        df = pd.read_excel(pFile)
    else:
        return

    os.makedirs("./certificates", exist_ok=True)
    name_list = df[pNamecol].to_list()
    for i in name_list:
        im = Image.open(pTemplate)
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background

        d = ImageDraw.Draw(im)
        location = (pXlocation, pYlocation)
        text_color = (0, 0, 0)
        font = ImageFont.truetype("arial.ttf", pFontSize)
        d.text(location, i, fill=text_color,font=font)

        rgb.paste(im, mask=im.split()[3])               # paste using alpha channel as mask

        rgb.save("./certificates/certificate_"+i+".{0}".format(pOutformat), 'PDF', resoultion=100.0)


if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Generate certificates.')

    parser.add_argument('-c', '--csvfile', type=str, 
        default="", help='The rute of the csv file.', required=True)

    parser.add_argument('-t','--template', type=str, 
        default="", help='The certificate template in pdf format.', required=True)

    parser.add_argument('-o','--outformat', type=str, 
        default="pdf", help='The output format can be pdf, png or jpeg.')

    parser.add_argument('-n','--namecol', type=str, 
        default="name", help='Field column name of the person.', required=True)

    parser.add_argument('-i','--identcol', type=str, 
        default="identification", help='Field column name of the identification.')

    parser.add_argument('-x','--xlocation', type=float, 
        default=133, help='The x location in the axis X of the start of the name.')

    parser.add_argument('-y','--ylocation', type=float, 
        default=665, help='The x location in the axis Y of the start of the name.')
    
    parser.add_argument('-f','--fontSize', type=int, 
        default=12, help='Font size.')
    
    args = parser.parse_args()
    generate_certificates(args.csvfile, args.template, args.outformat, args.namecol, args.identcol, args.xlocation, args.ylocation, args.fontSize)