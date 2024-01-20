# using Puppet to make changes to our configuration file
$content = 'Include /etc/ssh/ssh_config.d/*.conf'
file { 'Change-file':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => $content,
}
