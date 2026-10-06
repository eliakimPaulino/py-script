# Algoritmo de Otimização para Aplicação de PR

Projeto em Python para leitura de circuitos a partir de arquivos PDF, transformação 
dos dados em objetos e posterior aplicação de um algoritmo de análise/otimização de 
cortes de cabos.

## Estrutura do projeto

```text
.
├── alg.py
├── circuit.py
├── config.py
├── main.py
└── pdf_reader.py
```

### Descrição dos arquivos

| Arquivo         | Responsabilidade                                      |
| --------------- | ----------------------------------------------------- |
| `main.py`       | Ponto de entrada da aplicação e orquestração do fluxo |
| `pdf_reader.py` | Leitura e interpretação das tabelas presentes no PDF  |
| `circuit.py`    | Definição da classe `Circuito`                        |
| `alg.py`        | Regras e processamento do algoritmo de corte          |
| `config.py`     | Configurações gerais do projeto                       |

---

# Fluxo da aplicação

O fluxo principal do projeto é:

```
                    ┌──────────────┐
                    │     PDF      │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  pdf_reader.py  │
                  │                 │
                  │ Lê as tabelas   │
                  │ do documento    │
                  └────────┬────────┘
                           │
                           │ dados extraídos
                           ▼
                  ┌─────────────────┐
                  │   circuit.py    │
                  │                 │
                  │     Circuito    │
                  │                 │
                  │ ID              │
                  │ Origem          │
                  │ Destino         │
                  │ Cabo            │
                  │ Diâmetro        │
                  │ Comprimento     │
                  └────────┬────────┘
                           │
                           │ lista de Circuitos
                           ▼
                  ┌─────────────────┐
                  │     alg.py      │
                  │                 │
                  │ Processamento   │
                  │ do algoritmo    │
                  │ de corte        │
                  └────────┬────────┘
                           │
                           │ resultado
                           ▼
                  ┌─────────────────┐
                  │     main.py     │
                  │                 │
                  │ Orquestra o     │
                  │ processamento   │
                  └─────────────────┘

                  ┌─────────────────┐
                  │    config.py    │
                  │                 │
                  │ Configurações   │
                  │ gerais          │
                  └─────────────────┘
```

## Fluxo simplificado

```text
PDF
 ↓
pdf_reader.py
 ↓
Lista[Circuito]
 ↓
alg.py
 ↓
Resultado do algoritmo
```

O `main.py` coordena esse fluxo.

---

# Responsabilidade de cada módulo

## `main.py`

É o ponto de entrada do programa.

Sua função é coordenar as etapas do processamento, sem concentrar a lógica de leitura 
do PDF ou as regras do algoritmo.

Fluxo esperado:

```python
def main():

    circuitos = ler_pdf()

    resultado = executar(circuitos)

    # utilização do resultado
```

A ideia é que `main.py` seja simples e funcione como o orquestrador do projeto.

---

## `pdf_reader.py`

Responsável pela entrada de dados.

Esse módulo:

1. Abre o arquivo PDF;
2. Acessa as páginas desejadas;
3. Extrai as tabelas;
4. Identifica o cabeçalho;
5. Seleciona as colunas necessárias;
6. Limpa os dados;
7. Cria objetos `Circuito`;
8. Retorna uma lista de circuitos.

Fluxo:

```text
PDF
 │
 ├── página
 │
 ├── tabela
 │
 ├── cabeçalho
 │
 ├── dados
 │
 └── Circuito
```

A saída esperada é:

```python
[
    Circuito(...),
    Circuito(...),
    Circuito(...),
]
```

Dessa forma, o restante do sistema não precisa saber como os dados foram extraídos do PDF.

---

## `circuit.py`

Contém a classe responsável por representar um circuito.

Um circuito possui informações como:

```text
ID
Origem
Destino
Cable DTR
Diâmetro/Tipo
Comprimento
```

Exemplo conceitual:

```python
Circuito(
    id="123",
    origem="DEVICE_A/1",
    destiny="DEVICE_B/2",
    cable_dtr="CABO_001",
    diameter="TYPE_A",
    length=25
)
```

A classe também possui métodos auxiliares para:

* representação do circuito;
* representação para corte;
* comparação;
* filtragem de possíveis sobras;
* igualdade entre circuitos;
* utilização em estruturas como `set` e `dict`.

### Responsabilidade

`circuit.py` representa **o que é um circuito**.

Ele não deve ser responsável por:

* abrir PDFs;
* ler DataFrames;
* executar o algoritmo de otimização;
* definir configurações globais.

---

# `alg.py`

É o núcleo lógico do projeto.

Esse módulo recebe uma lista de objetos `Circuito` e aplica as regras necessárias para encontrar uma solução de corte.

Fluxo:

```text
Lista de Circuitos
        │
        ▼
┌───────────────────┐
│     alg.py        │
│                   │
│ Agrupamento       │
│ Comparações       │
│ Regras de corte   │
│ Cálculo de sobra  │
│ Otimização        │
└─────────┬─────────┘
          │
          ▼
      Resultado
```

A lógica de otimização pode evoluir posteriormente para considerar, por exemplo:

