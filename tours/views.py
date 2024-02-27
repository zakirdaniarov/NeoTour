from django.shortcuts import render
from rest_framework.views import Response, status, APIView
from .models import Tours, TourCategories
from .serializers import *
from datetime import datetime


# Create your views here.
class CategoriesListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = TourCategories.objects.all()
        categories_api = CategoryListAPI(categories, many=True)
        content = {"Categories": categories_api.data}
        return Response(content, status=status.HTTP_200_OK)


class CategoryToursListAPIView(APIView):
        def get(self, request, *args, **kwargs):
            category = TourCategories.objects.all().get(id=kwargs['pk'])
            tours = category.tours.all()
            tours_api = TourListAPI(tours, many=True)
            content = {"Category Tours": tours_api.data}
            return Response(content, status=status.HTTP_200_OK)


class ToursListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tours = Tours.objects.all()
        tours_api = TourListAPI(tours, many=True)
        content = {"Tours": tours_api.data}
        return Response(content, status=status.HTTP_200_OK)


class RecommendedToursListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        recommended_tours = Tours.objects.all().filter(is_recommended=True)
        recommended_tours_api = RecommendedTourListAPI(recommended_tours, many=True)
        content = {"Recommended Tours": recommended_tours_api.data}
        return Response(content, status=status.HTTP_200_OK)

class RecommendedToursListBySeasonAPIView(APIView):
    def get(self, request, *args, **kwargs):
        winter_recommended_tours = Tours.objects.all().filter(season='Winter')
        spring_recommended_tours = Tours.objects.all().filter(season='Spring')
        summer_recommended_tours = Tours.objects.all().filter(season='Summer')
        fall_recommended_tours = Tours.objects.all().filter(season='Fall')
        winter_recommended_tours_api = RecommendedTourListAPI(winter_recommended_tours, many=True)
        spring_recommended_tours_api = RecommendedTourListAPI(spring_recommended_tours, many=True)
        summer_recommended_tours_api = RecommendedTourListAPI(summer_recommended_tours, many=True)
        fall_recommended_tours_api = RecommendedTourListAPI(fall_recommended_tours, many=True)
        content = {"Winter Recommended Tours": winter_recommended_tours_api.data,
                   "Spring Recommended Tours": spring_recommended_tours_api.data,
                   "Summer Recommended Tours": summer_recommended_tours_api.data,
                   "Fall Recommended Tours": fall_recommended_tours_api.data,}
        return Response(content, status=status.HTTP_200_OK)


class TourInfoReservationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            tour = Tours.objects.all().get(id = kwargs['pk'])
        except:
            return Response({'data': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        reviews = tour.reviews.all()
        tour_api = TourInfoAPI(tour)
        review_api = ReviewListAPI(reviews, many=True)
        content = {"Tour Info": tour_api.data,
                   "Reviews": review_api.data,}
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request.data['tour_name'] = kwargs['pk']
        serializer = ReservationAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Order has been submitted successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "message": "There is an error"},
                        status=status.HTTP_400_BAD_REQUEST)


class TourReservationsListAPIView(APIView):
        def get(self, request, *args, **kwargs):
            tour = Tours.objects.all().get(id=kwargs['pk'])
            reservations = tour.reservations.all()
            reservations_api = ReservationAPI(reservations, many=True)
            content = {"Reservations": reservations_api.data}
            return Response(content, status=status.HTTP_200_OK)


class ReviewListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tour = Tours.objects.all().get(id=kwargs['pk'])
        reviews = tour.reviews.all()
        reviews_api = ReviewListAPI(reviews, many=True)
        content = {"Reviews": reviews_api.data}
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request.data['tour'] = kwargs['pk']
        serializer = ReviewListAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Review has been submitted successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "message": "There is an error"},
                        status=status.HTTP_400_BAD_REQUEST)





