set -x

# Paths to place the new production libraries and notebooks
VERSION="0.1"
DEPLOY_STRING=$VERSION"__$(date +%Y%m%d_%H%M%S)"
# LIBRARY="pipeline-$VERSION.egg"
NOTEBOOK="MyDataPipelineBeforeLibrary"
UNIFIED_PATH="/Automation/qa/data_pipeline/$DEPLOY_STRING"
PRODUCTION_LIB_PATH="dbfs:$UNIFIED_PATH/$LIBRARY"
PRODUCTION_WORKSPACE_PATH=$UNIFIED_PATH

# Copy the library from local filesystem to dbfs.
# cd pipeline_library
# python3 setup.py bdist_egg
# mv dist/pipeline-$VERSION-py3.?.egg dist/pipeline-$VERSION.egg
# databricks --profile auto_deploy fs cp dist/pipeline-$VERSION.egg $PRODUCTION_LIB_PATH
# cd ..

# Recursively import the appropriate notebooks to the production folder.
databricks --profile auto_qa workspace import_dir notebooks $PRODUCTION_WORKSPACE_PATH

# Deploy the job
#sed "s/__LIBRARY__/$PRODUCTION_LIB_PATH/g; s/__NOTEBOOK__/$NOTEBOOK/g" jobconfig.json > tempconf.json
sed "s/__VERSION__/$DEPLOY_STRING/g; s/__LIBRARY__/$LIBRARY/g;  s/__NOTEBOOK__/$NOTEBOOK/g;" jobconfig.json > tempconf.json
RESPONSE=`databricks --profile auto_qa jobs create --json-file tempconf.json`
rm tempconf.json

# Run the job--in a deployment scenario we would lso capture the run_id and watch for completion to execute further tests
[[ $RESPONSE =~ .*job_id\"\:\ ([0-9]+) ]]
JOB_ID=${BASH_REMATCH[1]}
echo $JOB_ID
databricks --profile auto_qa jobs run-now --job-id $JOB_ID