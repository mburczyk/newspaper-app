from django.contrib import admin

from .models import Article, Comment

'''
WERSJA NR JEDEN (kazda linijka osobno)

class CommentInline(admin.StackedInline):
    model = Comment    
    extra = 0
'''



'''
WERSJA NR DWa (wszystko w jednej linijce)
'''

class CommentInline(admin.TabularInline):
    model = Comment    
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]



admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)