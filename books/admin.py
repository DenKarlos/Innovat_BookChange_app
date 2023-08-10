from django.contrib import admin
from .models import Book, Genre, Order, Chat



class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'owner',)
admin.site.register(Book, BookAdmin)


class GenreAdmin(admin.ModelAdmin):

    list_display = ('id', 'genre_name',)
admin.site.register(Genre, GenreAdmin)


class OrderAdmin(admin.ModelAdmin):

    list_display = ('requester', 'requested_part', 'status', 
                    'requester_approval', 'requested_part_approval', 
                    'requester_is_changed','requested_part_is_changed')
admin.site.register(Order, OrderAdmin)


class ChatAdmin(admin.ModelAdmin):

    list_display = ('messege', 'owner_user','owner_book')
admin.site.register(Chat, ChatAdmin)



