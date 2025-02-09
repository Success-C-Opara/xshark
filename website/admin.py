from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from website.models import UserLink, Site,PageData





class UserLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'site', 'copy_link', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('user__username', 'site__name')
    actions = ['deactivate_expired_links']

    def copy_link(self, obj):
        if obj.is_active:
            return format_html(
                '<input type="text" value="{}" id="link-{}" readonly>'
                '<button onclick="copyToClipboard(\'link-{}\')">Copy</button>',
                obj.link, obj.id, obj.id
            )
        return "Inactive"
    copy_link.short_description = "Copy Link"

    def deactivate_expired_links(self, request, queryset):
        expired_links = queryset.filter(end_date__lt=timezone.now())
        expired_links.update(is_active=False)
        self.message_user(request, f"{expired_links.count()} expired links deactivated.")

    deactivate_expired_links.short_description = "Deactivate expired links"

admin.site.register(UserLink, UserLinkAdmin)
admin.site.register(Site)




class PageDataAdmin(admin.ModelAdmin):
    list_display = ['user_link', 'name', 'surname', 'date_added',"user", "page_name", "link"]
    search_fields = ['name', 'surname', 'user_link__user__username', 'user_link__site']

    # Add filtering by user link (page) for easy management
    list_filter = ['user_link__site', 'user_link__user']

admin.site.register(PageData, PageDataAdmin)


