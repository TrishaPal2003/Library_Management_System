
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from ..models.member_model import Member



class MemberListView(ListView):
    model = Member
    template_name = 'library/members.html'
    context_object_name = 'members'
