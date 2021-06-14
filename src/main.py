from PIL import Image, ImageDraw, ImageFont

import os
import pandas as pd
import argparse

# generate_certificates
# Generate certificates with the name and identification

def generate_certificates(**kwargs):

    df = None
    if(".csv" in kwargs['data_file']):
        df = pd.read_csv(kwargs['data_file'], sep=',')
    elif(".xlsx" in kwargs['data_file']):
        df = pd.read_excel(kwargs['data_file'])
    else:
        return
    os.makedirs("./certificates", exist_ok=True)

    for index, row in df.iterrows():

        im = Image.open(kwargs['template_file'])

        name_draw = ImageDraw.Draw(im)
        name_location = ( kwargs['x_name'],  kwargs['y_name'])
        name_text_color = (0, 0, 0)
        name_font = ImageFont.truetype("arial.ttf", kwargs['name_font_size'])

        name_draw.text(name_location, row[kwargs['name_col']], fill=name_text_color,font=name_font)

        if kwargs['ident_col'] != "":
            ident_draw = ImageDraw.Draw(im)
            ident_location = ( kwargs['x_ident'],  kwargs['y_ident'])
            ident_text_color = (0, 0, 0)
            ident_font = ImageFont.truetype("arial.ttf", kwargs['ident_font_size'])

            ident_draw.text(ident_location, row[kwargs['ident_col']], fill=ident_text_color,font=ident_font)

        im.save("./certificates/certificate_"+ row[kwargs['name_col']] +".{0}".format(kwargs['out_format']), 'PDF', resoultion=100.0)
    
if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Generate certificates.')

    parser.add_argument('-d', '--data_file', type=str, 
        help='The path of the csv or excel file with the data.', required=True)

    parser.add_argument('-t','--template_file', type=str, 
        help='The certificate template in pdf format.', required=True)

    parser.add_argument('-o','--out_format', type=str, 
        default="pdf", help='The output format can be pdf, png or jpeg.')

    parser.add_argument('-n','--name_col', type=str, 
        default="name", help='Name of the field column name.', required=True)

    parser.add_argument('-i','--ident_col', type=str, 
        default="", help='Name of the field column name of the identification.')

    parser.add_argument('-xn','--x_name', type=float, 
        default=100, help='The x location of the name field in the template.')

    parser.add_argument('-yn','--y_name', type=float, 
        default=492, help='The y location of the name field in the template.')
    
    parser.add_argument('-xi','--x_ident', type=float, 
        default=100, help='The y location of the identification field in the template.')

    parser.add_argument('-yi','--y_ident', type=float, 
        default=610, help='The y location of the identification field in the template.')

    parser.add_argument('-nfs','--name_font_size', type=int, 
        default=80, help='Font size of the name column.')

    parser.add_argument('-ifs','--ident_font_size', type=int, 
        default=50, help='Font size identification column.')
    
    args = parser.parse_args()
    args_dict = vars(args)
    generate_certificates(**args_dict)

