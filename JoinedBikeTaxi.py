#Source:https://github.com/jorgehpo/

from pyspark import SparkContext
import datetime
import pytz 

sc = SparkContext(appName="DataMunging")


#reading in bike data
bikedir = sc.textFile("s3://irm238finalproject/input/*tripdata.csv")

bikedir = bikedir.zipWithIndex().filter(lambda (row, index): index > 0).map(lambda (row,index): row.split(","))


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
    return(key, value)

bikedir_tindexed = bikedir.map(createYearMonthDayHourKey_bike)

biketrips = bikedir_tindexed.reduceByKey(lambda a,b:a, 1)
biketrips.persist()

#reading taxi data
taxidir = sc.textFile("s3://jpo286-ds1004-sp16/Project/datasets/yellow*")

taxidir = taxdir.filter(lambda line: line[0:8]!="VendorID").map(lambda row: row.split(","))

# indexing taxi by date and selecting end trip time, start/end latitude and longitude
def createYearMonthDayHourKey_taxi(line):
    date = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
    key = (date.year, date.month, date.day, date.hour)
    value = (line[2], line[5], line[6], line[9],line[10])
    return(key, value)


taxitrips = file_taxi.map(createYearMonthDayHourKey_taxi)
taxitrips.persist()



# Joining datasets on temporal index
 

joined_data = taxitrips.join(biketrips)

# adding neighborhoods


joined_data.saveAsTextFile('s3://irm238finalproject/output/')