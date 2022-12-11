from __future__ import print_function
import datetime
import logging
import time

import grpc
import WeatherService_pb2
import WeatherService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = WeatherService_pb2_grpc.WeatherServiceStub(channel)

        while True:
            time.sleep(2)
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            response = stub.SearchEvents(WeatherService_pb2.Query(date=date, location=WeatherService_pb2.Location(latitude=const.LATITUDE, longitude=const.LONGITUDE)))
            print(f"Found {len(response.weather_event_data)} registers for {date}.")
            stub = WeatherService_pb2_grpc.WeatherServiceStub(channel)

if __name__ == '__main__':
    logging.basicConfig()
    run()