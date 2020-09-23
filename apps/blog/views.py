# apps/blog/views.py

import datetime

from calendar import month_name

# from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView

from taggit.models import Tag

from .models import BlogEntry


class BlogPostList(ListView):

    template_name = 'list.html'

    def _get_posts_for_month_year(self, month, year):
        return BlogEntry.objects.filter(
            publish_date__month=month,
            publish_date__year=year,
            published=True
        ).count()

    def _get_list_of_months(self):
        start_date = BlogEntry.objects.filter(
            published=True
        ).order_by(
            '-publish_date'
        ).values_list(
            'publish_date',
            flat=True
        ).first()
        today = datetime.datetime.today()

        # loop over years and months
        for year in range(today.year, start_date.year - 1, -1):
            start, end = 12, 0
            if year == today.year:
                start = today.month
            if year == start_date.year:
                end = start_date.month - 1
            return [
                dict(
                    year=year,
                    name=month_name[month],
                    post_count=self._get_posts_for_month_year(month, year)
                )
                for month in range(start, end, -1)
            ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months'] = self._get_list_of_months()
        context['tags'] = Tag.objects.all().order_by('name') #Tag.objects.annotate(post_count=Count('taggit_taggeditem_items'))
        return context

    def get_queryset(self):
        posts = BlogEntry.objects.filter(published=True).order_by('-publish_date')

        # if self.kwargs.get('tag', None):
        #     self.tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        #     posts = posts.filter(tags__name=self.tag)

        if self.kwargs.get('slug', None):
            posts = posts.filter(slug=self.kwargs['slug']).first()

        return posts


def view_acronyms(request):
    return render(request, 'acronyms.html', context=dict())