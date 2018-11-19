import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kotlin_is_installed(host):
    f = host.file('/usr/local/bin/kotlin')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kotlinc_is_installed(host):
    f = host.file('/usr/local/bin/kotlinc')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kotlinc_js_is_installed(host):
    f = host.file('/usr/local/bin/kotlinc-js')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kotlinc_jvm_is_installed(host):
    f = host.file('/usr/local/bin/kotlinc-jvm')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kotlin_compiler_is_installed(host):
    f = host.file('/usr/local/bin/kotlin-compiler')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kotlin_dce_js_is_installed(host):
    f = host.file('/usr/local/bin/kotlin-dce-js')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
