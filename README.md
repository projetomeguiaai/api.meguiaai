# Me Guia.AI API
API criada para classificação de imagens com Tensorflow e FastAPI do projeto científico Me Guia.AI do FESTEC V

## Tecnologias utillizadas
- Python
- FastAPI
- Tensorflow & Keras

## Modo de rodar
Requisitos:
- Python 3.10 >
- pip 23.1.2 >
- poetry (latest)

Primeiramente, clone o repositório `https://github.com/victor-renan/api.meguiaai`

Em seguida, instale o `poetry` para instalar os pacotes e gerenciar os envs

Após isso, entre no diretório do projeto com `cd api.meguiaai` e digite `poetry install`

Ao instalar, digite `poetry shell` e em seguida `uvicorn --reload src/app:app --port 5000`


*Valeu!*
