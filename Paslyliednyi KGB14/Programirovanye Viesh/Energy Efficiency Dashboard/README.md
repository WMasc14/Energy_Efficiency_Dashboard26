# Energy Efficiency Dashboard

Este projeto é um dashboard de eficiência energética para uma fábrica, desenvolvido usando Python e Streamlit. Ele permite monitorar o consumo de energia, a produção e o fator de potência em tempo real.

## Estrutura do Projeto

```
energy_efficiency_dashboard/
├── app/
│   ├── components/
│   │   ├── cards.py          # Componentes de métricas
│   │   ├── charts.py         # Gráficos com Plotly
│   │   └── filters.py        # Filtros laterais
│   ├── pages/
│   │   ├── overview.py       # Página principal
│   │   ├── machines.py       # Análise por máquinas
│   │   └── alarms.py         # Alarmes e anomalias
│   └── main.py               # Ponto de entrada do Streamlit
├── config/
│   └── settings.py           # Configurações e caminhos
├── database/
│   └── connection.py         # Conexão com banco de dados
├── data/
│   └── mock/
│       └── generate_mock_data.py  # Geração de dados fictícios
├── etl/
│   ├── extract.py            # Extração de dados
│   ├── transform.py          # Transformação e cálculo de KPIs
│   └── load.py               # Carregamento no banco
├── models/
│   └── kpi.py                # Cálculos de KPIs
├── tests/
│   └── test_kpi.py           # Testes unitários
└── archive/
    └── energy_efficiency_dashboard.py  # Versão antiga concatenada
```

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Gere dados mock (opcional):
   ```bash
   python data/mock/generate_mock_data.py
   ```

3. Execute o dashboard:
   ```bash
   python -m streamlit run app/main.py
   ```

## Funcionalidades

- **Visão Geral**: Métricas principais e gráficos de consumo
- **Máquinas**: Análise detalhada por máquina
- **Alarmes**: Detecção de anomalias baseada em estatísticas
- **Filtros**: Por linha, máquina e período de datas

## Arquitetura

O projeto segue uma arquitetura ETL simples:
- **Extract**: Lê dados de CSV
- **Transform**: Calcula KPIs
- **Load**: Salva no SQLite

A interface é construída com Streamlit e Plotly para visualizações interativas.