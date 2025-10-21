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
    # Consulta os registros da tabela
    cursor.execute("SELECT * FROM enem_goias")
    records = cursor.fetchall()
    return render_template('index.html', records=records)

# Rota para exibir os registros conforme consulta na tabela
@app.route('/query', methods=['GET', 'POST'])
# Consulta os registros da tabela
def query():
    records = []

    if request.method == 'POST':
        sql_query = request.form['sql_query']
        print(sql_query)

        try:
            cursor.execute(sql_query)

            if sql_query.strip().upper().startswith('SELECT'):
                records = cursor.fetchall()
                print(f"Numero de registros: {len(records)}")
                print(f"Primeiros 5 registros {records[:5]}")
            else:
                conn.commit()
                print("Ação não commitada")
        except Exception as e:
            print(f"Erro ao executar a query: {e}")
            conn.rollback()

    return render_template('index.html', records=records)

# Rota para adicionar um novo registro
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Insere um novo registro na tabela
        cursor.execute("INSERT INTO enem_goias (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        
    return redirect('/')

# Rota para editar um registro existente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor.execute("SELECT * FROM enem_goias WHERE id = %s", (id,))
    record = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Atualiza o registro na tabela
        cursor.execute("UPDATE enem_goias SET name = %s, email = %s WHERE id = %s", (name, email, id))
        conn.commit()
        
        return redirect('/')
    
    return render_template('edit.html', record=record)

# Rota para excluir um registro
@app.route('/delete/<int:id>')
def delete(id):
    # Exclui o registro da tabela
    cursor.execute("DELETE FROM enem_goias WHERE id = %s", (id,))
    conn.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)