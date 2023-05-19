# Modify the upper limit and restart Nginx
exec { 'increase upper limit':
  provider => shell,
  command  => 'sed -i s/15/1000000/ /etc/default/nginx'
}

exec { 'restart Nginx server':
  provider => shell,
  command  => 'service nginx restart'
}
