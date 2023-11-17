#Change the OS configuration so that it is possible to login with the holberton user

exec { 'change hard limit':
  command  => 'sed -i "/holberton hard/s/5/4000/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'change soft limit':
  command  => 'sed -i "/holberton soft/s/4/4000/" /etc/security/limits.conf',
  provider => shell,
}
