Part 1:

Trial	Learning Rate	   Iterations	Training MSE	Testing MSE
1	    0.010	             1000	      2.826546	     5.667602
2	    0.005	             1000	      2.860408	     5.693639
3	    0.005	             2000	      2.826556	     5.667607
4	    0.010	             500	      2.860351	     5.693698 
5	    0.020	             1000	      2.823103	     5.658709
6	    0.050	             1000	      2.823054	     5.656668
7	    0.050	             500	      2.823062	     5.657646
8	    0.100	             500	      2.823054	     5.656667 
9	    0.100	             250	      2.823062	     5.657633
10	    0.200	             500	      2.823054	     5.656643
11	    0.500	             500	      inf	         inf
12          0.250                    500              2.823054       5.656643    
(converges)
13          0.200                    250              2.823054        5.656666
14          0.200                    1000             2.823054        5.656643
15          0.200                    1500             2.823054        5.656643
16          0.200                    2000             2.823054        5.656643
17          0.100                    1000             2.823054        5.656643
18          0.100                    1500             2.823054        5.656643
19          0.100                    2000             2.823054        5.656643

Are you satisfied that you have found the best
solution?

Yes, I am satisfied that I have found the best solution. From early on, I found
out that the MSe is basically the same if not slightly better when there are 500 iterations
instead of 1000. When I tried keeping the learning rate the same and reducing the iteration 
count to 250, I noticed that the MSE was extremely slightly worse, so I decided that the optimal
conditions had 500 iterations. When it comes to elarning rate, I saw that the MSE for the learning reates of both
0.2 and 0.25 were about the same, but the MSE for the learning rate of 0.5 went to infiinty. So I believe the ideal
was 0.2 and 500 when it comes to learning rate and iterations.




Part 2:

Trial   Learning Rate      Iterations   Training MSE    Testing MSE

1       0.010              1000         3.415150        5.589607
2       0.005              1000         2.954542        5.504685
3       0.005              2000         3.096577        5.587393
4       0.005              500          2.957435        6.177135
5       0.005              250          3.080653        6.338567
6       0.005              1500         2.936214        5.829994
7       0.002              1000         2.834682        5.621782
8       0.0075             1000         3.153920        5.490974
9       0.007              1000         3.108355        5.484726
10      0.0065             1000         3.065400        5.483105
11      0.006              1000         3.025279        5.486028
12      0.0065             750          2.996228        5.752445
13      0.0065             1250         3.051470        5.937755
14      0.0065             250          3.284379        6.685151
15      0.0065             500          3.072177        6.413214
16      0.0065             1500         3.031763        6.007210
17      0.0065             2000         3.348917        5.669611


I am happy with the solution the package has found a good solution. For the learning rate of 0.0065 and the iteration count of 1000, the testing MSE is at its lowest.
I tested other parameters, but found this to be most accurate as the MSE wasn't decreasing any more. To test more, it is possible to alter the values of the 
learning rate and/or the iteration count.


