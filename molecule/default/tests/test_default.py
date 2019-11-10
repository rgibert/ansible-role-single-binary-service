import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def service_enabled(host):
    assert host.service('prometheus_node_exporter').is_enabled


def service_running(host):
    assert host.service('prometheus_node_exporter').is_running
