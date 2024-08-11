import polars as pl
from DbConnection import GetConnection

def ExtractData(Query: str) -> pl.DataFrame:
    connection = GetConnection()
    cursor = connection.cursor()
    cursor.execute(Query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    connection.close()
    return pl.DataFrame(data, schema=columns)

def GetSalesData() -> pl.DataFrame:
    query = """
        SELECT s.SaleID, s.SaleDate, sd.Quantity, sd.UnitPrice
        FROM sales s
        JOIN salesdetails sd ON s.SaleID = sd.SaleID
    """
    return ExtractData(query)
