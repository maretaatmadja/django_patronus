from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #aman ga ubah data
            return True
        else:
            return obj.author == request.user