"""Filters used in our views."""

from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, ChoiceFilter, DateFromToRangeFilter, FilterSet

from readthedocs.audit.models import AuditLog


class UserSecurityLogFilter(FilterSet):

    ip = CharFilter(field_name='ip', lookup_expr='exact')
    project = CharFilter(field_name='log_project_slug', lookup_expr='exact')
    action = ChoiceFilter(
        field_name='action',
        lookup_expr='exact',
        choices=[
            (AuditLog.AUTHN, _("Authentication success")),
            (AuditLog.AUTHN_FAILURE, _("Authentication failure")),
            (AuditLog.INVITATION_SENT, _("Invitation sent")),
            (AuditLog.INVITATION_REVOKED, _("Invitation revoked")),
            (AuditLog.INVITATION_ACCEPTED, _("Invitation accepted")),
            (AuditLog.INVITATION_DECLINED, _("Invitation declined")),
        ],
    )
    date = DateFromToRangeFilter(field_name='created')

    class Meta:
        model = AuditLog
        fields = []


class OrganizationSecurityLogFilter(UserSecurityLogFilter):

    action = ChoiceFilter(
        field_name='action',
        lookup_expr='exact',
        choices=[
            (AuditLog.AUTHN, _("Authentication success")),
            (AuditLog.AUTHN_FAILURE, _("Authentication failure")),
            (AuditLog.PAGEVIEW, _("Page view")),
            (AuditLog.DOWNLOAD, _("Download")),
            (AuditLog.INVITATION_SENT, _("Invitation sent")),
            (AuditLog.INVITATION_REVOKED, _("Invitation revoked")),
            (AuditLog.INVITATION_ACCEPTED, _("Invitation accepted")),
        ],
    )
    user = CharFilter(field_name='log_user_username', lookup_expr='exact')
