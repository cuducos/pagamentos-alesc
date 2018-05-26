# Raspagem de dados da ALESC

O [Portal de Transparência da ALESC](http://transparencia.alesc.sc.gov.br/pagamentos.php), na sessão de _Pagamentos_, oferece um CSV, mas o CSV **não** inclui informações essenciais, como a **descrição** do gasto.

Esse aplicativo complementa os CSVs disponibilizados com essas descrições dos dados.

## Requisitos

* [Docker](https://docs.docker.com/install/)

## Montando o container

```sh
$ docker build -t alesc .
```

## Coletando os dados

Esse comando gera o arquivo `data.csv`:

```sh
docker run -it -v $(pwd):/alesc alesc scrapy crawl alesc -o data.csv
```

## Explorando os dados

Inicia uma sessão do Jupyter Notebook com:

```sh
docker run -it -v $(pwd):/alesc -p 8888:8888 alec
```