import uuid
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
import random

from superior import  models

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.States
        fields = "__all__"


class MandalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mandal
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Districts
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = "__all__"

    def create(self, validated_data):
        otp_generated = random.randint(10000,99999)
        phone = validated_data['phone']
        if models.Users.objects.filter(phone=phone):
            user = models.Users.objects.get(phone=phone)
            user.otp=otp_generated
            user.save()
            return user
        else:
            user = models.Users.objects.create(name=validated_data['name'],phone = validated_data['phone'],uid = uuid.uuid4(),otp=otp_generated, state_id= validated_data['state'].id, mandal_id =validated_data['mandal'].id , district_id =validated_data['district'].id )
            user.save()
            return user
    
    def validate(self,validated_data):
        if validated_data.get('name'):
            name = validated_data['name']
            if len(name) < 7:
                raise serializers.ValidationError('name cannot be less than 8 characters')
        return validated_data




class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImages
        fields = "__all__"
    def create(self, validated_data):
        image_news = models.NewsImages.objects.create(news_id = validated_data['news_id'],image =validated_data['image'] )
        image_news.save()
        return image_news


class NewsSerializersForEndUsers(serializers.ModelSerializer):
    news_images = NewsImagesSerializer(many=True,read_only = True)
    class Meta:
        model = models.News
        fields = "__all__"
        depth = 1
        

class NewsSerializersForPostingNews(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"
        



class AdvertisementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertisement
        fields = "__all__"


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Polls
        fields = "__all__"


class JobpostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPostings
        fields = "__all__"



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = "__all__"





class GetOnlyImageForNewsSerializer(serializers.ModelSerializer):
    model = models.NewsImages
    fields = ["image"]


class LocationCategoryNewsSerializer(serializers.ModelSerializer):
    news_img = GetOnlyImageForNewsSerializer()
    fields = "__all__"

    




