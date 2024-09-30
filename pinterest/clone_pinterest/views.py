from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News,Pin,Board,Profile,Comments,SavedPin,Update,Message
from django.contrib.auth.models import User,auth
from .forms import BoardForm,PinForm,ProfileForm,CommentsForm,SavedPinForm

# Create your views here.



def home(request):
   b=Board.objects.all()
   return render(request,'home.html',{'boards':b})
 
def about(request):
    return render(request,'about.html')



@login_required(login_url='/login')
def business(request):
    return render(request,'business.html')

@login_required(login_url='/login')
def choice(request):

        if Profile.objects.filter(user=request.user).exists():
           return render(request,'choice.html')
        else:
            messages.error(request,"You have to create a Profile to Add Products...")
            return redirect('/addprofile')


@login_required(login_url='/login')
def choice2(request):

        if Profile.objects.filter(user=request.user).exists():
           return render(request,'choice2.html')
        else:
            messages.error(request,"You have to create a Profile to Save Pins...")
            return redirect('/addprofile')

def press(request):
    n=News.objects.all()
    return render(request,'press.html',{'news':n})

def login(request):
    if request.method == 'POST':

            uname=request.POST['username']
            password=request.POST['password']
        
            user=auth.authenticate(username=uname,password=password)


            if user:
                auth.login(request,user)

                return redirect('/dashboard')
        
            else:
             
                messages.error(request,"Invalid Credentials...")
                return redirect('/login')
                
    else:
            
            return render(request,'login.html')


def signup(request):
     if request.method == 'POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=uname).exists():

                return HttpResponse("Username taken")
            
            elif User.objects.filter(email=email).exists():

                return HttpResponse("E-mail taken")
            
            else:
                u=User.objects.create_user(username=uname,email=email,first_name=fname,last_name=lname,password=password1)

                u.save()

                messages.success(request,"Account Created!!...")
                return redirect('/login')
              
        else:

              messages.error(request,"Password is not Matching...")
              return redirect('/signup')
            
    
     else:

        return render(request,'signup.html')
     



def dashboard(request):

    p=Pin.objects.all()
    b=Board.objects.filter(user=request.user)

   
    pgn=Paginator(p,25)
    page_number=request.GET.get('page')
    
    x=pgn.get_page(page_number)

    return render(request,'dashboard.html',{'pins':x,'board':b})

def explore(request):
    b=Board.objects.all()
    return render(request,'explore.html',{'boards':b})

def allpins(request):
    p=Pin.objects.filter(user=request.user)
    return render(request,'allpins.html',{'pins':p})


def savedpins(request):
    p=SavedPin.objects.filter(user=request.user)
    return render(request,'savedpins.html',{'pins':p})

def viewpin(request,pin_id):
    if request.method == 'POST':
        form=CommentsForm(request.POST)
        p=Pin.objects.get(id=pin_id)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.pin=p
            abc.save()
            return redirect(f'/viewpin/{pin_id}')

    else:
        x=Pin.objects.get(id=pin_id)

        p=Profile.objects.get(user=x.user)
        f=CommentsForm()
        cmnt=Comments.objects.filter(pin=pin_id)

        return render(request,'viewpin.html',{'p':x,'pro':p,'form':f,'comments':cmnt})














def viewprofile(request,p_id):
    p=Profile.objects.get(id=p_id)
    x=Board.objects.filter(user=p.user)
    pin=Pin.objects.filter(user=p.user)
    return render(request,'profile.html',{'profile':p,'boards':x,'pins':pin})

def board(request,b_id):

    p=Pin.objects.filter(board=b_id)
    b=Board.objects.get(id=b_id)
    return render(request,'board.html',{'pins':p,'board':b})


@login_required(login_url='/login')
def search(request):
    item=request.GET['sdata']
    # b=Board.objects.filter(name__icontains=item)
    p=Pin.objects.filter(title__icontains=item)
    return render(request,'dashboard.html',{'pins':p,})


