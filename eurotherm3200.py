#!/usr/bin/env python
#
#   Copyright 2012 Jonas Berg
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

"""

.. moduleauthor:: Jonas Berg <pyhys@users.sourceforge.net>

Driver for the Eurotherm3500 process controller, for communication via the Modbus RTU protocol.

"""

import minimalmodbus

__license__ = "Apache License, Version 2.0"


class Eurotherm3216(minimalmodbus.Instrument):
    """Instrument class for Eurotherm 3216 temperature controller. 
    
    Communicates via Modbus RTU protocol (via RS232 or RS485), using the *MinimalModbus* Python module.    

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    Implemented with these function codes (in decimal):
        
    ==================  ====================
    Description         Modbus function code
    ==================  ====================
    Read registers      3
    Write registers     16
    ==================  ====================

    """
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
    
    ## Process value
    
    def get_pv(self):
        return self.read_register(1,1)

    def get_working_setpoint(self):
        return self.read_register(5,1)
    
    def get_setpoint1(self, value):
        return self.read_register(24,1)
        
    def set_setpoint1(self, value):
        self.write_register(24,value,numberOfDecimals=1)

    def set_setpoint2(self, value):
        self.write_register(25,value,numberOfDecimals=1)

    def set_remote_setpoint(self,value):
        self.write_register(26,value)
    
########################
## Testing the module ##
########################

if __name__ == '__main__':

    minimalmodbus._print_out( 'TESTING EUROTHERM 3500 MODBUS MODULE')

    a = Eurotherm3216('COM5', 2)
    a.debug = False
    
    minimalmodbus._print_out( 'SP1:                    {0}'.format(  a.get_sp_loop1()             ))
    minimalmodbus._print_out( 'SP1 target:             {0}'.format(  a.get_sptarget_loop1()       ))
    minimalmodbus._print_out( 'SP2:                    {0}'.format(  a.get_sp_loop2()             ))
    minimalmodbus._print_out( 'SP-rate Loop1 disabled: {0}'.format(  a.is_sprate_disabled_loop1() ))
    minimalmodbus._print_out( 'SP1 rate:               {0}'.format(  a.get_sprate_loop1()         ))
    minimalmodbus._print_out( 'OP1:                    {0}%'.format( a.get_op_loop1()             ))
    minimalmodbus._print_out( 'OP2:                    {0}%'.format( a.get_op_loop2()             ))
    minimalmodbus._print_out( 'Alarm1 threshold:       {0}'.format(  a.get_threshold_alarm1()     ))
    minimalmodbus._print_out( 'Alarm summary:          {0}'.format(  a.is_set_alarmsummary()      ))
    minimalmodbus._print_out( 'Manual mode Loop1:      {0}'.format(  a.is_manual_loop1()          ))
    minimalmodbus._print_out( 'Inhibit Loop1:          {0}'.format(  a.is_inhibited_loop1()       ))
    minimalmodbus._print_out( 'PV1:                    {0}'.format(  a.get_pv_loop1()             ))
    minimalmodbus._print_out( 'PV2:                    {0}'.format(  a.get_pv_loop2()             ))
    minimalmodbus._print_out( 'PV module 3:            {0}'.format(  a.get_pv_module3()           ))
    minimalmodbus._print_out( 'PV module 4:            {0}'.format(  a.get_pv_module4()           ))
    minimalmodbus._print_out( 'PV module 6:            {0}'.format(  a.get_pv_module6()           ))

    #a.set_sprate_loop1(30)
    #a.enable_sprate_loop1() 

    minimalmodbus._print_out( 'DONE!' )

pass    
