# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /dbfs/databricks-datasets/COVID

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets/COVID/USAFacts"))

# COMMAND ----------

dbutils.fs.head("dbfs:/databricks-datasets/COVID/USAFacts/USAFacts_readme.md")

# COMMAND ----------

usa_confirmed = spark.read.csv("dbfs:/databricks-datasets/COVID/USAFacts/covid_confirmed_usafacts.csv")
display(usa_confirmed)

# COMMAND ----------

usa_confirmed = (
  spark.read
  .option("header", True)
  .option("inferSchema", True)
  .csv("dbfs:/databricks-datasets/COVID/USAFacts/covid_confirmed_usafacts.csv")
)
display(usa_confirmed)

# COMMAND ----------

usa_fatalities = (
  spark.read
  .option("header", True)
  .option("inferSchema", True)
  .csv("dbfs:/databricks-datasets/COVID/USAFacts/covid_deaths_usafacts.csv")
)
display(usa_fatalities)

# COMMAND ----------

# TODO: unpivot each by day and join to put confirmed and deaths together

# COMMAND ----------

from pyspark.sql.functions import col, sum

march_confirmed = usa_confirmed.select(col('State').alias('state'), col('3/1/20').alias('march_confirmed')).groupBy(col('state')).agg(sum('march_confirmed').alias('march_confirmed'))

display(march_confirmed)

# COMMAND ----------

display(march_confirmed)