import pdb

import arrow
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import requests
from pandas import Series
from pandas.io.json import json_normalize


def get_api_endpoint(url: str) -> pd.DataFrame:
    """ Get API endpoint and convert to DataFrame
    Example:
    url: https://swapi.co/api/starships/9/
    data:
        +(Pdb) print(d)
        {'MGLT': '10', 'cargo_capacity': '1000000000000',
        'films': ['https://swapi.co/api/films/1/'],
        'manufacturer': 'Imperial Department of Military Research, Sienar Fleet Systems',
        'starship_class': 'Deep Space Mobile Battlestation',
        'created': '2014-12-10T16:36:50.509000Z',
        'model': 'DS-1 Orbital Battle Station',
        'url': 'https://swapi.co/api/starships/9/',
        'consumables': '3 years', 'hyperdrive_rating': '4.0',
        'crew': '342953', 'name': 'Death Star', 'max_atmosphering_speed': 'n/a',
        'edited': '2014-12-22T17:35:44.452589Z', 'length': '120000',
        'pilots': [], 'cost_in_credits': '1000000000000', 'passengers': '843342'}
    df:
        df.columns
        Index(['MGLT', 'cargo_capacity', 'consumables', 'cost_in_credits', 'created',
              'crew', 'edited', 'films', 'hyperdrive_rating', 'length',
              'manufacturer', 'max_atmosphering_speed', 'model', 'name', 'passengers',
              'pilots', 'starship_class', 'url'],
             dtype='object')
        +(Pdb) df.head()
         MGLT cargo_capacity consumables cost_in_credits  \
        0   10  1000000000000     3 years   1000000000000 ...
    """
    r = requests.get(url)
    d = r.json()
    return pd.DataFrame(dict([(k, Series(v)) for k, v in d.items()]))


def df_add_partition_columns(df, date_field):
    """ Return a dataframe with new columns used for partitioning by datetime
    Example: 2018-03-04T14:12:15.653Z returns with new df columns of 'year', 'month', day'
    """
    df[date_field] = df[date_field].map(lambda t: pd.to_datetime(t, format="%Y-%m-%dT%H:%M:%S.%fZ"))
    df['year'], df['month'], df['day'] = df[date_field].apply(lambda x: x.year), df[date_field].apply(lambda x: x.month), df[date_field].apply(lambda x: x.day)
    return df


