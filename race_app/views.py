from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
import random
import time
from django.shortcuts import render
import requests
from .utils import generate_random_color

def garage(request):
    # Fetch JSON data (example if from a local file)
    # with open('path/to/your/data.json') as f:
    #     car_brands = json.load(f)

    # OR fetch from an external API
    response = requests.get('http://127.0.0.1:8000/api/cars/')  # Update with your API URL
    car_brands = response.json() if response.status_code == 200 else []

    return render(request, 'garage.html', {'car_brands': car_brands})

def winners(request):
    return render(request, 'winners.html')


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()  # Define the queryset
    serializer_class = CarSerializer  # Define the serializer class

    def create_random_cars(self, request):
        # Create random cars
        num_cars = 100  # You can change this to create more or fewer cars
        cars = []
        
        for _ in range(num_cars):
            car_name = f"Car {_ + 1}"  # Give the car a name (e.g., "Car 1")
            car = Car(brand=car_name, color=generate_random_color())  # Assign a random color
            car.save()
            cars.append({"brand": car.brand, "color": car.color})  # Use 'brand' instead of 'name'

        return Response(cars)