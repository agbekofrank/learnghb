from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'you dont have permission to update this file, (this message is overridden)'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user