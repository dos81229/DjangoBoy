from django.shortcuts import render  #render 是渲染的意思，渲染一個頁面以返回請求，返回的是一個 HttpResponse 對象
from django.http import HttpResponse  #request
from datetime import datetime

from django.contrib import auth     	#使用者登入驗證
from django.core.context_processors import csrf  #使用者登入驗證
from django.contrib.auth.forms import UserCreationForm # Django 中 auth 應用中內建的註冊表單模型

from django.template import RequestContext  #只有當你使用 RequestContext 的時候 並且 你的 TEMPLATE_CONTEXT_PROCESSORS 設置包含 "django.core.context_processors.auth" 的時候，這個變量才是有效的。
from django.http import HttpResponseRedirect #他吃一個 pattern 參數，如果 return 了這個物件，則會將頁面重導至 pattern 對應的 action
from django.core.mail import send_mail,mail_admins  #寄電子信箱
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from trips.forms import  MessageForm, CommentForm, ContactForm,MusicForm
from trips.models import Post, Restaurant, Food, Comment
from trips.models import Band, Member, Music_Comment,BitchFace


# django.http 模組中引用 HttpResponse 類別


def index(request): #宣告登入畫面
	return render(request,
				  'index.html',
				  {'current_time':datetime.now()})

def login(request): #宣告登入
	c = {}
	c.update(csrf(request))
	return render(request,
				  'login.html',
				  {'c':c})

def auth_view(request): #宣告登入驗證
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	# auth.authenticate() 使用者登入驗證
	user = auth.authenticate(username=username, password=password) 

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')

	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):  #宣告登入成功
	return render(request,
				  'loggedin.html',
				  {'full_name':request.user.username})

def invalid_login(request): #宣告登入失敗
	return render(request,
				  'invalid_login.html',
				  {'full_name':request.user.username})

def logout(request):  #宣告登出
	auth.logout(request)
	return render(request,
				  'logout.html',
				  {'full_name':request.user.username})

def register(request):  #宣告註冊
	if request.method =='POST':  #要求方法為POST
		form = UserCreationForm(request.POST)
		if form.is_valid(): #form驗證處理
			user = form.save()
			return HttpResponseRedirect('/accounts/register_success') #導向至accounts/register_success

		else:
			return HttpResponseRedirect('/accounts/register_invalid') #導向至accounts/register_invalid
	#args = {}
	#args = update(csrf(request))	
	#args['form'] = UserCreationForm()	

	else:
		form = UserCreationForm()
		return render(request,
					  'register.html',
					  {'form':form}, 
          context_instance=RequestContext(request))

def register_success(request): #宣告註冊成功
	return render(request,
				  'register_success.html',
				  {'datetime':datetime.now()})

def register_invalid(request): #宣告註冊失敗
	return render(request,
				  'register_invalid.html',
				  {'datetime':datetime.now()})

def set_c(request):  #宣告設置 cookies
	response = HttpResponse('set your lucky_number as 7')
	response.set_cookie('lucky_number', 7)
	return response 


