from django.contrib import admin
from django.urls import path, include 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"), name = "index"),
    path('praktika_page',TemplateView.as_view(template_name="praktika_page.html"), name = "praktika_page"),
    path('buro_page',TemplateView.as_view(template_name="buro_page.html"), name = "buro_page"),
    path('team_page',TemplateView.as_view(template_name="team_page.html"), name = "team_page"),
    path('news_page',TemplateView.as_view(template_name="news_page.html"), name = "news_page"),
    path('contact_page',TemplateView.as_view(template_name="contact_page.html"), name = "contact_page"),

    path('pract_1',TemplateView.as_view(template_name="pract_pages/pract_1.html"), name = "pract_1"),
    path('pract_2',TemplateView.as_view(template_name="pract_pages/pract_2.html"), name = "pract_2"),
    path('pract_3',TemplateView.as_view(template_name="pract_pages/pract_3.html"), name = "pract_3"),
    path('pract_4',TemplateView.as_view(template_name="pract_pages/pract_4.html"), name = "pract_4"),
    path('pract_5',TemplateView.as_view(template_name="pract_pages/pract_5.html"), name = "pract_5"),
    path('pract_6',TemplateView.as_view(template_name="pract_pages/pract_6.html"), name = "pract_6"),
    path('pract_7',TemplateView.as_view(template_name="pract_pages/pract_7.html"), name = "pract_7"),
    path('pract_8',TemplateView.as_view(template_name="pract_pages/pract_8.html"), name = "pract_8"),
    path('pract_9',TemplateView.as_view(template_name="pract_pages/pract_9.html"), name = "pract_9"),
    path('pract_10',TemplateView.as_view(template_name="pract_pages/pract_10.html"), name = "pract_10"),
    path('pract_11',TemplateView.as_view(template_name="pract_pages/pract_11.html"), name = "pract_11"),
    path('pract_12',TemplateView.as_view(template_name="pract_pages/pract_12.html"), name = "pract_12"),
    path('pract_13',TemplateView.as_view(template_name="pract_pages/pract_13.html"), name = "pract_13"),
    path('pract_14',TemplateView.as_view(template_name="pract_pages/pract_14.html"), name = "pract_14"),
    path('pract_15',TemplateView.as_view(template_name="pract_pages/pract_15.html"), name = "pract_15"),
    path('pract_16',TemplateView.as_view(template_name="pract_pages/pract_16.html"), name = "pract_16"),
    path('pract_17',TemplateView.as_view(template_name="pract_pages/pract_17.html"), name = "pract_17"),
    path('pract_18',TemplateView.as_view(template_name="pract_pages/pract_18.html"), name = "pract_18"),
    path('pract_19',TemplateView.as_view(template_name="pract_pages/pract_19.html"), name = "pract_19"),
    path('pract_20',TemplateView.as_view(template_name="pract_pages/pract_20.html"), name = "pract_20"),
    path('pract_21',TemplateView.as_view(template_name="pract_pages/pract_21.html"), name = "pract_21"),
    
    path('BSV',TemplateView.as_view(template_name="team_pages/BSV.html"), name = "BSV"),
    path('BSP',TemplateView.as_view(template_name="team_pages/BSP.html"), name = "BSP"),
    path('BKV',TemplateView.as_view(template_name="team_pages/BKV.html"), name = "BKV"),
    path('ChEV',TemplateView.as_view(template_name="team_pages/ChEV.html"), name = "ChEV"),
    path('DKV',TemplateView.as_view(template_name="team_pages/DKV.html"), name = "DKV"),
    path('FAI',TemplateView.as_view(template_name="team_pages/FAI.html"), name = "FAI"),
    path('KDU',TemplateView.as_view(template_name="team_pages/KDU.html"), name = "KDU"),
    path('KDV',TemplateView.as_view(template_name="team_pages/KDV.html"), name = "KDV"),
    path('SDS',TemplateView.as_view(template_name="team_pages/SDS.html"), name = "SDS"),
    
    path('new_1',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_1"),
    path('new_2',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_2"),
    path('new_3',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_3"),
    path('new_4',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_4"),
    path('new_5',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_5"),
    path('new_6',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_6"),
    path('new_7',TemplateView.as_view(template_name="news_pages/new_1.html"), name = "new_7"),
    
    
    
    
]
