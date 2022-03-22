import unittest
from unittest.mock import Mock

from cloudshell.orch.pool.helpers.master_sandbox import get_master_sandbox


class TestMasterSandboxHelpers(unittest.TestCase):

    def setUp(self) -> None:
        self.sandbox = Mock()

    def test_get_master_sandbox_not_found_error(self):
        # arrange
        resource1 = Mock(Name="")
        resource2 = Mock(Name="")
        self.sandbox.components.resources = {resource1.Name: resource1, resource2.Name: resource2}
        self.sandbox.automation_api.GetResourceDetails.return_value = Mock(ResourceAttributes=[])

        # act & assert
        with self.assertRaisesRegex(ValueError, "Master sandbox not found"):
            get_master_sandbox(self.sandbox)

    def test_get_master_sandbox_sub_resource(self):
        #region arrange
        def get_resource_details(*args, **kwargs):
            if args[0] == root_resource_name:
                return root_resource
            elif args[0] == pool_name:
                return vm_pool_resource
            else:
                return Mock(ResourceAttributes=[])

        def get_resource_availability(*args, **kwargs):
            return resource_availability_api_result if args[0][0] == pool_name else Mock()

        def get_reservation_details(*args, **kwargs):
            return master_sandbox_api_result if args[0] == master_sandbox_id else Mock()

        master_sandbox = Mock()
        master_sandbox_api_result = Mock(ReservationDescription=master_sandbox)

        self.sandbox.automation_api.GetResourceDetails.side_effect = get_resource_details
        self.sandbox.automation_api.GetReservationDetails.side_effect = get_reservation_details
        self.sandbox.automation_api.GetResourceAvailability.side_effect = get_resource_availability

        master_sandbox_id = Mock()
        vm_pool_reservation = Mock(ReservationId=master_sandbox_id)
        vm_pool_resource_availability = Mock(Reservations=[vm_pool_reservation])
        resource_availability_api_result = Mock(Resources=[vm_pool_resource_availability])

        pool_name = "pool1"
        vm_pool_resource = Mock(Name=pool_name)

        root_resource_name = "a"
        root_resource = Mock(Name=root_resource_name, ResourceAttributes=[])
        vm_pool_name_att = Mock(Name=f"{root_resource.ResourceModelName}.VM Pool Name", Value=pool_name)
        root_resource.ResourceAttributes.append(vm_pool_name_att)

        sub_resource_name = "b"
        sub_resource = Mock(Name=f"{root_resource_name}/{sub_resource_name}")
        resource2 = Mock(Name="")

        self.sandbox.components.resources = {resource2.Name: resource2, sub_resource.Name: sub_resource}

        #endregion

        # act
        result = get_master_sandbox(self.sandbox)

        # assert
        self.assertEqual(result, [master_sandbox])
