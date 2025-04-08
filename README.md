
# 🐳 Docker Concepts Summary

| **Concept**            | **Description**                                                                 | **Command / Notes**                                                                                   |
|------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Image**              | A read-only template used to create containers                                  | `docker pull image_name`<br>`docker build -t my-image .`                                               |
| **Container**          | A running instance of an image                                                  | `docker run image_name`<br>`docker ps -a` to list all                                                  |
| **Dockerfile**         | File with instructions to build Docker image                                    | Use with `docker build -t image_name .`                                                                |
| **Volumes**            | Persistent storage for containers                                               | `-v volume_name:/path/in/container`                                                                    |
| **Docker Hub**         | Online registry for Docker images                                               | Default public registry for `docker pull`                                                              |
| **Repository**         | A collection of related images (e.g., tags)                                     | Found within a registry                                                                                 |
| **Registry**           | Server that stores Docker images                                                | Docker Hub, GitHub Container Registry, etc.                                                            |
| **Networks**           | Connect multiple containers so they can talk                                    | `docker network create my-network`                                                                     |
| **MongoDB**            | NoSQL database used inside Docker                                               | `docker run mongo`                                                                                     |
| **Mongo Express**      | Web GUI for MongoDB                                                             | `docker run mongo-express`                                                                             |
| **Compose (Docker Compose)** | Tool for defining & running multi-container apps                          | Uses `docker-compose.yml`, started with `docker compose up`                                            |
| **restart: always**    | Policy to auto-restart containers                                               | In Compose: `restart: always`                                                                          |
| **docker exec**        | Run commands inside a running container                                         | `docker exec -it container_name bash` or `psql`, etc.                                                  |
| **docker logs**        | See logs/output of a running container                                          | `docker logs container_name`                                                                           |
| **docker rm**          | Remove a container                                                              | `docker rm container_name`                                                                             |
| **docker rmi**         | Remove an image                                                                 | `docker rmi image_name`                                                                                |
| **docker stop/start**  | Stop or start a container                                                       | `docker stop/start container_name`                                                                     |
| **docker-compose.yml** | YAML file to define services, volumes, networks, etc. for multi-container apps | Contains `services:`, `volumes:`, and `networks:` sections                                             |
| **docker scout**       | Tool to analyze security & dependencies in images                               | `docker scout quickview image_name`                                                                    |
| **docker extensions**  | Add-ons in Docker Desktop for extended functionality                            | View/manage from Docker Desktop > Extensions                                                           |
