import datetime
from django.db import models
import uuid





# Duper Admin Class
class SuperAdmin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "0.Super Admin"


# Categories
class Categories(models.Model):
    category = models.CharField(max_length=150)
    category_img = models.ImageField(upload_to='categories/', null=True)
    def __str__(self):
        return str(self.id) + "." + self.category
    class Meta:
        verbose_name_plural = "4.Categories"


# States API
class States(models.Model):
    state_name = models.CharField(max_length=250)
    state_representing_image = models.ImageField(
        upload_to='states/', null=True)
    def __str__(self):
        return str(self.id) + "." + self.state_name
    class Meta:
        verbose_name_plural = "1.States"


# Districts API
class Districts(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.id) + "." + self.district_name
    class Meta:
        verbose_name_plural = "2.districts"

# Mandal API
class Mandal(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    mandal_name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)+"."+self.mandal_name
    class Meta:
        verbose_name_plural = "3.Mandal"

# Country Model
class Country(models.Model):
    contry_name = models.CharField(max_length=200)
    def __str__(self):
        return self.contry_name


##############################################################################################
###########################################################################
###############################################
###########################
############
######

class Epaper(models.Model):
    paper_name = models.CharField(max_length=500)
    paper_file = models.FileField(upload_to='epaper/')
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)


class UserBaseModel(models.Model):
    id = models.CharField(default ="", max_length=100)
    uid = models.UUIDField(primary_key=True, editable=False,default = uuid.uuid4())
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)

    class Meta:
        abstract = True


# User Model
class Users(UserBaseModel):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    otp = models.CharField(max_length=10,default="00000")
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE)
    mandal = models.ForeignKey(Mandal,on_delete=models.CASCADE)
    email = models.EmailField(max_length=200,default="")
    profile_picture = models.ImageField(upload_to='user_profiles/', default="")
    is_verified = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.phone



# News Model
class News(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=200)
    video = models.URLField(default="")
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE,null=True)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE,null=True)
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE,null=True)
    likes_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    spam_count = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    status = models.CharField(max_length=200,default="Under Review")
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    by_admin = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "2.News"



# News Comments
class NewsComments(models.Model):
    news_id = models.ForeignKey(News,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)



##############################################################################################
###########################################################################
###############################################
###########################
############
######



# News Images
class NewsImages(models.Model):
    news_id = models.ForeignKey(News,on_delete=models.CASCADE,related_name='news_images')
    image = models.ImageField(upload_to='news_imgs/', null=True)


#  Reporters
class Reporters(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, default="")
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "3.Reporters"


# Polls
class Polls(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(default='', max_length=200)
    option_4 = models.CharField(default='', max_length=200)
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    status = models.CharField(max_length=200, default="published")
    class Meta:
        verbose_name_plural = "6.Polls"


# Sub-Categories
class SubCategories(models.Model):
    sub_category = models.CharField(max_length=150)
    def __str__(self):
        return str(self.id) + "." + self.sub_category
    class Meta:
        verbose_name_plural = "5.Sub Categories"


# Advertisements
class Advertisement(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='advertisements/', null=True)
    link = models.URLField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE , null=True)
    status = models.CharField(max_length=200,default="Under Review")
    by_admin = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)+"."+self.title
    class Meta:
        verbose_name_plural = "9.Advertisements"


# Job Categories
class JobCategory(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category


# Job Postings View
class JobPostings(models.Model):
    title = models.CharField(max_length=200)
    jobSubCategory = models.CharField(max_length=200)
    JobCategory = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name="jobCategory")
    no_of_openings = models.CharField(max_length=200)
    jobType = models.CharField(max_length=200)
    state = models.ForeignKey(States, on_delete=models.CASCADE, related_name="state")
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, related_name="district")
    address = models.TextField()
    interested_in_hiring_from = models.CharField(max_length=200)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    jobHours = models.CharField(max_length=200)
    timings_shift = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    your_role_in_company = models.CharField(max_length=200)
    manage_candidate_through = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    whatsappNumber = models.CharField(max_length=200,null=True)
    company_logo = models.ImageField(upload_to="job_post_company_logo/", null=True)
    years_of_experience = models.CharField(max_length=200)
    graduation = models.CharField(max_length=200)
    Preferred_gender = models.CharField(max_length=200)
    Fees_required = models.BooleanField(default=False)
    Fee_amount = models.CharField(max_length=200, null=True)
    fee_reasons = models.CharField(max_length=250,null=True)
    Fee_before_getting_job = models.BooleanField(default=True)
    additiona_info = models.TextField()
    tac = models.BooleanField(default=False)
    Job_poster = models.ImageField(upload_to="job_poster/", null=True)
    created_date = models.DateField(auto_now_add=True)
    created_time= models.TimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=200,default="Under Review")
    by_admin = models.BooleanField(default=False)



