import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    pkg_rsyslog = host.package("rsyslog")

    assert pkg_rsyslog.is_installed