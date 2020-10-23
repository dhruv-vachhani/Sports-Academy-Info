from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.about,name='about'),
    path('',views.classes,name='classes'),
    path('',views.contact,name='contact'),
    path('',views.events,name='events'),
    path('yoga/',views.YogaListView.as_view() , name = 'club'),
    path('center/<int:pk>', views.YogaDetailView.as_view(), name='yoga-detail'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)