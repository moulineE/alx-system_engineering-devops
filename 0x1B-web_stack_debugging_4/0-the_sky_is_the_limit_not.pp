# using Pupphuge amount of failed requests

exec { 'fixing-nginx':
  command  => 'sed -i "s/15/9999/" /etc/default/nginx',
  provider => shell,
}

exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fixing-nginx']
}
