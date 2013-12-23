clear all

x=load('outfile.txt'); % load column array from data

t=linspace(1,10800,10800);  % create a vector of 3600 1/60th second segments

t = t / 10800 * 3;

MAX= mean(x);    % store mean of array

x_pu = x / MAX;    % store p.u. of array

plot(t,x_pu)   % plot magnitude vs time