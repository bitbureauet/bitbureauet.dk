from xml.dom import minidom
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone

from blog import models


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not args[0]:
            raise CommandError('Need xml file')

        if args[1] == 'delete':
            print('Flushing all posts ... ', end='')
            models.Post.objects.all().delete()
            print('Done!')

        xmldoc = minidom.parse(args[0])

        authors = xmldoc.getElementsByTagName('wp:author')
        for author in authors:
            username = author.getElementsByTagName('wp:author_login')[0].childNodes[0].nodeValue
            email = author.getElementsByTagName('wp:author_email')[0].childNodes[0].nodeValue

            first_name_nodes = author.getElementsByTagName('wp:author_first_name')[0].childNodes
            first_name = ''
            if first_name_nodes:
                first_name = first_name_nodes[0].nodeValue

            last_name_nodes = author.getElementsByTagName('wp:author_first_name')[0].childNodes
            last_name = ''
            if last_name_nodes:
                last_name = first_name_nodes[0].nodeValue

            User.objects.get_or_create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

        posts = xmldoc.getElementsByTagName('item')


        for field in models.Post._meta.local_fields:
            if field.name == "created_at":
                field.auto_now_add = False
            elif field.name == "updated_at":
                field.auto_now_add = False
                field.auto_now = False

        for post in posts:
            title = post.getElementsByTagName('title')[0].childNodes[0].nodeValue

            slug_nodes = post.getElementsByTagName('wp:post_name')[0].childNodes
            slug = None
            if len(slug_nodes):
                slug = slug_nodes[0].nodeValue

            pub_date = post.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            pub_date = datetime.fromtimestamp(mktime_tz(parsedate_tz(pub_date)))
            pub_date = timezone.make_aware(pub_date, timezone.get_current_timezone())

            creator = post.getElementsByTagName('dc:creator')[0].childNodes[0].nodeValue
            creator = User.objects.get(username=creator)

            status = post.getElementsByTagName('wp:status')[0].childNodes[0].nodeValue
            published = status == 'publish'

            content = post.getElementsByTagName('content:encoded')[0].childNodes[0].nodeValue

            print('Adding "{}" ... '.format(title), end='')

            post = models.Post.objects.create(
                title=title,
                slug=slug,
                published=published,
                body=content,
                created_at=pub_date,
                updated_at=pub_date
            )
            if post.published:
                post.published_at = pub_date
            post.edited_by.add(creator)

            print('Done!')
