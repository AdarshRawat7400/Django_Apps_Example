from django.urls import path,include
# from .views import article_detail, article_list
from  .views import ArticleAPIView, ArticleDetailAPIView, ArticleGenericAPIView
from .routers import router
urlpatterns = [

    ## Using APIView class based views
    path('article/',ArticleAPIView.as_view(),name='article'),
    path('detail/<int:pk>/',ArticleDetailAPIView.as_view(),name='article-detail'),    
    ## function based apiview urls 

    ## Using Generic class based views
    path('generic/article/<int:id>/',ArticleGenericAPIView.as_view(),name='generic_article'),
    # path('list/',article_list,name='article_list'),
    # path('detail/<int:pk>/',article_detail,name='article_detail'),

    # Using viewset with routers
    path('viewset/',include(router.urls),name='article_viewset'),
    path('viewset/<int:pk>/',include(router.urls),name='article_viewset')
]