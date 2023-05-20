from fastapi import FastAPI
from controllers.models_controller import models_router

# Cria a instância
app = FastAPI()
# Adiciona as rotas para cada entidade
app.include_router(models_router)

# dataset = load_dataset_from_link('https://drive.google.com/uc?export=download&id=1DUtezZYuhaYJCagw4yfcRRfDsEbYB3-9')
# dataset_data = configure_dataset_data(dataset)

# model = load_saved_model('./data/teste_escola.h5')

# pred = predict(
#     img_url="https://drive.google.com/uc?export=download&id=1Toa5h34w0nVqseIoEhwitxurM_gWcJRQ",
#     model=model,
#     class_names=dataset_data["class_names"])


@app.get('/')
async def asdf():
    return {"data": "ASDF"}
