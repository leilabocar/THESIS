import django_filters

from .models import *

class buyersFilter(django_filters.FilterSet):
    lot_choices=[('Lawn Lot','Lawn Lot'),
                      ('Mausoleum','Mausoleum'),
                      ('Niche','Niche')]
    
    terms_choices=[('Cash','Cash'),
                   ('1 Year','1 Year'),
                   ('2 Years','2 Years'),
                   ('3 Years','3 Years'),
                   ('Full Down','Full Down'),
                   ('Reservation','Reservation')]

    lot_type = django_filters.ChoiceFilter(empty_label='Select Lot Type',choices=lot_choices)
    terms = django_filters.ChoiceFilter(empty_label='Terms',choices=terms_choices)
    class Meta:
        model = BuyersFormModel
        fields = '__all__'

class appointmentFilter(django_filters.FilterSet):
    class Meta:
        model = BookAppointmentModel
        fields = '__all__'

class clientpaymentFilter(django_filters.FilterSet):
    terms_choices=[('Cash','Cash'),
                   ('1 Year','1 Year'),
                   ('2 Years','2 Years'),
                   ('3 Years','3 Years'),
                   ('Full Down','Full Down'),
                   ('Reservation','Reservation')]

    terms = django_filters.ChoiceFilter(empty_label='Terms',choices=terms_choices)
    class Meta:
        model = LotOrder
        fields = '__all__'

class inquiryFilter(django_filters.FilterSet):
    lot_choices=[('Lawn Lot','Lawn Lot'),
                      ('Mausoleum','Mausoleum'),
                      ('Niche','Niche'),
                      ('Apartment','Apartment')]

    lot_type = django_filters.ChoiceFilter(empty_label='Select Lot Type',choices=lot_choices)
    class Meta:
        model = InquiryFormModel
        fields = '__all__'
        
class productFilter(django_filters.FilterSet):
    lot_choices=[('Lawn Lot','Lawn Lot'),
                      ('Mausoleum','Mausoleum'),
                      ('Niche','Niche'),
                      ('Apartment','Apartment')]

    lot = django_filters.ChoiceFilter(empty_label='Select Lot Type',choices=lot_choices)
    class Meta:
        model = Product
        fields = '__all__'

class applicationFilter(django_filters.FilterSet):
    class Meta:
        model = ApplicationFormModel
        fields = '__all__'

