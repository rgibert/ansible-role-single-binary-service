# Single Binary Service

![Ansible Role](https://img.shields.io/ansible/role/ANSIBLE_GALAXY_ID?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-single-binary-service?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/ANSIBLE_GALAXY_ID?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/ANSIBLE_GALAXY_ID?label=downloads&style=flat-square)

## Description

Ansible role to install a single binary as a systemd service

## Requirements

- none

## Role Variables

| Variable | Description |
|----------|-------------|
| single_binary_service_checksum | Checksum of the download file |
| single_binary_service_dl_url | Download target |
| single_binary_service_group | Primary group of the single_binary_service_user |
| single_binary_service_is_archive | Whether the download artifact is an archive to be unpacked |
| single_binary_service_name | Service name |
| single_binary_service_share_path | Shared path to install to |
| single_binary_service_start_cmd | Command to start the service |
| single_binary_service_stop_cmd | Command to stop the service |
| single_binary_service_user | User to run the service as |

## Dependencies

- none

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: rgibert.single_binary_service
      single_binary_service_is_archive: true
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
