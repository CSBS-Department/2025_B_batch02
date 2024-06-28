from django.urls import path
from monitor import views 
from monitor.views import Index, Network, File, Firewall, Alert, EncryptView, DecryptView, Ddos, User_profile, User_privacy_setting, Sign_in, Sign_up, Recoverpw, EncryptSuccessView,DecryptSuccessView
urlpatterns = [
    # ... other url patterns
    #path('alerts/', monitor_views.alert_list, name='alert_list'),
    #path('alerts/<int:alert_id>/', monitor_views.alert_detail, name='alert_detail'),
    path('', Index.as_view(), name='index'),
    path('network', Network, name='network'),
    path('file', File.as_view(), name='file'),
    path('firewall', Firewall.as_view(), name='firewall'),
    path('alert', Alert.as_view(), name='alert'),
    path('encrypt/', EncryptView.as_view(), name='encrypt'),
    path('encrypt/success/', EncryptSuccessView.as_view(), name='encryption_success'),
    path('decrypt/', DecryptView.as_view(), name='decrypt'),
    path('decrypt/success/', DecryptSuccessView.as_view(), name='decryption_success'),
    
    path('ddos', Ddos.as_view(), name='ddos'),


    path('user-profile',User_profile.as_view(), name='user-profile'),
    path('user-privacy-setting',User_privacy_setting.as_view(), name='user-privacy-setting'),
    path('sign-in',Sign_in.as_view(), name='sign-in'),
    path('sign-up',Sign_up.as_view(), name='sign-up'),
    path('recoverpw',Recoverpw.as_view(), name='recoverpw'),


    
]

