import findspark
findspark.init("/opt/spark/spark-3.1.1-bin-hadoop3.2")

from pyspark.sql import *  
import time

spark = SparkSession.builder.getOrCreate()
df1 = spark.read.json(r"/home/vedang/Desktop/LSDP/Project/tweets1.json") 
df1.show()
df1.createOrReplaceTempView("tweets1")

q2 = spark.sql("desc tweets1")
q2.show()

start = time.time()
q1 = spark.sql("SELECT count(*) FROM tweets1")
q1.show()
end = time.time()
print("Time taken = " + str(end - start))

start = time.time()
q5 = spark.sql("SELECT count(*) as count, user.name from tweets1 where user.name is not null group by user.name order by count desc limit 10")
q5.show()
end = time.time()
print("Time taken = " + str(end - start))

start = time.time()
q3 = spark.sql("SELECT user.name, max(user.followers_count) as followers_count FROM tweets1 WHERE text like '%AAPL%' group by user.name order by followers_count desc limit 15")
q3.show()
end = time.time()
print("Time taken = " + str(end - start))

q3 = spark.sql("SELECT place.country,count(*) AS count FROM tweets1 GROUP BY place.country ORDER BY count DESC limit 10")

start = time.time()
q3 = spark.sql("SELECT user.name, max(user.followers_count) as followers_count FROM tweets1 WHERE text like '%AAPL%' group by user.name order by followers_count desc limit 15")
q3.show()
end = time.time()
print("Time taken = " + str(end - start))

q4 = spark.sql("SELECT substring(created_at,1,3) as day,count(*) as count from tweets1 group by substring(created_at,1,3)")
q4.show()

start = time.time()
q5 = spark.sql("SELECT count(*) as count, user.name from tweets1 where user.name is not null group by user.name order by count desc limit 10")
q5.show()
end = time.time()
print("Time taken = " + str(end - start))

start = time.time()
q5 = spark.sql("select user.name,retweet_count from tweets1 where retweet_count in (select max(retweet_count) from tweets1);")
q5.show()
end = time.time()
print("Time taken = " + str(end - start))

q6 = spark.sql("SELECT substring(created_at,5,3) as month, count(*) as count from tweets1 group by substring(created_at,5,3)")
q6.show()

q7 = spark.sql("SELECT user.location,count(*) as count FROM tweets1 WHERE place.country='United States' AND user.location is not null GROUP BY user.location ORDER BY count DESC LIMIT 15")
q7.show()

df2 = spark.read.csv(r"/home/vedang/Desktop/LSDP/Project/out_data.csv") 
df2.show()

df2.createOrReplaceTempView("out_data")

start = time.time()
q8 = spark.sql("select _c5 as polarity from out_data limit 10")
q8.show()
end = time.time()
print("Time taken = " + str(end - start))

start = time.time()
q9 = spark.sql("select _c3 as screenname,_c5 as polarity from out_data where _c5>0.0")
q9.show()
end = time.time()
print("Time taken = " + str(end - start))

start = time.time()
q9 = spark.sql("SELECT count(*) FROM out_data")
q9.show()
end = time.time()
print("Time taken = " + str(end - start))
