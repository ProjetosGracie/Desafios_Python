# ☕ Sistema de Pedidos de Cafeteria

Um sistema simples e interativo em Python para calcular o valor de pedidos de bebidas, aplicando regras de negócio como descontos para estudantes e brindes promocionais.

## 🎯 Sobre o Projeto
Este projeto foi desenvolvido para automatizar o cálculo de valores em uma cafeteria. O sistema recebe os dados do cliente, o tipo de bebida, o tamanho e a quantidade, e retorna um resumo detalhado do pedido, incluindo o valor bruto, descontos aplicados, valor final e a elegibilidade para brindes.

## ⚙️ Funcionalidades
- Cálculo dinâmico de preço com base na bebida e no tamanho.
- Aplicação automática de **10% de desconto** para alunos FIAP em pedidos acima de R$ 15,00.
- Verificação automática de **brinde** para pedidos com valor final igual ou superior a R$ 20,00.
- Interface de linha de comando (CLI) simples e intuitiva.

## 💰 Tabela de Preços

| Bebida       | Tamanho P | Tamanho M | Tamanho G |
|--------------|-----------|-----------|-----------|
| **Café**     | R$ 4,00   | R$ 5,50   | R$ 7,00   |
| **Capuccino**| R$ 6,00   | R$ 7,50   | R$ 9,00   |
| **Chocolate**| R$ 5,50   | R$ 7,00   | R$ 8,50   |

## 📜 Regras de Negócio
1. **Desconto Estudantil:** Clientes que se identificam como alunos FIAP (`sim`) e cujo pedido sem desconto seja **maior que R$ 15,00** recebem 10% de desconto sobre o valor total.
2. **Brinde:** Qualquer pedido cujo **valor final** (após descontos) seja **maior ou igual a R$ 20,00** recebe um brinde.

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado no seu computador.
2. Clone ou baixe este repositório para o seu computador.
3. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) na pasta do projeto.
4. Execute o script com o seguinte comando:
   ```bash
   python cafeteria.py
