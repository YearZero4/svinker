import os, pyfiglet
from time import sleep as t
from colorama import Fore, Style, init
init(autoreset=True)
nf='xmksh.txt'
def svinker():
 so=os.name
 if so == 'nt':
  os.system("cls")
 else:
  os.system("clear")
 r=pyfiglet.figlet_format("Svinker")
 print(f"{Fore.RED}{Style.BRIGHT}{r}")
 
 def textbin(texto):
  return ' '.join(format(ord(c), '08b') for c in texto)

 def bintext(binario):
  binario = binario.replace(" ", "")
  while len(binario) % 8 != 0:
   binario = '0' + binario

  texto = ''
  for i in range(0, len(binario), 8):
   byte = binario[i:i + 8]
   decimal = int(byte, 2)
   texto += chr(decimal)
  return texto

 print(f"""
  {Fore.WHITE}{Style.BRIGHT}[1] {Fore.RED}Binario a texto
  {Fore.WHITE}[2] {Fore.RED}Texto a Binario
  """)

 opc = input("Seleccionar Opcion -> ")

 x0=[]
 if opc == "1":
  x = input("Binario -> ")
  y = bintext(x)
  x0.append(y)
 elif opc == "2":
  x = input("Texto -> ")
  y = textbin(x)
  x0.append(y + ' ')
 else:
  print(f"\n{Fore.WHITE}{Style.BRIGHT}Opcion Invalida...")
  t(3)
  svinker()

 for i in x0:
  with open(nf, 'w') as f:
   f.write(i)
  if os.path.exists(nf):
   with open(nf, 'r') as v:
    ver=v.read()
    print(f"\n{Fore.RED}{Style.BRIGHT}{ver}")
   print(f"\nGuardado en -> {Fore.WHITE}{Style.BRIGHT}{nf}")

 input("\nPresione [ENTER] para continuar")
 svinker()
svinker()
