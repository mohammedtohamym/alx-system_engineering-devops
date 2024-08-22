# puppet file to increase number of open files for a user

file { '/etc/security/limits.conf':
  ensure => present,
  content => [
    'holberton hard nofile 60000',
    'holberton soft nofile 20000',
  ],
  mode   => '0644',
}