FROM        centos7-base
RUN         yum install -y memcached
EXPOSE      11211
CMD         ['/usr/bin/memcached','-u','memcached','-p','11211','-m','64','-c','1024'] 
