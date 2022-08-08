from django.urls import path
from blogs import views

urlpatterns=[
   path("",views.getRout,name="routes"),
   path("blogs",views.getBlogs,name="blogs"),
   path("blog/<str:id>",views.getBlog,name="getblog"),
   path("blogs/new",views.createBlog,name="createblog"),
   path("blog/<str:id>/update",views.updateBlog,name="updateblog"),
   path("blog/<str:id>/delete/",views.deleteBlog,name="deleteblog"),
]