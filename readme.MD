docker build -t crawler_container --rm .
docker run -it --name crawler --rm crawler_container
docker run -it --name crawler -v "$(pwd)/src:/src" --rm crawler_container
