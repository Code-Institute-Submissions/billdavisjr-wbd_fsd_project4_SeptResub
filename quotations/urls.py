"""home app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_quotations, name='quotations'),
    path('<int:quotation_id>/', views.quotation_detail, name='quotation_detail'),
    path('add/', views.add_quotation, name='add_quotation'),
    path('edit/<int:quotation_id>/', views.edit_quotation, name='edit_quotation'),
    path('delete/<int:quotation_id>/', views.delete_quotation, name='delete_quotation'),
    path('categories/', views.all_categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]
