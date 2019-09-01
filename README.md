gabops.packages
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-gabops.packages.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-gabops.packages)

Installs packages on different Linux family distributions

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| | | |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: all
      vars:
        packages:
          All:
            top: present
            nmap: present
          Centos_6:
            tmux: present
          Centos_7:
            vim: present
          Amazon_1:
           tcpdump: present 
      roles:
         - role: gabops.packages
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
