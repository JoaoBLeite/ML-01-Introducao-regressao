# ML-California-Housing

Uma **introdução prática e didática a Machine Learning** usando Python e o dataset **California Housing**.

## 🎯 Objetivo

Este repositório é um caderno de estudos para quem está **começando em Machine Learning e em Python**. Ao longo de 7 notebooks, construímos passo a passo um modelo que prevê o **valor mediano das casas** em regiões da Califórnia. Cada etapa é explicada do zero.

O foco não é só chegar a um bom modelo. É **entender o porquê** de cada decisão:

- 🎓 **Cada conceito novo** de Machine Learning é apresentado e contextualizado antes de ser usado.
- 💬 **Cada célula de código** tem comentários explicando tanto a ideia de ML quanto a sintaxe Python.
- 📌 **Cada análise termina com uma conclusão**: o que os números e gráficos estão dizendo.
- 🔁 **Cada notebook continua o anterior**: os problemas encontrados em um motivam as técnicas do próximo.

### O dataset

O [California Housing](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) vem junto com o scikit-learn e tem dados do **censo de 1990**. Cada uma das 20.640 linhas é um **bloco censitário** (uma pequena região), descrito por 8 atributos: renda mediana, idade das casas, média de cômodos e quartos, população, moradores por domicílio, latitude e longitude.

O alvo (`MedHouseVal`) é o valor mediano das casas do bloco, em centenas de milhares de dólares.

## 📚 Trilha de estudos

| Notebook | O que você aprende |
|---|---|
| [01 · Análise exploratória](01_analise_exploratoria.ipynb) | Conhecer os dados: distribuições, valores ausentes, outliers, correlação e mapas |
| [02 · Primeiro modelo](02_primeiro_modelo.ipynb) | Aprendizado supervisionado, treino/teste, baseline, métricas (MAE, RMSE, R²), regressão linear, under/overfitting, resíduos |
| [03 · Pré-processamento e Pipeline](03_preprocessamento_e_pipeline.ipynb) | Conjunto de validação, padronização, vazamento de dados, `Pipeline`, engenharia de atributos, transformação logarítmica |
| [04 · Modelos não lineares](04_modelos_nao_lineares.ipynb) | Árvores de decisão, overfitting extremo, hiperparâmetros, curva de complexidade, random forest e ensembles |
| [05 · Validação cruzada](05_validacao_cruzada.ipynb) | K-Fold, média ± desvio padrão, comparação pareada entre modelos |
| [06 · Ajuste de hiperparâmetros](06_ajuste_de_hiperparametros.ipynb) | `GridSearchCV`, `RandomizedSearchCV`, interação entre hiperparâmetros, a "maldição do vencedor" |
| [07 · Avaliação final e interpretação](07_avaliacao_final_e_interpretacao.ipynb) | Avaliação no teste, análise de erros no mapa, *permutation importance*, dependência parcial, salvar o modelo, limitações e uso responsável |

### Evolução dos resultados (no conjunto de teste)

| Notebook | Modelo | Erro médio (MAE) | R² |
|---|---|---|---|
| 02 | Baseline (sempre prevê a média) | US$ 90.600 | 0,00 |
| 02 | Regressão linear | US$ 53.300 | 0,58 |
| 03 | Regressão linear + pré-processamento | US$ 46.400 | 0,68 |
| 04 | Árvore de decisão | US$ 42.600 | 0,68 |
| 04 | Random forest + atributos | US$ 30.600 | 0,83 |
| 07 | **Random forest ajustada (modelo final)** | **US$ 30.300** | **0,83** |

## 🛠️ Configurando o ambiente

### Pré-requisitos

- **Python 3.10 ou mais recente.** Para conferir sua versão:
  ```bash
  python3 --version
  ```
- **Git**, para baixar o repositório.

### 1. Baixe o repositório

```bash
git clone https://github.com/JoaoBLeite/ML-California-Housing.git
cd ML-California-Housing
```

### 2. Crie um ambiente virtual

