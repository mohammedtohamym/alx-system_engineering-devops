# puppet file to fix nginx server

file { '/etc/default/nginx':
  ensure => present,
  content => "ULIMIT='-n 4096'",
  mode   => '0644',
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  subscribe  => [ File['/etc/default/nginx'] ],
}