import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def gerar_grafico_base64(records, columns, tipo_grafico='bar'):
    if not records or len(columns) < 2: # Casjo haja menos de 2 colunas, retorna um gráfico vazio
        return "" 

    try:
        df = pd.DataFrame(records, columns=columns)
        grafico_gerado = False

    except Exception as e:
        print(f"Erro na preparação dos dados para o gráfico: {e}")
        return ""

    if len(columns) == 2:

        # Assume que a primeira coluna é a categoria (eixo X) e a segunda é o valor (eixo Y)
        x_label = columns[0]
        y_label = columns[1]
        x_data = df[x_label].astype(str).head(20) # Limita a 20 barras/pontos para visualização

        try:
            y_data = df[y_label].astype(float).head(20)
        except ValueError as ve:
            print(f"Erro: Dados na coluna '{y_label}' não são numéricos. {ve}")
            return ""

        # Gráfico de barra/linha simples
        plt.figure(figsize=(10, 6))
        
        if tipo_grafico == 'bar':
            plt.bar(x_data, y_data, color='#3498db')
        elif tipo_grafico == 'line':
            plt.plot(x_data, y_data, color='#2ecc71', marker='o')
        else:
            plt.bar(x_data, y_data, color='#3498db')

        plt.title(f'Gráfico de {y_label} por {x_label}', fontsize=16)
        plt.xlabel(x_label, fontsize=12)
        plt.ylabel(y_label, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        grafico_gerado = True


    elif len(columns) >= 3:
        # Colunas 1 (série A) e 2 (série B) contra coluna 0 (eixo X)
        x_label = columns[0]
        y1_label = columns[1]
        y2_label = columns[2]
        
        x_data = df[x_label].astype(str).head(10)

        try:
            y1_data = df[y1_label].astype(float).head(10)
            y2_data = df[y2_label].astype(float).head(10)
        except ValueError as ve:
            print(f"Erro: Dados nas colunas '{y1_label}' ou '{y2_label}' não são numéricos. {ve}")
            return ""

        # Gráfico de Barras Agrupadas
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Verificação do tipo de gráfico escolhido
        if tipo_grafico == 'bar':
            # Posições das barras
            bar_width = 0.35
            r1 = range(len(x_data))
            r2 = [x + bar_width for x in r1]
            
            ax.bar(r1, y1_data, color='#3498db', width=bar_width, edgecolor='grey', label=y1_label)
            ax.bar(r2, y2_data, color='#e74c3c', width=bar_width, edgecolor='grey', label=y2_label)

            ax.set_xticks([r + bar_width/2 for r in range(len(x_data))])
            ax.set_xticklabels(x_data, rotation=45, ha='right')
            
            plt.title(f'Comparação de {y1_label} e {y2_label} (Barras) por {x_label}', fontsize=16)

        elif tipo_grafico == 'line':
            # Plotagem das duas linhas
            ax.plot(x_data, y1_data, color='#3498db', marker='o', label=y1_label)
            ax.plot(x_data, y2_data, color='#e74c3c', marker='s', label=y2_label)
            
            ax.set_xticks(range(len(x_data)))
            ax.set_xticklabels(x_data, rotation=45, ha='right')
            
            plt.title(f'Comparação de {y1_label} e {y2_label} (Linhas) por {x_label}', fontsize=16)

        plt.xlabel(x_label, fontsize=12)
        plt.ylabel('Contagem / Valor', fontsize=12)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        grafico_gerado = True


    if grafico_gerado:
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        buffer.seek(0)
        grafico_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()

        return f"data:image/png;base64,{grafico_base64}"