* comprimento disponível da bobina;
* comprimento dos circuitos;
* tipo de cabo;
* diâmetro;
* compatibilidade entre circuitos;
* quantidade de cortes;
* sobra de cada corte;
* sobra total;
* quantidade de bobinas utilizadas;
* outras restrições do projeto.

---

# `config.py`

Centraliza as configurações utilizadas pelo sistema.

Exemplos:

```python
PDF_FILENAME = "..."

PAGINAS_DESEJADAS = [...]

COLUNAS_DESEJADAS = [...]
```

Também pode conter configurações do Pandas:

```python
pd.set_option(...)
```

Centralizar essas informações evita que valores de configuração fiquem espalhados pelos outros módulos.

Por exemplo, para alterar as páginas processadas:

```python
PAGINAS_DESEJADAS = [5]
```

pode ser alterado para:

```python
PAGINAS_DESEJADAS = [5, 6, 7]
```

sem modificar o código de leitura.

---

# Arquitetura

A dependência entre os módulos pode ser representada da seguinte forma:

```text
                   config.py
                      │
                      │ configura
                      ▼
                  main.py
                 /       \
                /         \
               ▼           ▼
      pdf_reader.py      alg.py
             │              │
             │              │
             ▼              │
        circuit.py ◄────────┘
```

Uma visão mais detalhada:

```text
                 ┌─────────────┐
                 │ config.py   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   main.py   │
                 └──────┬──────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
     ┌────────────────┐   ┌───────────────┐
     │ pdf_reader.py  │   │    alg.py     │
     └───────┬────────┘   └───────┬───────┘
             │                    │
             │ cria               │ processa
             ▼                    │
       ┌─────────────┐            │
       │ circuit.py  │◄───────────┘
       └─────────────┘
```

---

# Execução

A aplicação deve ser executada através do `main.py`.

```bash
python main.py
```

O fluxo de execução será:

```text
python main.py
       │
       ▼
   main.py
       │
       ▼
pdf_reader.py
       │
       ▼
 Lista de Circuitos
       │
       ▼
    alg.py
       │
       ▼
   Resultado
```

---

# Exemplo de dados

A partir de uma tabela do PDF, uma linha como:

```text
001 | DEV_A | 01 | DEV_B | 02 | TYPE_A | CABO_001 | 25 | A
```

pode ser transformada em:

```python
Circuito(
    id="001",
    origem="DEV_A/01",
    destiny="DEV_B/02",
    cable_dtr="CABO_001",
    diameter="TYPE_A",
    length="25"
)
```

Depois da leitura do PDF, o algoritmo trabalha com objetos:

```python
circuitos = [
    Circuito(...),
    Circuito(...),
    Circuito(...),
]
```

em vez de trabalhar diretamente com as linhas do PDF.

---

# Separação de responsabilidades

Uma das principais características do projeto é a separação entre **dados**, **entrada**, **processamento** e **orquestração**.

```text
┌───────────────────────────────────────────┐
│                  PDF                      │
│              Entrada bruta                │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│             pdf_reader.py                 │
│             Entrada de dados              │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│               circuit.py                  │
│          Modelo dos dados                 │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│                 alg.py                    │
│           Regras e otimização             │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│                main.py                    │
│          Orquestração da aplicação        │
└───────────────────────────────────────────┘
```

Essa separação permite modificar uma parte do sistema sem precisar alterar as outras.

Por exemplo:

* trocar o PDF não exige alterar `circuit.py`;
* alterar a classe `Circuito` não exige reescrever o algoritmo inteiro;
* alterar o algoritmo não exige alterar a leitura do PDF;
* adicionar novas configurações pode ser feito em `config.py`.

---

# Dependências

O projeto utiliza Python e as seguintes bibliotecas:

```text
pdfplumber
pandas
```

Instalação:

```bash
pip install pdfplumber pandas
```

Ou, caso seja utilizado um ambiente virtual:

```bash
python -m venv .venv
```

Ativação no Linux/macOS:

```bash
source .venv/bin/activate
```

Instalação das dependências:

```bash
pip install pdfplumber pandas
```

---

# Estado atual do projeto

Atualmente, o projeto possui a seguinte divisão:

```text
main.py
    │
    ├── coordena a execução
    │
    ▼
pdf_reader.py
    │
    ├── lê o PDF
    ├── extrai tabelas
    └── cria Circuitos
            │
            ▼
       circuit.py
            │
            ▼
        alg.py
            │
            └── processamento do algoritmo
```

A arquitetura foi preparada para que a lógica de otimização possa crescer sem transformar o `main.py` em um arquivo monolítico.

---

# Próximas etapas

A evolução natural do projeto é implementar o algoritmo de otimização em `alg.py`.

Uma possível evolução é:

```text
Circuitos
    │
    ▼
Agrupar por tipo de cabo
    │
    ▼
Agrupar por características compatíveis
    │
    ▼
Ordenar por comprimento
    │
    ▼
Distribuir nos cortes/bobinas
    │
    ▼
Calcular sobra
    │
    ▼
Comparar soluções
    │
    ▼
Escolher melhor solução
```

O objetivo final pode ser encontrar uma combinação de circuitos que minimize:

```text
Sobra total
```

e/ou:

```text
Quantidade de bobinas utilizadas
```

respeitando as restrições definidas para cada tipo de cabo.

---

# Licença

Projeto de uso interno/desenvolvimento.
