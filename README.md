# HaveiBeenPwned_Consult
Consulta Automatizada via Python3 no site haveibeenpwned

Este script realiza uma pesquisa no site do Have I Been Pwned usando o endereço de e-mail fornecido. Ele simula uma solicitação do navegador adicionando um cabeçalho de agente de usuário para evitar a detecção como um bot. Em seguida, ele usa a biblioteca BeautifulSoup para analisar a resposta HTML e extrair as informações relevantes sobre violações de dados.

# Execução HaveiBeenPwned_Consult.py :
$python3 HaveiBeenPwned_Consult.py exemplo@gmail.com

-------------------------------------------------------------

# Execução CheckListEmails.py :
$python CheckListEmails.py

Este exemplo lê um arquivo de texto chamado "emails.txt" que contém uma lista de endereços de e-mail, um por linha. Em seguida, para cada e-mail na lista, o script executa a consulta no Have I Been Pwned como antes e imprime as informações relevantes sobre violações de dados, incluindo o endereço de e-mail verificado.
Certifique-se de que o arquivo de lista de e-mails que você deseja consultar esteja na mesma pasta do arquivo HaveiBeenPwned_Consult.
