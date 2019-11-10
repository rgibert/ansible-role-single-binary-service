import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def file_installed(host):
    assert host.file('/usr/local/share/prometheus_node_exporter-0.18.1/node_exporter-0.18.1.linux-amd64/node_exporter').is_file
