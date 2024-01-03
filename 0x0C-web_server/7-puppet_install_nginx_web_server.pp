# It installs Nginx package
package { 'nginx':
  ensure => installed,
}

# It creates simple HTML page with Hello World!
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# It configure Nginx to listen on port 80 and use created HTML page
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    server_name localhost;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}",
  notify  => Service['nginx'],
}

# It ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
}
