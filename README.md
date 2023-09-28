# MVP - Engenharia de Dados


## Overview

Welcome to project! 

Este projeto tem como objetivo criar uma infraestrutura básica para coletar, armazenar e processar dados de forma escalável, utilizando serviços como o Google Cloud Storage, BigQuery e Dataflow.  Todo os procedimentos realizados estão detalhados no arquivo .pdf 

## Cloud Services

Configuração do ambiente virtual: a fim de não haver conflitos com versões específicas de pacotes cria-se um ambiente virtual e nele instala-se o apache-beam[gcp]:

### Requirements
```sh
python3 -m pip install — user virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install 'apache-beam[gcp]'
```

###  Pipeline e Job Dataflow
```sh
python data-ingestion.py \
--project=mvp-puc-399408 \
--runner=DataflowRunner \
--staging_location=gs://mvp-streamings/staging \
--temp_location gs://mvp-streamings/temp \
--input 'gs://mvp-streamings/netflix-spotify/*.csv' \
--region=us-east1
```

