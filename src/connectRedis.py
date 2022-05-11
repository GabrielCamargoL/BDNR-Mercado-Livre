import redis

def connect():
  redisConn = redis.Redis(
    host='host',
    port='porta',
    password='senha'
  )

  return redisConn