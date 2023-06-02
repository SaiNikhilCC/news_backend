from rest_framework.views import APIView
# from .serializers import NewsSerializer, ReporterSerializer, StateSerializer, NewsEditSerializer, DistrictSerializer,CreateMandalSerializer,CountrySerializer ,AllDistrictsDetailedSerializer ,AllMandalsDetailSerializer ,CreateStateSerializer ,PollsSerializer, DetailedNewsSerializer, AdvertisementsSerializer, MAndalSerializer, PostSerializer, CategoriesSerializer, SubCategorySerializer, JobCategorySerializer, JobPostingsSerializer, JobEditSerializer,CreateDistrictSerializer
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# HEllo
# Super Admin Login View
@csrf_exempt
def SuperAdminLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if models.SuperAdmin.objects.filter(username=username, password=password):
        superAdmin = models.SuperAdmin.objects.get(username=username)
        return JsonResponse({'bool': True, 'super_admin_id': superAdmin.id})
    else:
        return JsonResponse({'bool': False, 'msg': 'invalid credentials'})


# Super Admin Login View
@csrf_exempt
def super_admin_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if models.SuperAdmin(username=username, password=password).DoesNotExist:
        return JsonResponse({'bool': False, 'msg': 'Invalid Credentials'})
    else:
        admin = models.SuperAdmin.objects.filter(
            username=username, password=password)
        admin_id = admin.id
        return JsonResponse({'bool': True, 'admin_id': admin_id})


# Create News Post
from enduser.serialzers import NewsImagesSerializer,NewsSerializersForEndUsers,NewsSerializersForPostingNews


class PostNewsByAdmin(APIView):
    def post(self,request):
        serializer = NewsSerializersForPostingNews(data = request.data)
        if serializer.is_valid():
            serializer.save()
            images = request.data.getlist('img')
            serialized_news_id = serializer.data['id']
            for i in images:
                img_serializer = NewsImagesSerializer(data={'news_id':serialized_news_id,'image':i})
                if img_serializer.is_valid():
                    img_serializer.save()
                else:
                    return Response({
                        'status':200,
                        'data':serializer.errors,
                        'message':'News Posted Successfully'
                    })
            return Response({
                'status':200,
                'data':serializer.data,
                'message':'News Posted Successfully'
            })
        else:
            print(serializer.errors)
            return Response({
                'status':400,
                'message':'Post Not Uploaded',
                'errors':serializer.errors
            })





# Fetch State And District Based on Postt ID
@csrf_exempt
def postStateDistrict(request, post_id):
    post = models.News.objects.get(pk=post_id)
    post_state_id = post.state_id
    state = models.States.objects.get(pk=post_state_id)
    state_name = state.state_name
    return JsonResponse({'bool': True, 'State': state_name})


