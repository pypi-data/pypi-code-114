from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.utils.translation import gettext_lazy as _
from django.views import generic

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class CustomerConfig(OscarConfig):
    label = 'customer'
    name = 'apps.customer'
    verbose_name = _('Customer')

    namespace = 'customer'

    def ready(self):
        from .views import ProfileUpdateView, AddressCreateView, AccountAuthView
        from oscar.apps.customer import receivers  # noqa
        from oscar.apps.customer.alerts import receivers  # noqa
        from .views import (BankAccountListView, BankAccountUpdateView,
                            BankAccountCreateView, BankAccountDeleteView)
        self.bank_account_list = BankAccountListView
        self.bank_account_update = BankAccountUpdateView
        self.bank_account_create = BankAccountCreateView
        self.bank_account_delete = BankAccountDeleteView

        from apps.customer.wishlists.views import WishlistToggleProduct
        self.wishlists_toggle_product_view = WishlistToggleProduct

        self.summary_view = get_class('customer.views', 'AccountSummaryView')
        self.order_history_view = get_class('customer.views', 'OrderHistoryView')
        self.order_detail_view = get_class('customer.views', 'OrderDetailView')
        self.anon_order_detail_view = get_class('customer.views',
                                                'AnonymousOrderDetailView')
        self.order_line_view = get_class('customer.views', 'OrderLineView')

        self.address_list_view = get_class('customer.views', 'AddressListView')
        self.address_create_view = AddressCreateView
        self.address_update_view = get_class('customer.views', 'AddressUpdateView')
        self.address_delete_view = get_class('customer.views', 'AddressDeleteView')
        self.address_change_status_view = get_class('customer.views',
                                                    'AddressChangeStatusView')

        self.email_list_view = get_class('customer.views', 'EmailHistoryView')
        self.email_detail_view = get_class('customer.views', 'EmailDetailView')
        self.login_view = AccountAuthView
        self.logout_view = get_class('customer.views', 'LogoutView')
        self.register_view = get_class('customer.views', 'AccountRegistrationView')
        self.profile_view = get_class('customer.views', 'ProfileView')
        self.profile_update_view = ProfileUpdateView
        self.profile_delete_view = get_class('customer.views', 'ProfileDeleteView')
        self.change_password_view = get_class('customer.views', 'ChangePasswordView')

        self.notification_inbox_view = get_class('communication.notifications.views',
                                                 'InboxView')
        self.notification_archive_view = get_class('communication.notifications.views',
                                                   'ArchiveView')
        self.notification_update_view = get_class('communication.notifications.views',
                                                  'UpdateView')
        self.notification_detail_view = get_class('communication.notifications.views',
                                                  'DetailView')

        self.alert_list_view = get_class('customer.alerts.views',
                                         'ProductAlertListView')
        self.alert_create_view = get_class('customer.alerts.views',
                                           'ProductAlertCreateView')
        self.alert_confirm_view = get_class('customer.alerts.views',
                                            'ProductAlertConfirmView')
        self.alert_cancel_view = get_class('customer.alerts.views',
                                           'ProductAlertCancelView')

        self.wishlists_add_product_view = get_class('customer.wishlists.views',
                                                    'WishListAddProduct')
        self.wishlists_list_view = get_class('customer.wishlists.views',
                                             'WishListListView')
        self.wishlists_detail_view = get_class('customer.wishlists.views',
                                               'WishListDetailView')
        self.wishlists_create_view = get_class('customer.wishlists.views',
                                               'WishListCreateView')
        self.wishlists_create_with_product_view = get_class('customer.wishlists.views',
                                                            'WishListCreateView')
        self.wishlists_update_view = get_class('customer.wishlists.views',
                                               'WishListUpdateView')
        self.wishlists_delete_view = get_class('customer.wishlists.views',
                                               'WishListDeleteView')
        self.wishlists_remove_product_view = get_class('customer.wishlists.views',
                                                       'WishListRemoveProduct')
        self.wishlists_move_product_to_another_view = get_class(
            'customer.wishlists.views', 'WishListMoveProductToAnotherWishList')
        self.wishlists_realtime_search_view = get_class(
            'customer.wishlists.views', 'RealtimeSearchView')

    def get_urls(self):
        urls = [
            path(
                'favoriten/toggle/<int:product_pk>/',
                login_required(self.wishlists_toggle_product_view.as_view()),
                name='wishlists-toggle-product'),
            path(
                'favoriten/toggle/<int:product_pk>/<str:to_key>/',
                login_required(self.wishlists_toggle_product_view.as_view()),
                name='wishlists-toggle-product'),
            # Login, logout and register doesn't require login
            path('login/', self.login_view.as_view(), name='login'),
            path('logout/', self.logout_view.as_view(), name='logout'),
            path('register/', self.register_view.as_view(), name='register'),
            path('', login_required(self.summary_view.as_view()), name='summary'),
            path('change-password/', login_required(self.change_password_view.as_view()), name='change-password'),

            # Profile
            path('bankdaten/', login_required(self.bank_account_list.as_view()), name='bankaccount-list'),
            path('bankdaten/create/', login_required(self.bank_account_create.as_view()), name='bankaccount-create'),
            path('bankdaten/<int:pk>/edit/', login_required(self.bank_account_update.as_view()), name='bankaccount-update'),
            path('bankdaten/<int:pk>/delete/', login_required(self.bank_account_delete.as_view()), name='bankaccount-delete'),

            # Profile
            path('profil/', login_required(self.profile_view.as_view()), name='profile-view'),
            path('profil/edit/', login_required(self.profile_update_view.as_view()), name='profile-update'),
            path('profil/delete/', login_required(self.profile_delete_view.as_view()), name='profile-delete'),

            # Order history
            path('bestellungen/', login_required(self.order_history_view.as_view()), name='order-list'),
            re_path(
                r'^bestell-status/(?P<order_number>[\w-]*)/(?P<hash>[A-z0-9-_=:]+)/$',
                self.anon_order_detail_view.as_view(), name='anon-order'
            ),
            path('bestellungen/<str:order_number>/', login_required(self.order_detail_view.as_view()), name='order'),
            path(
                'bestellungen/<str:order_number>/<int:line_id>/',
                login_required(self.order_line_view.as_view()),
                name='order-line'),

            # Address book
            path('adressen/', login_required(self.address_list_view.as_view()), name='address-list'),
            path('adressen/add/', login_required(self.address_create_view.as_view()), name='address-create'),
            path('adressen/<int:pk>/', login_required(self.address_update_view.as_view()), name='address-detail'),
            path(
                'adressen/<int:pk>/delete/',
                login_required(self.address_delete_view.as_view()),
                name='address-delete'),
            re_path(
                r'^adressen/(?P<pk>\d+)/(?P<action>default_for_(billing|shipping))/$',
                login_required(self.address_change_status_view.as_view()),
                name='address-change-status'),

            # Email history
            path('emails/', login_required(self.email_list_view.as_view()), name='email-list'),
            path('emails/<int:email_id>/', login_required(self.email_detail_view.as_view()), name='email-detail'),

            # Notifications
            # Redirect to notification inbox
            path(
                'benachrichtigungen/', generic.RedirectView.as_view(url='/accounts/notifications/inbox/', permanent=False)),
            path(
                'benachrichtigungen/inbox/',
                login_required(self.notification_inbox_view.as_view()),
                name='notifications-inbox'),
            path(
                'benachrichtigungen/archive/',
                login_required(self.notification_archive_view.as_view()),
                name='notifications-archive'),
            path(
                'benachrichtigungen/update/',
                login_required(self.notification_update_view.as_view()),
                name='notifications-update'),
            path(
                'benachrichtigungen/<int:pk>/',
                login_required(self.notification_detail_view.as_view()),
                name='notifications-detail'),

            # Alerts
            # Alerts can be setup by anonymous users: some views do not
            # require login
            path('produktbenachrichtigungen/', login_required(self.alert_list_view.as_view()), name='alerts-list'),
            path('produktbenachrichtigungen/create/<int:pk>/', self.alert_create_view.as_view(), name='alert-create'),
            path('produktbenachrichtigungen/confirm/<str:key>/', self.alert_confirm_view.as_view(), name='alerts-confirm'),
            path('produktbenachrichtigungen/cancel/key/<str:key>/', self.alert_cancel_view.as_view(), name='alerts-cancel-by-key'),
            path(
                'produktbenachrichtigungen/cancel/<int:pk>/',
                login_required(self.alert_cancel_view.as_view()),
                name='alerts-cancel-by-pk'),

            # Wishlists
            path('favoriten/', login_required(self.wishlists_list_view.as_view()), name='wishlists-list'),
            path(
                'favoriten/add/<int:product_pk>/',
                login_required(self.wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            path(
                'favoriten/<str:key>/add/<int:product_pk>/',
                login_required(self.wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            path(
                'favoriten/create/',
                login_required(self.wishlists_create_view.as_view()),
                name='wishlists-create'),
            path(
                'favoriten/create/with-product/<int:product_pk>/',
                login_required(self.wishlists_create_view.as_view()),
                name='wishlists-create-with-product'),
            # Wishlists can be publicly shared, no login required
            path('favoriten/<str:key>/', self.wishlists_detail_view.as_view(), name='wishlists-detail'),
            path(
                'favoriten/<str:key>/update/',
                login_required(self.wishlists_update_view.as_view()),
                name='wishlists-update'),
            path(
                'wishlists/<str:key>/delete/',
                login_required(self.wishlists_delete_view.as_view()),
                name='wishlists-delete'),
            path(
                'favoriten/<str:key>/lines/<int:line_pk>/delete/',
                login_required(self.wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            path(
                'favoriten/<str:key>/products/<int:product_pk>/delete/',
                login_required(self.wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            path(
                'favoriten/<str:key>/lines/<int:line_pk>/move-to/<str:to_key>/',
                login_required(self.wishlists_move_product_to_another_view.as_view()),
                name='wishlists-move-product-to-another'),
            path(
                'favoriten/<str:key>/realtime-search/',
                login_required(self.wishlists_realtime_search_view.as_view()),
                name='product-realtime-search',
            ),
            path(
                'favoriten/<str:key>/realtime-search/<int:product>/',
                login_required(self.wishlists_realtime_search_view.as_view()),
                name='product-realtime-search',
            ),
        ]
        return self.post_process_urls(urls)
