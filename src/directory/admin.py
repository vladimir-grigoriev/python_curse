from django.contrib import admin
from .models import *


models_list = [
    Author,
    Series,
    Genre,
    Publisher,
]
for model in models_list:
    admin.site.register(model)