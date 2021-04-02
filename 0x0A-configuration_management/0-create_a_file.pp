#Create a file in /tmp with permissions 0744
file { '/tmp/holberton':
    ensure  => file,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
