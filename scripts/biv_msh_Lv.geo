Mesh.CharacteristicLengthMax = 3 * 0.75;  // Aproximadamente 2.61
Mesh.CharacteristicLengthMin = 1 * 0.75;  // Aproximadamente 0.87



Coherence Mesh;

// RefineMesh;

CreateTopology;


// CreateGeometry; // Tá dando erro de syntax. pq? não sei, não achei documentação

Merge "/home/daniel/3D-heart-models/tempFiles/teste/outputs/Patient_scar.stl";
// Merge "/home/daniel/3D-heart-models/tempFiles/stlFiles/resultado_booleano.stl";
// Merge "/home/daniel/3D-heart-models/tempFiles/stlFiles/Patient_1_scar_processed_processed.stl";
// Merge "/home/daniel/3D-heart-models/tempFiles/stlFiles/scar_processed.stl"

Delete Physicals;

Surface Loop(1) = {5, 6, 8, 9};
// Surface Loop(1) = {5, 6, 8};

Physical Surface("base", 10) = {8};
Physical Surface("epi", 40) = {6};
Physical Surface("ve", 30) = {5};
// Physical Surface("vd", 30) = {8};

Volume(1) = {1};

Surface Loop(2) = {9};

Volume(2) = {2};

Physical Volume("healthy", 1) = {1};

Physical Volume("fibrose", 2) = {2};
Coherence;
