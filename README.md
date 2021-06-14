# Certificates generator
Automate certificate generator

## Table of content

- [Requeriments](#requeriments)
- [List of arguments available](#list-of-arguments-available)
- [How to use](#how-to-use)

## Requeriments
- python
- os
- pandas
- PIL

## List of arguments available

Argument| Description
:------:|:-----------:
-h, --help | show this help message and exit
-c, --csvfile | The rute of the csv file.
-t, --template | The certificate template in pdf format.
-o, --outformat | The output format can be pdf, png or jpeg.
-n, --namecol | Field column name of the person.
-i, --identcol | Field column name of the identification.
-x, --xlocation | The x location in the axis X of the start of the name.
-y, --ylocation | The x location in the axis Y of the start of the name.
-f, --fontSize | Font size.

## How to use

```python
  python main.py -d "name.csv" -t "certificate.jpg" -n "name" -i "identification" -t "hours"
```
