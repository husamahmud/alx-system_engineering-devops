file { 'Change-file':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => $cont,
}
