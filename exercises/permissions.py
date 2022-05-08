from rest_framework.permissions import BasePermission
from django.conf import settings


class IsOwner(BasePermission):
    message = "You must be the owner of this object to perform this function"

    def has_object_permission(self, request, view, object):
        return object.user.pk == request.user.pk
