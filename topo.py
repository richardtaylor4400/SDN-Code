"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
#        leftHost = self.addHost( 'h1' )
 #       rightHost = self.addHost( 'h2' )
  #      leftSwitch = self.addSwitch( 's3' )
   #     rightSwitch = self.addSwitch( 's4' )

        # Add links
    #    self.addLink( leftHost, leftSwitch )
     #   self.addLink( leftSwitch, rightSwitch )
      #  self.addLink( rightSwitch, rightHost )


	topsw = self.addSwitch( 's1' )
	botsw = self.addSwitch( 's2' )
	botsw1 = self.addSwitch( 's3' )

	host1 = self.addHost( 'PC1' )
	host2 = self.addHost( 'PC2' )
	host3 = self.addHost( 'PC3' )
	
	self.addLink( topsw,botsw )
	self.addLink( botsw,botsw1 )
#	self.addLink( botsw1,topsw )

	self.addLink( host1,topsw )
	self.addLink( host2,botsw )
	self.addLink( host3,botsw1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
