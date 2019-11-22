#library(pracma)
#library(rootSolve)

#E: R2-The two roots, M-a (ENERGY, REPS)-matrix, e-enerty value in M, n-current iteration
#S: Compute the energy of a pair of roots, not zero.
Nn<-function(R2,M,e,n) { #E: Compute N(e) for the recent pair of roots coming from e at it. n 
  if((n==1) && (R2[1]==0)) {
      print("entro al caso n==1 zeros")
      return(c(2,2)) # zero 0 eigenvalue has degeneracy 2 in level 1
}
  H<-matrix(which(M[,1] == e, arr.ind = T),ncol=2) #which return an index.err, which index col in M = e
  I<-min(H[,1]) #if there is more coincidences with e, return minimum index 
  find<-M[I,2] #Assign the number of repetitions of energy e in iter. n ti find
  return(c(find,find)) #return concatenation two repetitions per energy??
}

#E: R2-The two roots, M-a (ENERGI, REPS)-matrix, e-enerty value in M, n-current iteration
#S: Compute the energy of a vector of roots, not zero.
NSn<-function(R2,M,e,n) { #E: Compute N(e) for the recent pair of roots coming from e at it. n
  v<-c()
  forbd1<-which(Re(R2)==-4)
  forbd2<-c(forbd1,which(Re(R2)==-2))
  forbd3<-c(forbd2,which(Re(R2)==1))
  forbd<-c(forbd3,which(Re(R2)==2)) #ford tiene los indices que contienen los elementos prohibidos

  if(length(forbd)>0 && length(forbd)<=2 ) {
for(r in forbd) #forbd tiene cardinalidad a lo mas 2
  {
   if(R2[r]==-4) 
    v<-c(v,1) #Nn(-4)=1
   if(R2[r]==2) 
     v<-c(v,3^{n}) #Nn(2)=Nn-1, n>=1
   if(R2[r]==1) 
     v<-c(v,3^{n-1}+1) #Nn(1)=(Nn-1)/3+1, n>=1
   if(R2[r]==-2 && n==1){
     print("Entro energia -2 en iteracion n=1")
     v<-c(v,1) #Nn(2)=d(n,1)
  }
   if(R2[r]==-2 && n!=1){ #Nn(2)=d(n,1)
     print("Entro energia -2 en iteracion n!=1")
     v<-c(v,0) 
   }
  } #end-for
} #end-if
  
  if(length(v)==2) return(v) # para ambas raices ya se determino su duplicidad
  if(length(v)==1) #solo una raiz fue probida
  {
    if(forbd[1]==1) ie<-2 #forbd tiene indices de R2, el indice que falta es el 2
    else ie<-1 #si no el 1
    H<-matrix(which(M[,1] == R2[ie], arr.ind = T),ncol=2) #which energy in M is R2[ie]
    I<-min(H[,1]) #if there is more coincidences with e, return minimum index
    v<-c(v,I)
    return(v)
  }
  if(length(v)==0){ #No hubo energias +/-2,1, o 4 Las dos duplicidades consideradas corresponden a la duplicidad de la raiz proveniente
  #buscamos la degenerancia en la matriz M
  H<-matrix(which(M[,1] == e, arr.ind = T),ncol=2) #which return an index.err, which index col in M = e
  I<-min(H[,1]) #if there is more coincidences with e, return minimum index 
  find<-M[I,2] #Assign the number of repetitions of energy e in iter. n ti find
  return(c(find,find)) #return concatenation two repetitions per energy??
  }
}


#E:
#S:
En<-function(E,n) {
  O=c()
  for(i in 1:length(which(E == n))) #Repeat the numbr of zeros in E, which return a set of indexes
    O<-c(O,2) #concatenates the 2 value in O
      return(O)
}

#############CYCLE FRACTAL 
#n=0, 2^(0+1) = vertices 
#Hay un digono con dos posibles eigenvalues E=-2,E=+2
#polyroot(c(2-2, 0,1)) #E->(0,0)
#x<-polyroot(c(-2-2, 0,1)) #E->(2,-2)
E0<-c(2,-2) #Energy states on a digon
N0<-c(1,1) #Number of repetitions? or states in digon?
M<-matrix(c(E0,N0),ncol=2)

