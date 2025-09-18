🎯 O Desafio

O objetivo deste projeto foi aprimorar um modelo de linguagem para classificar requisitos de software como funcionais ou não-funcionais. Modelos de propósito geral, como o GPT-3.5, frequentemente falham em tarefas específicas, como evidenciado pela acurácia inicial de apenas 55.14% na nossa base de dados.

💡 A Solução

Para otimizar o desempenho, aplicamos a técnica de Fine-Tuning. Um conjunto de dados personalizado de requisitos já classificados foi preparado para treinar o modelo gpt-3.5-turbo, permitindo que ele aprendesse a reconhecer padrões e nuances do domínio de engenharia de software.

✅ Resultados

O Fine-Tuning foi altamente eficaz. A acurácia do modelo ajustado subiu de 55.14% para 91.59%, uma melhoria de mais de 36%. Este resultado demonstra que o treinamento com dados específicos é crucial para adaptar modelos de IA a tarefas de classificação complexas.

🛠️ Destaques Técnicos
Python: Linguagem principal para o desenvolvimento dos scripts de automação.

OpenAI API: Interface para interagir com os modelos de linguagem.

Fine-Tuning: Técnica central usada para otimizar o modelo base para a tarefa específica.

📂 Estrutura do Projeto
.
├── dataset.jsonl                  # Dados de teste e avaliação (107 requisitos)
├── dataset-train.jsonl            # Dados usados para o Fine-Tuning
├── check_accuracy.py              # Script para avaliar a acurácia do modelo
└── start_fine_tuning.py           # Script para iniciar o processo de Fine-Tuning
🚀 Como Rodar
Instale as dependências:

Bash

pip install openai
Configure sua chave da API da OpenAI:

Bash

export OPENAI_API_KEY='sua_chave_aqui'
Inicie o Fine-Tuning:

Bash

python start_fine_tuning.py
Após a conclusão, avalie o modelo:

Bash

python check_accuracy.py
✒️ Autor
[Seu Nome Completo]

Link para seu GitHub

📄 Licença
Este projeto está licenciado sob a Licença MIT.
Nota: Substitua os campos [Seu Nome Completo] e [Link para seu GitHub] com as suas informações. A seção de licença foi incluída como um lembrete para você adicionar a licença ao seu repositório.
