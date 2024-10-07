from django.shortcuts import render
from .utils import convert_mol_img, defaultVal
from django.conf import settings

# convert to structure-svg and build context with structure-svg-path
def structure_handler(drug_obj) -> object:
    convert_mol_img(drug_obj)
    context = {}
    context['mol_img_url'] = settings.MOL_IMG_URL
    context['drug_pk']=drug_obj.pk
    return context

# Home site
def home(request):
    default_obj = defaultVal
    context = structure_handler(default_obj)
    context['title'] = 'Drug Structure'
    return render(request, 'mol_to_img/home.html', context)