n=0 #level

E1=c() #Null vector
N1=c()

#This only for n>=2, the first time i need to use i=1
for(i in seq(1:10)) {
#for(j in 1:10)
for(e in E0) { #Para cada energia en E0
  print(e)
  R2<-polyroot(c(e-2,0,1))
  E1<-c(E1,R2) #E->(2,-2),E->(0,0)
  N1<-c(N1,Nn(R2,M,e,i)) #adds to N1 repetitions
}
n<-n+1
M<-matrix(c(E1,N1),ncol=2) #Creates a new matrix from those previosly computed
E0<-E1 #go forward with new energy eigestates E1, but zeros adquiere #states through  N_{n+1}(E)=N_{n}(E')
} #end for i=1,...,10

inter<-0.10
U <- seq(-2.0,2.0,by=inter); #intervals
counts <- numeric(length(U)); #Vector of zeros to posit the number of states

#Interval counting
for(j in 1:length(counts)) {
  counts[j] <- sum(M[which(Re(M[,1])>=U[j] & Re(M[,1])<=U[j+1]),2]);
}

plot(U+inter/2,counts/(2^{n+1} - 1), ylim=c(0,max(Re(counts))*0.001),main="Linear Chain",
    xlab="E", ylab="p(E)*0.001")

#a<-c(0,1,0,1,0,2,3,4,3,2)
#b<-c(3,3,3,4,4,4,7,7,7,10)
#c<-data.frame(a,b)


##########SIERPINSKI GASKET FRACTAL##########
#n=0, 3^(0+1) = 3 vertices

#First level energies .
E0<-c(2,-2) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6) 
#2->(-1,-2), -2->(0.5615528+0i,-3.5615528-0i)
N0<-c(2,0) #Number of repetitions? or states in digon?
M<-matrix(c(E0,N0),ncol=2)

n=0 #level

E1=c() #Null vector
N1=c()

#Poliniomio 2do grado
#eigenvaluees E'=-4,1,2,-2
#polyroot(c(-4, 3, 1)) #E'=-4,E->(1,-4)
#polyroot(c(1, 3, 1)) #E'=1,E->(-0.381966, -2.618034)
#polyroot(c(2, 3, 1)) #E'=2,E->(-1,-2)
#polyroot(c(-2, 3, 1)) #E'=-1,E->(0.5615528,-3.5615528)

#Initially we start with paper N0(2)=2,N0(-2)=0

#This only for n>=2, the first time i need to use i=1
for(i in seq(1:11)) {
  #for(j in 1:10)
  for(e in E0) { #Para cada energia en E0
    print(e)
    R2<-polyroot(c(e,3,1)) #E^2+3E+E'=0, E=(-3+/-sqrt(9-4E'))/2
    E1<-c(E1,R2) 
    N1<-c(N1,NSn(R2,M,e,i)) #adds to N1 repetitions
  }
  n<-n+1
  M<-matrix(c(E1,N1),ncol=2) #Creates a new matrix from those previosly computed
  E0<-E1 #go forward with new energy eigestates E1, but zeros adquiere #states through  N_{n+1}(E)=N_{n}(E')
} #end for i=1,...,10

#interval counting
inter<-0.01
U <- seq(-4.0,4.0,by=inter); #intervals
counts <- numeric(length(U)); #Vector of zeros to posit the number of states

#Buscamos los valores para los cuales la recursion no aplica, PROHIBIDOS

  if(length(forbd1<-which(Re(E1)==-4))==0){
    E1<-c(E1,-4) #for all n Nn(4)=1
    N1<-c(N1,1)
  }
  if(length(forbd2<-which(Re(E1)==2))==0){
    E1<-c(E1,2) #for all n Nn(2)=Nn-1
    N1<-c(N1,3^{n})
  }
  if(length(forbd3<-which(Re(E1)==1))==0){
    E1<-c(E1,1) #for all n Nn(1)=(Nn-1)/3+1
    N1<-c(N1,3^{n-1}+1)
  }
  if(length(forbd4<-which(Re(E1)==-2))==0){
  E1<-c(E1,-2) #for all n Nn(-2)=0=d(1,n)
  N1<-c(N1,0)
  }

