gabops.packages_os
==================
[![Build Status](https://travis-ci.org/gabops/ansible-role-packages-os.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-packages-os)

Installs system packages on multiple GNU/Linux distributions

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| packages_os | {} | Defines packages to be installed/uninstalled. This variable can be used alone or in conjuction with any of the variables `package_os_common`,`packages_os_group` or `packages_host`. See `Example Playbook` below. |
| packages_os_common | {} | Defines packages to be installed/uninstalled. Tipically you will define this variable in the default metagroup `all` (group_vars/all/) |
| packages_os_group | {} | Defines packages to be installed/uninstalled. Tipically you will define this variable in any of the groups your inventory has like for example `webservers` (group_vars/webservers/). The group obviously depends of the configuration of your inventory. |
| packages_os_host | {} | Defines packages for an `specific host`. Tipically you will define this in a host_vars file(host_vars/host-01/). |
| packages_os_yum_enablerepo | "" | Performs a `--enablerepo` operation when installing packages from `yum` |
| packages_os_yum_disablerepo | "" | Performs a `--disablerepo` operation when installing packages from `yum` |
| packages_os_apt_default_release | "" | Performs a `--target-release` operation when installing packages from `apt` |
| packages_os_apt_update_cache | true | Performs a `update cache` operation when installing packages form `apt` |

Dependencies
------------

None.

Example Playbook
----------------

- group_vars/all/packages.yml:
```yaml
packages_os_common:
  all:
    tcpdump: present
  centos_6:
    iptables: present
    curl: present
  centos_7:
    httpd: present
    zip: present
    tcpdump: absent
  amazon_1:
    telnet: present
  amazon_2:
    zsh: present
  ubuntu_18.04:
    apt-file: present
```
- group_vars/group_foo/packages.yml:

```yaml
packages_os_group:
  centos_7:
    traceroute: present
```
- host_vars/host_bar/packages.yml:
```yaml
packages_os_host:
  vim: present
```
- playbook:
```yaml
    - hosts: all
      vars:
        packages_os:
          centos_7:
            python-devel: present
      roles:
        - role: gabops.packages_os
```
- As you can see, the grouping of packages in the `packages_os`, `packages_os_common` and `packages_os_group` variables follows the format `DISTO_VERSION` or just `all` for matching all distributions. Bare in mind that if you define a package in `all` and you are targeting different Linux distro families, the role probably will fail as the package names can change between different distros.

- The dictionary `packages_os_host` is the only one that does not follow the format `DISTO_VERSION`. As the intention of this variable is to apply packages to an specific host, does not make sense to group by distros nor all. 

- The hierarchy of the variables, from lighter to heavier is:
  - packages_os_common
  - packages_os_group
  - packages_os_host
  - packages_os

  This means that a package defined in package_os will overwrite any definition in any of the other variables. As the idea of
  package_os is to be defined normally in a playbook, makes sense to give more priority to it.

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
