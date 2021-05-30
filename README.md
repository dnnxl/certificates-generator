# certificates-generator
Automate certificate generator

How to use
optional arguments:
  -h, --help            show this help message and exit
  -c CSVFILE, --csvfile CSVFILE
                        The rute of the csv file.
  -t TEMPLATE, --template TEMPLATE
                        The certificate template in pdf format.
  -o OUTFORMAT, --outformat OUTFORMAT
                        The output format can be pdf, png or jpeg.
  -n NAMECOL, --namecol NAMECOL
                        Field column name of the person.
  -i IDENTCOL, --identcol IDENTCOL
                        Field column name of the identification.
  -x XLOCATION, --xlocation XLOCATION
                        The x location in the axis X of the start of the name.
  -y YLOCATION, --ylocation YLOCATION
                        The x location in the axis Y of the start of the name.
  -f FONTSIZE, --fontSize FONTSIZE
                        Font size.
                        
> python main.py -c "name.csv" -t "certificate.png" -o "pdf" -n "name" -x 133 -y 665 -f 80
