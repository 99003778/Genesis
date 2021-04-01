%Team memebrs: Pushkar Antony, Shiva Kumar, Sai Kalki, Subba Reddy and
%Jyothi 
%Introduction: We have built a automated script which can take user keyword
%and search for it and produce the countand list of occurances of the same
%in a excell sheet and export it.
user_input ='WiperControl_Automation';
test_str='Wiper_Output';
open_system(user_input);
%open_system(user_input/WiperControl_Automation,window);
sys_t = find_system(user_input);
new_t = regexprep(sys_t,'WiperControl_Automation/','','ignorecase');
count=0;
final_str=[];
for i=1:length(new_t)
    if contains(new_t(i),test_str,'IgnoreCase',true)
        count = count+1;
        final_str=[new_t(i),final_str]; 
    end
end
final_transposed = transpose(final_str);
count_str = "The count of the keyword--> "+ test_str +" is: " + count;
xlswrite("Out.xlsx",cellstr(count_str));
xlswrite("Out.xlsx",cellstr(final_transposed),'Names');