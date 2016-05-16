


import datetime
import pytz
import csv
import matplotlib.pyplot as plt
from StringIO import StringIO
from pyspark import SparkContext


sc = SparkContext(appName="DataMunging")


#reading in bike data
bikedir = sc.textFile("s3://irm238finalproject/input/*tripdata.csv")

bikedir.count() #9937981

#split row into fields using comma delimiter, add index to each field
bikedir = bikedir.zipWithIndex().filter(lambda (row, index): index > 0).map(lambda (row,index): row.split(","))

bikedir.count() #9937980


#create date time key based on start time and pair with tripduration, start/end latitude and longitude . 
#Use pytz to solve any daylight savings issues
#map start time to duration and location


def timekey_bike(line):
    utc=pytz.utc
    eastern=pytz.timezone('US/Eastern')
    date = datetime.datetime.strptime(line[1], "%Y/%m/%d/ %H%:M")
    utcdate = utc.localize(date, is_dst=None)
    date_eastern = utcdate.astimezone(eastern)
    key = (date_eastern.year, date_eastern.month, date_eastern.day, date_eastern.hour)
    value = (line[6], line[7], line[10], line[11])
    return(key, value)

bikedir_tindexed = bikedir.map(timekey_bike)

biketrips = bikedir_tindexed.reduceByKey(lambda a,b:a, 1)

#reading taxi data
taxidir = sc.textFile("s3://irm238finalproject/input/yellow*")

taxidir = taxdir.filter(lambda line: line[0:10]).map(lambda row: row.split(","))

# indexing taxi by date and selecting end trip time, start/end latitude and longitude
def timekey_taxi(line):
    utc=pytz.utc
    eastern=pytz.timezone('US/Eastern')
    date = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
    utcdate = utc.localize(date, is_dst=None)
    date_eastern = utcdate.astimezone(eastern)
    key = (date_eastern.year, date_eastern.month, date_eastern.day, date_eastern.hour)
    value = (line[5], line[6], line[9],line[10])
    return(key, value)


taxidir_tindexed = taxidir.map(timekey_taxi)
taxitrips = taxidir_tindexed.reduceByKey(lambda a,b:a, 1)



# Joining datasets on temporal index
 

joined_data = taxitrips.join(biketrips)

# adding neighborhoods




joined_data.saveAsTextFile('output.txt')

