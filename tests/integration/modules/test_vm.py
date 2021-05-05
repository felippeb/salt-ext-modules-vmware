# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import saltext.vmware.modules.vm as vm
import pytest


@pytest.mark.parametrize(
    'arg_name', [
        "cluster",
        "esxi_hostname",
        "guest_name",
        "guest_fullname",
        "ip_address",
        "power_state",
        "uuid"
    ]
)
def test_vm_get_basic_facts(service_instance, integration_test_config, arg_name):
    vm_facts = vm.get_vm_facts(service_instance=service_instance)
    for host_id in vm_facts:
        for vm_name in vm_facts[host_id]:
            expected_value = integration_test_config["vm_facts"][host_id][vm_name][arg_name]
            assert vm_facts[host_id][vm_name][arg_name] == expected_value