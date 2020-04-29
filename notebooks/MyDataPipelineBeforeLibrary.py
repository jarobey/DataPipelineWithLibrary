# Databricks notebook source
usa_confirmed = (
  spark.read
  .option("header", True)
  .option("inferSchema", True)
  .csv("dbfs:/databricks-datasets/COVID/USAFacts/covid_confirmed_usafacts.csv")
)

usa_fatalities = (
  spark.read
  .option("header", True)
  .option("inferSchema", True)
  .csv("dbfs:/databricks-datasets/COVID/USAFacts/covid_deaths_usafacts.csv")
)

# COMMAND ----------

