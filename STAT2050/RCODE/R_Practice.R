#1. Read the dataset “StudentSurvey” into R.
SS<-read.csv("StudentSurvey.csv", header = TRUE)

#2. Check if there is any missing in the dataset. If yes, remove them.
B<-complete.cases(SS)
table(B)
#is.na(SS)
#table(a)
SS.N<-SS[B,]

#3. Create a new dataset using variables- Smoke, TV, Height, SAT, Pulse.
names(SS.N)
SS.NEW<-SS.N[,c(3,7,8,14,16)]

#4. Create a new dataset using the number of rows 1, 10, 15-20.
SS.N[c(1,10,15:20),]

#5. Take a random sample of size 50.
id<-sample(1:331,5,FALSE)
sample.SS<-SS.N[id,]

#6. Take a random sample of remaining the observations except for the observations in Q5.
sample.Remain<-SS.N[-id,]

#7. Take variable GPA from the dataset “StudentSurvey”.
SS.N$GPA
SS.N[,15]

#8. Split the dataset into two groups based on Sex and save them into R.
gr<-split(SS.N, SS.N$Sex)
