# Dependencies
######################
import delta.tables
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Type setting
######################

# Functions
######################
def delta_readfile(_path:str):
  """
  Read the Delta Lake file stored at the specified path.
  
  Additional keyword arguments are not supported
  """
  return spark.read.format('delta').load(_path)


def delta_writefile(_df, _path:str, _writemode='append', _cond=None, _partition=False, _partcols=[], **kwargs):
  """
  Write out the PySpark dataframe _df to the specified _path as a Databricks Delta Lake file.
  
  Different types of writing behaviour are supported:
  _writemode='overwrite':  overwrites existing Delta Lake files at the specified _path with the dataframe
  _writemode='append':     appends the dataframe to the existing Delta Lake files (default)
  _writemode='ignore':     does not write out any data if files exist at the _path location (allows for integration testing)
  _writemode='insert_all': appends the dataframe to the existing Delta Lake files and inserts complete rows for all matches rows according to the condition
  _writemode='insert_none':appends the dataframe to the existing Delta Lake files and inserts *no* rows for all matches rows according to the condition
  _writemode='insert_specific': not yet supported
  
  **Note**: the original table needs to be referred as "table" for the insert condition and the new table as "updates"
  
  Setting the _partitioning of the Delta Lake file during overwrite write mode is supported.  Any existing partitioning will be automatically followed during all other write modes.
  _partition: boolean to indicate whether partitioning is needed
  _partcols:  list of column names to be used for partitioning
  """
  assert _writemode in ['overwrite', 'append', 'ignore', 'insert_all', 'insert_none'], 'Illegal _writemode specified'
  
  # Default Parquet behaviour
  if _writemode in ['overwrite', 'append', 'ignore']:
    _conn = (_df.write
             .format('delta')
             .mode(_writemode)
            )
    # Overwrite behaviour:
    if _writemode == 'overwrite':
      _conn = _conn.option('overwriteSchema', 'true')
    
    # Include partioning
    if _partition:
      _conn = _conn.partitionBy(_partcols)

    # Work with the additional keyword arguments
    for _key, _val in kwargs.items():
          _conn = _conn.option(_key, _val)
    
    _conn.save(_path)
    return
  
  # WhenMatchedInsertAll behaviour
  elif _writemode == 'insert_all':
    # Connect to the existing table
    _table = delta.tables.DeltaTable.forPath(spark, _path)
    
    # Create an execution plan
    _plan = (_table
             .alias('table')
             .merge(_df.alias('updates'), _cond)
             .whenMatchedUpdateAll()
             .whenNotMatchedInsertAll()
            )
    _plan.execute()
    return
  
  # WhenMatchedInsertNone behaviour  
  elif _writemode == 'insert_none':
    # Connect to the existing table
    _table = delta.tables.DeltaTable.forPath(spark, _path)
    
    # Create an execution plan
    _plan = (_table
             .alias('table')
             .merge(_df.alias('updates'), _cond)
             .whenNotMatchedInsertAll()
            )
    _plan.execute()
    return
