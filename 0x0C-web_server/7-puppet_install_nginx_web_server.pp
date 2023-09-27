# using Puppet, install nginx server

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file_line { 'redirect':
  ensure  => present,
  require => Package['nginx'],
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => "	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;",
  before  => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
  before  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
