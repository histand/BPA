clear all

x=load('outfile.txt'); % load column array from data

t=linspace(1,18000,18000);  % create a vector of 3600 1/60th second segments

t = t / 18000 * 5;

plot(t,x)   % plot magnitude vs time