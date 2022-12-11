docker ps -aq | xargs docker stop | xargs docker rm # Remove all containers

docker run -d -p 50051:50051 guilhermefaleiros/grpc-server:latest | xargs docker logs -f # Run server
docker run -d guilhermefaleiros/grpc-producer:latest | xargs docker logs -f # Run producer
docker run -d guilhermefaleiros/grpc-client:latest | xargs docker logs -f  # Run client