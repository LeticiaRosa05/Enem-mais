from flask import Flask, render_template, request, redirect
from graphics_functions import gerar_grafico_base64
import psycopg2

app = Flask(__name__, template_folder='templates')

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': '0000'
}

# Conexão com o banco de dados
conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

# Rota para exibir os registros da tabela
@app.route('/')
def index():
    columns = []
    # Consulta os registros da tabela
    cursor.execute("SELECT * FROM enem_goias")
    records = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return render_template('index.html', records=records, columns=columns)

# Rota para exibir os registros conforme consulta na tabela
@app.route('/query', methods=['GET', 'POST'])
# Consulta os registros da tabela
def query():
    records = []
    columns = []
    sql_query = ""

    if request.method == 'POST':
        sql_query = request.form.get('sql_query', '')
        sql_query = sql_query.strip()
        sql_query = sql_query.replace('\n', ' ').replace('\r', ' ')
        print(sql_query)

        if sql_query:
            try:
                cursor.execute(sql_query)

                if sql_query.strip().upper().startswith('SELECT'):
                    records = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]  # nomes das colunas
                    print(f"Colunas: {columns}")
                    print(f"Numero de registros: {len(records)}")
                    print(f"Primeiros 5 registros {records[:5]}")
                else:
                    conn.commit()
                    print("Ação não commitada")
                    cursor.execute("SELECT * FROM enem_goias")
                    records = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]
            except Exception as e:
                print(f"Erro ao executar a query: {e}")
                error_message = str(e)
                if "erro de sintaxe no fim da entrada" in error_message:
                    ultimos_caracteres = sql_query[-50:]
                    ascii_codes = [ord(c) for c in ultimos_caracteres]
                    print(f"Códigos Unicode do final da query: {ascii_codes}")
                    pass
                conn.rollback()

    return render_template('query_interface.html', records=records, columns=columns)

#Página de geração de gráficos
@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    records = []
    columns = []
    grafico_data = ""
    sql_query = ""
    error_message = ""

    # 1. Processar a query recebida via POST/Formulário
    if request.method == 'POST':
        sql_query = request.form.get('sql_query', '').strip()
        tipo_grafico = request.form.get('tipo_grafico', 'bar') # tipo de gráfico
        
        if sql_query and sql_query.upper().startswith('SELECT'):
            try:
                cursor.execute(sql_query)
                records = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                if records:
                    grafico_data = gerar_grafico_base64(records, columns, tipo_grafico)
                
            except Exception as e:
                error_message = f"Erro ao executar a query. Verifique se a consulta retorna duas colunas de dados. Erro: {e}"
                print(error_message)
                conn.rollback()

    return render_template('graphics_interface.html', records=records, columns=columns, grafico=grafico_data, sql_query_antiga=sql_query, error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
