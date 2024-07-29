
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from .models import Recipe, RecipeLike

@shared_task
def send_email(subject, message, recipient_list):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

@shared_task
def send_daily_likes_notification():
    today = timezone.now().date()
    authors = Recipe.objects.values('author').distinct()

    for author in authors:
        author_id = author['author']
        recipes = Recipe.objects.filter(author_id=author_id)
        total_likes = 0

        for recipe in recipes:
            total_likes += RecipeLike.objects.filter(recipe=recipe, created__date=today).count()

        if total_likes > 0:
            subject = 'Daily Likes Notification'
            message = f'You have received {total_likes} likes on your recipes today.'
            recipient_list = [recipe.author.email for recipe in recipes if recipe.author.email]

            if recipient_list:
                send_email.delay(subject, message, recipient_list)
