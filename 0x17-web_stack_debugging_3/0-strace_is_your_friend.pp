# using Puppet, fix the apache2 error 500

exec { 'apache2_error_fix':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
