import polars as pl

def ProcessData(DataFrame: pl.DataFrame) -> pl.DataFrame:
    """Procesa los datos y retorna un DataFrame listo para el modelo predictivo."""
    processedDataFrame = DataFrame.with_columns([
        (pl.col('Quantity') * pl.col('UnitPrice')).alias('TotalAmount')
    ])
    return processedDataFrame.select(['TotalAmount'])
