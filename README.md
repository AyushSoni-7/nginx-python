# nginx-python
This is a repo where some nginx template has been used to configure.

# Directory structure
- docker-compose.yaml - This file runs 4 server in docker container and nginx server which is going to serve as a load balancer to route the traffic server.
- flask_app - This contain flask main application along with the Dockerfile. 
	- views - Views directory contains routes for the application. This application contains following routes:
		- / 
		- /blue
		- /green
	All these routes are get request. Return metadata contains information about host, hostname, client ip, server ip, etc.
- nginx_proxy - This directory contains load balancer configuration and dockerfile to build the templated load balancer for nginx. 
	- conf-template - This folder configuration file for different load balancing(lb) type like round robin, ip hash, routing base lb and layer 4 lb(tcp). 


# How to use 
- Docker compose is used to set up the containers. To run the application run following commands:
	- `docker-compose build`
	- `docker-compose up -d`
	This will spin up the all five containers. 
- For testing the nginx lb. You can run following commands:
	- `for x in {1..20}; do; curl localhost:8888; sleep(5); done`
	You will see each request going to different **server_ip** in case of round robin.
- To test different lb configuration. Change the value of argument(nginx_conf_filepath) for dockerfile in docker-compose.yaml at line no 28. You have four option located in nginx_proxy/conf_template
- To destroy the containers once tested use:
	- `docker-compose down`

# Load Balacing Configuration

### lb_round_robin.conf
This configuration perform Layer 7 load balacing. It will do a robin robin to each request i.e. foward each request in circular manner to each server.

### lb_ip_hash.conf
This also perform application layer(L7) load balacing. It will a hash value based on the ip of the client. This enable stickness i.e. single hash will go to same server.

### lb_routing.conf
This is also Layer 7 load balacing. It will forward the request based on routing set on configuration. There are two routes set /blue and / will send the route to server1 and server2 and /green will forward the traffic to server3 and server4 in round robin manner. 
To test this you can use the following command:
- `for x in {1..20}; do; curl localhost:8888/blue; sleep(5); done`
- `for x in {1..20}; do; curl localhost:8888/green; sleep(5); done`
You can see the result in server_ip

### lb_tcp.conf

This is layer 4 load balacing. You can not configure any application based routing pattern in this configuration as load balacing is taking place at layer 4(tcp) layer. In these configuration nginx create some iptables rules which proxy the request to different server. Allocation of server is random in this load balacing.

 
- 
