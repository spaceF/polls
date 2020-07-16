from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Polls, Persons


class PersonsInline(admin.TabularInline):
    model = Persons
    extra = 1
    fields = ('votes', 'img', 'get_image', 'name',
              'middle_name', 'surname', 'age', 'bio')
    readonly_fields = ('votes', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} '
                         f'width="100" height="110"')

    get_image.short_description = "Фото"


@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    """Голосования"""
    """Детали голосования"""
    fieldsets = (
        ('Общие', {
            'fields': (('name', 'url',),)
        }),

        ('Информация о дате', {
            'fields': (('start', 'finish',
                        'max_count_votes'),)
        }),

        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('active',)
        }),
    )
    inlines = [PersonsInline]
    save_on_top = True
    save_as = True

    """Список голосований"""
    list_editable = ('active',)
    list_display = ('id', 'name', 'start',
                    'finish', 'active',)
    list_display_links = ('name',)
    list_filter = ('active', 'name',)
    search_fields = ('name',)


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    """Кандидаты"""
    """Детали кандидата"""
    exclude = ('polls', 'votes')
    readonly_fields = ('get_image',)

    """Список кандидатов"""
    list_display = ('id', 'get_image', 'name',
                    'middle_name', 'surname',
                    'age', 'bio')
    list_display_links = ('name',)
    list_filter = ('polls__name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} '
                         f'width="50" height="60"')

    get_image.short_description = "Фото"


admin.site.site_title = 'Django Тестовое Задание'
admin.site.site_header = 'Django Тестовое Задание'
