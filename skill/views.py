from django.shortcuts import render
from .models import Skill
def all_skills(request):
    skills = Skill.objects.order_by('-date')
    return render(request, 'skill/all_skills.html', {'skills':skills})

def details(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skill/detail.html',{'skill':skill})
