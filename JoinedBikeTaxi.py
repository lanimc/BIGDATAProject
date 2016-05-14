#Source:https://github.com/jorgehpo/WeatherTaxiExploration/blob/master/SparkScripts/JoinTaxiWeather.py

from pyspark import SparkContext
import datetime
import pytz 

sc = SparkContext(appName="JoinBikeAndTaxi")

######################################################################
# Bike

#reading bike data

#removing header and splitting " "
file_bike = file_bike.zipWithIndex().filter(lambda (row, index): index > 0).map(lambda (row,index): row.split())



#indexing bike by date and selecting tripduration, start/end latitude and longitude 
def createYearMonthDayHourKey_bike(line):
    utc=pytz.utc
    eastern=pytz.timezone('US/Eastern')
    date = datetime.datetime.strptime(line[1], "%Y%m%d%H%M")
    if date.minute > 30:
        date = date + datetime.timedelta(minutes=30)
    date_gmt = utc.localize(date, is_dst=None)
    date_eastern = date_gmt.astimezone(eastern)
    key = (date_eastern.year, date_eastern.month, date_eastern.day, date_eastern.hour)
    value = (line[1], line[6], line[7], line[10], line[11])
    #value = line
    return(key, value)

file_bike_tindexed = file_bike.map(createYearMonthDayHourKey_bike)

# removing and cleaning duplicate hours
biketrips = file_bike_indexed.reduceByKey(lambda a,b:a, 1)



######################################################################
# Taxi - time in EST Format


#reading taxi data
file_taxi = sc.textFile("s3://jpo286-ds1004-sp16/Project/datasets/yellow_tripdata_2015*")

#removing header and splitting ","
file_taxi = file_taxi.filter(lambda line: line[0:8]!="VendorID").map(lambda row: row.split(","))

# indexing taxi by date
def createYearMonthDayHourKey_taxi(line):
    date = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
    key = (date.year, date.month, date.day, date.hour)
    value = (line[2], line[5], line[6], line[9],line[10])
    return(key, value)



taxitrips = file_taxi.map(createYearMonthDayHourKey_taxi)



######################################################################
# Joining citibike and taxi data
 

joined_data = taxitrips.join(biketrips)

def toCSVLine(data):
    return ','.join([str(d) for d in data[0]]) + ',' + ','.join([str(d) for d in data[1][0]]) + ',' + ','.join([str(d) for d in data[1][1]]) #joining key and  values

lines_out = joined_data.map(toCSVLine)
lines_out.saveAsTextFile('s3://irm238finalproject/output/joined_bike_taxi.csv')