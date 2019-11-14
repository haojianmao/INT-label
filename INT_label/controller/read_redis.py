import redis
import numpy as np
import time


def read_coverage(r=redis.Redis(unix_socket_path='/var/run/redis/redis.sock', db=4)):
	keys = r.keys()
	t = r.lrange('coverage', 0, -1)
	t = map(float, t)
	# print(t[-320:-20])
	# print(r.lrange('time',0,-1))
	t = np.array(t)
	# print(t.mean())
	print(t[0:10].mean())
	# print(r.llen('coverage'),r.llen('time'))


def read3(r):
	keys = r.keys()
	for key in keys:
		print(key, r.get(key))


def read_loss(r3=redis.Redis(unix_socket_path='/var/run/redis/redis.sock', db=3)):
	send = int(r3.get('send'))
	rece = int(r3.get('receive'))
	print((send - rece) * 1.0 / send)


def read2(r):
	keys = r.keys()
	for key in keys:
		print(key, r.lrange(key, 0, -1))


def read_data(r=redis.Redis(unix_socket_path='/var/run/redis/redis.sock', db=1)):
	keys = r.keys()
	l = []
	for i in range(50):
		a = 0
		num = 0
		for key in keys:
			if r.lrange(key, 0, -1)[0] != '-1':
				a += float(r.lindex(key, 1))
				num += 1
		l.append(a / num)
		time.sleep(0.1)
	l = np.array(l)
	print(l.mean())
	print(l.std())


if __name__ == '__main__':
	r2 = redis.Redis(unix_socket_path='/var/run/redis/redis.sock', db=1)
	r3 = redis.Redis(unix_socket_path='/var/run/redis/redis.sock', db=3)
	# read2(r2)
	# time.sleep(20)
	read3(r3)
	# read_data()

	# read_coverage()
	for i in range(50):
		read_coverage()
		time.sleep(0.1)
	read_loss()
