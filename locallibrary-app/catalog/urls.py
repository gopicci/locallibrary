from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # name is for reverse url mapping, ie <a href="{% url 'index' %}">Home</a>, more robust than direct linking in case of updates
    path('books/', views.BookListView.as_view(), name='books'),  # calling view as class instead, less code, need to call .as_view()
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),  # could also use regular expressions. ?P returns strings
    # path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),  # these to pas additional options as third unnamed arg, useful ie to use same view for multiple resources
    # path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),  # don't use same var names as name

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksListView.as_view(), name='all-borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]