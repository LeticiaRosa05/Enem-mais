import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def gerar_grafico_base64(records, columns, tipo_grafico='bar'):
    """
    Gera um gráfico a partir dos resultados da consulta e o retorna em Base64.
    
    :param records: Lista de tuplas com os dados do banco.
    :param columns: Lista de strings com os nomes das colunas.
    :param tipo_grafico: O tipo de gráfico a ser gerado ('bar' ou 'line' - padrão 'bar').
    :return: String Base64 formatada para uso direto na tag <img>.
    """
    if not records or len(columns) < 2:
        # Retorna uma imagem Base64 de um gráfico vazio ou uma string vazia
        # se os dados não forem suficientes para um gráfico.
        return "" 

    # 1. Preparar os dados
    try:
        df = pd.DataFrame(records, columns=columns)
        
        # Assume que a primeira coluna é a categoria (eixo X) e a segunda é o valor (eixo Y)
        # Você pode precisar de lógica mais complexa dependendo da sua query.
        x_label = columns[0]
        y_label = columns[1]
        x_data = df[x_label].astype(str).head(20) # Limita a 20 barras/pontos para visualização
        y_data = df[y_label].head(20)
        
    except Exception as e:
        print(f"Erro na preparação dos dados para o gráfico: {e}")
        return ""

    # 2. Gerar o gráfico (usando Matplotlib)
    plt.figure(figsize=(10, 6))
    
    if tipo_grafico == 'bar':
        plt.bar(x_data, y_data, color='#3498db')
    elif tipo_grafico == 'line':
        plt.plot(x_data, y_data, color='#2ecc71', marker='o')
    else:
        # Padrão para barras se o tipo for desconhecido
        plt.bar(x_data, y_data, color='#3498db')

    plt.title(f'Gráfico de {y_label} por {x_label}', fontsize=16)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.xticks(rotation=45, ha='right') # Rotação para nomes longos no X
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout() # Ajusta para evitar cortes de labels
    
    # 3. Salvar o gráfico em um buffer de memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close() # Fecha a figura para liberar memória
    
    # 4. Converter a imagem em string Base64
    buffer.seek(0)
    grafico_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    
    # Retorna o string Base64
    return f"data:image/png;base64,{grafico_base64}"
