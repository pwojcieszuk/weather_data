# Installation

Set up:

Prerequisites: _Docker_ (https://docs.docker.com/get-docker/).

```
#In project's root folder
docker compose up --build
```

Access container's bash to perform CLI tasks:

```
docker exec -it crawler bash
```

Initialize the database - this needs to be done just once on project start (or restart):

```
# In the container bash

flask initdb
```

# Usage

Fetch latest stations data:

```
# In the container bash:

flask update-stations
```

Retrieve stations data from the api endpoint:

```
curl / "http://127.0.0.1:5000/get-stations?coordinates={latitude,longitude}&radius={radius_in_km}&date={date YYYY-MM-DD}"

# for examle:
curl / "http://127.0.0.1:5000/get-stations?coordinates=52.82555727245179,-6.9542953829544&radius=250&date=2021-05-29"

```

# Troubleshooting

In case you need restart the whole wthing clean:

```
# Remove containers and volumes
docker compose down -v

#In project's root folder
docker compose up --build
```
