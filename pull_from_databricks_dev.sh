set -x

UNIFIED_PATH="/Users/jason.robey@databricks.com/my_development/DataPipelineWithLibrary"

databricks --profile jdr_dev workspace export_dir -o $UNIFIED_PATH notebooks