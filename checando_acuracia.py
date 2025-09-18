import os
import json
from openai import OpenAI

# A variável de ambiente "OPENAI_API_KEY" deve conter sua chave.
client = OpenAI()

# --------------------
# 1. Configuração do Modelo e do Arquivo de Teste
# ATENÇÃO: Substitua 'nome_do_seu_novo_modelo' pelo nome completo do seu modelo fine-tuned
# que você recebeu por email.
# --------------------
MODEL_NAME = "ft:gpt-3.5-turbo-0125:personal:gabrielleandrade-gms-gmail-com:CH8bwOZc"
TEST_FILE = "dataset.jsonl"
print(f"Iniciando a checagem de acurácia do modelo {MODEL_NAME}...")

# 2. Função para classificar um requisito
def classify_requirement(requirement_text, model_name):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a Software Engineer and need to categorize requirements into 'functional' or 'non-functional'. Your answer must be 'functional' or 'non-functional' only."},
                {"role": "user", "content": requirement_text}
            ],
            temperature=0
        )
        classification = response.choices[0].message.content.strip().lower()
        return classification
    except Exception as e:
        print(f"Erro ao classificar o requisito: {e}")
        return None

# 3. Carregar os dados de teste
with open(TEST_FILE, 'r', encoding='utf-8') as f:
    test_data = [json.loads(line) for line in f]

# 4. Checar a acurácia
correct_classifications = 0
total_requirements = len(test_data)

for entry in test_data:
    requirement = entry['messages'][1]['content']
    correct_classification = entry['messages'][2]['content'].lower()

    # Classificar com o modelo fine-tuned
    model_classification = classify_requirement(requirement, MODEL_NAME)

    print("-" * 50)
    print(f"Requisito: {requirement}")
    print(f"  Classificação do modelo: {model_classification}")
    print(f"  Classificação correta:     {correct_classification}")

    if model_classification == correct_classification:
        correct_classifications += 1
        print("  Resultado: CORRETO")
    else:
        print("  Resultado: INCORRETO")

# 5. Calcular e imprimir a acurácia final
accuracy = (correct_classifications / total_requirements) * 100 if total_requirements > 0 else 0

print("-" * 50)
print("Checagem de acurácia finalizada.")
print(f"Total de requisitos processados: {total_requirements}")
print(f"Classificações corretas: {correct_classifications}")
print(f"Acurácia do modelo {MODEL_NAME}: {accuracy:.2f}%")