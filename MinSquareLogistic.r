library(lattice)
library(plotrix)
library(pracma)

#I
Y<-c(0.020408163,
     0.041666667,
     0.063829787,
     0.086956522,
     0.111111111,
     0.136363636,
     0.16279098,
     0.19047619,
     0.219512195,
     0.25,
     0.282051282,
     0.315789474,
     0.351351351,
     0.388888889,
     0.428571429,
     0.470588235,
     0.515151515,
     0.5625,
     0.612903226,
     0.666666667,
     0.724137931,
     0.785714286,
     0.851851852,
     0.923076923,
     1)
#C-M2 L=150 D-1 Random Ties
SY<-c(0.000327333,
      0.001638667,
      0.004072667,
      0.006242889,
      0.011475556,
      0.015972444,
      0.02382,
      0.030334444,
      0.039858889,
      0.049700444,
      0.061024667,
      0.075251333,
      0.090607556,
      0.103110444,
      0.125084667,
      0.134619111,
      0.159652222,
      0.178964,
      0.198542667,
      0.213521333,
      0.221723778,
      0.234644444,
      0.243347111,
      0.249539556,
      0.254611778)

NSY = SY / 0.254611778

#Funcion a determinar los coeficientes.
log<-function(r,x0){1/(1+exp(-r*(Y-x0)))}

#Intervalos 
x0 <- seq(0,1,length.out=25)
r <- seq(5,10,length.out=25)

#Funcion de error
e<-function(r,x0){
dot(SY,SY)-dot(log(r,x0),SY)^2/dot(log(r,x0),log(r,x0))
}

A=matrix(,nrow = length(r), ncol = length(x0))

for(i in 1:length(r)){
    for(j in 1:length(x0)){
     A[i,j]=e(r[i],x0[j])
      }
     }
     
persp(r,x0,A)
persp(r,x0,A, theta=-110)

#Determinamos el coeficiente de saturacion
dot(log(7.2916,0.458333),SY)/dot(log(7.2916,0.458333),log(7.2916,0.458333))
[1] 0.2600172

# Ecuacion logistica a usar y rango de x
logfit<-function(x){0.2600172/(1+exp(-7.2916*(x-0.4583333)))}
x<-seq(0,1,0.0001)

plot(Y,SY,lwd=2.5,col="dodger blue",xlim=c(0.01,1.0),ylim=c(0.001,0.2601),ylab='',xlab='')
par(new = TRUE)
plot(x,logfit(x),type="l",lwd=2.5,xlim=c(0.01,1.0),ylim=c(0.001,0.2601),ylab='',xlab='',tck=0.05)

