from django.contrib import admin
from django.urls import path

from board.views import board_view, thread_view

urlpatterns = [
    path('', board_view),
    path('<int:id>/', thread_view),
    path('admin/', admin.site.urls),
]
