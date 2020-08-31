fprintf('Waiting for model to open \n');
open_system('Model3D_PY') %Opens the simulink/simulation model
fprintf('Model opened \n');

%set_param('Model3D_PY', 'SimulationCommand', 'start'); %error

s = tcpip('localhost', 54320,  'NetworkRole', 'server'); %estabilishes the connection
set(s,'Timeout',200);
fprintf('connection opened \n');

fopen(s); %opens the connection
fprintf('connection estabilished \n');

number = 0;

while not(number == 5) %loop to receive the inputs from python, while 5 is not send
    %try
    number = str2double(fgetl(  s)); %matlab receives the connection data
    hws = get_param(bdroot, 'modelworkspace');
    hws.assignin('number1', number);
    disp(number);
    set_param('Model3D_PY', 'SimulationCommand', 'update'); %updates the model
   
end

fprintf('connection closed \n'); %if you send 5 in the python script, close the connection
set_param('Model3D_PY', 'SimulationCommand', 'stop'); %stops simulation;
delete(s);

%fclose(s);