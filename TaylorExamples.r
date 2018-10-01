#As expected when x = 1/2, f(x) = 1/(1 - x) = 2; 
#Also the expansion converges toward 2 as the power series increases.
#Below is a plot the f(x) and polynomial approximation through Taylor
#series p(x):
#https://www.rdocumentation.org/packages/pracma/versions/1.9.9/topics/taylor

library(pracma)

f <- function(x) (1/(1-x))
f# <- function(x) (log(x))
#Calcula los coeficientes
p <- taylor(f, 2, 5)
#Da la secuencia para las x's
x <- seq(-10.0, 10.0, length.out=100)
yf <- f(x)
#Evalua el polinomio
yp <- polyval(p, x)
plot(x, yf, type = "l", main =' Taylor Series Approximation of 1/(1-x)',col = "blue", lwd = 3)
lines(x, yp, col = "red")
legend('topleft', inset=.05, legend= c("Taylor Series", "f(x)=1/(1+x)")
       , lwd=c(2.5,2.5), col=c('red', 'blue'), bty='n', cex=.75) 

#Evaluando esta funcion
ExpansionTest <- function(x,n){
  y=0
  for (i in 0:n) y = y + sum(x^i) 
  return(y)
}

ExpansionTest(1/2, 100)

