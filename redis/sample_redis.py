import redis

r = redis.Redis('localhost') # connect to redis
r = redis.Redis(host = 'localhost', port = 6379) # specify a port
r = redis.Redis(unix_socket_path = '/tmp/redis.sock') # Unix socket

