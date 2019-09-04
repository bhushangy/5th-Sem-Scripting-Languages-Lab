BEGIN {

 lostpackets = 0;
 }

{

  event=$1;
  packetType=$5;


  if(packetType=="cbr")
    {
         if(event=="-")
          {
              lostpacket++;
           }
     }
}

END{
     printf("total packets lost are %d\n",lostpackets);
   }    
 
