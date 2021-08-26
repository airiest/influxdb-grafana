import threading
import time
import random
from datetime import datetime
from influxdb import InfluxDBClient


class TestInflux():
    def __init__(self):

        host = "localhost"
        port = 8086
        user = "user"
        passwd = "password"
        db = "dbname"
        self.__client = InfluxDBClient(host, port, user, passwd, db)

        self.__thread = threading.Thread(target=self.__woker, args=())
        self.__thread.daemon = True
        self.__thread.start()

    def __woker(self):
        while True:
            tim = datetime.utcnow()
            tag = {"tag": "tagname"}
            val = {}
            for unit_id in range(1, 10, 1):
                val.update([("unit_" + str(unit_id), random.randint(0, 1))])

            print(tim, tag, val)
            self.__write_db("meas", tim, tag, val)

            time.sleep(1.0)

    def __write_db(self, meas, time, tag, data):
        msg = {}
        msg["measurement"] = meas
        msg["time"] = time

        fields = {}
        for key, val in data.items():
            fields[key] = val

        tags = {}
        for key, val in tag.items():
            tags[key] = val

        msg["fields"] = fields
        msg["tags"] = tags

        msglist = [msg]

        try:
            self.__client.write_points(msglist)
        except Exception:
            print("influxdb write error: {}".format(msglist))


if __name__ == '__main__':
    app = TestInflux()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n")
