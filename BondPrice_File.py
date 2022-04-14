
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
ppy = 2

def getBondPrice(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    for t in range(1,m*ppy+1):
        cf = couponRate*face/ppy
        pv = (1+y/ppy)**(-t)
        pvcf = pv*cf
        pvcfsum += pvcf
        
    bondprice = pvcfsum + (1+y/ppy)**-(m*ppy)*face
    return(bondprice)
