start-redis-old:
	(cd redis-old && docker compose -p redis-old up --build)
start-shared-memory:
	(cd shared-memory && docker compose -p shared-memory up --build)
