#Create a manifet that kills a process named killmenow
exec { 'pkill killmenow':
    path    => '/usr/bin',
}
