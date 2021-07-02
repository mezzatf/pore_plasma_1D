dom0Mult = 1e3;

Point(1) = {0                , 0, 0, 50e-9 * dom0Mult};
Point(2) = {0.5e-3 * dom0Mult, 0, 0, 50e-6 * dom0Mult};
Point(3) = {1.0e-3 * dom0Mult, 0, 0, 50e-9 * dom0Mult};

Line(1) = {1,2};
Line(2) = {2,3};

Physical Line(0) = {1,2};
