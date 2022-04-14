
def getBondDuration(y, face, couponRate,m, ppy = 1):
    pvcftsum = 0
    pvcfsum = 0
    cf = face/ppy*couponRate
  
    for t in range(1,m+1):   
        pvcf = cf*(1+y)**(-t)
        pvcfsum += pvcf
        pvcft = pvcf*t
        pvcftsum += pvcft
  
    pvcfsum = pvcfsum + face*(1+y)**-m/ppy
    pvcftsum = pvcftsum +  m*face*(1+y)**-m/ppy
    
    BondDuration = pvcftsum/pvcfsum
    
    return(BondDuration)
