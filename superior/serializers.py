from rest_framework import serializers
from . import models


# For Creating News
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'


# Category Serializer
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'


# Complete News Serializer
class NewsEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'
        depth = 1

# News Serializer For Data Table in Dashboad Page With Edit Button Navigation
class DetailedNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'category_id', 'sub_category',
                  'img', 'video', 'date_time', 'district_id', 'state_id', 'mandal_id']


# Reporter Serializer
class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporters
        fields = ['id', 'name', 'email', 'phone', 'password']
        depth = 1


# Countries Serializer 
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


# States Serializer
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.States
        fields = ['id', 'state_representing_image', 'state_name']
        depth = 1

class CreateStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.States
        fields = ['id', 'state_representing_image', 'state_name']

# District Serializer
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Districts
        fields = '__all__'
        depth = 1

class CreateDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Districts
        fields = '__all__'

class AllDistrictsDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Districts
        fields = '__all__'
        depth=1


# Mandals Serializer
class MAndalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mandal
        fields = '__all__'
        depth = 1

class CreateMandalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mandal
        fields = '__all__'

class AllMandalsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mandal
        fields = '__all__'
        depth = 2

# Polls Serializer
class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Polls
        fields = '__all__'


# Advertisements Serializer
class AdvertisementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertisement
        fields = '__all__'


# News Post Creation Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'


# SubCategories Serializer
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategories
        fields = '__all__'


# Job Category Serializer
class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobCategory
        fields = "__all__"

# Job Creating Job Posting Serializers


class JobPostingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPostings
        fields = "__all__"


# Complete Job Serializer
class JobEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPostings
        fields = '__all__'
        depth = 1


# Epaper Serializer
class EpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Epaper
        fields = '__all__'


        