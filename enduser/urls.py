from django.urls import path, include
from . import views


urlpatterns = [


    # USER REGISTRATION AND VERIFYING OTP
    path('register-user/', views.RegisterUser.as_view()),
    path('verify-otp/',views.VerifyOtp.as_view()),


    # GET APIS WITHOUT AUTHENTICATION (JWT TOKEN)
    path('get-news/', views.NewsPostsAPIView.as_view()),
    path('get-news-details/<int:id>/',views.ParticularNewsPOstAPIView.as_view()),
    path('get-ads/',views.AdvertisementsGET.as_view()),
    path('get-polls/',views.PollsGET.as_view()),
    path('get-jobs/',views.JobsGET.as_view()),

    # POST APIS WITH AUTHENTICTAION (JWT TOKEN)
    path('post-news/', views.PostNewsByEndUser.as_view()),
    path('post-job/',views.PostJobByEndUser.as_view()),

    # POST API WITH DYNAMIC UPDATIONS WITH JWT TOKEN
    path('poll-update-response/',views.PollUpdation.as_view()),
    path('categories/',views.CategoriesList.as_view()),
    path('epaper/',views.CreateEpaperAPIView.as_view()),


    # GET APIs For Fetching news posts based on state district and mandal
    path('state-news/<int:state_id>/',views.StateLevelNewsList.as_view()),
    path('district-news/<int:district_id>/',views.DistrictLevelNewsList.as_view()),
    path('mandal-news/<int:mandal_id>/',views.MandalLevelNewsList.as_view()),

    path('state-category-news/<int:state_id>/<int:category_id>/',views.StateCategoryNewsList.as_view()),
    path('district-category-news/<int:district_id>/<int:category_id>/',views.DistrictCategoryNewsList.as_view()),
    path('mandal-category-news/<int:mandal_id>/<int:category_id>/',views.MandalCategoryNewsList.as_view()),


    path('get-user-profile/',views.GetUserProfileAPI.as_view()),
    path('update-user-profile/',views.UpdateUserProfileAPI.as_view()),


]
