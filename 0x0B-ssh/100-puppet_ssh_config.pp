# using Puppet to make changes to our configuration file
$content = '
  Include /etc/ssh/ssh_config.d/*.conf
  Host *
  	IdentityFile ~/.ssh/school
  	PasswordAuthentication no
'
file { 'Change-file':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => $content,
}
