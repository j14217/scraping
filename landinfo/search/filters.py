from .models import LandInfo
from  import filters


class MyOrderFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順) '

class LandInfoFilter(FilterSet):

    title = filters.CharFilter(name='title', label='タイトル', lookup_expr='contains')