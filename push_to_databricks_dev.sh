set -x

UNIFIED_PATH="/Users/jason.robey@databricks.com/my_development/DataPipelineWithLibrary"

databricks --profile jdr_dev workspace import_dir -o notebooks $UNIFIED_PATH