Mesh.CharacteristicLengthMin = 1;
Mesh.CharacteristicLengthMax = 3;

Merge "Patient_1-RVEpi-Frame_1.vtk";
Merge "Patient_1-RVEndo-Frame_1.vtk";
Merge "Patient_1-LVEndo-Frame_1.vtk";
Merge "base.stl";


Coherence Mesh;

RefineMesh;

// CreateTopology;


// CreateGeometry;

Merge "Patient_1_scar.vtk";


Surface Loop(1) = {1, 2, 3, 4, 5};

Physical Surface("base", 10) = {4};
Physical Surface("epi", 40) = {1};
Physical Surface("ve", 20) = {3};
Physical Surface("vd", 30) = {2};

Volume(1) = {1};

Surface Loop(2) = {5};

Volume(2) = {2};

Physical Volume("healthy", 1) = {1};

Physical Volume("fibrose", 2) = {2};
