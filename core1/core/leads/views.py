from django.shortcuts import render,redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from leads.models import Lead
from leads.forms import *



class LandingPageView(TemplateView):
    template_name = "landing.html"


class SignupView(CreateView):
    template_name = 'signup.html' 
    form_class = CustomUserCreation

    def get_success_url(self):
        # return '/'  becuse we want to use the name space 
        return reverse("login")

class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leadsy/lead_list.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset
 
def homepage(request):
    lead = Lead.objects.all()

    context = {"lead":lead}
    return render(request, 'index.html', context)

class LeadDetailView(DetailView):
    template_name = 'leaddetail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset


def leaddetail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead":lead}
    return render(request, 'leaddetail.html', context)

class CreateHome(CreateView):
    template_name = 'create.html'
    form_class = Createform

    def get_success_url(self):
        # return '/'  becuse we want to use the name space 
        return reverse("leads:home")

def lead_create(request):
    form = Createform(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context ={'form':form}
    return render(request, "create.html", context)


class UpdateHome(UpdateView):
    template_name = 'update.html'
    form_class = Createform

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        # return '/'  becuse we want to use the name space 
        return reverse("leads:home")

def leadUdate(request,id):
    lead = Lead.objects.get(id=id)
    form = Createform(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"lead":lead, "form":form }
    return render(request, 'update.html', context)


class DeleteHome(DeleteView):
    template_name = 'delete.html'   
    def get_success_url(self):
        # return '/'  becuse we want to use the name space 
        return reverse("leads:home")

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/")


