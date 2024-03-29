from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryToursListAPIView.as_view(), name='category_tours'),
    path('tours/', ToursListAPIView.as_view(), name='tours'),
    path('tours/recommended/', RecommendedToursListAPIView.as_view(), name='recommended_tours'),
    path('detailed-tours/', ToursListDetailAPIView.as_view(), name='tours'),
    path('detailed-tours/recommended/', RecommendedToursListDetailAPIView.as_view(), name='recommended_tours'),
    path('tours/seasons/', RecommendedToursListBySeasonAPIView.as_view(), name='recommended_tours'),
    path('tours/<int:pk>/', TourInfoAPIView.as_view(), name='tour_info'),
    path('tours/<int:pk>/reserve/', TourReservationAPIView.as_view(), name='tour_reserve'),
    path('tours/<int:pk>/reviews/', ReviewListAPIView.as_view(), name='tour_reviews'),
    path('tours/<int:pk>/create-review/', ReviewCreateAPIView.as_view(), name='tour_create-review'),
    path('tours/<int:pk>/reservations/', TourReservationsListAPIView.as_view(), name='tour_reservations'),
]
