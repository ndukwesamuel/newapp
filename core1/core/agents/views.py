from django.shortcuts import render,redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from leads.models import Agent
from agents.forms import AgentModelForm





class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agent_list.html'

    # def get_queryset(self):
    #     return Agent.objects.all()  becuse we want to filter by organisation 

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self): 
        return reverse("agents:agent")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agent_detail.html'
    context_object_name = "agent"

    # def get_queryset(self):  
    #     return Agent.objects.all()

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)



class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self): 
        return reverse("agents:agent")

    # def get_queryset(self):  
    #     return Agent.objects.all()

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(DeleteView):
    template_name = 'delete.html'
    # queryset = Agent.objects.all()
    def get_success_url(self):
        # return '/'  becuse we want to use the name space 
        return reverse("agents:agent")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
