from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='base'),
  url(r'^edit_libro/$', views.edit_libro, name='edit_libro'),
  url(r'^prestar/$', views.prestar, name='prestar'),
  path('pedir_prestamo/<int:id>', views.pedir_prestamo, name='pedir_prestamo'),
  path('devolver_prestamo/<int:id>', views.devolver_prestamo, name='devolver_prestamo'),
  path('update/', views.update, name='update'),
  path('update/<int:id>', views.update, name='update'),
  path('delete/<int:id>', views.delete),
  url(r'^estadisticas/$', views.estadisticas, name='estadisticas'),
  url(r'^json_estadisticas/$',views.json_estadisticas,name="json_estadisticas"),
]
