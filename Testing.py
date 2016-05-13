#hypothesis testing, does taxi start and stop volume predit citibike start and stop volume 
#source:https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/hypothesis_testing_example.py

from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.linalg import Matrices, Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.stat import Statistics
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="HypothesisTestingExample")

    # $example on$
    vec = Vectors.dense(0.1, 0.15, 0.2, 0.3, 0.25)  # a vector composed of the frequencies of events

    # compute the goodness of fit. If a second vector to test against
    # is not supplied as a parameter, the test runs against a uniform distribution.
    goodnessOfFitTestResult = Statistics.chiSqTest(vec)

    # summary of the test including the p-value, degrees of freedom,
    # test statistic, the method used, and the null hypothesis.
    print("%s\n" % goodnessOfFitTestResult)

    mat = Matrices.dense(3, 2, [1.0, 3.0, 5.0, 2.0, 4.0, 6.0])  # a contingency matrix

    # conduct Pearson's independence test on the input contingency matrix
    independenceTestResult = Statistics.chiSqTest(mat)

    # summary of the test including the p-value, degrees of freedom,
    # test statistic, the method used, and the null hypothesis.
    print("%s\n" % independenceTestResult)

    obs = sc.parallelize(
        [LabeledPoint(1.0, [1.0, 0.0, 3.0]),
         LabeledPoint(1.0, [1.0, 2.0, 0.0]),
         LabeledPoint(1.0, [-1.0, 0.0, -0.5])]
    )  # LabeledPoint(feature, label)

    # The contingency table is constructed from an RDD of LabeledPoint and used to conduct
    # the independence test. Returns an array containing the ChiSquaredTestResult for every feature
    # against the label.
    featureTestResults = Statistics.chiSqTest(obs)

    for i, result in enumerate(featureTestResults):
        print("Column %d:\n%s" % (i + 1, result))
    # $example off$

    sc.stop()