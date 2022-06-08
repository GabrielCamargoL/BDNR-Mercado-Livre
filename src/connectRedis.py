import redis

def connect():
  redisConn = redis.Redis(
    host='redis-18734.c11.us-east-1-2.ec2.cloud.redislabs.com',
    port='18734',
    password='nYckWRumUwKwOLgqVDFD3nIgchp2StQA'
  )

  return redisConn