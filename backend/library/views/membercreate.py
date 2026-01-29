
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView


from ..models.member_model import Member




class MemberCreateView(CreateView):
    model = Member
    fields = ['student_id', 'name', 'email', 'phone', 'department']
    template_name = 'library/add_member.html'
    success_url = reverse_lazy('member_list')
