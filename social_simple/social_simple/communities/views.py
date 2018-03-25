from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Community, Member
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
# Create your views here.


class CreateCommunity(LoginRequiredMixin,
                      generic.CreateView):
    permission_required = True
    model = Community
    fields = ['name', 'description']


class SingleCommunity(generic.DetailView):
    model = Community


class ListCommunities(generic.ListView):
    model = Community


class JoinCommunity(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('communities:single', kwargs={
            'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        community = get_object_or_404(
            Community,
            slug=self.kwargs.get('slug'))

        try:
            Member.objects.create(user=self.request.user, community=community)
        except IntegrityError:
            messages.warning(self.request, ("Already a member!"))
        else:
            messages.success(self.request, ('You are now a member!'))

        return super().get(request, *args, **kwargs)


class LeaveCommunity(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('communities:single', kwargs={
            'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = Member.objects.filter(
                user=self.request.user,
                community__slug=self.kwargs.get('slug')
            ).get()
        except Member.DoesNotExist:
            messages.warning(self.request, ("You are not a member!"))
        else:
            membership.delete()
            messages.success(self.request, ('You left the community :(!'))

        return super().get(request, *args, **kwargs)
