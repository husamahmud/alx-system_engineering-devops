# using Puppet to make changes to our configuration file
file { 'Change-file':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => $cont,
}
