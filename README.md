# influxdb-grafana

## Start
```
$ docker-compose up -d
```

## Open Grafana
```
http://localhost:3000/
```

## Setup Datasource
![](./doc/datasource_setup.png)

## Test
```
$ pip install -r requirements.txt
$ python test.py
```

![](./doc/panel_setup.png)