def df_to_parquet_table(df: pd.DataFrame) -> pa.Table:
    """ Convert DataFrame to Pyarrow Table
    Example:
    pyarrow.Table
    MGLT: string
    cargo_capacity: string
    consumables: string
    cost_in_credits: string
    created: string
    crew: string
    edited: string
    films: string
    hyperdrive_rating: string
    length: string
    manufacturer: string
    max_atmosphering_speed: string
    model: string
    name: string
    passengers: string
    pilots: double
    starship_class: string
    url: string
    __index_level_0__: int64
    metadata
    --------
    {b'pandas': b'{"columns": [{"field_name": "MGLT", "pandas_type": "unicode", "m'
            b'etadata": null, "name": "MGLT", "numpy_type": "object"}, {"field'
            b'_name": "cargo_capacity", "pandas_type": "unicode", "metadata": '
            b'null, "name": "cargo_capacity", "numpy_type": "object"}, {"field'
            b'_name": "consumables", "pandas_type": "unicode", "metadata": nul'
            b'l, "name": "consumables", "numpy_type": "object"}, {"field_name"'
            b': "cost_in_credits", "pandas_type": "unicode", "metadata": null,'
            b' "name": "cost_in_credits", "numpy_type": "object"}, {"field_nam'
            b'e": "created", "pandas_type": "unicode", "metadata": null, "name'
            b'": "created", "numpy_type": "object"}, {"field_name": "crew", "p'
            b'andas_type": "unicode", "metadata": null, "name": "crew", "numpy'
            b'_type": "object"}, {"field_name": "edited", "pandas_type": "unic'
            b'ode", "metadata": null, "name": "edited", "numpy_type": "object"'
            b'}, {"field_name": "films", "pandas_type": "unicode", "metadata":'
            b' null, "name": "films", "numpy_type": "object"}, {"field_name": '
            b'"hyperdrive_rating", "pandas_type": "unicode", "metadata": null,'
            b' "name": "hyperdrive_rating", "numpy_type": "object"}, {"field_n'
            b'ame": "length", "pandas_type": "unicode", "metadata": null, "nam'
            b'e": "length", "numpy_type": "object"}, {"field_name": "manufactu'
            b'rer", "pandas_type": "unicode", "metadata": null, "name": "manuf'
            b'acturer", "numpy_type": "object"}, {"field_name": "max_atmospher'
            b'ing_speed", "pandas_type": "unicode", "metadata": null, "name": '
            b'"max_atmosphering_speed", "numpy_type": "object"}, {"field_name"'
            b': "model", "pandas_type": "unicode", "metadata": null, "name": "'
            b'model", "numpy_type": "object"}, {"field_name": "name", "pandas_'
            b'type": "unicode", "metadata": null, "name": "name", "numpy_type"'
            b': "object"}, {"field_name": "passengers", "pandas_type": "unicod'
            b'e", "metadata": null, "name": "passengers", "numpy_type": "objec'
            b't"}, {"field_name": "pilots", "pandas_type": "float64", "metadat'
            b'a": null, "name": "pilots", "numpy_type": "float64"}, {"field_na'
            b'me": "starship_class", "pandas_type": "unicode", "metadata": nul'
            b'l, "name": "starship_class", "numpy_type": "object"}, {"field_na'
            b'me": "url", "pandas_type": "unicode", "metadata": null, "name": '
            b'"url", "numpy_type": "object"}, {"field_name": "__index_level_0_'
            b'_", "pandas_type": "int64", "metadata": null, "name": null, "num'
            b'py_type": "int64"}], "column_indexes": [{"field_name": null, "pa'
            b'ndas_type": "unicode", "metadata": {"encoding": "UTF-8"}, "name"'
            b': null, "numpy_type": "object"}], "pandas_version": "0.22.0", "i'
            b'ndex_columns": ["__index_level_0__"]}'}
    """
    pyarrow_deathstar_table = pa.Table.from_pandas(df)  # Create PyArrow Table from Pandas DF
    print(pyarrow_deathstar_table)
    pq.write_table(pyarrow_deathstar_table, 'deathstar.parquet')  # Convert PyArrow Table to Parquet Table / File
    parquet_table = pq.read_table('deathstar.parquet')  # Read back Parquet File as a Table
    parquet_table = pq.ParquetFile('deathstar.parquet')  # Read back Parquet File as a ParquetFile for finer-grained read and write
    print(parquet_table.metadata)
    #<pyarrow._parquet.FileMetaData object at 0x7fb755c29458>
    #  created_by: parquet-cpp version 1.4.1-SNAPSHOT
    #  num_columns: 19
    #  num_rows: 1
    #  num_row_groups: 1
    #  format_version: 1.0
    #  serialized_size: 4574

    print(parquet_table.schema)
    #<pyarrow._parquet.ParquetSchema object at 0x7efc80565408>
    #MGLT: BYTE_ARRAY UTF8
    #cargo_capacity: BYTE_ARRAY UTF8
    #consumables: BYTE_ARRAY UTF8
    #cost_in_credits: BYTE_ARRAY UTF8
    #created: BYTE_ARRAY UTF8
    #crew: BYTE_ARRAY UTF8
    #edited: BYTE_ARRAY UTF8
    #films: BYTE_ARRAY UTF8
    #hyperdrive_rating: BYTE_ARRAY UTF8
    #length: BYTE_ARRAY UTF8
    #manufacturer: BYTE_ARRAY UTF8
    #max_atmosphering_speed: BYTE_ARRAY UTF8
    #model: BYTE_ARRAY UTF8
    #name: BYTE_ARRAY UTF8
    #passengers: BYTE_ARRAY UTF8
    #pilots: DOUBLE
    #starship_class: BYTE_ARRAY UTF8
    #url: BYTE_ARRAY UTF8
    #__index_level_0__: INT64
    return parquet_table


def write_parquet_table_as_partitioned_dataset(parquet_file) -> pq.ParquetDataset:
    """ Write a parquet table as a parititioned dataset (i.e. multiple Parquet files)
    An example of a dataset partitioned by year and month on disk might look like:
        dataset_name/
            year=2018/
                month=09/
                    0.parq
                    1.parq
                month=10/
                    0.parq
                    1.parq
    """
    parquet_table = pq.read_table(parquet_file)  # Read back Parquet File as a Table
    #pq.write_to_dataset(parquet_table, root_path='starships', partition_cols=['created'])
    pq.write_to_dataset(parquet_table, root_path='starships', partition_cols=['year', 'month', 'day'], flavor='spark')
    dataset = pq.ParquetDataset('starships')
    return dataset


if __name__ == '__main__':

    # Basics of get request, save to DataFrame, PyArrow Table, Parquet File
    df_deathstar = get_api_endpoint('https://swapi.co/api/starships/9/')
    df_deathstar = df_add_partition_columns(df_deathstar, 'created')
    parquet_deathstar_table = df_to_parquet_table(df_deathstar)

    # Write to and Read from Partitioned Datasets
    write_parquet_table_as_partitioned_dataset('deathstar.parquet')
    print("Done")
