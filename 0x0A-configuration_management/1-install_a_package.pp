# sing Puppet, install flask from pip3.

exec { 'apt-get update':
    command => '/usr/bin/apt-get update'
}

package { 'flask':
    ensure   => '2.1.0'
    require  => Exec['apt-get update']
    provider => 'pip3'
}
