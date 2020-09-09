s = tcpip('localhost', 54320,  'NetworkRole', 'server'); %estabilishes the connection
set(s,'Timeout',200);
fprintf('connection opened \n');
number = 0;
set_param('Model3D_PY', 'SimulationCommand', 'start');

while not(number == 5)
    
end