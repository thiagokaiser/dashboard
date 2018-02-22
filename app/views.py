from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    update_session_auth_hash
    )
from django.contrib.auth.forms import (
    UserChangeForm, 
    UserCreationForm, 
    PasswordChangeForm
    )
from .forms import (    
    EditProfileForm,
    RegisterProfileForm,    
    ProfileForm,    
    )
from .models import Profile, Mensagem

# Create your views here.
def Home(request):
	return render(request, 'app/base.html', {})

def Profile(request):
    args = {'user': request.user,
            'profile': request.user.profile}
    return render(request, 'accounts/profile.html', args)

def Edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('app:profile')
        #else:
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def Register(request):
    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:profile')            
                
        args = {'form': form}
        return render(request,'accounts/register.html', args)
        
    else:
        form = RegisterProfileForm()
        args = {'form': form}
        return render(request,'accounts/register.html', args)

def Change_Password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('app:profile')
        else:
            args = {'form': form}
            return render(request,'accounts/change_password.html', args)


    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

def Inbox(request):        
    reg_pag           = request.GET.get('reg_pag', 10)        
    
    filtro_url = '?reg_pag=' + str(reg_pag)
    filtro = {'url': filtro_url,              
              'pag': reg_pag,              
              }    

    mensagem = Mensagem.objects.all()         

    page    = request.GET.get('page', 1)    

    paginator = Paginator(mensagem, reg_pag)
    try:
        pagamentos = paginator.page(page)
    except PageNotAnInteger:
        pagamentos = paginator.page(1)
    except EmptyPage:
        pagamentos = paginator.page(paginator.num_pages)    
    
    return render(request, 'app/inbox.html', {'mensagem': mensagem, 'filtro': filtro})

def Msg_View(request, pk):    
    mensagem = get_object_or_404(Mensagem, pk=pk)    
    return render(request, 'app/mensagem_detail.html', {'msg':mensagem})