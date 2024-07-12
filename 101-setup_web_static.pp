# 101-setup_web_static.pp
#
# This manifest sets up web servers for the deployment of web_static.
# It performs the following actions:
# - Installs Nginx if it is not already installed
# - Creates the required directories
# - Creates a fake HTML file for testing
# - Sets up the necessary symbolic links
# - Configures Nginx to serve content from the new directories

node default {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the service is running and enabled
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  # Create directories if they don't exist
  file { '/data/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/shared/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/test/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  # Create a fake HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
    content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  }

  # Create symbolic link
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    force  => true,
  }

  # Give ownership of the /data/ folder to the ubuntu user and group
  exec { 'chown -R ubuntu:ubuntu /data/':
    path    => '/usr/bin:/usr/sbin:/bin:/sbin',
    require => File['/data/'],
  }

  # Update Nginx configuration to serve the content
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Restart Nginx to apply the changes
  service { 'nginx-restart':
    ensure    => running,
    enable    => true,
    require   => File['/etc/nginx/sites-available/default'],
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}
