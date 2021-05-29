```
docker compose up --build
docker exec -it crawler bash
flask initdb
flask update-stations

curl / "http://127.0.0.1:5000/get-stations?coordinates=52.82555727245179,-6.9542953829544&radius=250&date=2021-05-29"
curl / "http://127.0.0.1:5000/get-stations?coordinates=latitude,longitude&radius=250&date=2021-05-29"

docker compose down -v
```
