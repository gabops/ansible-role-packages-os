import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    distro = host.system_info.distribution
    version = host.system_info.release

    if distro == "centos" and version.startswith("6"):
        pkg = host.package("iptables")
        assert pkg.is_installed

    elif distro == "centos" and version.startswith("7"):
        pkg = host.package("tmux")
        assert pkg.is_installed

    elif distro == "amazon" and version.startswith("1"):
        pkg = host.package("telnet")
        assert pkg.is_installed

    elif distro == "amazon" and version.startswith("2"):
        pkg = host.package("zsh")
        assert pkg.is_installed

    elif distro == "ubuntu" and version.startswith("18"):
        pkg = host.package("apt-file")
        assert pkg.is_installed

    pkg = host.package("wget")
    assert pkg.is_installed