def logout(request):
    auth.logout(request)

    return redirect('/home')


def addboard(request):
     
    if request.method=='POST':
        form=BoardForm(request.POST,request.FILES)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.save()
            return redirect('/addpin')
        
    else:

        f=BoardForm()
        return render(request,'addboard.html',{'form':f})
    



@login_required(login_url='/login')
def addpin(request):
    
    if request.method=='POST':
            
        form=PinForm(request.POST,request.FILES)
        if form.is_valid():
            xyz=form.save(commit=False)
            xyz.user=request.user
            xyz.save()
            return redirect('/dashboard')
    
        
    else:
        if Profile.objects.filter(user=request.user).exists():
            f=PinForm()
            b=Board.objects.filter(user=request.user)
          
            return render(request,'addpin.html',{'form':f,'boards':b})
        else:
            messages.error(request,"You have to create a Profile to Create Pins...")
            return redirect('/addprofile')

           
 
        
        
    
def editpin(request,p_id):



    if request.method=='POST':

        p=Pin.objects.get(id=p_id)
        form=PinForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        
        
    else:

        p=Pin.objects.get(id=p_id)
    
        f=PinForm(instance=p)

        return render(request,'editpin.html',{'form':f})
    

    
def editboard(request,b_id):



    if request.method=='POST':

        b=Board.objects.get(id=b_id)
        form=BoardForm(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        
        
    else:

        b=Board.objects.get(id=b_id)
    
        f=BoardForm(instance=b)

        return render(request,'editboard.html',{'form':f})
    



def deletepin(request,p_id):

        p=Pin.objects.get(id=p_id)
        p.delete()

        return redirect('/dashboard')

def deleteboard(request,b_id):

        b=Board.objects.get(id=b_id)
        b.delete()

        return redirect('/profile')


@login_required(login_url='/login')
def addprofile(request):
    if request.method=='POST':

        
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            xyz=form.save(commit=False)
            xyz.user=request.user
            xyz.save()
            return redirect('/profile')
        
        
    else:

    
        f=ProfileForm()

        return render(request,'addprofile.html',{'form':f})
    
@login_required(login_url='/login')
def profile(request):
    if Profile.objects.filter(user=request.user).exists():
        p=Profile.objects.get(user=request.user)
        b=Board.objects.filter(user=request.user)
        # pin=Pin.objects.filter(board=b)
        return render(request,'profile.html',{'profile':p,'boards':b})
    else:
        return redirect('/addprofile')
    

@login_required(login_url='/login')
def savepin(request,p_id):
    
    if request.method=='POST':
        p=Pin.objects.get(id=p_id)
        
        form=SavedPinForm(request.POST,request.FILES)
        if form.is_valid():
            xyz=form.save(commit=False)
            xyz.title=p.title
            xyz.description=p.description
            xyz.image=p.image
            xyz.user=request.user
            xyz.save()
            return redirect('/dashboard')
    
        
    else:
        if Profile.objects.filter(user=request.user).exists():
            # p=Pin.objects.get(id=p_id)
            # f=SavedPinForm(instance=p)
          
            return render(request,'choice2.html')
        else:
            messages.error(request,"You have to create a Profile to Create Pins...")
            return redirect('/addprofile')
        

# def updates(request):
#     u=Update.objects.all()
#     return render(request,'base.html',{'updates':u})
# def message(request):
#     m=Message.objects.all()
#     return render(request,'base.html',{'messages':m})



def editprofile(request,pro_id):

    if request.method=='POST':

        p=Profile.objects.get(id=pro_id)
        form=ProfileForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        
        
    else:

        p=Profile.objects.get(id=pro_id)
    
        f=ProfileForm(instance=p)

        return render(request,'editprofile.html',{'form':f})

def deleteprofile(request,pro_id):

        p=Profile.objects.get(id=pro_id)
        p.delete()

        return redirect('/dashboard')