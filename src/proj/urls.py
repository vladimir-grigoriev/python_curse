from django.contrib import admin
from django.urls import path, include
from hello_world.views import hello_world
from directory.views import all_directories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('directories/', include('directory.urls')),
    # path()
    #path('<int:author_id>/', get_detailed_directory_view),
]
