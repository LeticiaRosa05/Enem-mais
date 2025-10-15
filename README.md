# Enem+

# Estrutura do html
- No index.html, dentro dos '```<form action="/add" method="POST">```' estão as ações a serem executadas, que são a adição, edição e exclusão de um nome + email no banco
- As ações /add, /consulta, /edit e /delete que estão no index.html estão descritas no app.py, assim como as consultas que elas fazem no banco
- A entrada de uma consulta do usuário ainda ta sendo feita, mas ela já está em desenvolvimento, comentada nas linhas de 27 a 33 no app.py

# Execução do site
- Pra executar ele localmente precisa da configuração do flash e psyscopg2 no ambiente python, no caso to rodando ela com um ambiente virtual do VS Code do Anaconda Navigator, seguindo esse repositório: https://github.com/aasouzaconsult/Python_inserindo_dados_no_PostgreSQL

# Visualização/funções do site
- As imagens do site estão na pasta img
- A 1 imagem mostra o visual
- A 2 mostra um exemplo de adição de email + nome
- A 3 é dps de clicar em add, ou seja, os dados foram inseridos na tabela e agora vai ter +1 linha
- A 4 é um exemplo de clicar no "Editar" de um dos registros
- A 5 é após clicar em salvar. O site volta pra home e o registro foi alterado
- Como explicado na estrutura, o campo de consulta ainda n ta funcional, mas tem um esboço dele no app.py
