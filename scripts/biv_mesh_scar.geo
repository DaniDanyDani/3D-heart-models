Mesh.CharacteristicLengthMax = 3;
Mesh.CharacteristicLengthMin = 1;

// Geometry.HideCompounds = 0;
// CharacteristicLengthFromCurvature = 1;
// Lloyd = 1;
// Mesh.Algorithm    = 6; // (1=MeshAdapt, 2=Automatic, 5=Delaunay, 6=Frontal, 7=bamg, 8=delquad) (Default=2)
// Mesh.RecombineAll = 0;

// Mesh.RemeshAlgorithm = 1; // (0=no split, 1=automatic, 2=automatic only with metis) (Default=0)
// Mesh.SurfaceFaces = 1;

Surface Loop(2)={1, 2};

Volume(3)={2};

Physical Volume("healthy", 2) = {3};
