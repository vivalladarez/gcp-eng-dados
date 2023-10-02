from __future__ import absolute_import
import argparse
import logging
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import os


class DataIngestion:
    def parse_method(self, string_input):
        values = re.split(",",
                          re.sub('\r\n', '', re.sub(u'"', '', string_input)))
        row = dict(
            zip(('title', 'description', 'start_time', 'duration'),
                values))
        return row

# Função principal que cria o pipeline de dados e o executa


def run(argv=None):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to read. This can be a local file or '
        'a file in a Google Storage Bucket.',
        default='mvp-streamings/netflix-spotify/netflixactivity.csv')

    # Por padrão "default" é o nome do conjunto de dados criado no BigQuery
    parser.add_argument('--output',
                        dest='output',
                        required=False,
                        help='Output BQ table to write results to.',
                        default='streamings.netflixactivity')

    # Analise de argumentos da linha de comando.
    known_args, pipeline_args = parser.parse_known_args(argv)

    # DataIngestion é uma classe que contém a logica de transformação do arquivo
    data_ingestion = DataIngestion()

    # Inicia o pipeline usando argumentos passados na linha de comando
    p = beam.Pipeline(options=PipelineOptions(pipeline_args))

    (
        p | 'Read from a File' >> beam.io.ReadFromText(known_args.input,
                                                       skip_header_lines=1)
        | 'String To BigQuery Row' >>
        beam.Map(lambda s: data_ingestion.parse_method(s))
        | 'Write to BigQuery' >> beam.io.Write(
            beam.io.BigQuerySink(

                known_args.output,

                schema='title:STRING,description:STRING,start_time:DATE,duration:INTEGER',
                # Cria a tabela no BigQuery se ela ainda não existir
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                # Exclui todos os dados da tabela do BigQuery antes de gravá-los.
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))

    p.run().wait_until_finish()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
