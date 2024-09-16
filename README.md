# Hotel Reservations Classifier - AWS Machine Learning API

![_0b962214-baa7-4c7a-bdfc-cae9da277c00](https://github.com/user-attachments/assets/3a1ca14c-c5b3-4ef5-9c7e-1540f3da4b81)

## Tópicos
* [Descrição do Projeto](#descricao-do-projeto)
* [Retorno da API](#retorno-da-api)
* [Estrutura de Pastas](#estrutura-de-pastas)
* [Arquitetura AWS](#arquitetura-aws)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Dificuldades Superadas](#dificuldades-superadas)
* [Como Clonar](#como-clonar)
* [Autores](#autores)

---

<div id='descricao-do-projeto'/>

## Descrição do Projeto

Nossa equipe desenvolveu um modelo treinado utilizando SageMaker para classificar os dados do [Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset), a fim de categorizar as reservas de acordo com a faixa de preço por quarto. Para isso, foi criado um banco de dados AWS RDS em MySQL para armazenar as tabelas necessárias.

Além disso, foi desenvolvida uma API em Python que carrega o modelo treinado armazenado no Amazon S3 e expõe um endpoint para realizar a inferência. Esse endpoint recebe informações de uma reserva e retorna a previsão de classificação de preço da reserva.

### Implementação

1. **Criação de dataset no RDS MySQL**
2. **Treinamento do modelo no SageMaker**
3. **Armazenamento do modelo no S3**
4. **Desenvolvimento da API**
5. **Deploy da API em EC2 AWS com Docker**

---

<div id='retorno-da-api'/>

# Retorno da API


---

<div id='estrutura-de-pastas'/>

# Estrutura de Pastas

```sh
├── assets/
├── data/
│    ├── processed/
│    └── raw/
├── model/
│    └── training/
├── src/
│    ├── conexao_modelo/
│    ├── config/
│    └── projeto/
│        └──projeto/
│    └── main.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── README.md
```

---

<div id='arquitetura-aws'/>

# Arquitetura AWS


---

<div id='tecnologias-utilizadas'/>

# Tecnologias Utilizadas (com versao.)

| ![AWS SageMaker](https://img.shields.io/badge/aws_sagemaker-006400.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) | ![AWS RDS](https://img.shields.io/badge/aws_rds-527FFF.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) | ![AWS S3](https://img.shields.io/badge/aws_s3-569A31.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) |
|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|
| **Versão**: ...                     | **Versão**: MySQL 8.0.35            | **Versão**: ...                |

| ![FastAPI](https://img.shields.io/badge/fastapi-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white) | ![Docker](https://img.shields.io/badge/docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white) | ![Python](https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white) |
|:--------------------------------:|:-------------------------------:|:-----------------------------:|
| **Versão**: ...               | **Versão**: ...              | **Versão**: ...             |



---

<div id='dificuldades-superadas'/>

# Dificuldades Superadas

| **Problema** | **Solução** |
|-----------|---------|
| Alimentação do Banco | Encontramos dificuldades relacionadas à permissão ao tentar carregar arquivo .csv usando o comando `LOAD DATA INFILE`. Como alternativa, optamos por alimentar o banco de dados manualmente. |
| ... | ... |
| ... | ... |

---

<div id='como-clonar'/>

# Como Clonar

1. **Clone o repositorio.**
   - No terminal, execute o comando abaixo para clonar a branch específica do projeto:
```
git clone --branch grupo-3 https://github.com/Compass-pb-aws-2024-JULHO-A/sprints-4-5-pb-aws-julho-a.git
```

---

<div id='autores'>

# Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/AntonioRian">
        <img src="https://avatars.githubusercontent.com/u/114035144?v=4" width="100px;" alt=""/><br>
        <sub>
          <b>Antonio Rian de Jesus Felix</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gabalencar">
        <img src="https://avatars.githubusercontent.com/u/102690558?v=4" width="100px;" alt=""/><br>
        <sub>
          <b>Gabriel Alencar Gomes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/KalylSemi">
        <img src="https://avatars.githubusercontent.com/u/157990287?v=4" width="100px;" alt=""/><br>
        <sub>
          <b>Kalyl Semi Diab</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Leititcia">
        <img src="https://avatars.githubusercontent.com/u/130941056?v=4" width="100px;" alt=""/><br>
        <sub>
          <b>Leticia Pereira do Vale</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
