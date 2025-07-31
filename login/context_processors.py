from login.models import voter

def user_email_processor(request):
    user_email = None
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = voter.objects.get(id=user_id)
            user_email = user.email
        except voter.DoesNotExist:
            pass
    return {'user_email': user_email}