#Recalculate M  
M<-matrix(c(E1,N1),ncol=2) #Creates a new matrix from those previosly computed

#Interval counting
for(j in 1:length(counts)){
  counts[j] <- sum(M[which(Re(M[,1])>=U[j] & Re(M[,1])<=U[j+1]),2]);
}

#Finite additional values -1 from e=2, -3+/-sqrt(13)/2 from e=2, -3+/-sqrt(5)/2 from e=1 (all with finite iter. )
#check we are recalculating e=-1 (forbidden also)
#its density is on few iteration then is not divided by 3^{n+1} = #states
EFinite<-c(-1,(-3-sqrt(13))/2,(-3-sqrt(5))/2)
PFinite<-c(2/3^2,3/3^3,(1/3+1)/3^2)

mm<-which(U==1) #to plot from -4 to 1

plot(U+inter/2,counts/(3^{n+1}),type="h", xlim=c(-4,1),ylim=c(0,max(Re(counts[1:mm])/(3^{n+1}))))
par(new = TRUE)
mx1<-max(PFinite[1:3])
mx2<-max(Re(counts[1:mm])/(3^{n+1}))
plot(EFinite,PFinite,type="h", axes=FALSE, xlab=NA, ylab=NA, xlim=c(-4,1),ylim=c(0,max(mx1,mx2)))

plot(U+inter/2,counts, type="l",xlim=c(-4,1),ylim=c(0,max(Re(counts[1:mm])))) #check type h

#INTEGRATED DENSITY OF STATES N(E)
pcounts<-counts/(3^{n+1})
sumcounts<-c()
for(j in 1:length(counts)){
  sumcounts[j] <- sum(pcounts[1:j])
}

#U = [-4,4] with inter=0.01
plot(U,sumcounts,type="l",xlim=c(-4,2),ylim=c(0,1),main="Integrated Density of States - Sierp. Net, n=11")
write.table(c(U,sumcounts),file="IntegratedStatesSierp.txt",sep="\t")

#########INTEGRATED LEVEL SPACING DISTRIBUTION P(S)
#First level energies .
E0<-c(2,1) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6) 
##(1) E0<-c(2,-2) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6) 
##(2) E0<-c(2,-2) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6)
##(3) E0<-c(2,1) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6)
##(4) E0<-c(2,1) #Initial energy states on the sierpinski type fractal, other : (-6,-2,6)

#2->(-1,-2), -2->(0.5615528+0i,-3.5615528-0i)
##(1) N0<-c(2,0) #Number of repetitions? or states in digon?
##(2) N0<-c(2,2) #Number of repetitions? or states in digon?
##(3) N0<-c(2,1) #Number of repetitions? or states in digon?
##(4) N0<-c(2,2) #Number of repetitions? or states in digon?

N0<-c(2,1) #Number of repetitions? or states in digon?


M<-matrix(c(E0,N0),ncol=2)
n=0 #level
E1=c() #Null vector
N1=c()

#This only for n>=2, the first time i need to use i=1
for(i in seq(1:11)) {
  #for(j in 1:10)
  for(e in E0) { #Para cada energia en E0
    print(e)
    R2<-polyroot(c(e,3,1)) #E^2+3E+E'=0, E=(-3+/-sqrt(9-4E'))/2
    E1<-c(E1,R2) #Las que tiene mas las actuales
    N1<-c(N1,NSn(R2,M,e,i)) #adds to N1 repetitions
  }
  n<-n+1
  M<-matrix(c(E1,N1),ncol=2) #Creates a new matrix from those previosly computed
  
  E0<-E1 #go forward with new energy eigestates E1, but zeros adquiere #states through  N_{n+1}(E)=N_{n}(E')
} #end FOR i=1,...,n

