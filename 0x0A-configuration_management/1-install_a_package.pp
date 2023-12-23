package { 'werkzeug':
  ensure   => 'x.x.x',  # Specify the version you need
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
