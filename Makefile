start-redis-old:
	(cd redis-old && docker compose -p redis-old up --build)
start-shared-memory:
	(cd shared-memory && docker compose -p shared-memory up --build)
start-shared-volumes:
	(cd shared-volumes && docker compose -p shared-volumes up --build)
start-kafka:
	(cd kafka && docker compose -p kafka up --build)
start-rabbitmq:
	(cd rabbitmq && docker compose -p rabbitmq up --build)
