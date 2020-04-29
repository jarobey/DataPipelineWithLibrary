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

# unpivot

# usa_confirmed = usa_confirmec.expr("stack(3, 'Canada', Canada, 'China', China, 'Mexico', Mexico) as (Country,Total)"
import datetime
from pyspark.sql.functions import col, expr

base = datetime.datetime(2020,1,21,0,0,0)
date_list = [(base + datetime.timedelta(days=x)) for x in range(0, 47)]
date_str_list = ['{1}/{2}/{0}'.format(dt.year, dt.month, dt.day) for dt in date_list]
print('dates = {0}'.format(date_str_list))

stack_string = "stack(3, "
first = True
for date_str in date_str_list:
  if not first: stack_string += ","
  else: first = False
  stack_string += "'{0}'".format(date_str)

stack_string += ') as (Day, Confirmed)'

print(stack_string)

# unrolled_confirmed = usa_confirmed.select(col('County Name'),expr(stack_string))
# display(unrolled_confirmed)

print("I just want to see success")