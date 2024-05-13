# Puppet manifest to change ULIMIT -n to accomodate a sizable number of requests

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2096'\n",
}
