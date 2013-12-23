clear all

x=load('outfile.txt'); % load column array from data

t=linspace(1,3600,3600);  % create a vector of 3600 1/60th second segments

t = t / 3600;

plot(t,x)   % plot magnitude vs time