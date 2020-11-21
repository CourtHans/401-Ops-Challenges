-- HEAD --

description = [[
This is a very basic script to determine the timeout information of the target.
Contains RTTVAR(round trip time variation), SRTT(smoothed round trip time), and timeout.
]]

-- @usage 
-- nmap --script roundtrip.nse <target> -p <port(s)>
--
-- @output
-- PORT     STATE SERVICE
-- 21/tcp   open  ftp
-- | roundtrip: 
-- |   timeout: 0.1
-- |   rttvar: 0.001694
-- |_  srtt: 0.000711
-- 22/tcp   open  ssh
-- | roundtrip: 
-- |   timeout: 0.1
-- |   rttvar: 0.001694
-- |_  srtt: 0.000711
-- 80/tcp   open  http
-- | roundtrip: 
-- |   timeout: 0.1
-- |   rttvar: 0.001694
-- |_  srtt: 0.000711
-- 443/tcp  open  https
-- | roundtrip: 
-- |   timeout: 0.1
-- |   rttvar: 0.001694
-- |_  srtt: 0.000711
-- 3306/tcp open  mysql
-- | roundtrip: 
-- |   timeout: 0.1
-- |   rttvar: 0.001694
-- |_  srtt: 0.000711
-- MAC Address: {target MAC Address}


author = "Courtney Hans"

-- RULE --
portrule = function(host,port)
	return port.protocol == "tcp"
		and port.state == "open"
end

-- ACTION --

action = function(host,port)
	return host.times
end
