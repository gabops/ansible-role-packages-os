gabops.packages_os
==================
[![Build Status](https://travis-ci.org/gabops/ansible-role-packages-os.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-packages-os)

Installs system packages on multiple GNU/Linux distributions.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| packages_os | {} | Defines packages to be installed/uninstalled. The packages are defined by grouping them by the key `all` or for a key following the format `distro`_`version`. See `Notes` below and `Example playbook`. |
| packages_os_yum_enablerepo | "" | Performs a `--enablerepo` operation when installing packages from `yum` |
| packages_os_yum_disablerepo | "" | Performs a `--disablerepo` operation when installing packages from `yum` |
| packages_os_apt_default_release | "" | Performs a `--target-release` operation when installing packages from `apt` |
| packages_os_apt_update_cache | true | Performs a `update cache` operation when installing packages form `apt` |

#### Notes:
Inside packages_os, the packages grouped on `distro_version` have predecende over the packages grouped in `all`. Therefore, if for example you declare:
```yaml
  packages_os:
    all:
      vim: present
    centos_7:
      vim: absent
```
the vim package will not be installed on any **centos_7** host of the group you have declared this variable in.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    packages_os:
      all:
        tcpdump: present
        vim: present
      centos_6:
        iptables: present
        curl: present
      centos_7:
        httpd: present
        zip: present
        tcpdump: absent
        traceroute: present
        python-devel: present
      amazon_1:
        telnet: present
      amazon_2:
        zsh: present
      ubuntu_18.04:
        apt-file: present
  roles:
    - role: gabops.packages_os
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
