set -x

DATABRICKS_HOST=$1 # Take PAT in as second argument
DATABRICKS_TOKEN=$2 # Take PAT in as second argument

# For token auth there are two lines expected
# URL, PAT
echo -e "$DATABRICKS_HOST\n$DATABRICKS_TOKEN\n" | databricks --profile auto_qa configure --token