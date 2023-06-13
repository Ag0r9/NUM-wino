import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🍷",
)

"""
# Wycena win

## Biznes

### Cel biznesowy

Wycena produktów jest trudna. Trzeba patrzeć na koszt produkcji, popyt, jakość i wiele innych czynników.
Często przez błąd w wycenie możemy stracić ogromną ilość pieniędzy.
Możemy utrzymywać na rynku produkt, którego produkcja przewyższa jego cenę w jakości lub możemy nie wiedzieć,
że sprzedajemy dobry produkt za półowę ceny.
Naszym celem biznesowym jest **wycena win na podstawie ich cech**.

### Metryki

Metryk których używaliśmy do sprawdzeniu naszego modelu jest R2 i maksymalny błąd. 
R2 ponieważ jest nie jest one od wielkości cen jak mse. 
Maksymalny błąd może być bardziej czytelny dla SME.
Nie chcemy maksymalizować tych metryk, lecze utrzymać na stałm poziomie.

```
├── analytics
│   ├── cli
│   │   └── app.py
│   ├── notebooks
│   │   └── playground.ipynb
│   └── utils.py
├── data
│   ├── input
│   │   ├── WinePrices.csv
│   │   ├── WinePrices.csv.dvc
│   │   ├── WineQT.csv
│   │   └── WineQT.csv.dvc
│   ├── models
│   │   ├── RFR_METADATA
│   │   ├── RFR_METADATA.dvc
│   │   ├── RFR.p
│   │   └── RFR.p.dvc
│   ├── output
│   │   ├── trends
│   │   └── trends.dvc
│   └── prepared
│       ├── X_test
│       ├── X_test.dvc
│       ├── X_train
│       ├── X_train.dvc
│       ├── y_test
│       ├── y_test.dvc
│       ├── y_train
│       └── y_train.dvc
├── Home.py
├── Makefile
├── pages
│   ├── calculate_price.py
│   └── show_trends.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── cli
    │   └── app.py
    ├── config
    │   ├── default.yaml
    │   └── paths.py
    ├── pipeline
    │   ├── evaluate.py
    │   ├── prepare.py
    │   ├── train.py
    │   └── trends.py
    └── utils.py
```


"""