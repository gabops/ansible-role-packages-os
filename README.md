gabops.packages_os
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-packages-os.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-packages-os)

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
         - role: gabops.packages_os
```

- The the dictionaries `packages_os_common` and `packages_os_group` supports the same format.

- The group `all` defines packages for all the hosts no matter the distro. Bare in mind that the name of the packages must be the same across the hosts (distros) you are provisioning. 

- Apart from `all` you can define packages for an specific distro by using the format `distro + _ + version` as the above example shows.

- The `all` or `distro_version` keys inside `packages_os_common` and `packages_os_group` must be declared in **lower case**.

- The dictionary `packages_os_host` does not support anything other than just a list of packages. This variable is used for applying packages to an specific host, so, does not make sense to group packages per distro/all.

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
