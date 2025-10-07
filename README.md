# 🏭 Simulador de Linha de Produção Industrial

![Streamlit](https://img.shields.io/badge/Feito%20com-Streamlit-red?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)

Este projeto é uma simulação interativa de uma linha de produção industrial, desenvolvida em Python com uma interface gráfica web criada usando a biblioteca Streamlit. O foco principal do projeto é a aplicação prática de estruturas de dados fundamentais, como Pilhas (Stacks) e Listas, para gerenciar o fluxo de produção e o histórico de produtos.

## ✨ Funcionalidades Principais

* **Simulação de Processo:** Acompanhe produtos passando por múltiplas etapas de produção (Corte, Montagem, Pintura, etc.).
* **Interface Gráfica Interativa:** Controle a simulação através de uma interface web amigável, adicionando novos produtos e processando a linha com cliques de botão.
* **Gerenciamento de Histórico com Pilha:** Cada produto possui seu próprio histórico de etapas, implementado com uma Pilha customizada. Isso permite a funcionalidade de "desfazer" etapas.
* **Busca e Ordenação:** Ferramentas na interface para ordenar o estoque de produtos finalizados por número de série e para buscar um produto específico.
* **Representação Visual:** Produtos no estoque são representados com sprites para uma visualização mais agradável.
* **Lógica de "Undo" Avançada:** A estrutura da Pilha foi implementada do zero e inclui uma funcionalidade de "desfazer o pop", permitindo restaurar um estado removido.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Streamlit
* **Estruturas de Dados:**
    * **Pilha (Stack):** Implementação customizada com Nós (Nodes) de uma lista duplamente encadeada, incluindo a funcionalidade de `undo_pop`.
    * **Dicionário:** Para gerenciamento eficiente de produtos em andamento.
    * **Lista:** Para armazenamento dos produtos finalizados.

## 📁 Estrutura do Projeto

O projeto está organizado nos seguintes arquivos de lógica:

* `stack.py`: Contém a implementação da classe `Node` e da classe `Stack`.
* `product.py`: Define a classe `Product`, que representa um item individual na produção.
* `production_line.py`: Contém a classe `ProductionLine`, que orquestra todo o fluxo de simulação.
* `simulador_streamlit.py`: O arquivo principal que constrói e executa a interface gráfica web.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar a simulação em sua máquina local.

### Pré-requisitos

* Python 3.10 ou superior instalado.
* `pip` (gerenciador de pacotes do Python).

### Passos para Instalação

1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio/project 
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows
    .\.venv\Scripts\activate

    # Ativar no macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` com o conteúdo abaixo e depois execute o comando de instalação.
    ```txt
    streamlit
    ```
    Agora, instale a partir do arquivo:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run simulador_streamlit.py
    ```
    *Se o comando acima não for encontrado, use a alternativa:*
    ```bash
    python -m streamlit run simulador_streamlit.py
    ```

A aplicação será aberta automaticamente no seu navegador padrão.

## 🖼️ Demonstração

![Interface principal da aplicação](https://i.imgur.com/lrW0Gs9.png)

![Funcionalidade de busca na barra lateral](https://i.imgur.com/pOz4qDT.png)


## ✒️ Autor

**João R.** - *Desenvolvedor do Projeto*
