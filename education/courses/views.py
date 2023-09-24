from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from .models import Lesson, Product, UserAvailableProduct, UserProgress
from .serializers import LessonSerializers, AvailableProductSerializer, UserProgressSerializer


class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

    def get_queryset(self):
        lessons = list(Lesson.objects.filter(product__useravailableproduct__user_id=self.request.user.id).values())
        print(lessons)
        list_of_id = [x['id'] for x in lessons]
        print(list_of_id)
        lessons_data = UserProgress.objects.filter(lesson__in=list_of_id)
        return lessons_data


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

    def get_queryset(self):
        # curr_user = self.request.user.id
        # print(curr_user)

        lessons = Lesson.objects.filter(product__useravailableproduct__user_id=self.request.user.id)
        # print(lessons, type(lessons))
        # products = Product.objects.filter(useravailableproduct__user_id=curr_user).values()
        # print(products, type(products))
        # users_product_values = UserAvailableProduct.objects.filter(user_id=curr_user).values()
        # users_product_values = list(users_product_values)
        # user_available_product = UserAvailableProduct.objects.filter(user_id=curr_user)
        # print(users_product_values, type(users_product_values))
        return lessons


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = AvailableProductSerializer


# from .models import UserData
# from .serializers import UserDataSerializer


# class UserDataViewSet(viewsets.ModelViewSet):
#     queryset = UserData.objects.all()
#     serializer_class = UserDataSerializer

    # def get_queryset(self):
    #     curr_user = self.request.user.id
    #     user_available_videos = UserData.objects.filter(user_id=curr_user)
    #     return user_available_videos


# class UserDataAPIView(generics.ListCreateAPIView):
#     queryset = UserData.objects.all()
#     serializer_class = UserDataSerializer

    # def get_queryset(self):
    #     curruser = self.request.user
    #     return UserData.objects.filter(user=curruser)