# Create Reporter View
@csrf_exempt
def CreateReporters(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    if models.Reporters.objects.filter(phone=phone):
        return JsonResponse({'bool': False, 'message': 'A Reporter is Already Registered With This Number'})
    elif models.Reporters.objects.filter(email=email):
        return JsonResponse({'bool': False, 'message': 'A Reporter is Already Registered With This Email Address'})
    elif len(password) < 9:
        return JsonResponse({'bool': False, 'message': 'Password Must Be Minimum of 8 Characters'})
    else:
        newReporter = models.Reporters.objects.create(
            name=name, email=email, password=password, phone=phone)
        newReporter.save()
        return JsonResponse({'bool': True})


# Create New Polls View
def PollsUpdation(request, poll_id, option_id):
    poll = models.Polls.objects.get(pk=poll_id)
    option_1_score = poll.option_1_count
    option_2_score = poll.option_2_count
    option_3_score = poll.option_3_count
    option_4_score = poll.option_4_count
    poll_updation = models.Polls.objects.filter(id=poll_id)
    if option_id == 1:
        poll_updation.update(option_1_count=option_1_score+1)
    if option_id == 2:
        poll_updation.update(option_2_count=option_2_score+1)
    if option_id == 3:
        poll_updation.update(option_3_count=option_3_score+1)
    if option_id == 4:
        poll_updation.update(option_4_count=option_4_score+1)
    return JsonResponse({'bool': True, "message": 'poll has been submitted'})


# News List
class NewsList(generics.ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


# News Complete List for React Data table in admin dashboard
class DetaiedNewsList(APIView):
    def get(self,request):
        news_posts = models.News.objects.all()
        serializer = NewsSerializersForEndUsers(news_posts, many=True)
        return Response({
            'status':200,
            'data':serializer.data,
            'message':'all news posts fetched'
        })


# Non international News Complete List for React Data table in admin dashboard
class NonInterNationalNewsPosts(APIView):
    def get(self,request):
        news_posts = models.News.objects.filter(country = None)
        serializer = NewsSerializersForEndUsers(news_posts, many=True)
        return Response({
            'status':200,
            'data':serializer.data,
            'message':'all news posts fetched'
        })


# International News Complete List for React Data table in admin dashboard
class InterNationalNewsPosts(APIView):
    def get(self,request):
        news_posts = models.News.objects.filter(country = not None)
        serializer = NewsSerializersForEndUsers(news_posts, many=True)
        return Response({
            'status':200,
            'data':serializer.data,
            'message':'all news posts fetched'
        })




# Destroy View for news post
class DeleteNewsPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


# Reporters List
class ReporterList(generics.ListCreateAPIView):
    queryset = models.Reporters.objects.all().order_by('-id').values()
    serializer_class = serializers.ReporterSerializer


# Advertisements List View
class AdvertisementsList(generics.ListCreateAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementsSerializer


# All Polls List View
class PollsList(generics.ListCreateAPIView):
    serializer_class = serializers.PollsSerializer
    queryset = models.Polls.objects.all()


# Countries API View 
class Countries(generics.ListCreateAPIView):
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()


# All States List API View
class CreateStates(generics.ListCreateAPIView):
    serializer_class = serializers.CreateStateSerializer
    queryset = models.States.objects.all()


class StatesList(generics.ListCreateAPIView):
    queryset = models.States.objects.all()
    serializer_class = serializers.StateSerializer


# All Districts List API View
class CreateDistrictsList(generics.ListCreateAPIView):
    serializer_class = serializers.CreateDistrictSerializer
    queryset = models.Districts.objects.all()


class DistrictsList(generics.ListCreateAPIView):
    serializer_class = serializers.DistrictSerializer
    def get_queryset(self):
        state_id = self.kwargs['state_id']
        state = models.States.objects.get(pk=state_id)
        return (models.Districts.objects.filter(state=state))


class AllDistrictsDetailedView(generics.ListAPIView):
    serializer_class = serializers.AllDistrictsDetailedSerializer
    queryset = models.Districts.objects.all()


# All Mandals List API View
class CreateMandals(generics.ListCreateAPIView):
    serializer_class = serializers.CreateMandalSerializer
    queryset = models.Mandal.objects.all()


class AllMandalsDetailedView(generics.ListAPIView):
    serializer_class = serializers.AllMandalsDetailSerializer
    queryset = models.Mandal.objects.all()


class MandalsList(generics.ListCreateAPIView):
    serializer_class = serializers.MAndalSerializer

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        district = models.Districts.objects.get(pk=district_id)
        return (models.Mandal.objects.filter(district=district))


# All Reporters in a District
class ReportersInADistrict(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MAndalSerializer

    def get_queryset(self):
        district_id = self.kwargs['disstrict_id']
        district = models.Districts.objects.get(pk=district_id)
        return (models.Districts.objects.filter(id=district.id))


# Categories List
class CategoriesList(generics.ListCreateAPIView):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()


# Sub Categories List
class SubCategoriesList(generics.ListCreateAPIView):
    serializer_class = serializers.SubCategorySerializer
    queryset = models.SubCategories.objects.all()


# Job Category Serializer
class JobCategoriesList(generics.ListCreateAPIView):
    serializer_class = serializers.JobCategorySerializer
    queryset = models.JobCategory.objects.all()


# Job Postings List
class JobPostingList(generics.ListCreateAPIView):
    queryset = models.JobPostings.objects.all()
    serializer_class = serializers.JobPostingsSerializer


# Edit Job Postings
class EditJobPosting(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.JobPostings.objects.all()
    serializer_class = serializers.JobPostingsSerializer


# Particular Job Posting Details
class JobDetails(generics.RetrieveAPIView):
    serializer_class = serializers.JobEditSerializer
    queryset = models.JobPostings.objects.all()


# Particular News Post
class ParticularNewsPost(APIView):
    def get(self,request,id):
        news_post = models.News.objects.get(pk=id)
        serializer = NewsSerializersForEndUsers(news_post)
        news_imgs = models.NewsImages.objects.filter(news_id = serializer.data['id'])
        img_serializer = NewsImagesSerializer(news_imgs,many=True)        
        return Response({
            'status':200,
            'data':serializer.data,
            'news_imgs':img_serializer.data,
            'message':'news post details fetched'
        })  


# Edit News Post
class EditNewsPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


# Edit Poll
class EditPoll(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Polls.objects.all()
    serializer_class = serializers.PollsSerializer


# Edit Advertisement
class EditAdvertisement(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementsSerializer


# All News Posts
class CreateNewsPost(generics.CreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


# News Posts Based on Catgeory
class CategoryNewsPosts(APIView):
    def get(self,request,category_id):
        news_posts = models.News.objects.filter(category=category_id)
        serializer = NewsSerializersForEndUsers(news_posts, many=True)

        return Response({
            'status':200,
            'data':serializer.data,
            'message':'all news posts fetched'
        })



class PArticularCategoryData(generics.RetrieveAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer


# News Posts Based on States
class StateLevelNewsList(generics.ListAPIView):
    serializer_class = serializers.NewsEditSerializer

    def get_queryset(self):
        state_id = self.kwargs['state_id']
        state = models.States.objects.get(pk=state_id)
        return models.News.objects.filter(state=state)


# News Posts Based on Districts
class DistrictLevelNewsList(generics.ListAPIView):
    serializer_class = serializers.NewsEditSerializer

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        district = models.Districts.objects.get(pk=district_id)
        return models.News.objects.filter(district=district)


# News Posts Based on Mandal
class MandalLevelNewsList(generics.ListAPIView):
    serializer_class = serializers.NewsEditSerializer

    def get_queryset(self):
        mandal_id = self.kwargs['mandal_id']
        mandal = models.Mandal.objects.get(pk=mandal_id)
        return models.News.objects.filter(mandal=mandal)


# Get Ads
class AddsList(generics.ListAPIView):
    serializer_class = serializers.AdvertisementsSerializer
    queryset = models.Advertisement.objects.all()

# Particular Poll Data
class ParticularPollData(generics.RetrieveAPIView):
    serializer_class = serializers.PollsSerializer
    queryset = models.Polls.objects.all()




# Epaper API View
class CreateEpaperAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.EpaperSerializer
    queryset = models.Epaper.objects.all()


# Delete Mandal
@csrf_exempt
def DeleteMandal(request,id):
    mandal = models.Mandal.objects.get(pk = id)
    mandal.delete()
    return Response({
        'status':200,
        'message':'Mandal Deleted Succesfully'
    })


# Delete District
@csrf_exempt
def DeleteDistrict(request,id):
    district = models.Districts.objects.get(pk = id)
    district.delete()
    return Response({
        'status':200,
        'message':'District Deleted Succesfully'
    })

