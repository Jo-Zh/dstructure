from django.shortcuts import render
from .utils import molecule_to_svg, defaultVal

# convert to structure-svg list based on objects smol field
def structure_handler(drug_objs) -> dict:
    context ={}
    structure_list = [molecule_to_svg(obj).decode('utf-8') for obj in drug_objs]
    context['structure_list'] = structure_list  
    return context

# Home site
def home(request):
    default_objs = [defaultVal] # objects list from the model
    context = structure_handler(default_objs)
    context['title'] = 'Drug Structure'
    return render(request, 'mol_to_img/home.html', context)