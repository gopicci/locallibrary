from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Language, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)


# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # remove 3 weird new instances placeholders


# Register the Admin classes for Book using the decorator, same as admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'display_genre')  # can't display genre directly as it's a manytomany, high db cost. need to define a function, for example purposes
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
