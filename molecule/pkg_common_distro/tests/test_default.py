import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    os = host.system_info.distribution
    release = host.system_info.release
    print(host.system_info)

    if os == "amzn" and release == "2":
        pkg = host.package("vim-enhanced")
        assert pkg.is_installed
    elif os == "centos" and "7" in release:
        pkg = host.package("tmux")
        assert pkg.is_installed
    elif os == "ubuntu" and "18.04" in release:
        pkg = host.package("apt-file")
        assert pkg.is_installed
