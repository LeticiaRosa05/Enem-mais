# Enem+

# Estrutura do html
- Os arquivos da interfaceweb estão localizados dentro da pasta templates/
- Há o [index.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/index.html), que é a homepage da aplicação e onde se pode conferir todos os dados do banco, assim como navegar para as páginas de consulta no banco de dados (por comando) e a página de gráficos para análise
- No [query_interface.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/query_interface.html) se encontra um campo de texto que envia a consulta inserida para o Python no back que, por sua vez, a executa no banco conectado e então retorna a tabela resultante para a interface web
- No [graphics_interface.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/graphics_interface.html) há também um campo para consultas SQL, mas ele retorna um gráfico (de linhas ou barras) gerado a partir das colunas e linhas retornadas pelo banco. Nele também estão 3 botões de páginas com gráficos prontos abordando comparação de médias, quantitativo de alunos com determinada nota e especificamente as maiores e menores notas em determinada matéria, sendo possível aplicar um filtro por cidade, nota de base e matéria de acordo com o disponível em cada página.
- Na página [graph_avg.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/graph_avg.html) encontra-se o gráfico acerca das médias gerais e das médias de redação por cidade, sendo que a média geral não engloba a nota da redação. É possível filtrar os resultados do gráfico por cidade;
- Na página [graph_essay.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/graph_essay.html) encontra-se o gráfico de quantidade de alunos que tiraram acima/abaixo de determinada nota por cidade. É possível filtrar por cidade, uma nota base e por matéria;
- Na página [graph_subj.html](https://github.com/LeticiaRosa05/Enem-mais/blob/main/templates/graph_subj.html) encontra-se o gráfico dos extremos (maior e menor) de nota por cidade. É possível filtrar por cidade e por matéria;

# Back-end
- O código Python responsável pela navegação entre as páginas, recebimento e execução das consultas, conexão com o banco e parametrização de gráficos é o [app.py](https://github.com/LeticiaRosa05/Enem-mais/blob/main/app.py), localizado no root do projeto
- O arquivo [graphics_functions.py](https://github.com/LeticiaRosa05/Enem-mais/blob/main/graphics_functions.py) é responsável pela função da geração dos gráficos, bem como toda ação necessária para lidar com alterações nos filtros (parametrização), especifiações de quantidade de barras/linhas a serem exibidas e o tipo de gráfico a ser gerado (barras/linhas)

# Execução da aplicação
- Pra executar localmente é necessária a configuração do flask e psyscopg2 no ambiente python, no caso em um ambiente virtual do VS Code do Anaconda Navigator, seguindo o passo a passo desse repositório: https://github.com/aasouzaconsult/Python_inserindo_dados_no_PostgreSQL
- Após a configuração do ambiente, como orientado no repositório, executar o comando ´´´python app.py´´´ no root do projeto
