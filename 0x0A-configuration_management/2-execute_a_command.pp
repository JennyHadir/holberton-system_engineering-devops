#Create a manifet that kills a process named killmenow
exec { 'killmenow':
    path    => '/usr/bin',
    command => 'pkill',
}
