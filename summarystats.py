#Summary stats of data
# source:https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/summary_statistics_example.py

from __future__ import print_function

from pyspark import SparkContext

import numpy as np

from pyspark.mllib.stat import Statistics


if __name__ == "__main__":
    sc = SparkContext(appName="SummaryStatisticsExample")  # SparkContext

  
    bike = sc.textFile("s3://irm238FinalProject/input/*-citibike-tripdata.csv")  # an RDD of Vectors

	taxi = sc.textFile("s3://irm238FinalProject/input/*-citibike-tripdata.csv") 
   
    # Compute column summary statistics.
    summary = Statistics.colStats(bike)
    print(summary.mean())  # a dense vector containing the mean value for each column
    print(summary.variance())  # column-wise variance
    print(summary.numNonzeros())  # number of nonzeros in each column
    
    summary = Statistics.colStats(taxi)
    print(summary.mean())  # a dense vector containing the mean value for each column
    print(summary.variance())  # column-wise variance
    print(summary.numNonzeros())  # number of nonzeros in each column

    sc.stop()