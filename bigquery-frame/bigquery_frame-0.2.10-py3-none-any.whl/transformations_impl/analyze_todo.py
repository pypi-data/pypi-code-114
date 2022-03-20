from bigquery_frame import DataFrame


def export_analyze(df: DataFrame):
    # TODO: finish this
    df.withColumn("approx_top_100", f.expr('''ARRAY(
      SELECT CONCAT('(', SUBSTRING(x.value, 0, 10), CASE WHEN LENGTH(x.value) > 10 THEN '...' ELSE '' END, ',', CAST(x.count as STRING), ')')
      FROM UNNEST(approx_top_100) x
    )'''), replace=True)
    df = df.withColumn("approx_top_100", f.expr('''CONCAT('[', ARRAY_TO_STRING(approx_top_100, ", ") , ']')'''), replace=True)
    df.show()


