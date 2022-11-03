from rest_framework.permissions import BasePermission

from selections.models import Selection


class SelectionUpdatePermission(BasePermission):
    message = "Вы не можете изменять подборки."

    def has_permission(self, request, view):
        selection = Selection.objects.get(id=view.kwargs["pk"])

        if selection.owner.id != request.user.id:
            return False

        return True