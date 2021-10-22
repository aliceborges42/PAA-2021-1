from urllib.request import urlopen
from bs4 import BeautifulSoup

urls = [
          # Links da Alícia
          'https://coronavirus.jhu.edu/',
          'https://noticias.unb.br/',
          'http://coronavirus.df.gov.br/',
          'https://www.gov.br/pt-br',
          'https://www.paho.org/pt',
          'https://www.saude.df.gov.br/',
          'https://www.unasus.gov.br/',
          'https://unbciencia.unb.br/',
          'https://pt.wikipedia.org/wiki/COVID-19',
          'https://pt.wikipedia.org/wiki/Coronav%C3%ADrus',
          # Links do Caio
          'https://pt.wikipedia.org/wiki/Matrix',
          'https://pt.wikipedia.org/wiki/Star_Wars',
          'https://pt.wikipedia.org/wiki/Indiana_Jones',
          'https://pt.wikipedia.org/wiki/Back_to_the_Future',
          'https://pt.wikipedia.org/wiki/The_Terminator',
          'https://pt.wikipedia.org/wiki/O_Senhor_dos_An%C3%A9is',
          'https://pt.wikipedia.org/wiki/Harry_Potter',
          'https://pt.wikipedia.org/wiki/The_Shining',
          'https://pt.wikipedia.org/wiki/The_Dark_Knight',
          'https://pt.wikipedia.org/wiki/It_(2017)',
					# Links da Bebé
					'https://www.tencent.com/en-us',
					'https://pt.wikipedia.org/wiki/Samsung',
					'https://www.cisco.com/c/pt_br/about.html',
					'https://pt.wikipedia.org/wiki/Microsoft',
					'https://pt.wikipedia.org/wiki/Dell',
					'https://www.apple.com/br/',
					'https://www.intel.com/content/www/us/en/homepage.html',
					'https://abc.xyz/',
					'https://www.ibm.com/br-pt',
					'https://www.oracle.com/br/index.html',
          # Links da Alice
          'https://pt.wikipedia.org/wiki/Bororos',
          'https://pt.wikipedia.org/wiki/Tupiniquins',
          'https://pt.wikipedia.org/wiki/Caingangues',
          'https://pt.wikipedia.org/wiki/Ianom%C3%A2mis',
          'https://pt.wikipedia.org/wiki/Guaranis',
          'https://pt.wikipedia.org/wiki/Charruas',
          'https://pt.wikipedia.org/wiki/Tupinamb%C3%A1s',
          'https://pt.wikipedia.org/wiki/Caiap%C3%B3s',
          'https://pt.wikipedia.org/wiki/Guat%C3%B3s',
          'https://pt.wikipedia.org/wiki/Ticunas',
          # Links do Bruno
          'https://pt.wikipedia.org/wiki/Esporte_no_Brasil',
          'https://pt.wikipedia.org/wiki/Voleibol',
          'https://pt.wikipedia.org/wiki/Basquetebol',
          'https://pt.wikipedia.org/wiki/Voleibol_de_praia',
          'https://pt.wikipedia.org/wiki/Basquetebol_em_cadeira_de_rodas',
          'https://pt.wikipedia.org/wiki/Voleibol_do_Brasil',
          'https://pt.wikipedia.org/wiki/Futebol',
          'https://pt.wikipedia.org/wiki/Futebol_feminino',
          'https://pt.wikipedia.org/wiki/Futebol_nos_Jogos_Ol%C3%ADmpicos',
          'https://pt.wikipedia.org/wiki/Federa%C3%A7%C3%A3o_Internacional_de_Futebol'
	# Links do William
	   'https://pt.wikipedia.org/wiki/Acre'
           'https://pt.wikipedia.org/wiki/Alagoas'
	   'https://pt.wikipedia.org/wiki/Sergipe'
	   'https://pt.wikipedia.org/wiki/Tocantins'
	   'https://pt.wikipedia.org/wiki/Distrito_Federal_(Brasil)'
	   'https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(estado)'
	   'https://pt.wikipedia.org/wiki/Bahia'
	   'https://pt.wikipedia.org/wiki/Amazonas'
	   'https://pt.wikipedia.org/wiki/Para'
	   'https://pt.wikipedia.org/wiki/Rondonia'
	   'https://pt.wikipedia.org/wiki/Roraima'	
       ]

# Abrir arquivo
f = open('seeds.rb', 'w')

f.write("Document.destroy_all\n")

for url in urls:
  html = urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Recuperar titulo
  for title in soup.find_all('title'):
    title = title.get_text()

  # Retirar conteudo desnecessário
  for script in soup(["script", "style"]):
    script.extract()

  # Recuperar conteudo da pagina
  text = soup.get_text()

  # Quebrar conteúdo em linhas e tirar espaço desnecessário
  lines = (line.strip() for line in text.splitlines())

  # Quebrar em blocos
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

  # Retirar linhas vazias
  text = '\n'.join(chunk for chunk in chunks if chunk)

  # retirar aspas duplas e simples
  text = text.replace("'", "")
  text = text.replace('"', '')

  string = f"Document.create!(url: '{url}', title: '{title}', body: '{text}');\n"
  f.write(string)

f.close()
