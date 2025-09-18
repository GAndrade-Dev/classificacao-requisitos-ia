import os
from openai import OpenAI

# 1. Configurar a chave da API da OpenAI
# A variável de ambiente "OPENAI_API_KEY" deve conter sua chave.
# É altamente recomendado não expor a chave diretamente no código.
client = OpenAI()

# 2. Definir o nome do arquivo de treinamento e o e-mail (sufixo)
# ATENÇÃO: Substitua 'seu_email@dominio.com' pelo seu e-mail do Classroom.
TRAINING_FILE = 'dataset-train.jsonl'
SUFFIX_EMAIL = 'gabrielleandrade.gms@gmail.com'

# 3. Subir o arquivo de treinamento
print(f"Subindo o arquivo de treinamento: {TRAINING_FILE}...")
try:
    with open(TRAINING_FILE, "rb") as file:
        uploaded_file = client.files.create(
            file=file,
            purpose="fine-tune"
        )
    print(f"Arquivo subido com sucesso! ID do arquivo: {uploaded_file.id}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{TRAINING_FILE}' não foi encontrado.")
    print("Por favor, verifique se o arquivo está no mesmo diretório do script.")
    exit()

# 4. Criar o Job de Fine-Tuning
print("Criando o job de fine-tuning...")
try:
    fine_tuning_job = client.fine_tuning.jobs.create(
        training_file=uploaded_file.id,
        model="gpt-3.5-turbo",
        suffix=SUFFIX_EMAIL
    )
    print("Job de fine-tuning criado com sucesso!")
    print(f"ID do Job: {fine_tuning_job.id}")
    print(f"Status: {fine_tuning_job.status}")
    print("\nO treinamento foi iniciado. O modelo estará pronto quando o status for 'succeeded'.")
    print("Você pode monitorar o progresso usando o ID do Job na sua conta da OpenAI.")
except Exception as e:
    print(f"Ocorreu um erro ao criar o job de fine-tuning: {e}")