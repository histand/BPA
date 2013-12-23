clear all

x=load('outfile.txt'); % load column array from data

t=linspace(1,3600,3600);  % create a vector of 3600 1/60th second segments

t = t / 3600;

MAX= mean(x);    % store mean of array

x_pu = x / MAX;    % store p.u. of array

plot(t,x_pu)   % plot magnitude vs time