#interval counting
inter<-0.01 #Energy increment
U <- seq(-4.0,4.0,by=inter); #energy intervals (-4,+4)
counts <- numeric(length(U)); #Vector of zeros to posit the number of states
lengcounts <- numeric(length(U))
#Buscamos los valores para los cuales la recursion no aplica, PROHIBIDOS

if(length(forbd1<-which(Re(E1)==-4))==0){
  E1<-c(E1,-4) #for all n Nn(4)=1
  N1<-c(N1,1)
}
if(length(forbd2<-which(Re(E1)==2))==0){
  E1<-c(E1,2) #for all n Nn(2)=Nn-1
  N1<-c(N1,3^{n})
}
if(length(forbd3<-which(Re(E1)==1))==0){
  E1<-c(E1,1) #for all n Nn(1)=(Nn-1)/3+1
  N1<-c(N1,3^{n-1}+1)
}
if(length(forbd4<-which(Re(E1)==-2))==0){
  E1<-c(E1,-2) #for all n Nn(-2)=0=d(1,n)
  N1<-c(N1,0)
}

#Recalculamos M  
M<-matrix(c(E1,N1),ncol=2) #Creates a new matrix from those previosly computed

#Number of states for each ENERGY LEVEL, updates counts with new matrix M
for(j in 1:length(counts)){
  counts[j] <- sum(M[which(Re(M[,1])>=U[j] & Re(M[,1])<U[j+1]),2]) 
  #lengcounts[j] <- length(M[which(Re(M[,1])>=U[j] & Re(M[,1])<U[j+1]),2])
  }

pcounts<-counts/(3^{n+1}) #Divide by #Total of States on Sierp. at iteration n, aproximating p(Ei),i=1,,...,n

sumcounts<-c()
#Aproximating N(E)
for(j in 1:length(counts)){
  sumcounts[j] <- sum(pcounts[1:j]) #Aproximate the integrated density of states N(Ei),i=1,,...,n
}

plot(U,sumcounts,type="l",xlim=c(-4,2.1),ylim=c(0,1.01),main="Integrated Density of States - Sierp. Net, n=9")

#Computing S_i=<N(Ei+1)> - <N(Ei)>
#avereged integrated density of states = #states in a gap Si+1 - Si = 
mNe<-c()
for(j in 1:(length(sumcounts))){
  if(j==1){
  #mNe[j]<-sum(sumcounts[1:j+1])/(U[j+1]-U[1]) - sum(sumcounts[1:j])/(U[1])
  mNe[j]<-sumcounts[j]/U[1] #media del #de estados
  }
    #mNe[j]<-mean(sumcounts[1:j+1]) - mean(sumcounts[1:j])
  else { 
    #mNe[j]<-sum(sumcounts[1:j+1])/(U[j+1]-U[1]) - sum(sumcounts[1:j])/(U[j+1]-U[1])
    if(j>2)
    mNe[j]<- sumcounts[j]/(U[j]-U[1]) - sumcounts[j-1]/(U[j-1]-U[1])
    if(j==2)     
    mNe[j]<- sumcounts[j]/(U[j]-U[1]) - sumcounts[j-1]/(U[j-1])
   }
}

sortmNe <- sort(mNe, method = "shell")

inter2<-(max(Re(mNe[1:length(mNe)-1]))-min(Re(mNe[1:length(mNe)-1])))/(length(mNe)-1)
S <- seq(min(Re(mNe[1:length(mNe)-1])),max(Re(mNe[1:length(mNe)-1])),by=inter2); #S intervals, min/max(Re(mNe[1:800]))
#inter2<-(exp(1)-exp(-7))/(length(mNe)-1)
# <- seq(exp(-7),exp(1),by=inter2);
#Averaged <N(Ei)>
#mNe<-c(mNe,mean(sumcounts)) #mNe has the mean of all integreted values PER LEVEL 

#S<-c(mNe[1]) #S1
#mNe[length(mNe)+1]=0
#for(i in 1:length(mNe)-1){ #n
#  S<-c(S,mNe[i+1]-mNe[i])
#}

