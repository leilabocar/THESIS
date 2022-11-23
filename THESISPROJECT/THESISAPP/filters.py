import django_filters

from .models import *

class buyersFilter(django_filters.FilterSet):
    class Meta:
        model = BuyersFormModel
        fields = '__all__'

class appointmentFilter(django_filters.FilterSet):
    class Meta:
        model = BookAppointmentModel
        fields = '__all__'

class clientpaymentFilter(django_filters.FilterSet):
    class Meta:
        model = LotOrder
        fields = '__all__'

class inquiryFilter(django_filters.FilterSet):
    class Meta:
        model = InquiryFormModel
        fields = '__all__'
        
class productFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'