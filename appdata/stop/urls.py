from django.urls import path, include

from . import views
urlpatterns = [
    path('stop/', views.NoteListview.as_view(), name="node.list"),
    path('stop/<int:pk>', views.NoteDetailsview.as_view(), name='note.detail'),
    path('stop/<int:pk>/edit/', views.NodeUpadte.as_view(), name='note.update'),
    path('stop/<int:pk>/delete/', views.DeleteNode.as_view(), name='note.delete'),
    path('stop/new/', views.CreateNodeView.as_view(), name="form.detail")

]
