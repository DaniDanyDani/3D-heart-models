Merge "Patient_1.msh";
//+
SetFactory("OpenCASCADE");
BooleanDifference{ Volume{3}; Delete; }{ Volume{13}; Delete; }
//+
Show "*";
//+
Show "*";
