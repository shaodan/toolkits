import numpy as np
import matplotlib.pyplot as plt

#parameters
#true model
coeff=np.random.uniform(-2,2,20)
#education tell you only 6 out of 20 true parameters
education=np.random.choice(range(20),6,replace=False)

#generate factor and true economic fundamental, 100 periods
factor=np.random.normal(0,1,[20,100])
ytrue=np.dot(coeff,factor)

#educated guess of economic fundamental
coeffedu=np.zeros(20)
for edu in education:
    coeffedu[edu]=coeff[edu]
yedu=np.dot(coeffedu,factor)

#uneducated parameters, take -1, 0 or 1, a.k.a signs of parameter
#people knows 1,5,10,15,or 20 signs of the true parameter, but not the magnitude
def unedu(numfac):
    returntemp=np.zeros(20)
    choicetemp=np.random.choice(range(20),numfac,replace=False)
    for cho in choicetemp:
        if coeff[cho]!=0:
            returntemp[cho]=coeff[cho]/np.abs(coeff[cho])
    return returntemp
unedu1=unedu(1)
unedu5=unedu(5)
unedu10=unedu(10)
unedu15=unedu(15)
unedu20=unedu(20)

#prediction from uneducated people
yunedu1=np.dot(unedu1,factor)
yunedu5=np.dot(unedu5,factor)
yunedu10=np.dot(unedu10,factor)
yunedu15=np.dot(unedu15,factor)
yunedu20=np.dot(unedu20,factor)

#plot
def plotpred(series,labelvalue):
    fig,example=plt.subplots(figsize=(16,10))
    example.plot(series,label=labelvalue)
    example.plot(ytrue,label='True value of economic fundamental')
    example.legend(loc='right')
    example.set_title('Predicted VS true, educated VS uneducated')
    example.set_xlabel('Time')
    example.set_ylabel('Economic fundamental')
    plt.show()

plotpred(yedu,'Educated guess')
plotpred(yunedu1,'Uneducated guess, know 1 signs')
plotpred(yunedu5,'Uneducated guess, know 5 signs')
plotpred(yunedu10,'Uneducated guess, know 10 signs')
plotpred(yunedu15,'Uneducated guess, know 15 signs')
plotpred(yunedu20,'Uneducated guess, know 20 signs')
