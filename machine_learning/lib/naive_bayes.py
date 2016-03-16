import pandas as pd
from scipy import stats

def trainNaiveBayes(trainData):
  #training Gausian Naive Bayes Classifier
  tY=trainData.loc[:,trainData.columns[0]]
  ind1=tY==0
  ind2=tY==1
  dp=pd.DataFrame(columns=trainData.columns, index=['mu1','sigma1','mu2','sigma2'])
  #estimate priors
  dp[trainData.columns[0]]['mu1']=1.0*sum(ind1)/len(trainData.index)
  dp[trainData.columns[0]]['mu2']=1.0*sum(ind2)/len(trainData.index)
  #estimate sample distribution paramters for p(xi|y=b)
  for i in trainData.columns[1:]:
    dp.loc['mu1',i]=(trainData[i][ind1]).mean()
    dp.loc['sigma1',i]=(trainData[i][ind1]).std()
    dp.loc['mu2',i]=(trainData[i][ind2]).mean()
    dp.loc['sigma2',i]=(trainData[i][ind2]).std()
  return dp

def classifyNaiveBayes(classData,dp):
  #classifying using trained Gausian Naive Bayes Classifier
  Y=classData.loc[:,classData.columns[0]]*0
  for j in classData.index:
    #start from the priors
    P1=dp[classData.columns[0]]['mu1'];
    P2=dp[classData.columns[0]]['mu2'];
    #multiply by conditional probability densities p(xi|y=b)
    for i in classData.columns[1:]:
        if dp[i]['sigma1']==0: #if sigma can not be defined (sample does not have variance)
            P1=P1*stats.norm.pdf(classData[i][j], loc=dp[i]['mu1'],scale=1) #pick up arbitrary sigma if undefined
        else:
            P1=P1*stats.norm.pdf(classData[i][j], loc=dp[i]['mu1'],scale=dp[i]['sigma1'])

        if dp[i]['sigma2']==0: #if sigma can not be defined (sample does not have variance)
            P2=P2*stats.norm.pdf(classData[i][j], loc=dp[i]['mu2'],scale=1) #pick up arbitrary sigma if undefined
        else:
            P2=P2*stats.norm.pdf(classData[i][j], loc=dp[i]['mu2'],scale=dp[i]['sigma2'])
    Y[j]=int(P2>P1)


  return Y

def trainNaiveBayesDiscrete(trainData):
  #training discrete Naive Bayes Classifier
  tY=trainData.loc[:,trainData.columns[0]]
  m=int(max([trainData[j][i] for j in trainData.columns[1:] for i in trainData.index])) #maximal number of classes in each feature of a training set
  #create output data structure for the probabilities - same column labels, rows correspond to values of x and there are two arrays like that for different b
  dp=[pd.DataFrame(columns=trainData.columns, index=range(1,m+1)), pd.DataFrame(columns=trainData.columns, index=range(1,m+1))]
  #split the training data between two labels
  ind1=tY==0
  ind2=tY==1
  #estimate P(y=b)
  dp[0][trainData.columns[0]][1]=1.0*ind1.sum()/len(trainData.index)
  dp[1][trainData.columns[0]][1]=1.0*ind2.sum()/len(trainData.index)
  #estimate conditional probabilities P(x|y=b)
  for j in trainData.columns[1:]:
    for i in range(1,m+1):
        dp[0].loc[i,j]=1.0*(trainData[j][ind1]==i).sum()/ind1.sum();
        dp[1].loc[i,j]=1.0*(trainData[j][ind2]==i).sum()/ind2.sum();
  return dp

def classifyNaiveBayesDiscrete(classData,dp):
  #classifying using trained discrete Naive Bayes Classifier
  Y=classData[classData.columns[0]]*0 #initialize the empty array
  for i in classData.index: #for al records to classify
    #start with the priors
    P1=dp[0][classData.columns[0]][1];
    P2=dp[1][classData.columns[0]][1];
    #and multiply them by the corresponding conditional probabilities P(x_i|y=b)
    for j in classData.columns[1:]:
      P1=P1*dp[0][j][classData[j][i]]
      P2=P2*dp[1][j][classData[j][i]]
    Y[i]=int(P2>P1) #finally for each record decide which P(y|x) is higher and choose the label
  return Y
