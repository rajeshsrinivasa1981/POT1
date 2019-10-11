import unittest

from Frameworks.Unit_Test.package1.TC_LoginTest import LoginTest
from Frameworks.Unit_Test.package1.TC_SignupTest import SignUpTest
from Frameworks.Unit_Test.package2.TC_PaymentReturnsTest import PaymentReturnsTest
from Frameworks.Unit_Test.package2.TC_PaymentTest import PaymentTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

sanitytestsuite=unittest.TestSuite([tc1,tc2])
regressiontestsuite=unittest.TestSuite([tc3,tc4])
mastertestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner().run(regressiontestsuite)
