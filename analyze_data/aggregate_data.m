ants = zeros(30,20);
nests = zeros(30,20);
steps = zeros(30,20);

for i = 1:30
   file = strcat('results/ants',int2str(i-1),'.mat');
   load(file);
   for j = 1:20
       trial = data(j);
       ants(i,j) = trial{1}.ants;
       nests(i,j) = trial{1}.nests;
       steps(i,j) = trial{1}.steps;
   end
end