import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    pkg_1 = host.package("iotop")
    pkg_2 = host.package("unzip")

    assert pkg_1.is_installed
    assert pkg_2.is_installed
