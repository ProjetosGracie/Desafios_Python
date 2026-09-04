# 📦 Sistema de Controle de Produtos

Sistema desenvolvido em **Python** para realizar o cadastro e o controle básico de produtos, permitindo armazenar informações, consultar dados, registrar vendas e acompanhar a situação do estoque.

O projeto utiliza principalmente **listas, dicionários, funções, estruturas de repetição e estruturas condicionais**, sendo uma aplicação prática dos conceitos fundamentais da linguagem Python.

---

## 🎯 Objetivo

O objetivo do sistema é facilitar o **controle de produtos e estoque**, permitindo que o usuário cadastre produtos e acompanhe suas informações de forma simples através de um menu interativo.

O sistema pode ser utilizado como base para aplicações maiores de gerenciamento de estoque.

---

## ⚙️ Funcionalidades

O sistema possui um menu principal com as seguintes opções:

### 1. 📝 Armazenar

Permite cadastrar um novo produto informando:

* Código do produto
* Nome
* Preço
* Quantidade em estoque

Cada produto é armazenado como um **dicionário** dentro de uma **lista**.

Exemplo:

```python
produto = {
    "codigo": codigo,
    "nome": nome,
    "preco": preco,
    "estoque": estoque
}
```

---

### 2. 📋 Dados

Exibe os dados dos produtos cadastrados no sistema.

Para cada produto são apresentados:

* Código
* Nome
* Preço
* Estoque

O sistema utiliza um loop `for` para percorrer a lista de produtos e os itens de cada dicionário.

---

### 3. 💰 Vendas

Permite registrar a venda de um produto.

O usuário informa o nome do produto vendido e a quantidade de unidades. O sistema então atualiza automaticamente a quantidade disponível no estoque.

Exemplo:

```python
produto["estoque"] = produto["estoque"] - vendidos
```

---

### 4. 📦 Estoque

Permite verificar a situação do estoque de cada produto.

O sistema classifica o estoque em três situações:

| Quantidade  | Situação         |
| ----------- | ---------------- |
| `0`         | ❌ Sem estoque    |
| `1 a 3`     | ⚠️ Estoque baixo |
| `4 ou mais` | ✅ Estoque normal |

Isso permite identificar rapidamente quais produtos precisam de reposição.

---

### 5. 🚪 Encerrar

Finaliza a execução do sistema e apresenta a mensagem:

```text
Sistema Encerrado
```

---

## 🧠 Conceitos de Python utilizados

O projeto foi desenvolvido utilizando conceitos fundamentais de programação:

* **Listas**
* **Dicionários**
* **Funções**
* **Laços de repetição `for` e `while`**
* **Estruturas condicionais `if`, `elif` e `else`**
* **Entrada de dados com `input()`**
* **Conversão de tipos com `int()` e `float()`**
* **Manipulação de listas com `.append()`**
* **Percorrimento de dicionários com `.items()` e `.values()`**
* **F-strings para formatação de informações**
* **Modularização através de funções**

---

## 🗂️ Estrutura do projeto

O sistema é organizado em funções responsáveis por diferentes partes da aplicação:

```text
Sistema de Controle de Produtos
│
├── produtos
│   └── Lista responsável por armazenar os produtos
│
├── menu()
│   └── Exibe e controla o menu principal
│
├── inicio()
│   └── Realiza o cadastro dos produtos
│
├── dadosProduto()
│   └── Exibe os dados dos produtos
│
├── vendas()
│   └── Registra vendas e atualiza o estoque
│
└── informarEstoque()
    └── Verifica a situação do estoque
```

---

## 💻 Exemplo de utilização

Ao executar o programa, o usuário encontra o seguinte menu:

```text
--------MENU--------
1 - ARMAZENAR
2 - DADOS
3 - VENDAS
4 - ESTOQUE
5 - ENCERRAR

Digite a opcao:
```

O usuário pode escolher uma das opções para realizar as operações de controle dos produtos.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **VS Code** ou outro editor de código
* Terminal/Console para execução

---

## 📚 Finalidade acadêmica

Este projeto foi desenvolvido com finalidade **acadêmica**, como forma de praticar conceitos de programação em Python e desenvolver uma aplicação simples de **controle de produtos e estoque**.

A proposta permite aplicar conceitos teóricos em uma situação prática, simulando funcionalidades encontradas em sistemas comerciais de gerenciamento de estoque.

---

## 👨‍💻 Desenvolvedor

Projeto desenvolvido como parte dos estudos de **Programação em Python**, com foco em estruturas de dados e desenvolvimento de sistemas de controle.

---

⭐ Projeto criado para colocar em prática os fundamentos de **Python, listas, dicionários e lógica de programação**.
