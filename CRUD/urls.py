from django.urls import path
from .views import KegiatanList, KegiatanDetails
# kegiatan_list,kegiatan_details, 

urlpatterns =[
    path('kegiatan/', KegiatanList.as_view()),
    path('kegiatan/<int:id>/', KegiatanDetails.as_view()),

    # path('kegiatan/', kegiatan_list),
    # path('kegiatan/<int:pk>/', kegiatan_details),
]