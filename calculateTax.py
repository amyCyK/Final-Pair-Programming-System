#Group members:
#Law Hong Chun Zachary (56237888)
#Chan Yik Kit Amy (56237852)
#Martinez Kiel Marc (57162491)
#Prentation Time: 1300-13:10
#500000 V
#600000 V
#300 000
#2 500 000
#600000 V
#800000 V

import numpy as np
def calculateTax(income,mpf_prefix='',married=False,joint_mpf=0):
    tax = 0.0
    if married:mpf=joint_mpf
    else:mpf=np.clip(income*0.05,0,18000)
    if mpf_prefix:print(mpf_prefix+' Mpf: '+str(mpf))
    income_mpf = income - mpf
    if married:Chargeable_Income= income_mpf - 264000 
    else: Chargeable_Income = income_mpf - 132000
    #print(' Chargeable_Income:'+str(Chargeable_Income))
    if Chargeable_Income <= 50000:
        tax = Chargeable_Income*0.02
        if tax<0: tax=0
    elif Chargeable_Income <= 100000:tax=(Chargeable_Income-50000)*.06 + 1000
    elif Chargeable_Income <= 150000:tax=(Chargeable_Income-100000)*.1 + 4000
    elif Chargeable_Income <= 200000:tax=(Chargeable_Income-150000)*.14 + 9000
    elif Chargeable_Income > 200000:
        tax=(Chargeable_Income-200000)*.17 + 16000
        if income_mpf*.15<tax:return int(income_mpf*.15)
    return int(tax)