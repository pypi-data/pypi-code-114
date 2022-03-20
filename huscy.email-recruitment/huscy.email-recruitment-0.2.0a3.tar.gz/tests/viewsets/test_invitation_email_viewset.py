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


def test_admin_user_can_create_invitation_emails(admin_client, project):
    response = create_invitation_email(admin_client, project)

    assert response.status_code == HTTP_201_CREATED


def test_admin_user_can_delete_invitation_emails(admin_client, invitation_email):
    response = delete_invitation_email(admin_client, invitation_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_admin_user_can_list_invitation_emails(admin_client, project):
    response = list_invitation_emails(admin_client, project)

    assert response.status_code == HTTP_200_OK


def test_admin_user_can_update_invitation_emails(admin_client, invitation_email):
    response = update_invitation_email(admin_client, invitation_email)

    assert response.status_code == HTTP_200_OK


def test_user_with_permission_can_create_invitation_emails(client, user, project):
    add_permission = Permission.objects.get(codename='add_invitationemail')
    user.user_permissions.add(add_permission)

    response = create_invitation_email(client, project)

    assert response.status_code == HTTP_201_CREATED


def test_user_with_permission_can_delete_invitation_emails(client, user, invitation_email):
    delete_permission = Permission.objects.get(codename='delete_invitationemail')
    user.user_permissions.add(delete_permission)

    response = delete_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_user_with_permission_can_update_invitation_emails(client, user, invitation_email):
    change_permission = Permission.objects.get(codename='change_invitationemail')
    user.user_permissions.add(change_permission)

    response = update_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_200_OK


def test_user_with_membership_can_create_invitation_emails(client, user, project):
    baker.make('projects.Membership', project=project, user=user)

    response = create_invitation_email(client, project)

    assert response.status_code == HTTP_201_CREATED


def test_user_with_membership_can_delete_invitation_emails(client, user, invitation_email):
    baker.make('projects.Membership', project=invitation_email.project, user=user)

    response = delete_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_user_with_membership_can_update_invitation_emails(client, user, invitation_email):
    baker.make('projects.Membership', project=invitation_email.project, user=user)

    response = update_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_200_OK


def test_user_without_permissions_or_membership_cannot_create_invitation_emails(client, project):
    response = create_invitation_email(client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_without_permissions_or_membership_cannot_delete_invitation_emails(client,
                                                                                invitation_email):
    response = delete_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_without_permissions_or_membership_can_list_invitation_emails(client, project):
    response = list_invitation_emails(client, project)

    assert response.status_code == HTTP_200_OK


def test_user_without_permissions_or_membership_cannot_update_invitation_emails(client,
                                                                                invitation_email):
    response = update_invitation_email(client, invitation_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_create_invitation_emails(anonymous_client, project):
    response = create_invitation_email(anonymous_client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_delete_invitation_emails(anonymous_client, invitation_email):
    response = delete_invitation_email(anonymous_client, invitation_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_list_invitation_emails(anonymous_client, project):
    response = list_invitation_emails(anonymous_client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_anonymous_user_cannot_update_invitation_emails(anonymous_client, invitation_email):
    response = update_invitation_email(anonymous_client, invitation_email)

    assert response.status_code == HTTP_403_FORBIDDEN


def create_invitation_email(client, project):
    return client.post(
        reverse('invitationemail-list', kwargs=dict(project_pk=project.id)),
        data=dict(footer='footer', text='text')
    )


def delete_invitation_email(client, invitation_email):
    return client.delete(
        reverse(
            'invitationemail-detail',
            kwargs=dict(project_pk=invitation_email.project.id, pk=invitation_email.id)
        )
    )


def list_invitation_emails(client, project):
    return client.get(reverse('invitationemail-list', kwargs=dict(project_pk=project.id)))


def update_invitation_email(client, invitation_email):
    return client.put(
        reverse(
            'invitationemail-detail',
            kwargs=dict(project_pk=invitation_email.project.id, pk=invitation_email.id)
        ),
        data=dict(footer='new_footer', text='new_text')
    )
