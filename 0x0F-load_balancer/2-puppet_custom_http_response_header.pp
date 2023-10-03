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

file_line { 'custom_header':
  ensure  => present,
  require => Package['nginx'],
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => "  add_header X-Served-By $HOSTNAME;",
  before  => Service['nginx'],
}

file_line { 'custom_header':
  ensure  => present,
  require => Package['nginx'],
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => "  error_page 404 /custom_404.html;\nlocation = /custom_404.html {\n\troot /usr/share/nginx/html;\n\tinternal;\n}",
  before  => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
  before  => Service['nginx'],
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
  before  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
