# This file installs 'flask' from pip3

#package { 'flask':
#  ensure   => '2.1.0',
#  provider => 'pip3',
#}

package {'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  creates => '/usr/local/lib/python3.8/dist-packages/flask',
}
