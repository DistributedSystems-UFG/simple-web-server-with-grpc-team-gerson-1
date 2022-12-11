from concurrent import futures

import grpc
import WeatherService_pb2
import WeatherService_pb2_grpc

eventsDB = []

class WeatherServer(WeatherService_pb2_grpc.WeatherServiceServicer):

    def CreateWeatherEvent(self, request, context):
        data = {
            'date': request.date,
            'location': {
                'latitude': request.location.latitude,
                'longitude': request.location.longitude,
            },
            'temperature': request.temperature,
        }
        print(f"Received event: {data}")
        eventsDB.append(data)
        return WeatherService_pb2.StatusReply(status='OK')
    
    def SearchEvents(self, request, context):
        data = [
            event for event in eventsDB if (event['location']['longitude'] == request.location.longitude) and (event['location']['latitude'] == request.location.latitude) and event['date'] == request.date
        ]
        return WeatherService_pb2.WeatherEventList(weather_event_data=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    WeatherService_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
