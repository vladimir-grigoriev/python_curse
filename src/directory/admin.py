from django.contrib import admin
from .models import *


models_list = [
    Author,
    Series,
    Genre,
    Publisher,
    Binding,
    BookFormat,
    AgeRestriction
]

for model in models_list:
    admin.site.register(model)