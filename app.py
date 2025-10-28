from flask import Flask, render_template, request, redirect
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

    if request.method == 'POST':
        sql_query = request.form['sql_query']
        print(sql_query)

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
            conn.rollback()

    return render_template('index.html', records=records, columns=columns)

    # falta a exibição dos nomes das colunas (Gemini) + exibição de gráficos na pg edit.html


if __name__ == '__main__':
    app.run(debug=True)