Um **ambiente virtual** é uma pasta isolada com o Python e as bibliotecas **só deste projeto**. Assim, as versões instaladas aqui não interferem em outros projetos do seu computador, e vice-versa.

```bash
python3 -m venv .venv
```

Isso cria a pasta `.venv/` dentro do projeto. Ela não vai para o Git, porque já está no `.gitignore`.

> 💡 **No Ubuntu/Debian**, se aparecer um erro dizendo que o `venv` não está disponível, instale-o com:
> `sudo apt install python3-venv`

### 3. Ative o ambiente virtual

O ambiente precisa ser **ativado em cada novo terminal** que você abrir.

| Sistema | Comando |
|---|---|
| Linux / macOS | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Prompt de Comando) | `.venv\Scripts\activate.bat` |

Quando o ambiente está ativo, o nome `(.venv)` aparece no começo da linha do terminal. Para desativar, use `deactivate`.

### 4. Instale as bibliotecas

Com o ambiente **ativado**:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

O arquivo `requirements.txt` lista as versões exatas usadas no projeto. As principais são:

| Biblioteca | Para quê |
|---|---|
| `pandas` | Manipular tabelas de dados |
| `numpy` | Cálculos numéricos |
| `matplotlib` | Gráficos |
| `scikit-learn` | Modelos de Machine Learning, métricas e o dataset |
| `jupyter` | Rodar os notebooks |

Para conferir se deu tudo certo:

```bash
python -c "import pandas, sklearn, matplotlib; print('Tudo instalado!')"
```

## ▶️ Como executar

### 1. Abra o Jupyter

Com o ambiente virtual **ativado**, na pasta do projeto:

```bash
jupyter notebook
```

O navegador vai abrir com a lista de arquivos do projeto. Se preferir uma interface mais completa, use `jupyter lab`.

> 💡 **Usa o VS Code?** Abra a pasta do projeto, abra um notebook e, no canto superior direito, escolha o *kernel* do Python que está em `.venv`.

### 2. Siga os notebooks em ordem

Comece pelo **01** e siga até o **07**. Cada notebook pressupõe os conceitos dos anteriores.

Dentro de um notebook:
- **`Shift + Enter`** executa a célula atual e passa para a próxima.
- Execute as células **de cima para baixo**: uma célula pode depender de variáveis criadas nas anteriores.
- Para rodar tudo do zero: menu **Kernel → Restart Kernel and Run All Cells**.
- Enquanto uma célula está rodando, aparece `[*]` à esquerda dela.

### Observações

- **Na primeira execução**, o dataset é baixado da internet (cerca de 400 KB) e fica salvo em `~/scikit_learn_data`. Nas próximas vezes, não é preciso conexão.
- **O notebook 06 demora alguns minutos** (cerca de 4 minutos), porque treina centenas de modelos.
- **O notebook 07 salva o modelo final** na pasta `modelos/` (cerca de 33 MB). Essa pasta não vai para o Git: ela é recriada sempre que o notebook 07 é executado.
- Os notebooks já estão salvos **com os resultados**, então dá para lê-los aqui no GitHub mesmo sem executá-los.

## 📁 Estrutura do projeto

```
ML-California-Housing/
├── 01_analise_exploratoria.ipynb
├── 02_primeiro_modelo.ipynb
├── 03_preprocessamento_e_pipeline.ipynb
├── 04_modelos_nao_lineares.ipynb
├── 05_validacao_cruzada.ipynb
├── 06_ajuste_de_hiperparametros.ipynb
├── 07_avaliacao_final_e_interpretacao.ipynb
├── atributos.py          # funções de engenharia de atributos (usadas no notebook 07)
├── requirements.txt      # bibliotecas e versões do projeto
└── modelos/              # criada pelo notebook 07 (não versionada)
```

## ⚠️ Limitações

Este projeto é para **aprender**, não para avaliar imóveis de verdade. Os dados são de 1990, descrevem regiões e não casas individuais, e têm um teto artificial em US$ 500 mil. O notebook 07 discute essas limitações e os cuidados com o uso responsável de modelos como este.
