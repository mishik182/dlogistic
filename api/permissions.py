from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'Permissions error!'

    def has_object_permission(self, request, view, obj):
        # print(obj.user)
        print(request.user)
