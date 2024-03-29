# 100-puppet_ssh_config.pp

include stdlib

file_line { 'nopwd':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}
file_line { 'identity':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
