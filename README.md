# dataset

Repositório para armazenar ferramentas e conjuntos de dados utilizados no projeto de Matemática Computacional.

## Instruções de utilização - Aquisição de dados

Os scripts de aquisição de dados estão divididos em dois tipos: [Dados nacionais](dataset_tool/load_national.py) e [Dados Internacionais](dataset_tool/load_international.py).

Para utilizar cada um desses *scripts*, começe realizando a instalação dos pacotes utilizados:

```shell
pip install -r requirements.txt
```

Com a instalação finalizada já será possível executar os scripts. A execução pode ser feita como apresentado abaixo

```shell
python3 dataset_tool/load_national.py
python3 dataset_tool/load_international.py
```

Caso esteja utilizando ambiente Linux é possível utilizar o exec.sh

```shell
./exec.sh
```

Com o final da execução, cada um dos scripts executados terá gerado o resultado em trẽs formatos diferentes (csv, json e sqlite3).

### Fonte dos dados

Todos os dados internacionais são adquiridos da [Our World in Data](https://ourworldindata.org/how-to-use-our-world-in-data). Para os dados nacionais, o site [Brasil.io](https://brasil.io/home/) está sendo consultado, este centraliza as bases de dados de diferentes municípios.

Caso necessário, a descrição de cada atributo da tabela de dados nacionais podem ser encontrados na [documentação do Brasil.io](https://github.com/turicas/covid19-br/blob/master/api.md#caso_full). Para os dados do [Our World in Data](https://ourworldindata.org/how-to-use-our-world-in-data) há a [tabela de metadados](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data-codebook.md)
