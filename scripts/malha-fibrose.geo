Mesh.CharacteristicLengthMin = 1;
Mesh.CharacteristicLengthMax = 3;
// Mesh.SmoothNormals = 1; // Melhora a suavidade das normais
// Mesh.AngleTolerance = 0.000239703; // Reduz a tolerância do ângulo diédrico


// Merge "RVepi.stl";
// Merge "RVendo.stl";
// Merge "LVendo.stl";
// Merge "base.stl";


Coherence Mesh;

RefineMesh;

CreateTopology;


CreateGeometry;

// Merge "/home/daniel/3D-heart-models/tempFiles/teste/fibrose.stl";


// Surface Loop(1) = {1, 2, 3, 4, 5};
// Surface Loop(1) = {1, 2, 3, 4};
Surface Loop(1) = {1, 2};
// Surface Loop(1) = {1};

// Physical Surface("septo", 50) = {5};
// Physical Surface("base", 10) = {4};
Physical Surface("rv", 40) = {1};
Physical Surface("septo", 30) = {2};
// Physical Surface("vd", 20) = {3};


// Volume(1) = {1};

// Surface Loop(2) = {5};

// Volume(2) = {2};

// Physical Volume("healthy", 1) = {1};

// Physical Volume("fibrose", 2) = {2};
