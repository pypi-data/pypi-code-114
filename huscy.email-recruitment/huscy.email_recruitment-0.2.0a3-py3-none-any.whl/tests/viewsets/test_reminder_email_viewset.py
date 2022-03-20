import pytest
from model_bakery import baker

from django.contrib.auth.models import Permission
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
)

pytestmark = pytest.mark.django_db


def test_admin_user_can_create_reminder_emails(admin_client, project):
    response = create_reminder_email(admin_client, project)

    assert response.status_code == HTTP_201_CREATED


def test_admin_user_can_delete_reminder_emails(admin_client, reminder_email):
    response = delete_reminder_email(admin_client, reminder_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_admin_user_can_list_reminder_emails(admin_client, project):
    response = list_reminder_emails(admin_client, project)

    assert response.status_code == HTTP_200_OK


def test_admin_user_can_update_reminder_emails(admin_client, reminder_email):
    response = update_reminder_email(admin_client, reminder_email)

    assert response.status_code == HTTP_200_OK


def test_user_with_permission_can_create_reminder_emails(client, user, project):
    add_permission = Permission.objects.get(codename='add_reminderemail')
    user.user_permissions.add(add_permission)

    response = create_reminder_email(client, project)

    assert response.status_code == HTTP_201_CREATED


def test_user_with_permission_can_delete_reminder_emails(client, user, reminder_email):
    delete_permission = Permission.objects.get(codename='delete_reminderemail')
    user.user_permissions.add(delete_permission)

    response = delete_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_user_with_permission_can_update_reminder_emails(client, user, reminder_email):
    change_permission = Permission.objects.get(codename='change_reminderemail')
    user.user_permissions.add(change_permission)

    response = update_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_200_OK


def test_user_with_membership_can_create_reminder_emails(client, user, project):
    baker.make('projects.Membership', project=project, user=user)

    response = create_reminder_email(client, project)

    assert response.status_code == HTTP_201_CREATED


def test_user_with_membership_can_delete_reminder_emails(client, user, reminder_email):
    baker.make('projects.Membership', project=reminder_email.project, user=user)

    response = delete_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_user_with_membership_can_update_reminder_emails(client, user, reminder_email):
    baker.make('projects.Membership', project=reminder_email.project, user=user)

    response = update_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_200_OK


def test_user_without_permissions_or_membership_cannot_create_reminder_emails(client, project):
    response = create_reminder_email(client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_without_permissions_or_membership_cannot_delete_reminder_emails(client,
                                                                              reminder_email):
    response = delete_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_without_permissions_or_membership_can_list_reminder_emails(client, project):
    response = list_reminder_emails(client, project)

    assert response.status_code == HTTP_200_OK


def test_user_without_permissions_or_membership_cannot_update_reminder_emails(client,
                                                                              reminder_email):
    response = update_reminder_email(client, reminder_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_create_reminder_emails(anonymous_client, project):
    response = create_reminder_email(anonymous_client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_delete_reminder_emails(anonymous_client, reminder_email):
    response = delete_reminder_email(anonymous_client, reminder_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_list_reminder_emails(anonymous_client, project):
    response = list_reminder_emails(anonymous_client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_update_reminder_emails(anonymous_client, reminder_email):
    response = update_reminder_email(anonymous_client, reminder_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def create_reminder_email(client, project):
    return client.post(
        reverse('reminderemail-list', kwargs=dict(project_pk=project.id)),
        data=dict(footer='footer', text='text')
    )


def delete_reminder_email(client, reminder_email):
    return client.delete(
        reverse(
            'reminderemail-detail',
            kwargs=dict(project_pk=reminder_email.project.id, pk=reminder_email.id)
        )
    )


def list_reminder_emails(client, project):
    return client.get(reverse('reminderemail-list', kwargs=dict(project_pk=project.id)))


def update_reminder_email(client, reminder_email):
    return client.put(
        reverse(
            'reminderemail-detail',
            kwargs=dict(project_pk=reminder_email.project.id, pk=reminder_email.id)
        ),
        data=dict(footer='new_footer', text='new_text')
    )
