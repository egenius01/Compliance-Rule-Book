from .models import MasterRuleBook, Upload
import django_filters

class RuleFilter(django_filters.FilterSet):
    returns= django_filters.CharFilter(lookup_expr='icontains')
    section = django_filters.CharFilter(lookup_expr='icontains')
    initial_date_of_rendition=django_filters.DateFilter(field_name='initial_date_of_rendition')
    class Meta:
        model = MasterRuleBook
        fields = ['returns', 'section', 'frequency', 'authority','Responsible_Officer', 'department']

class RuleBookFilter(django_filters.FilterSet):
    returns= django_filters.CharFilter(lookup_expr='icontains')
    section = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = MasterRuleBook
        fields = ['returns', 'section', 'department']


class AuthenticateFilter(django_filters.FilterSet):
    published_date = django_filters.DateFilter(field_name='published_date')
    class Meta:
        model = Upload
        fields = ['returns','published_date','posted_by','approved']
