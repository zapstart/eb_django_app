from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import blog_text, user_password 
from .utils import signup_login 

year         = []
_oldest_year = 0
_latest_year = 0

def show_front(request):
    global year, _oldest_year, _latest_year 
    
    year = ['2015']
    _blog_order_by_time = blog_text.objects.order_by('-b_created_time')[ : 10]
    if _blog_order_by_time: 
        _oldest_year = int(str(_blog_order_by_time.reverse()[0].b_created_time)[ : 4])
        _latest_year = int(str(_blog_order_by_time[0].b_created_time)[ : 4])
        for i in range(_oldest_year, _latest_year + 1):
            if str(i) not in year: 
                year.append(i)
    _blog_front           = {'blog_data'     : _blog_order_by_time,
                             'time_category' : year,
                             'login'         : request.session.get('loggedin'),
                             'username'      : 'zaptyping' 
                            }
    
    return render(request, 'lovehome/front_page.html', _blog_front)

def show_time_category(request, blog_year):
    global year, _oldest_year, _latest_year 
    
    _blog_order_by_time      = blog_text.objects.order_by('-b_created_time')
    _10_blog_order_by_time   = _blog_order_by_time[ : 10] 
    #_oldest_year = int(str(_blog_data.reverse()[0].b_created_time)[ : 4])
    #_latest_year = int(str(_blog_data[0].b_created_time)[ : 4])
    #for i in range(_oldest_year, _latest_year + 1):
    #    if str(i) not in year_array: 
    #        year_array.append(i) 

    _blog_time   = _blog_order_by_time.filter(b_created_time__year = str(blog_year))    
    _blog_year = {'blog_year'     : _10_blog_order_by_time, 
                  'blog_data'     : _blog_time, 
                  'time_category' : year,
                  'login'         : request.session.get('loggedin'),
                  'username'      : 'zaptyping' 
                 } 
    
    return render(request, 'lovehome/time_category.html', _blog_year)

def add_blog(request):
    if request.method == 'POST':
        _blog_text = blog_text(title        = request.POST['title'], 
                               blog_content = request.POST['blog'],
                              )
        _blog_text.save()
         
        return HttpResponseRedirect(reverse('lovehome:front_page'))
    else:
        if request.session.get('loggedin'):
            return render(request, 'lovehome/add_blog.html', {'login' : request.session.get('loggedin')})
        else:
            return HttpResponseRedirect(reverse('lovehome:front_page'))

def edit_blog(request, page_id):
    if request.method == 'POST':
        _blog_text              = blog_text.objects.get(pk=page_id)
        _blog_text.title        = request.POST['title']
        _blog_text.blog_content = request.POST['blog']
        _blog_text.save()
        return HttpResponseRedirect(reverse('lovehome:front_page'))
    else:
        if request.session.get('loggedin'):
            _blog_data = blog_text.objects.get(pk=page_id)
            return render(request, 'lovehome/edit_blog.html', {'blog_data' : _blog_data})
        else:
            return HttpResponseRedirect(reverse('lovehome:front_page'))

def show_blog(request, page_id):
    global year, _oldest_year, _latest_year 
    
    _blog_data                 = blog_text.objects.order_by('-b_created_time')[ : 10] 
    _blog_data_show            = get_object_or_404(blog_text, pk=page_id)
    _blog_content = {'blog_data_show' : _blog_data_show, 
                     'login'          : request.session.get('loggedin'),
                     'username'       : 'zaptyping',
                     'time_category'  : year,
                     'blog_data'      : _blog_data
                    } 

    return render(request, 'lovehome/show_blog.html', _blog_content)

def delete_blog(request, page_id):
    get_object_or_404(blog_text, pk=page_id).delete()
     
    return HttpResponseRedirect(reverse('lovehome:front_page'))

def signup(request):
    hashpassword = '' 
    _signup_login = signup_login() 
     
    if request.method == 'POST':
        _name     = request.POST['username'] 
        _password = request.POST['password'] 
        if _signup_login.check_signup(_name, _password):
            hashpassword = _signup_login.make_secure_value(str.encode(_password))
            request.session['loggedin'] = True 
            user_password(name     = _name,
                          password = hashpassword).save()
            return HttpResponseRedirect(reverse('lovehome:front_page'))
        else:
            return render(request, 'lovehome/signup.html', {'username_info' : _signup_login.username_info, 
                                                            'password'      : _signup_login.password_info
                                                           }) 
    else:
        if user_password.objects.all():
            return render(request, 'lovehome/signup.html', {'username_info' : 'No signup now!!', 
                                                            'password'      : 'No signup now!!',
                                                            'signup'        : True
                                                           }) 
        else:
            return render(request, 'lovehome/signup.html')
    
def login(request):
    _name     = ''
    _password = ''
    _signup_login = signup_login() 
    
    if request.method == 'POST':
        _name     = request.POST['username'] 
        _password = request.POST['password'] 
        _valid_username = _signup_login.valid_username(_name) 
        _valid_password = _signup_login.valid_password(_password)
        
        if not _valid_password or not _valid_username:
            return render(request, 'lovehome/login.html', {'error_info' : 'username or password not match!'}) 
        else:
            user = user_password.objects.filter(name = _name)
            if user:
                if _signup_login.check_secure_val(user[0].password,str.encode(_password)):
                    request.session['loggedin'] = True 
                    return HttpResponseRedirect(reverse('lovehome:front_page'))
            return render(request, 'lovehome/login.html', {'error_info' : 'username or password not match!'}) 
    else:
        return render(request, 'lovehome/login.html')
            
def logout(request):
    request.session['loggedin'] = False 
    return HttpResponseRedirect(reverse('lovehome:front_page'))

