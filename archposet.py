#! /usr/bin/env python

#Created by Achierp
#Contact:archlinux@gmail.com
#
#This file is part of Foobar.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Includes
import os
import sys

sys.path.append('Func/') 
sys.path.append('Library/') 
from functions import ficheiro, instalar, check_system, database, user, start_check
from termcolor import colored, cprint
os.system("clear")
linha =  colored("-"*30, 'blue')
ans=True
erro=""
db= database()
utilizador=user()
global dbselected 
dbselected=""

while ans:
	os.system("clear")
	start_check()
	valor1=("valor 1 ")
	valor2=("valor 2 ")
	#print("menu1 %-20s menu2 %10s" % (valor1, valor2))
	print (colored("\nMenu", 'white' , attrs=['bold']))
	menu = ["Utilizadores [Done]","GitHub [Done]","Drivers","Applications","Clear Orpans [Done]"]
	print (linha)
	for i in range(len(menu)):
		print(colored(i , 'yellow') ,menu[i])
	print (erro)

	print ("x) Sair")
	erro= ""
	ans=input("\nWhat would you like to do? ")
	if ans=="0":
		erro= ""
		os.system("clear")
		utilizador.list()
		print("\n"+ linha)
		users = ["Add User","Remove User","Back"]
		for i in range(len(users)):
			print(colored(i , 'yellow') ,users[i]) 
		print (erro)
		ans=input("\nWhat would you like to do? ")
		if ans=="0":
			utilizador.add()
			#text=input(colored("\nMenu principal ", 'green' ) + "<enter>"))
		elif ans=="1":
			 utilizador.remove()
			 text=input("")
		elif ans== "2":
			pass

	elif ans=="1":
		print("\n GitHub") 
		os.system("clear")
		print(linha+(colored("GitHub: ", 'cyan', attrs=['bold']))+linha)
		instalar('xclip git', 'pacman')
		os.system("clear")
		print((colored("GitHub: ", 'cyan', attrs=['bold'])))
		rsp="no"
		while rsp == "no":
			github_utilizador=input(colored('\nGitHub','yellow') + colored('@', 'red') + 'Nome:')
			github_email=input(colored('GitHub','yellow') + colored('@', 'red') +  'Email:')
			confirm=input("Confirmar? yes/no/(Back = b)")
			if confirm == "yes":
				if all([github_email, github_utilizador]):
					input("Nome de utilizador ou Email!")
					#os.system('git config --global user.email ' + github_email )
					#os.system('git config --global user.name ' + github_utilizador )
					break
				else:
					input("Nome de utilizador ou Email vazios!")
					pass
			elif confirm == "b":
				pass
		exit=input(colored("\nMenu principal ", 'green' ) + "<enter>")
	elif ans=="2":
		print("\n Drivers\n Cheking system... VGA graphics") 
		check_system()
		input("Done chipset")
	elif ans=="3":
		rsp="no"
		while rsp == "no":
			os.system("clear")
			#rsp=input("Create[Done],read [Done], insert[Done] ,remove[Done], install[Done](1,2,3,4,5)")
			print (colored("\nMenu Base de dados", 'white' , attrs=['bold']))
			if dbselected:
				print ("Base de dados - " + colored(dbselected, 'red') )
				submenu_dbselected = ["Read - ", "Add - ", "Remove - ", "Instalar  "]
				submenu2_dbselected = ["Ler apps", "Adicionar programas", "Remover apps", "Instalar apps"]

				print (linha)
				for i in range(len(submenu_dbselected)):
					print(colored(submenu_dbselected[i] , 'yellow')+ colored(submenu2_dbselected[i] , 'white'))
				print (erro)

			basededados=os.listdir("Databases/")
			submenu = ["Selecionar Base de dados", "Criar Nova base de Dados", "Voltar"]
			print (linha)
			for i in range(len(submenu)):
				print(colored(i , 'yellow') ,submenu[i])
			print (erro)
			print ("Remover Base de dados")
			print ("x) Sair")
			rsp=input("Opcao:")
			if rsp == "0":
				print (colored("\nSelecionar Base de dados", 'white' , attrs=['bold']))
				basededados=os.listdir("Databases/")
				print (linha)
				for i in range(len(basededados)):
					print(colored(i , 'yellow') ,basededados[i])
				print (erro)
				selbd=int(input("Base de dados numero:"))
				if basededados[selbd] in basededados: 
					dbselected=basededados[selbd]
					rsp ="no"
				else:
					input("Numero  incorrecto!!!")

			elif rsp == "1":
				db.create()
			elif rsp == "Add":
				tabela= db.readtabelas(dbselected)
				apps_add=input("Applicacoes a adicionar (ex:thunar fman etc): ")
				apps=db.add(dbselected, tabela, apps_add)
				rsp ="no"
			elif rsp == 'Read':
				tabela= db.readtabelas(dbselected)
				apps=db.read(dbselected, tabela)
				rsp ="no"
			elif rsp == 'Remove':
				tabela= db.readtabelas(dbselected)
				apps=input("Applicacoes a remover:")
				apps = db.remove(dbselected, tabela, apps)
				rsp ="no"
			elif rsp == 'Instalar':
				tabela= db.readtabelas(dbselected)
				apps = db.instalar(dbselected, tabela)
				rsp ="no"
	elif ans=="4":
		utilizador.clean()
	elif ans=="x":
		print("\n Goodbye")
		ans = None 
	elif ans !="":
		#os.system("clear")
		erro =(colored('Opção não válida', 'red', attrs=['bold']))