def get_c(request):  #宣告讀取 cookies
	if 'lucky_number' in request.COOKIES:
		return HttpResponse('your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
	else:
		return HttpResponse('No COOKIES')


def use_session(request): #宣告session
	request.session['lucky_number'] = 7  			#設置lucky_number

	if 'lucky_number' in request.session:			#讀取lucky_number
		lucky_number = request.session['lucky_number']

		response = HttpResponse('Your lucky_number is ' + lucky_number)

		del request.session['lucky_number']			#刪除lucky_number

		return response

def hello_world(request):  #宣告hello_world 
	return render(request,
				  'hello_fucking_world.html',
				  {'current_time':datetime.now()})

def home(request):  #宣告首頁
	post_list = Post.objects.all()  #宣告清單為Post的全部物件
	return render(request,
				  'home.html',
				  {'post_list': post_list})

def post_detail(request, id): #宣告顯示Post的個別物件
	post = Post.objects.get(id=id)  #以id抓取來顯示POST個別選項
	return render(request,
				  'post.html',
				  {'post': post})	

def message(request):  #宣告Post留言板
	if request.method == 'POST': #要求方法為POST
		form = MessageForm(request.POST) #宣告form 為 form.py中的MessageForm之定義物件
		if form.is_valid():#form驗證處理
			title 		 = form.cleaned_data['留言者'] #cleaned_data將資料轉換成python 型別
			photo		 = form.cleaned_data['相片']
			content		 = form.cleaned_data['留言']
			location 	 = form.cleaned_data['出沒地點']
			food     	 = form.cleaned_data['喜歡的食物']
			habit	 	 = form.cleaned_data['好習慣']
			relationship = form.cleaned_data['感情狀況']
			m = Post(title	  	  =title ,
					 photo	  	  =photo,
					 content  	  =content,
					 location 	  =location,
					 food 	  	  =food,
					 habit 	  	  =habit,
					 relationship =relationship)
			m.save()#如果驗證通過的話。把form的數據添加到數據庫裡
		return HttpResponseRedirect('/message/')

	else :
		form = MessageForm()
		messages = Post.objects.all()
		return render(request,
					  'message.html',
					  {'form':form, 'messages':messages})

def welcome(request): #宣告腹黑試煉
	if 'user_name' in request.GET :
		return HttpResponse('寶傑好，大家好 !' + ' '+ request.GET['user_name']+ '久違了! 早晨的雞雞還是硬的嗎?' ) #顯示寶傑問候
		return HttpResponseRedirect('/bitch_face/') #跳轉至bitch_face方法
	else :
		return render(request,
					  'welcome.html',
					   {'current_time':datetime.now()})

def bitch_face(request): #腹黑結果
	return render(request,
				  'bitch_face.html',
				  {'full_name':request.GET['user_name']})

def restaurants_list(request):   #宣告餐廳列表頁面
	restaurants = Restaurant.objects.all()
	request.session['restaurants'] = restaurants  #利用session保存模型物件
	return render(request,
				  'restaurants_list.html',
				  {'restaurants':restaurants})

def menu(request,id):      #宣告餐廳菜單
	if id:
		r = Restaurant.objects.get(id=id) #定義r 以Restaurant的物件id抓取物件
		return render(request,
					  'menu.html',
					  {'r':r})
	else :
		return HttpResponseRedirect('/restaurants_list/')

def comment(request,id): #宣告餐廳評價
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        user 		= request.POST['留言者']
        content 	= request.POST['評論']
        email 		= request.POST['留言者信箱']
        created_at 	= datetime.now()
        c = Comment(user=user, 
        			email=email, 
        			content=content, 
        			created_at=created_at,
        			restaurant=r)
        c.save()  #如果驗證通過的話。把POST的數據添加到數據庫裡
    f = CommentForm()
    return render(request,
    			  'comments.html',
    			  {'r':r, 'f':f})


def band(request):  #宣告樂團列表
	bands = Band.objects.all()
	request.session['bands'] = bands
	return render(request,
				  'band.html',
				  {'bands':bands})

def band_menu(request,id):  #宣告樂團團員
    if id:
	    b = Band.objects.get(id=id)
	    return render(request,
				     'band_menu.html',
				     {'b':b})
    else:
        return HttpResponseRedirect('/bands/')

def music_comment(request,id): #宣告樂團評價
    if id:
        b = Band.objects.get(id=id)
    else :
        return HttpResponseRedirect('/bands/')

    if 'ok' in request.POST:	
        user        = request.POST['留言者']
        content     = request.POST['評論']
        email       = request.POST['留言者信箱']
        created_at  = datetime.now()
        c = Music_Comment(user=user,
                          content=content,
                          email=email,
                          created_at=created_at,
                          band=b)
        c.save() #如果驗證通過的話。把POST的數據添加到數據庫裡
    f = MusicForm()
    return render(request,
                  'music_comment.html',
                  {'b':b, 'f':f})

def contact(request):   #宣告寄信件
	success = False 
	email 		= ""
	message 	= ""
	full_name 	= ""

	if request.method == "POST": #要求方法為POST
		contact_form = ContactForm(request.POST)

		if contact_form.is_valid():  #驗證
			success = True
			email 		= contact_form.cleaned_data['email']
			message 	= contact_form.cleaned_data['message']
			full_name 	= contact_form.cleaned_data['full_name']

			#subject = 'site contact form'
			#from_email = settings.EMAIL_HOST_USER
			#to_email = [from_email, 'yourgmail@gmail.com'] 
			#contact_message = "%s: %s via %s"%(
					#full_name, 
					#message, 
					#email)

			send_mail("subject", 
				  	  "contact_message:%s %s %s" % (full_name,message,email), 
				  	  'email.from@gmail.com', 
				      ['user.to@server.com'],
				      fail_silently=True)
			
			mail_admins("other subject",
						"some text",
						fail_silently=True)
	else:
		contact_form = ContactForm()

	context = {'contact_form':contact_form,
			   'email':email,
			   'message':message,
			   'full_name':full_name,
			   'success':success}

	return render(request,
				  'contact.html',
				  context,
				  context_instance = RequestContext(request))




#def session_test(request):
	#sid = request.COOKIES['sessionid']
	#sid2 = request.session.session_key
	#s = Session.objects.get(pk=sid)
	#s_info = 'Session ID:' + sid + '<br>SessionID2:' + sid2 + '<br>Expire_date:' +
			 #str(s.expire_date) + '<br>Data:' + str(s.get_decoded())

	#return HttpResponse(s_info)