clear all

x=load('outfile.txt'); % load column array from data

t=linspace(1,10800,10800);  % create a vector of 3600 1/60th second segments

t = t / 10800 * 3;

plot(t,x)   % plot magnitude vs time