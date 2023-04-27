from django.urls import path
from . import views

urlpatterns = [
    # Super Admin
    path('super-admin-login/', views.SuperAdminLogin),

    # Reporters
    path('create-reporters/<int:id>/', views.CreateReporters),
    path('reporters-list/<int:id>/', views.ReporterList.as_view()),
    path('reporters-in-district/<int:district_id>/',
         views.ReportersInADistrict.as_view()),


    # Post
    path('all-post-news/', views.NewsList.as_view()),
    path('post-news/', views.PostNewsByAdmin.as_view()),
    path('detailed-news-post-data/', views.DetaiedNewsList.as_view()),

    path('non-international-news-post-data/',
         views.NonInterNationalNewsPosts.as_view()),
    path('international-news-post-data/',
         views.InterNationalNewsPosts.as_view()),



    path('post-State-district/<int:post_id>/', views.postStateDistrict),
    path('edit-news-post/<int:pk>/', views.EditNewsPost.as_view()),
    path('particular-news-post/<int:id>/', views.ParticularNewsPost.as_view()),
    path('category-news-post/<int:category_id>/',
         views.CategoryNewsPosts.as_view()),
    path('state-news/<int:state_id>/', views.StateLevelNewsList.as_view()),
    path('district-news/<int:district_id>/',
         views.DistrictLevelNewsList.as_view()),
    path('mandal-news/<int:mandal_id>/', views.MandalLevelNewsList.as_view()),
    path('get-ads/', views.AddsList.as_view()),
    path('delete-news/<int:pk>/', views.DeleteNewsPost.as_view()),


    # General APIs
    path('countries/', views.Countries.as_view()),
    path('states/', views.StatesList.as_view()),
    path('create-states/', views.CreateStates.as_view()),
    path('districts/<int:state_id>/', views.DistrictsList.as_view()),
    path('all-districts/', views.AllDistrictsDetailedView.as_view()),
    path('create-districts/', views.CreateDistrictsList.as_view()),
    path('mandals/<int:district_id>/', views.MandalsList.as_view()),
    path('create-mandals/', views.CreateMandals.as_view()),
    path('all-mandals/', views.AllMandalsDetailedView.as_view()),

    # Categories
    path('categories/', views.CategoriesList.as_view()),
    path('particular-category/<int:pk>/',
         views.PArticularCategoryData.as_view()),

    # SubCategories
    path('sub-categories/', views.SubCategoriesList.as_view()),


    # Advertisements
    path("advertisements/<int:id>/", views.AdvertisementsList.as_view()),
    path('edit-advertisement/<int:pk>/', views.EditAdvertisement.as_view()),


    # Polls
    path('polls/', views.PollsList.as_view()),
    path('polls-response/<int:poll_id>/<int:option_id>/', views.PollsUpdation),
    path('particular-poll-data/<int:pk>/', views.ParticularPollData.as_view()),
    path('edit-poll/<int:pk>/', views.EditPoll.as_view()),

    # Epaper
    path('epaper/', views.CreateEpaperAPIView.as_view()),


    # Job Postings
    path('job-categories/', views.JobCategoriesList.as_view()),
    path('post-job/', views.JobPostingList.as_view()),
    path('edit-job-posting/<int:pk>/', views.EditJobPosting.as_view()),
    path('particular-job-details/<int:pk>/', views.JobDetails.as_view()),
    # path('create-job-post/',views.createJobPost),


    # Delete Mandal
    path('delete-mandal/<int:id>/', views.DeleteMandal),
    # Delete District
    path('delete-district/<int:id>/', views.DeleteDistrict),


]
