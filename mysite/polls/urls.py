from django.urls import path

from . import views

app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:foo_id>/foo/', views.foo, name='foo'),
    path('foolistview/', views.FooListView.as_view(), name='foolist'),
    path('<int:pk>/foodetailview/', views.FooDetailView.as_view(), name='foodetail'),
    path('<int:question_id>/baz/', views.baz, name='baz'),
    path('baz2/', views.baz2, name='baz2_nickname'),  
    path('users/',views.users, name='users'),
    path('userlistview/',views.UserListView.as_view(), name='userlist'),
    path('emails/',views.emails,name='emails'),
    path('employees/',views.employees,name='employees'),
]