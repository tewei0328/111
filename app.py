# -*- coding: utf-8 -*-
"""line-notify-text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FiovhzFGpH5VAOVI2pbHCNi_e_G6UJsH
"""

!pip install lineTool

!pip install lineTool

import lineTool

token="N737HRc9YYFNCRNlcai7OPIU1NkvDroc5EXCooi0XlUxxx"

def linePush(msg):
    lineTool.lineNotify(token, msg)

lineTool.lineNotify(token, 'hello')

lineTool.lineNotify(token, '1111')

linePush(222)