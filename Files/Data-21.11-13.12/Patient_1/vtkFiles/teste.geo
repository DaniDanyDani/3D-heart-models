Merge "Patient_1-LVEndo-Frame_1.vtk";
Merge "Patient_1-RVEndo-Frame_1.vtk";
Merge "Patient_1-RVEpi-Frame_1.vtk";
Merge "Patient_1_scar.vtk";

// os.system('{} -3 {} -merge {} {} {} -o {} 2>&1 {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh, msh, out))
// /home/daniel/Programs/gmsh/build/gmsh -3 /home/daniel/3D-heart-models/Files/Data-21.11-13.12/Patient_1/vtkFiles/teste.geo


Mesh.CharacteristicLengthMax = 3;
Mesh.CharacteristicLengthMin = 1;
//Mesh.CharacteristicLengthFactor = .4;

Geometry.HideCompounds = 0;
CharacteristicLengthFromCurvature = 1;
Lloyd = 1;
Mesh.Algorithm    = 6; // (1=MeshAdapt, 2=Automatic, 5=Delaunay, 6=Frontal, 7=bamg, 8=delquad) (Default=2)
Mesh.RecombineAll = 0;

Mesh.RemeshAlgorithm = 1; // (0=no split, 1=automatic, 2=automatic only with metis) (Default=0)

//Mesh.RemeshParametrization = 7; // (0=harmonic_circle, 1=conformal_spectral, 2=rbf, 3=harmonic_plane, 4=convex_circle, 5=convex_plane, 6=harmonic square, 7=conformal_fe) (Default=4)

//Mesh.Algorithm3D    = 4; // (1=Delaunay, 4=Frontal, 5=Frontal Delaunay, 6=Frontal Hex, 7=MMG3D, 9=R-tree) (Default=1)
//Mesh.Recombine3DAll = 0;

Mesh.Optimize = 1;
Mesh.OptimizeNetgen = 1;

//Mesh.Smoothing = 0;
Mesh.SurfaceFaces = 1;

CreateTopology;
ll[] = Line "*";
L_LV_base = newl; Compound Line(L_LV_base) = ll[2];
L_RV_base = newl; Compound Line(L_RV_base) = ll[0];
L_epi_base = newl; Compound Line(L_epi_base) = ll[1];
Physical Line("EPI_BASE") = {L_epi_base};

ss[] = Surface "*";
S_LV = news; Compound Surface(S_LV) = ss[0];
S_RV = news; Compound Surface(S_RV) = ss[1];
S_epi = news; Compound Surface(S_epi) = ss[2];
S_scar = news; Compound Surface(S_scar) = ss[3];
Physical Surface("LV") = {S_LV};
Physical Surface("RV") = {S_RV};
Physical Surface("EPI") = {S_epi};
Physical Surface("SCAR") = {S_scar};



LL_base = newll; Line Loop(LL_base) = {L_LV_base, L_RV_base, L_epi_base};
S_base = news; Plane Surface(S_base) = {LL_base};
Physical Surface("BASE") = {S_base};



SL_wall = newsl; Surface Loop(SL_wall) = {S_LV, S_RV, S_epi, S_base};
V_wall = newv; Volume(V_wall) = {SL_wall};
Physical Volume("WALL") = {V_wall};
Coherence;














// Coherence Mesh;

// RefineMesh;

// CreateTopology;


// CreateGeometry;

// Merge "scar.stl";


// Surface Loop(1) = {1, 2, 3, 4, 5};

// Physical Surface("base", 10) = {4};
// Physical Surface("epi", 40) = {1};
// Physical Surface("ve", 20) = {2};
// Physical Surface("vd", 30) = {3};

// Volume(1) = {1};

// Surface Loop(2) = {5};

// Volume(2) = {2};

// Physical Volume("healthy", 1) = {1};

// Physical Volume("fibrose", 2) = {2};
// //+
// Compound Surface {1, 2, 3};
// //+
// Compound Surface {1};
// //+
// Compound Surface {3};
// //+
// Compound Surface {2};
Line Loop(16) = {5};
Line Loop(17) = {7};
Line Loop(18) = {6};
Plane Surface(19) = {16, 17, 18};
Plane Surface(20) = {16};
Plane Surface(21) = {18};
Plane Surface(22) = {16, 17, 18};
Plane Surface(23) = {16, 17, 18};
