import polars as pl

def ProcessData(DataFrame: pl.DataFrame) -> pl.DataFrame:
    processedDataFrame = DataFrame.with_columns([
        (pl.col('Quantity') * pl.col('UnitPrice')).alias('TotalAmount')
    ])
    return processedDataFrame.select(['TotalAmount'])
