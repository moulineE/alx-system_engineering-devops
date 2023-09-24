# Using Puppet set up your client SSH configuration file that you can connect to a server without typing a password with private key ~/.ssh/school
file_line { 'refuse to auth using a passwd':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "    PasswordAuthentication no",
}

file_line { 'use the private key ~/.ssh/school':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "    IdentityFile ~/.ssh/school",
}
