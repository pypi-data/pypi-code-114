from django.contrib.auth import authenticate


class FirebaseTokenMiddleware:

    def resolve(self, next, root, info, **kwargs):
        context = info.context

        user = authenticate(request=context, **kwargs)

        if user is not None:
            context.user = user

        return next(root, info, **kwargs)
