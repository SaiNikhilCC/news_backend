from jsonschema import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . import serialzers
from rest_framework.permissions import IsAuthenticated
from . import models
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
from news_backend.customauth import CustomAuthentication
from django.http import JsonResponse
from rest_framework import generics

from superior.serializers import CategoriesSerializer, EpaperSerializer, NewsEditSerializer
from superior.models import Categories, Epaper, News, NewsComments, States, Districts, Mandal, NewsImages, Polls, Advertisement, JobPostings, Users


# FAST2SMS API To Send OTP Code
url = "https://www.fast2sms.com/dev/bulkV2"


def sendsms(num, phone):
    payload = f"sender_id=FTWSMS&message=To Verify Your Mobile Number with Time2Time News is {num} &route=v3&numbers={phone}"
    print(payload)
    headers = {
        'authorization': "ulBGWHeNb4qJ9KmyA1fip0RdPYh6kXjwEscTSQ3ODFvC2rgnIZezvgnxpTBcjmlJZQAkY7LKVSHGMU4d",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = "sent"
    response = requests.request("POST", url, data=payload, headers=headers)
    return True
# End of FAST2SMS API


# USER REGISTRATION AND REQUESTS FOR OTP
class RegisterUser(APIView):
    try:
        def post(self, request):
            serializer = serialzers.UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'some error occurred'})
            serializer.save()
            otp = serializer.data['otp']
            phone = serializer.data['phone']
            # sendsms(otp,phone)
            print("OTP to Verify Your Number is : ",
                  otp, " -----> sent to : ", phone)
            return Response({
                'status': 200,
                'data': serializer.data,
                'message': 'success'
            })

    except Exception as e:
        raise ValidationError('somthing went wrong')


# USER ENTERS OTP AND GETS VERIFIED BASED ON HIS UUID AND OTP
class VerifyOtp(APIView):
    try:
        def post(self, request):
            
            if Users.objects.filter(uid=request.data["uid"], otp=request.data["otp"]):
                user = Users.objects.get(uid=request.data['uid'])
                user.is_verified = True
                user.otp = ""
                user.save()
                refresh = AccessToken.for_user(user)

                updated_user = Users.objects.filter(uid=request.data["uid"])
                serializer = serialzers.UserSerializer(updated_user, many=True)

                response = Response({
                    'status': 200,
                    'data': serializer.data,
                    'access': str(refresh),
                    'message': 'success'
                })
                response.content_type = "application/json"
                return response
            else:
                return Response({
                    'status': 400,
                    'message': 'incorrect otp'
                })
    except Exception as e:
        raise ValidationError('something went wrong')


# GET API for News Posts Without Token Authentication
class NewsPostsAPIView(APIView):
    def get(self, request):
        news_posts = News.objects.filter(status="published")
        serializer = serialzers.NewsSerializersForEndUsers(
            news_posts, many=True)

        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'all news posts fetched'
        })


class StateCategoryNewsList(APIView):
    def get(self, request, state_id, category_id):
        category = Categories.objects.get(pk=category_id)
        state = States.objects.get(pk=state_id)
        news_posts = News.objects.filter(state=state, category=category)
        serializer = serialzers.NewsSerializersForEndUsers(
            news_posts, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'state category news posts fetched'
        })


# News Posts Based on Districts
class DistrictCategoryNewsList(APIView):
    def get(self, request, district_id, category_id):
        category = Categories.objects.get(pk=category_id)
        district = Districts.objects.get(pk=district_id)
        news_posts = News.objects.filter(district=district, category=category)
        serializer = serialzers.NewsSerializersForEndUsers(
            news_posts, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'district category news posts fetched'
        })


# News Posts Based on Mandal
class MandalCategoryNewsList(APIView):
    def get(self, request, mandal_id, category_id):
        category = Categories.objects.get(pk=category_id)
        mandal = Mandal.objects.get(pk=mandal_id)
        news_posts = News.objects.filter(mandal=mandal, category=category)
        serializer = serialzers.NewsSerializersForEndUsers(news_posts, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'mandal category news posts fetched'
        })


# GET API for Particular News Post Based on Post ID
class ParticularNewsPOstAPIView(APIView):
    def get(self, request, id):
        news_post = News.objects.get(pk=id)
        serializer = serialzers.NewsSerializersForEndUsers(news_post)
        news_imgs = NewsImages.objects.filter(news_id=serializer.data['id'])
        img_serializer = serialzers.NewsImagesSerializer(news_imgs, many=True)
        # print(img_serializer.data)

        return Response({
            'status': 200,
            'data': serializer.data,
            'news_imgs': img_serializer.data,
            'message': 'news post details fetched'
        })