#Counting
#US <- seq(min(Re(log(S))),max(Re(log(S))),by=0.01) #intervals for S
scounts <- numeric(length(S)); #Vector of zeros to posit the number of states

#sum number of values of S=<N(Ei+1)>-<N(Ei)> that fall into S intervals 
for(j in 1:length(S)){
  #scounts[j] <- sum(mNe[which(Re(mNe)>=Re(S[j]) & Re(mNe)<Re(S[j+1]))]); #aproximate P(Si),i=1,,...,n
  #Otra seria contar no sumar 
  scounts[j] <- length(which(Re(sortmNe)>Re(S[j]) & Re(sortmNe)<=Re(S[j+1])))/inter2; #aproximate P(Si),i=1,,...,n
  ##scounts[j] <- sum(M[which(Re(M[,1])>=Re(sortmNe[j]) & Re(M[,1])<Re(sortmNe[j+1])),2]) #aproximate P(Si),i=1,,...,n
}

length(which(scounts==0))
plot(S,scounts,type="l")

#pcounts<-scounts/(3^{n+1})
sumScounts<-c()
normalizing <- sum(scounts[1:length(scounts)])
scounts <- scounts/normalizing

for(j in 1:length(scounts)){
  sumScounts[j] <- sum(scounts[j:length(scounts)])
}

#Esta y revisar porque hay m}uchos 0 en sumScounts

#plot(log(Re(S)+inter2/2),log(Re(sumScounts)),ylim=c(-4,-0.7),xlim=c(-7.4,-0.55),type="l")
par(new=TRUE)
plot(log(Re(S)+inter2/2),log(Re(sumScounts)),type="l")
plot(log(Re(S)),log(Re(sumScounts)),type="l",ylim=c(-9,-0.7),xlim=c(-7.4,1))
write.table(c(Re(S),Re(sumScounts)),file="AveragedIntegratedSpacinStatesDistSierpN11-INI5.txt",sep="\t")

plot(Re(S)+inter2/2,Re(sumScounts),type="l",log="xy")
plot(Re(S)+inter2/2,((Re(S)+inter2/2))^(-0.57),type="l",log="xy",xlab='',ylab='',axes=FALSE)

#ESTA
par(new=TRUE)
plot(log(Re(S)+inter2/2),log(Re(sumScounts)),type="l")
write.table(c(Re(S),Re(sumScounts)),file="AveragedIntegratedSpacinStatesDistSierp11.txt",sep="\t")

par(new=TRUE)
plot(log(Re(S)+inter2/2),(-0.57)*(log(Re(S)+inter2/2))-2.5,type="l",main=NULL,xlab='',ylab='',axes=FALSE)

plot(log(Re(S)+inter2/2),log(Re(sumScounts)),type="l")
par(new=TRUE)
plot(log(Re(S)+inter2/2),(log(Re(S)+inter2/2))^{-0.56},type="l")


#if(length(which(U==-1))==0){ #search in M
 # print("Agregamos e = -1 con N(-1)=N1(2)=3^1")
#  E1<-c(E1,-1) #for all n Nn(2)=Nn-1=3^n
#  N1<-c(N1,3) #Repetitions Modificar count de otra manera
#}

#if(length(which(Re(E1)==(-3-sqrt(13))/2)==0)){ #search in M, -3.302776
#  print("Agregamos e = (-3-sqrt(13))/2 con N(-3.302776)=N2(2)=3^2")
#  E1<-c(E1,(-3-sqrt(13))/2) #for all n Nn(2)=Nn-1=3^n
#  N1<-c(N1,3^2)
#}

#if(length(which(Re(E1)==(-3-sqrt(5))/2)==0)){ #search in M, -3.302776
#  print("Agregamos e = (-3-sqrt(5))/2) con N(-2.618034)=N1(1)=3^1/3+1")
#  E1<-c(E1,(-3-sqrt(5))/2) #for all n Nn(1)=Nn-1/3+1=3^n/3+1
#  N1<-c(N1,3^1/3+1)
#}