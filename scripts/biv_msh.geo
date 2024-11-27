Mesh.CharacteristicLengthMin = 1;
Mesh.CharacteristicLengthMax = 3;


Coherence Mesh;

// RefineMesh;

CreateTopology;


// CreateGeometry; // Tá dando erro de syntax. pq? não sei, não achei documentação

Merge "/home/daniel/3D-heart-models/tempFiles/stlFiles/Patient_scar.stl";

Delete Physicals;

Surface Loop(1) = {7, 8, 9, 11, 12};

Physical Surface("base", 10) = {11};
Physical Surface("epi", 40) = {9};
Physical Surface("ve", 20) = {7};
Physical Surface("vd", 30) = {8};

Volume(1) = {1};

Surface Loop(2) = {12};

Volume(2) = {2};

Physical Volume("healthy", 1) = {1};

Physical Volume("fibrose", 2) = {2};
Coherence;
