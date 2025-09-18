import os
import json
from openai import OpenAI

# 1. Configurar a chave da API da OpenAI
# É altamente recomendado usar variáveis de ambiente por segurança.
# A variável de ambiente "OPENAI_API_KEY" deve conter sua chave.
client = OpenAI()

# 2. Definir o nome do arquivo de dados e o modelo
DATASET_FILE = 'dataset.jsonl'
MODEL_NAME = 'gpt-3.5-turbo' # Usamos 'gpt-3.5-turbo' como modelo base para o exercício

# 3. Inicializar contadores
total_requirements = 0
correct_classifications = 0

# Dicionário de tradução para normalizar as respostas do modelo
translation_map = {
    'funcional': 'functional',
    'não-funcional': 'non-functional'
}

# 4. Iniciar o processo de checagem
print(f"Iniciando a checagem de acurácia do modelo {MODEL_NAME}...")
print("-" * 50)

# Abrir o arquivo e processar linha por linha
with open(DATASET_FILE, 'r') as file:
    for line in file:
        try:
            # Carregar a linha como um objeto JSON
            data = json.loads(line)
            
            # Extrair o requisito e a classificação correta da nova estrutura do JSON
            requirement_text = data['messages'][1]['content']
            correct_label = data['messages'][2]['content'].lower().strip() # Normaliza para evitar erros de case
            
            # Construir o prompt para o modelo
            messages = [
                {"role": "system", "content": "You are a Software Engineer and need to categorize requirements into 'functional' or 'non-functional'. Your answer must be 'functional' or 'non-functional' only."},
                {"role": "user", "content": requirement_text}
            ]

            # Fazer a chamada à API da OpenAI
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.0 # Temperatura baixa para respostas mais determinísticas
            )

            # Obter a classificação do modelo e normalizá-la
            model_classification = response.choices[0].message.content.lower().strip()
            
            # --- CORREÇÃO APLICADA AQUI ---
            # Traduzir a classificação do modelo para inglês se necessário
            model_classification = translation_map.get(model_classification, model_classification)


            # Comparar a classificação do modelo com a correta
            total_requirements += 1
            is_correct = "INCORRETO"
            if model_classification == correct_label:
                correct_classifications += 1
                is_correct = "CORRETO"

            # Exibir o resultado para acompanhar o progresso
            print(f"Requisito: {requirement_text}")
            print(f"  Classificação do modelo: {model_classification}")
            print(f"  Classificação correta:   {correct_label}")
            print(f"  Resultado: {is_correct}\n")

        except (json.JSONDecodeError, IndexError, KeyError) as e:
            print(f"Erro ao processar uma linha ou estrutura JSON inválida: {e}")
            continue

# 5. Exibir os resultados finais
print("-" * 50)
print("Checagem de acurácia finalizada.")
print(f"Total de requisitos processados: {total_requirements}")
print(f"Classificações corretas: {correct_classifications}")

# Calcular e exibir a porcentagem
if total_requirements > 0:
    accuracy_percentage = (correct_classifications / total_requirements) * 100
    print(f"Acurácia do modelo {MODEL_NAME}: {accuracy_percentage:.2f}%")
else:
    print("Nenhum requisito foi processado.")