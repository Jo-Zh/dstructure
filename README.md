# Quick Start with dstructure

## Use dstructure as a Package

Follow these steps to utilize this package for drawing molecular structures from your model data:

1. **install Dependencies**: run `pip install -r requirements.txt`
2. **build the package**: run `python setup.py sdist`, generating the install file:
   `/your/local/path/to/dstructure/dist/mol_to_img-0.1.tar.gz`
3. **install package**: install `mol_to_img-0.1.tar.gz` as a pip package in your own django project by running
   `pip install /your/local/path/to/dstructure/dist/mol_to_img-0.1.tar.gz`
4. **Use `structure_handler` Function**: to draw molecular structures, for example:

- in `<your-app>/views.py`:

```
from mol_to_img import structure_handler
# Home site
def home(request):
    # Retrieve your objects from the model, such as a drug model
    context = structure_handler(drug_object)
    context['title'] = 'Drug Structure'
    return render(request, 'home.html', context)
```

- in your templates: `home.html`:

```
{% include 'mol_to_img/structure.html' %}

```

## Run as Individual project:

1. run `pip install -r requirements.txt` - install all dependencies in environment
2. start project via `python manage.py runserver`
