# Árvores Balanceadas - Simulador de Fila de Prioridade (RBT)

## Alunos  
| Matrícula | Nome |  
|:----------:|:---------------------------:|  
| 20/2046229 | Kallyne Macêdo Passos |  
| 20/0022199 | Leonardo Sobrinho de Aguiar | 

Dupla: 18 

## Descrição do projeto

Este projeto é um visualizador interativo que demonstra o funcionamento de uma **Árvore Red-Black (Rubro-Negra)** utilizada como uma Fila de Prioridade. A aplicação permite que o usuário adicione "tarefas" com diferentes níveis de prioridade, que são armazenadas e gerenciadas pela Árvore Red-Black no backend, com o objetivo de fornecer uma visualização da eficiência de árvores auto-balanceadas. Assim, o simulador mostra como a árvore garante performance de **$O(\log n)$** para inserções e para extrair o item de maior prioridade, mesmo sob carga constante.

A aplicação conta com dois modos de uso:
1.  **Modo Manual:** O usuário pode adicionar tarefas uma a uma e processar a próxima tarefa de maior prioridade ao clicar em um botão.
2.  **Modo de Simulação:** Inicia um "teste de estresse" que adiciona tarefas aleatórias e processa a fila automaticamente em intervalos de tempo, demonstrando visualmente a estabilidade da árvore.

## Guia de instalação

**Linguagem**: Python, HTML, CSS (Bootstrap) e JavaScript<br>
**Framework**: Flask<br>
**Pré-requisitos**: Navegador web, Python e Flask instalados no computador.

### Passo a Passo

### 1. Clonar repositório:
```bash
git clone https://github.com/EDAII/ArvoresBalanceadas_FilaPrioridade.git
```
### 2. Instale as Dependências:
Abra um terminal ou prompt de comando na pasta do projeto e execute:
```bash
pip install Flask 
```
### 3. Inicie o Servidor:
Digite no mesmo terminal:
```bash
python app.py
```
### 4. Acesse a Aplicação:
Abra seu navegador web e acesse o seguinte endereço: http://127.0.0.1:5000

## Capturas de tela

<div align="center">
Simulação Ativada 
<img width="1919" height="928" alt="image" src="https://github.com/user-attachments/assets/49a103e7-d5c6-4ed0-854e-7dcd3f7eab14" />
</div>
<br>

<div align="center">
Fila de Espera - Sem Processamento 
<img width="1917" height="910" alt="image" src="https://github.com/user-attachments/assets/45b2cc13-5c71-472c-91cc-51790644c145" />
</div>
<br>

<div align="center">
Fila de Espera - Processada Manualmente 
<img width="1918" height="926" alt="image" src="https://github.com/user-attachments/assets/ae1629a7-00c2-4078-8ddc-254996eed1ac" />
</div>
<br>


## Conclusões

O projeto é uma ferramenta didática eficaz para o estudo de estruturas de dados avançadas, movendo o conceito de uma Árvore Red-Black da teoria para uma aplicação prática em que se torna intuitivo entender o *propósito* da RBT (Red-Black Tree): manter a eficiência **$O(\log n)$** em operações dinâmicas de inserção e busca/remoção de máximo/mínimo.

A aplicação permite comparar, implicitamente, o desempenho da RBT com o que seria uma lista não ordenada (que teria performance $O(n)$ para processar a maior prioridade) ou uma lista ordenada (que teria performance $O(n)$ para inserção). O Modo de Simulação demonstra que, mesmo com tarefas chegando e sendo processadas rapidamente, a aplicação continua responsiva, o que prova a eficiência da estrutura de dados escolhida.

## Gravação 

[Link da gravação](https://youtu.be/bSKsdaWjBRc)
