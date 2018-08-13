# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15
receber = salario + comissao

print('TOTAL = R$ {:.2f}'.format(receber))