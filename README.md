gabops.packages_os
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-gabops.packages.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-packages-os)

Installs system packages on multiple GNU/Linux distributions

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| packages_os_common | {} | Defines packages for all hosts grouped in "all" or distribution_version (see playbook example). Usually you would put this in the `all` default metagroup inside of group_vars |
| packages_os_group | {} | Defines packages for all hosts grouped in "all" or distribution_version (see playbook example). Usually you would put this in any more specific group or metagroup of hosts other than `all` inside of group_vars |
| packages_os_host | {} | Defines packages for an `specific host`. Usually you put this in a host_vars file |
| packages_os_yum_enablerepo | "" | Performs a `--enablerepo` operation when installing packages from `yum` |
| packages_os_yum_disablerepo | "" | Performs a `--disablerepo` operation when installing packages from `yum` |
| packages_os_apt_default_release | "" | Performs a `--target-release` operation when installing packages from `apt` |
| packages_os_apt_update_cache | true | Performs a `update cache` operation when installing packages form `apt` |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: all
      vars:
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
        packages_os_group:
          centos_7:
            traceroute: present
        packages_os_host:
          vim: present
      roles:
         - role: gabops.packages
```

The structure of the dictionary `packages_os_common` and `packages_os_group` is the same. You can have an `all` group which will apply packages to all the hosts the playbook runs over and you can have defined packages specifically for the distribution of the hosts you are provisioning using the format `DISTRO_VERSION`. The `all` or `DISTRO_VERSION` groups can be defined in lower case or upper case or whatever you prefer, so `ALL` will work the same as `all` and also `DeBiAn_10` (:astonished:) will work in the same way as `Debian_10`.


License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
