# Single Binary Service

![Ansible Role](https://img.shields.io/ansible/role/44520?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-single-binary-service?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/44520?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/44520?label=downloads&style=flat-square)

## Description

Ansible role to install a single binary as a systemd service

## Requirements

- RHEL-based or Debian-based OS

## Role Variables

| Variable | Description |
|----------|-------------|
| single_binary_service_checksum | Checksum of the download file |
| single_binary_service_dl_url | Download target |
| single_binary_service_exec_files | Files (relative to single_binary_service_share_path) to make +x |
| single_binary_service_group | Primary group of the single_binary_service_user |
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
      prometheus_node_exporter_base_url: "https://github.com/prometheus/node_exporter/releases/download"
      prometheus_node_exporter_dl_url: "{{ prometheus_node_exporter_base_url }}/v{{ single_binary_service_version }}/node_exporter-{{ single_binary_service_version }}.linux-{{ prometheus_node_exporter_arch }}.tar.gz"
      single_binary_service_checksum: "sha256:{{ prometheus_node_exporter_base_url }}/v{{ single_binary_service_version }}/sha256sums.txt"
      single_binary_service_dl_url: "{{ prometheus_node_exporter_base_url }}/v{{ single_binary_service_version }}/node_exporter-{{ single_binary_service_version }}.linux-{{ prometheus_node_exporter_arch }}.tar.gz"
      single_binary_service_group: prometheus
      single_binary_service_is_archive: true
      single_binary_service_name: prometheus_node_exporter
      single_binary_service_start_cmd: "/usr/local/share/prometheus_node_exporter-{{ single_binary_service_version }}/node_exporter-{{ single_binary_service_version }}.linux-{{ prometheus_node_exporter_arch }}/node_exporter"
      single_binary_service_stop_cmd: "/usr/bin/ps auwwx | grep /usr/local/share/prometheus_node_exporter-{{ single_binary_service_version }}/node_exporter-{{ single_binary_service_version }}.linux-{{ prometheus_node_exporter_arch }}/node_exporter | grep -v grep | awk '{print $2}' | xargs kill -9"
      single_binary_service_user: prometheus
      single_binary_service_version: 0.18.1
      prometheus_node_exporter_arch: amd64
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
