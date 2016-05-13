#What neighborhoods have similar citibke and taxi trip profiles - clustering
#Source: https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/k_means_example.py

from __future__ import print_function


from numpy import array
from math import sqrt


from pyspark import SparkContext

from pyspark.mllib.clustering import KMeans, KMeansModel


if __name__ == "__main__":
    sc = SparkContext(appName="KMeansApp")  # SparkContext

   
    # Load and parse the data
    data = sc.textFile("s3://irm238FinalProject/input/citibike*")
    parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

    # Build the model (cluster the data)
    clusters = KMeans.train(parsedData, 2, maxIterations=10,
                            runs=10, initializationMode="random")

    # Evaluate clustering by computing Within Set Sum of Squared Errors
    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))

    WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("Within Set Sum of Squared Error = " + str(WSSSE))

    # Save and load model
    clusters.save(sc, "KmeansModel")
    sameModel = KMeansModel.load(sc, "KMeansModel")
    

    sc.stop()