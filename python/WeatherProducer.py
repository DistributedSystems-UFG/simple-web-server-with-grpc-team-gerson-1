from __future__ import print_function
import datetime
import logging
import random
import time

import grpc
import WeatherService_pb2
import WeatherService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = WeatherService_pb2_grpc.WeatherServiceStub(channel)

        while True:
            time.sleep(5)
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            temperature = random.uniform(20.00, 40.00)
            event = WeatherService_pb2.WeatherEvent(date=date, location=WeatherService_pb2.Location(latitude=const.LATITUDE, longitude=const.LONGITUDE), temperature=temperature)
            response = stub.CreateWeatherEvent(event)
            print ('Added new event: ' + response.status)
        

if __name__ == '__main__':
    logging.basicConfig()
    run()