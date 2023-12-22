# It makes manifest that kills process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
