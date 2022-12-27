from django.db import models
# Song display
# class Normal(AbstractUser):
#          Uploader=models.BooleanField('Is Uploader', default = False)
#          Listener=models.BooleanField('Is Uploader', default = False)
# class Listener(models.Model):
#         pass

class Song(models.Model):
    song_ID = models.AutoField(primary_key=True)
    song_Name = models.CharField(max_length=500)
    singer_Name = models.CharField(max_length=500)
    song_Genre = models.CharField(max_length=100)
    song_desc =  models.CharField(max_length=1500)
    song_Image = models.ImageField(upload_to="images")
    song_File = models.FileField(upload_to="Song")
    def  __str__(self):
        return self.song_Name


# class User(AbstractBaseUser, PermissionsMixin):
#     ROLES = (
#         ("uploader", "uploader"),
#         ("listener", "listener"),
#     )
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250, blank=True)
#     email = models.EmailField(_("email address"), unique=True)
#     role = models.CharField(choices=ROLES, max_length=10, default="listener")
#     status = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     object = CustomUserManager()


    