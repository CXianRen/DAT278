# COO and CSR formate
ref: https://zhuanlan.zhihu.com/p/188700729

### What is COO.
+ COO: Coordinate-Offset formate
+ store only the non-zero elements along with their corresponding row and column indices ( /ˈɪn.dɪ.siːz/).

### Data Structures:
+ 3 arrays to store V(value), R(row) and C(column).

### Example:
Let's take a sparse matrix as an example:
``` shell
A:
0 0 0 0
5 0 8 0
0 0 3 0
0 6 0 0

V: 5 8 3 6
R: 1 1 2 3
C: 0 2 2 1
```

![img](https://pic1.zhimg.com/v2-0e24a642bfd95d61e5f0e8ce7b5b167c_b.webp)

### What is CSR 
+ CSR: Compressed Sparse Row (more memory-efficient)
+ store only the non-zero elements along with their corresponding column indices. and an additional arrays(/əˈreɪ/) to keep track of where each row stats and ends in the non-zero values and column indices arrays.

### Data Structures:
+ 3 arrays to store V(value), C(column), RP (row pointers).

### Example:
Let's take a sparse matrix as an example:
``` shell
A:
0 0 0 0
5 0 8 0
0 0 3 0
0 6 0 0

V:  5 8 3 6
C:  0 2 2 1
RP: 0 0 2 3 4
```
+ How to explane RP?
```shell
# Rp representing the start of each row,
# if you want to access A[1,0]
# First:
RP[1] = 0 # row 1 first non-zero elements stored at V[0] 
R[2] = 2  # there are 2-0 = 2, non-zero elements in row 1
# Then
V[0] = 5; C[0] = 0; # then that is the value we want.

# IF we want to access A[0,0]
RP[0] = 0;
R[1] = 0;
return 0

# IF we want to access A[1,1]
RP[1] = 0;
RP[2] = 2
V[0] = 5; C[0] = 0;
V[1] = 8; C[1] = 2 > 1
return 0
```

### How to identify a matrix is sparse?
+ NNZs = Non Zero Elements

+ For COO
```
If there is a N*N matrix, and M non-zero elements.
Convert it to COO formate, we need memory: M*3

M * 3 < N*N => M< (N*N)/3

Sparse factor = M/(N*N) =>  < 30%
```
+ For CSR
```
If there is a N*N matrix, and M non-zero elements.
Convert it to CSR formate, we need memory: M*2 + N+1

M*2 + N + 1 < N*N => M< (N*N-N-1)/2

Sparse factor = (N*N-N-1)/2/(N*N) =>  < 50% 
```

+ COO VS CSR
```math
\begin{align}

\frac{N^2}{3} &<= \frac{N^2-N-1}{2} \\

2N^2 &= 3N^2-3N -3 \\
0 & = N^2 -3N -3    
\end{align}
```
Differentiate with respect to (3):
```math
0 = 2N -3 
```
So When $N<2$, COO use less memory than CSR, but from above we know, $M< \frac{N^2}{3}$, which mean N should at least 2. Then we can say CSR always better than COO. 