Understanding the Complex Interactions in New York City
-------------------------------------------------------

"Cities are the loci of resource consumption, of economic activity, and of innovation; they are the cause of our looming sustainability problems but also where those problems must be solved. Our increasing ability to collect, transmit, and store data, coupled with the growing trend towards openness, creates a unique opportunity that can benefit government, science, citizens and industry.

Urban data is unique in that it captures the behavior of the different components of a city, namely its citizens, existing infrastructure (physical and policies), the environment (e.g.: weather), and interactions between these elements. The availability of these data makes it possible to not only better understand the individual components but also obtain insights into how they interact.

In this project, you will work with spatio-temporal urban data and try to find and explain some interactions between these elements of the city. You will use event detection and correlation techniques to analyze different types of urban data and uncover interesting relationships among them.""




My Questions
-------------
Is there any correlation in the number of trips per hour between citibike and taxi data
  by neighborhood?

What neighborhoods have similar travel patterns for destinations (start end pair) (start lat/long) or ended (end lat/long) of citibike and taxi trips taken?

Does the number and destination of taxi trips predict the number of citibike trips?




DOCUMENTS
--------------------------
Project Report and Progress Log: https://docs.google.com/a/nyu.edu/document/d/1qw7-NyXSNQVSBq2X0uLG60X0CEyBI1oGmP-muqOxMLk/edit?usp=sharing

Github Repo: https://github.com/lanimc/BIGDATAProject.git

S3 Bucket: https://s3.amazonaws.com/s3/home?region=us-west-2#&bucket=irm238finalproject&prefix=

Poster: 

Code Method Sources: 
  Apache Spark github examples available at https://github.com/apache/spark/tree/master/examples/src/main/python/mllib
  Karau, Konwinski, Wendell & Zaharia, Learning Spark: Lightning-FAST Big Data Analysis O'REILLY Books 2015





DATA
-------------

- 2015 Yellow Taxi Dataset

  Available at http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
  Metadata available at: http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
  Temporal data is in EST (second resolution).
  Spatial data is in GPS.

  Field List: VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, Passenger_count, Trip_distance, Pickup_longitude, Pickup_latitude, RateCodeID, Store_and_fwd_flag, Dropoff_longitude, Dropoff_latitude, Payment_type, Fare_amount, Extra, MTA_tax, Improvement_surcharge, Tip_amount, Tolls_amount, Total_amount.



- 2015 Citi Bike Trip Histories

  Available at: https://www.citibikenyc.com/system-data ("Citi Bike Trip Histories" section)
  Temporal data is in EST (second resolution).
  Spatial data is in GPS.


- Community districts clipped to shoreline shapefile
  Available at:http://www1.nyc.gov/site/planning/data-maps/open-data/districts-download-metadata.page
  TITLE New York City Community Districts CREATION DATE 2/23/2016
  PUBLICATION DATE 2/23/2016
  EDITION 16A
  PRESENTATION FORMATS * digital map
  SERIES
  NAME BYTES of the BIG APPLE ISSUE 16A


 -Places (Formerly "Areas of Interest")

  The New York City Places point file was created as a guide to New York City’s non-neighborhood place locations that appear in “New York: A City of Neighborhoods.” These place locations include parks, cemeteries, and airports. Best estimates of label centroids were established at a 1:1,000 scale, but are ideally viewed at a 1:50,000 scale.

  Geographic files of areas of interest labels as depicted in New York: A City of Neighborhoods.

  Release............. 2014.8 
  Date of Data..... August 2014



