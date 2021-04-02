#Create a manifet that kills a process named killmenow
exec { 'pkill':
    command => 'pkill killmenow',
    path    => '/usr/bin',
}
