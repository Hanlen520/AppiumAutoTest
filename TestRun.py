import unittest
import HTMLTestRunner
from TestCases.SYLogin.TestLogin import TestLogin
from TestCases.SYMinePage.SYMine import MineTest
from TestCases.SYCocloudPage.SYCocloud import SYCocloud
from TestCases.SYmain.SYMain import SYMain

# MineTest.suite(MineTest('test_mine'))


#
testunit = unittest.TestSuite()  # 定义一个单元测试容器
#
# # testunit.addTest(TestLogin("test_login"))
# testunit.addTest(MineTest("test_mine"))
# testunit.addTest(MineTest("test_account"))
# testunit.addTest(MineTest("test_hardDisk"))
# testunit.addTest(MineTest("test_user_management"))
# testunit.addTest(MineTest("test_Router"))
# testunit.addTest(MineTesSYMaint("test_sys"))
# testunit.addTest(SYCocloud("test_image"))
# testunit.addTest(SYCocloud("test_video"))
# testunit.addTest(SYCocloud("test_management"))
# testunit.addTest(SYMain("test_add"))
# testunit.addTest(SYMain("test_router_ap"))
# testunit.addTest(SYMain("test_router_access"))
testunit.addTest(SYMain("test_pager_source"))
filename = "./myAppiumLog.html"  # 定义个报告存放路径。
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='算云自动化测试报告',
                                       description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
runner.run(testunit)  # 自动进行测试


#
#
# suite1 = unittest.TestLoader().loadTestsFromTestCase(SYMain)
# suite2 = unittest.TestLoader().loadTestsFromTestCase(SYCocloud)
# suite3 = unittest.TestLoader().loadTestsFromTestCase(MineTest)
# suite = unittest.TestSuite([suite1, suite2, suite3])
# filename = "./myAppiumLog.html"  # 定义个报告存放路径。
# fp = open(filename, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='算云自动化测试报告',
#                                        description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
# runner.run(suite)  # 自动进行测试
