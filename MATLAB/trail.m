clear all;
clc;
handle = load_system('WiperControl_Automation')
object = find_system('WiperControl_Automation')
%Output = get(object,'output')
%x = get_param(
%Output = object.get('output')
%d1 = Simulink.findBlocksOfType('PowerOutlet_Automation','type','options')