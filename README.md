# MVP - Engenharia de Dados


## Overview

Welcome to project! 🚀🎲

Este projeto tem como objetivo criar uma infraestrutura básica para coletar, armazenar e processar dados de forma escalável, utilizando serviços como o Google Cloud Storage, BigQuery e Dataflow.  Todo os procedimentos realizados estão detalhados no arquivo <b><i>gcp-mvp-report.pdf</i></b>

## Cloud CLI

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

<ul>
  <li><b><i>Read from a File:</i></b> o pipeline inicia usando os argumentos fornecidos, que incluem informações como o ID do projeto, o local dos dados (bucket no Google Storage) e a localização para o armazenamento dos arquivos temporários do Dataflow.</li>
  <li><b><i>Write to BigQuery:</i></b> após a leitura dos dados armazenados no Google Storage, este estágio transforma uma linha de arquivo CSV para um objeto de dicionário consumível pelo BigQuery. Além disso esta etapa realiza o tratamento do dataset
  Substitui todas as aspas duplas (") por uma string vazia
  Substitui todas as ocorrências da sequência de escape \r\n por uma string vazia
  divide a string em uma lista de valores com base nas vírgulas como separadores, após a remoção das aspas duplas e das quebras de linha. </li>
  <li><b><i>Write to BigQuery:</i></b> cria uma tabela no BigQuery se ela ainda não existir ou exclui todos os dados se ela já existir antes de gravar os dados já tratados.</li>
</ul>
