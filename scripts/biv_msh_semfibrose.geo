Mesh.CharacteristicLengthMax = 3;
Mesh.CharacteristicLengthMin = 1;


Coherence Mesh;

// RefineMesh;

CreateTopology;


// CreateGeometry; // Tá dando erro de syntax. pq? não sei, não achei documentação


Delete Physicals;

// Surface Loop(1) = {7, 8, 9, 11, 12};
Surface Loop(1) = {7, 8, 9, 11};

Physical Surface("base", 10) = {11};
Physical Surface("epi", 40) = {9};
Physical Surface("ve", 30) = {7};
Physical Surface("vd", 20) = {8};

Volume(1) = {1};

// Surface Loop(2) = {12};

// Volume(2) = {2};

Physical Volume("healthy", 1) = {1};

// Physical Volume("fibrose", 2) = {2};
Coherence;