# GET API for Polls
class PollsGET(APIView):
    def get(self, request):
        polls_get = Polls.objects.all()
        serializer = serialzers.PollsSerializer(polls_get, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'all polls fetched'
        })


# GET API for Advertisements
class AdvertisementsGET(APIView):
    def get(self, request):
        ads_posts = Advertisement.objects.all()
        serializer = serialzers.AdvertisementsSerializer(ads_posts, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'all advertisements fetched'
        })


# GET API for Jobs
class JobsGET(APIView):
    def get(self, request):
        jobs = JobPostings.objects.all()
        serializer = serialzers.JobpostingSerializer(jobs, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'all jobs fetched'
        })


# POST API FOR END USER TO POST NEWS THROUGH MOBILE
class PostNewsByEndUser(APIView):
    authentication_classes = [CustomAuthentication]

    def post(self, request):
        serializer = serialzers.NewsSerializersForPostingNews(data=request.data)
        if serializer.is_valid():
            serializer.save()
            images = request.data.getlist('img')
            serialized_news_id = serializer.data['id']
            for i in images:
                img_serializer = serialzers.NewsImagesSerializer(
                    data={'news_id': serialized_news_id, 'image': i})
                if img_serializer.is_valid():
                    img_serializer.save()
                    print("inside of Image serializer")
                    print(img_serializer)
                else:
                    print("serializer Error : ", img_serializer.errors)
            return Response({
                'status': 200,
                'data': serializer.data,
                'message': 'News Posted Successfully'
            })
        else:
            return Response({
                'status': 400,
                'message': 'Post Not Uploaded'
            })


# POST API for End User With TOken Authentication
class PostJobByEndUser(APIView):
    authentication_classes = [CustomAuthentication]

    def post(self, request):
        serializer = serialzers.JobpostingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'data': serializer.data,
                'message': 'Job Posted Successfully'
            })
        else:
            return Response({
                'status': 400,
                'message': 'Job Not Uploaded',
                'errors': serializer.errors
            })


# POST API for Selecting a Poll Option
class PollUpdation(APIView):
    authentication_classes = [CustomAuthentication]

    def post(self, request):
        poll_id = request.data['poll_id']
        selected_option = request.data['option_id']
        poll = Polls.objects.get(pk=poll_id)
        option_1_score = poll.option_1_count
        option_2_score = poll.option_2_count
        option_3_score = poll.option_3_count
        option_4_score = poll.option_4_count
        poll_updation = Polls.objects.filter(id=poll_id)
        if selected_option == 1:
            poll_updation.update(option_1_count=option_1_score+1)
        if selected_option == 2:
            poll_updation.update(option_2_count=option_2_score+1)
        if selected_option == 3:
            poll_updation.update(option_3_count=option_3_score+1)
        if selected_option == 4:
            poll_updation.update(option_4_count=option_4_score+1)
        poll_data = Polls.objects.get(id=poll_id)
        serializer = serialzers.PollsSerializer(poll_data)
        return Response({
            'status': 400,
            'data': serializer.data,
            'message': 'Poll Updated Succefully'
        })


# News Posts Based on States
class StateLevelNewsList(generics.ListAPIView):
    serializer_class = NewsEditSerializer

    def get_queryset(self):
        state_id = self.kwargs['state_id']
        state = States.objects.get(pk=state_id)
        return News.objects.filter(state=state)


# News Posts Based on Districts
class DistrictLevelNewsList(generics.ListAPIView):
    serializer_class = NewsEditSerializer

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        district = Districts.objects.get(pk=district_id)
        return News.objects.filter(district=district)


# News Posts Based on Mandal
class MandalLevelNewsList(generics.ListAPIView):
    serializer_class = NewsEditSerializer

    def get_queryset(self):
        mandal_id = self.kwargs['mandal_id']
        mandal = Mandal.objects.get(pk=mandal_id)
        return News.objects.filter(mandal=mandal)


# Categories List
class CategoriesList(generics.ListCreateAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


# Epaper API View
class CreateEpaperAPIView(generics.ListCreateAPIView):
    serializer_class = EpaperSerializer
    queryset = Epaper.objects.all()


# APIView to Fetch User Profile Details
class GetUserProfileAPI(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user = Users.objects.filter(uid=user_id)
        serializer = serialzers.UserProfileSerializer(user, many=True)
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'User Details Fetched'
        })


# Update APIView for user profile
class UpdateUserProfileAPI(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user = Users.objects.filter(uid=user_id)

        user.update(email=request.data["email"], profile_picture=request.data.get(
            "profile_picture"))

        serializer = serialzers.UserProfileSerializer(user, many=True)

        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'User Details Fetched'
        })
