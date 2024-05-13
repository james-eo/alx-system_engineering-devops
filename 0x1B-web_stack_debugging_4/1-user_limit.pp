# A Puppet manifest to set user login to a sizable limit
exec { 'set_value_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'set_value_to_40':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}
