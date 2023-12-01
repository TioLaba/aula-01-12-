# interface grafica

import PySimpleGUI as psg

import calcmulti
from calcmulti import soma


layout = _______[
             [psg.Text('informe N1'), psg.inputText(key= 'num1')],
             [psg.Text('informe N2'), psg.inputText(key= 'num2')],
             [psg.Text('****'), psg.Text('',key= "Total"), psg.Text('****')]
             [psg.Button('calcular'), psg.Button('limpar')],

           ]
janela = psg.Window("ola calculadora simples", layout)

while True:
    evento, valores = janela.read()
     if evento == psg.WIN_CLOSED:
         break
     elif evento == 'Limpar':
         janela['num1'].update('')
         janela['num2'].update('')
         janela['Total'].update('')
         janela['num1'].set_focus()
     else:
         n1 = int(valores['num1'])
         n2 = int(valores['num2'])
         janela['Total'].update(calcmulti.soma(num1, num2 ))

janela.close()

