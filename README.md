# MVP Engenharia de Dados @ PUC-Rio


## Overview

Welcome to project! 🚀🎲

Este projeto aborda o desenvolvimento de uma infraestrutura básica no Google Cloud Platform para coletar, armazenar e processar dados de forma escalável, utilizando serviços como o Cloud Storage, BigQuery, Dataflow e Looker Studio. Todos os procedimentos realizados estão detalhados no arquivo <b><i>gcp-mvp-report.pdf</i></b>.

<img src="gcp-pipeline-schematic.png">

<b>1.</b> Criação e armazenamento de arquivos .csv em um bucket do Cloud Storage  
<b>2.</b> Orquestração de pipelines de dados, lendo os arquivos no Storage, tratando-os e
escrevendo-os no BigQuery  
<b>3.</b> Armazenamento dos dados tratados e padronizados, data warehouse do GCP  
<b>4.</b> Consumo final dos dados, ambiente BI conectado ao BigQuery  

## Cloud CLI

Para a execução do pipeline de dados ```data-ingestion.py``` no Cloud CLI, é necessário configurar o ambiente virtual. A fim de evitar conflitos com versões específicas de pacotes, cria-se um ambiente virtual e, nele, instala-se o apache-beam[gcp].

### Requirements
```sh
python3 -m pip install — user virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install 'apache-beam[gcp]'
```

###  Execução do Pipeline | Job Dataflow
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

## Informações da autora
<li>Nome: Maria Vitória Barbosa Valladares</li>
<li>E-mail: vitoria_valladares@hotmail.com</li>
<li>Linkedin: www.linkedin.com/in/vivalladares</li>
