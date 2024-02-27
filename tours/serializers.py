from rest_framework.serializers import ModelSerializer
from .models import *


class CategoryListAPI(ModelSerializer):
    class Meta:
        model = TourCategories
        fields = ['name']


class TourListAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['name', 'category', 'image', 'location']


class RecommendedTourListAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['name', 'image', 'location']


class TourInfoAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['name', 'image', 'location', 'description']


class ReservationAPI(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['tour_name', 'phone_number', 'order_comment', 'people_num']


class ReviewListAPI(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['nickname', 'image', 'review_text', 'created_at']

