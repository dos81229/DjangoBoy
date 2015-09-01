from django.db import models

#blank = True 欄位檢查允許為空值
#blank = False 欄位檢查不允許為空值
#null = True 寫入資料庫允許為 NULL (Python 為 None)
#null = False 寫入資料庫不允許為 NULL (Python 為 None)

class Post(models.Model): # Django 的 Field 有兩種值可以設定: blank and null
	title 			= models.CharField(max_length=100) 
	content 		= models.TextField(blank=True)
	photo			= models.URLField(blank=True)
	location		= models.CharField(max_length=100) 
	created_at 		= models.DateTimeField(auto_now_add=True) 
	food 			= models.TextField(blank=True)
	habit			= models.TextField(blank=True)
	relationship	= models.CharField(max_length=100)


	def __str__(self):
		return self.title



class Restaurant(models.Model): 
	name			= models.CharField(max_length=100)
	phone_number	= models.CharField(max_length=20)
	address			= models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Food(models.Model):
	name			= models.CharField(max_length=20)
	price			= models.DecimalField(max_digits=3,decimal_places=0)
	comment			= models.CharField(max_length=50, blank=True)
	restaurant 		= models.ForeignKey(Restaurant) #ForeignKey() 繼承方法，繼承餐廳物件		
	def __str__(self):
		return self.name


class Comment(models.Model):
	content			= models.CharField(max_length=200)
	user			= models.CharField(max_length=20)
	email			= models.EmailField(max_length=20)
	created_at 		= models.DateTimeField(auto_now_add=True) 
	restaurant 		= models.ForeignKey(Restaurant) #ForeignKey() 繼承方法，繼承餐廳物件

	def __str__(self):
		return self.user


class Band(models.Model):  #樂團團名
	name   = models.CharField(max_length=50)
	genres = models.CharField(max_length=20)  #風格
	pieces = models.CharField(max_length=50)  #作品
	
	def __str__(self):
		return self.name

class Member(models.Model): #樂團團員
	name 		= models.CharField(max_length=50)
	instrument 	= models.CharField(max_length=20)
	gender		= models.CharField(max_length=5)
	band 		= models.ForeignKey(Band) #ForeignKey() 繼承方法，繼承餐廳物件

	def __str__(self):
		return self.name	
	

class Music_Comment(models.Model):
    content         = models.CharField(max_length=200)
    user            = models.CharField(max_length=20)
    email           = models.EmailField(max_length=20)
    created_at      = models.DateTimeField(auto_now_add=True) 
    band            = models.ForeignKey(Band) #ForeignKey() 繼承方法，繼承餐廳物件

    def __str__(self):
        return self.user

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ImageThing(models.Model):
    name  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class BitchFace(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title
