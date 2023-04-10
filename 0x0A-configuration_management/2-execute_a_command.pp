exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin', # Specify the PATH environment variable to ensure pkill is found
  onlyif  => 'pgrep killmenow', # Check if the process "killmenow" is currently running
  refreshonly => true, # Only execute when refreshed, not on every run
}
