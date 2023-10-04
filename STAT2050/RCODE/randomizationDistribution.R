x<-c(12,10,13,14,11,9)
xbar.0<-mean(x)
dif<-xbar.0 - 10
shift<-x-dif
shift

randDist<-replicate(1000,mean(sample(shift, size=6, replace=T)))
library(BHH2)
dotPlot(randDist)
abline(v=c(11.5,8.5), col="red", lty=2)
p.value<-sum(randDist>=11.5 | randDist<=8.5)/1000
p.value