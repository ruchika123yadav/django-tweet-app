from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect

# Create your views here.


def home(req):
    return HttpResponse("This is the home of app Tweet")

def Tweett(req):
    return render(req,'index.html')

def Tweet_list(req):
    Tweets = Tweet.objects.all().order_by('-created_at')  # Lowercase 'Tweet'
    return render(req, 'tweet_list.html', {'Tweets': Tweets})

# **********Tweet CREATE*************

    # ishme ham user ko ek form denge jisme user shyd wo form submit krr chuka ho ya form ham user ko de rhe
    # STANDARDS METHODS
    # 1- sabe phele to ye dekhte hai ki user se ek request ayi hai or wo request ham dekh rhe hai
    # 2- User ko ham ek Empty form de rhe hai
#  3- User ke form ka data sara aa chuka hai uske bss Render krwa doo bs

def Tweet_create(req):
    if req.method=='POST':
      form=TweetForm(req.POST,req.FILES)
      if form.is_valid():
          Tweet=form.save(commit='false')#kyuki hame user bhi add krna hai uske andr
          Tweet.user=req.user
          Tweet.save()
          return redirect('Tweet_list')
      
    else:
        form =TweetForm()

    return render(req,'tweet_form.html',{'form':form})


# *****************Tweet EDIT**************
def Tweet_edit(req,Tweet_id):
    Tweet=get_object_or_404(Tweet,pk=Tweet_id,user=req.user)
     
    if req.method=='POST':
      form=TweetForm(req.POST,req.FILES,instance=Tweet)
      if form.is_valid():
          Tweet=form.save(commit='false') 
          Tweet.user=req.user
          Tweet.save()
          return redirect('Tweet_list')
    else:
        form =TweetForm(instance=Tweet)
    return render(req,'tweet_form.html',{'form':form})

def Tweet_delete(req,Tweet_id):
    Tweet=get_object_or_404(Tweet,pk=Tweet_id,user=req.user)
    if req.method=='POST':
        Tweet.delete()
        return redirect('Tweet_list')
    return render(req,'tweet_delete.html')


