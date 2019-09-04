   

   #Create a simulator object
   set ns [new Simulator]

   $ns color 2 red
 
   #Tell the simulator to use static routing
   $ns rtproto Static


   #set up trace files
   set traceFile [open 1.tr w]
   $ns trace-all $traceFile


   set namFile [open out1.nam w]
   $ns namtrace-all $namFile
   
   
   proc finish {} {
  
           global ns namFile traceFile 
       
      $ns flush-trace
  
       #Close the trace files
    close $traceFile
    close $namFile
        exec nam out1.nam 
	exec awk -f stats.awk 1.tr &
	exit 0

}



   #set up 3 nodes
   set n(1) [$ns node]
   set n(2) [$ns node]
   set n(3) [$ns node]
   
   
   #set up duplex links
   $ns duplex-link $n(1) $n(2) 0.5Mb 20ms DropTail
   $ns duplex-link $n(2) $n(3) 0.5Mb 20ms DropTail
   $ns queue-limit $n(1) $n(2) 10
   $ns queue-limit $n(2) $n(3) 10



   #aesthetics
   #source (udp)
   $n(1) shape hexagon
   $n(1) color red

 
   #destination (udp)
   $n(3) shape square
   $n(3) color blue

  
   #Create a udp agent and attach it node n1
   set udp0 [new Agent/UDP]
   $ns attach-agent $n(1) $udp0

   
   #Create a CBR source and attach it to usp0
    set cbr0 [new Application/Traffic/CBR]
    $cbr0 set packetSize_ 512
    $cbr0 set interval 0.005
    $cbr0 attach-agent $udp0

 
   #Create a null agent (a traffic sink) and attach it to n(3)
   set null0 [new Agent/Null]
   $ns attach-agent $n(3) $null0


   #Connect the traffic source with traffic sink and assign flowid color
   $ns connect $udp0 $null0
   $udp0 set fid_ 2


   #sim events
   $ns at 0.5 "$cbr0 start"
   $ns at 2.0 "$cbr0 stop"
   $ns at 2.0 "finish"
    
    $ns run





   






