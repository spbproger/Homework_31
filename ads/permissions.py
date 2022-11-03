from rest_framework.permissions import BasePermission

from ads.models import Ad
from users.models import User


class AdUpdatePermission(BasePermission):
    message = "Вы не можете изменять и удалять это объявление."

    def has_permission(self, request, view):
        ad = Ad.objects.get(id=view.kwargs["pk"])

        if ad.author_id == request.user.id:
            return True

        if request.user.role in [User.ADMIN, User.MODERATOR]:
            return True

        return False
