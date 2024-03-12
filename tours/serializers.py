from rest_framework.serializers import ModelSerializer
from .models import *


class CategoryListAPI(ModelSerializer):
    class Meta:
        model = TourCategories
        fields = ['id', 'name']


class TourListAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'category', 'image', 'location']


class TourListDetailAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'category', 'image', 'description', 'location']


class RecommendedTourListAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'image', 'location']


class TourInfoAPI(ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'image', 'location', 'description']


class ReservationAPI(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'tour_name', 'phone_number', 'order_comment', 'people_num']


class ReviewListAPI(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'nickname', 'image', 'review_text', 'created_at']

