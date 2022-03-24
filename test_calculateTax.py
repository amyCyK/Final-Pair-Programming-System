#Group members:
#Law Hong Chun Zachary (56237888)
#Chan Yik Kit Amy (56237852)
#Martinez Kiel Marc (57162491)
#Prentation Time: 1300-13:10

import calculateTax,unittest
class testCalc(unittest.TestCase):
    def testcases(self):
        for [input,output] in [[150000,300],[200000,1480],[250000,4550],[300000,9420],[350000,16085]]:
            self.assertEqual(calculateTax.calculateTax(input),output)
if __name__=='__main__':unittest.main()