import csv 

lista = []

class InstrumentoOuGeneroInvalido(Exception):
    def __init__(self, message = 'Você deve no mínimo tocar um. '):
        self.message = message
        super().__init__(self.message)

def append_value(dict_obj, key, *value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        if value not in dict_obj[key]:
            dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]

dict_obj = {}

def cadastrar_instrumentos(item):
  if item == '':
    raise InstrumentoOuGeneroInvalido()
  else:
    lista.append(item)

def padronizar(texto, email=True):
  x = ""
  if email:
    if texto.count('@') != 1:
        texto = str(input("Digite o email novamente, com um @"))
    for i in texto:
      if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i == '@') or (i == '.') or (i == "_"):
        x += i
  else:
    for i in texto:
      if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i == ' '):
        x += i
  return x
  
email_inpt = input("Digite o seu email: ").lower()
if email_inpt not in lista:
  email = padronizar(email_inpt, email=True)
  nome_inpt = input("Digite o nome: ").title()
  nome = padronizar(nome_inpt, email=False)
  try:
    instrumento = input("Digite todos os instrumentos que você toca, separados por vírgulas. Se não toca nenhum, tecle enter. ")
    cadastrar_instrumentos(instrumento)
    try:
      generos = input("Digite todos os gêneros que você toca, separados por vírgulas. Se não toca nenhum, tecle enter.")
      cadastrar_instrumentos(generos)
      lista.append(email)
      lista.append(nome)
    except InstrumentoOuGeneroInvalido as excecao:
      instrumento = print("Que pena. Deve haver ao menos um. ")
  except InstrumentoOuGeneroInvalido as excecao:
      instrumento = print("Que pena. Deve haver ao menos um. ")
      
x = append_value(dict_obj, nome, lista)

with open('records.csv', 'w') as f:
  fieldnames = ['Nome', 'Email', 'Instrumento(s)', 'Gênero(s)']
  csv_writer = csv.writer(f, delimiter = '\t')
  csv_writer.writerow(fieldnames)
  for nome, values in dict_obj.items():
    csv_writer.writerow([nome, email, instrumento, generos])

f.close()