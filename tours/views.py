from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.views import Response, status, APIView
from .models import Tours, TourCategories
from .serializers import *
from datetime import datetime


# Create your views here.
class CategoriesListAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of categories",
            description="This endpoint allows you to get information about various categories",
    )
    def get(self, request, *args, **kwargs):
        categories = TourCategories.objects.all()
        categories_api = CategoryListAPI(categories, many=True)
        content = {"Categories": categories_api.data}
        return Response(content, status=status.HTTP_200_OK)


class CategoryToursListAPIView(APIView):
        @extend_schema(
            summary="Displaying lists of tours in each category",
            description="This endpoint allows you to get information about tours divided by category",
    )
        def get(self, request, *args, **kwargs):
            category = TourCategories.objects.all().get(id=kwargs['pk'])
            tours = category.tours.all()
            tours_api = TourListAPI(tours, many=True)
            content = {"Category Tours": tours_api.data}
            return Response(content, status=status.HTTP_200_OK)


class ToursListAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of tours",
            description="This endpoint allows you to get information about all the tours",
    )
    def get(self, request, *args, **kwargs):
        tours = Tours.objects.all()
        tours_api = TourListAPI(tours, many=True)
        content = {"Tours": tours_api.data}
        return Response(content, status=status.HTTP_200_OK)


class RecommendedToursListAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of recommended tours",
            description="This endpoint allows you to get information about recommended tours",
    )
    def get(self, request, *args, **kwargs):
        recommended_tours = Tours.objects.all().filter(is_recommended=True)
        recommended_tours_api = RecommendedTourListAPI(recommended_tours, many=True)
        content = {"Recommended Tours": recommended_tours_api.data}
        return Response(content, status=status.HTTP_200_OK)

class RecommendedToursListBySeasonAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of recommended tours for each seasons",
            description="This endpoint allows you to get information about recommended tours for each season",
    )
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


class ToursListDetailAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of tours with description and reviews",
            description="This endpoint allows you to get information about all the tours with description and reviews",
    )
    def get(self, request, *args, **kwargs):
        tours = Tours.objects.all()
        data_list = []
        for tour in tours:
            tour_api = TourListDetailAPI(tour)
            reviews = tour.reviews.all()
            review_api = ReviewListAPI(reviews, many=True)
            data = {"Tour Info": tour_api.data,
                       "Reviews": review_api.data,}
            data_list.append(data)
        content = {"All Tours": data_list}
        return Response(content, status=status.HTTP_200_OK)

class RecommendedToursListDetailAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of Recommended tours with description and reviews",
            description="This endpoint allows you to get information about the Recommended tours with description and reviews",
    )
    def get(self, request, *args, **kwargs):
        tours = Tours.objects.all().filter(is_recommended=True)
        data_list = []
        for tour in tours:
            tour_api = TourListDetailAPI(tour)
            reviews = tour.reviews.all()
            review_api = ReviewListAPI(reviews, many=True)
            data = {"Tour Info": tour_api.data,
                       "Reviews": review_api.data,}
            data_list.append(data)
        content = {"Recommended Tours": data_list}
        return Response(content, status=status.HTTP_200_OK)


class TourInfoReservationAPIView(APIView):
    @extend_schema(
            summary="Displaying detailed information about the tour",
            description="This endpoint allows you to get detailed information about the tour: name, image,"
                        "location, description and review left by clients of the tour",
    )
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

    @extend_schema(
            summary="Posting reservation information",
            description="This endpoint allows you to reserve a tour using a phone number and showing the number of people",
    )
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
        @extend_schema(
            summary="Displaying lists of reservations for each tour",
            description="This endpoint allows you to get information about reservations for each tour",
        )
        def get(self, request, *args, **kwargs):
            tour = Tours.objects.all().get(id=kwargs['pk'])
            reservations = tour.reservations.all()
            reservations_api = ReservationAPI(reservations, many=True)
            content = {"Reservations": reservations_api.data}
            return Response(content, status=status.HTTP_200_OK)


class ReviewListCreateAPIView(APIView):
    @extend_schema(
            summary="Displaying lists of reviews for each tour",
            description="This endpoint allows you to get information about reviews for each tour",
    )
    def get(self, request, *args, **kwargs):
        tour = Tours.objects.all().get(id=kwargs['pk'])
        reviews = tour.reviews.all()
        reviews_api = ReviewListAPI(reviews, many=True)
        content = {"Reviews": reviews_api.data}
        return Response(content, status=status.HTTP_200_OK)

    @extend_schema(
            summary="Posting a tour review",
            description="This endpoint allows you to post a tour review",
        )
    def post(self, request, *args, **kwargs):
        request.data['tour'] = kwargs['pk']
        serializer = ReviewListAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Review has been submitted successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "message": "There is an error"},
                        status=status.HTTP_400_BAD_REQUEST)





