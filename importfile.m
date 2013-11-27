DELIMITER = ',';
HEADERLINES = 2;

% Import the file
newData1 = importdata('/Users/histand/Desktop/CSV/BPAe_1305132321.csv',DELIMITER, HEADERLINES);

% Create new variables in the base workspace from those fields.
vars = fieldnames(newData1);
for i = 1:length(vars)
    assignin('base', vars{i}, newData1.(vars{i}));
end


