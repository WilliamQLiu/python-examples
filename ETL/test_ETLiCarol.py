# contents of test_ETLiCarol.py
# Runs multiple tests for iCarol's Extraction, Transformation, Loading system
# Run using $python test_ETLiCarol.py

import os
import unittest
import pandas

### Initialize File
originaldirectory = str('C:\iCarolFTPFiles\Original')
os.chdir(originaldirectory) #Change Local directory (where files go to)
myfilename= 'iCarolExportTest.csv'
myfullfilepath = os.path.join(originaldirectory, myfilename)
#mydataframe = pandas.read_csv(myfilename)
mydataframe = pandas.io.parsers.read_table(myfullfilepath, sep=',',
        quotechar='"', header=0, index_col='CallReportNum', error_bad_lines=True,
        warn_bad_lines=True)

class TestClass(unittest.TestCase):
    
    ### Testing Fixtures - Preparation needed to perform tests ###
    #def test_dbconnections(self):
    #    print "Testing DB Connections"
    #    # ToDo: Mock Module for DB connection
   
    #def test_import_ftp_files(self):
    #    print "Testing FTP Connections"
    #    # ToDo: Mock Module for FTP Connection

    ### Testing Cases - Check for specific responses to a particular set of inputs """
    def test_is_there_a_file(self):
        #print "Testing if there is a file"
        assert(os.path.exists(myfullfilepath)==1)

    def test_is_there_a_dataframe(self):
        #print "Testing if there is a dataframe"
        self.assertIsNotNone(mydataframe)

    def test_third_party_relationship(self):
        self.assertEqual(mydataframe.loc[17027716, ['Third Party Information - Relationship']],'Client Friend/Relative')

    def test_call_date_and_time_start(self):
        self.assertEqual(mydataframe.loc[17031875, ['CallDateAndTimeStart']],'1/1/2014 20:28')

    def test_report_version(self):
        self.assertEqual(mydataframe.loc[17032018, ['ReportVersion']], 'Lifeline Chat')

    def test_substance_abuse_how_caller_heard_substance_abuse(self):
        self.assertEqual(mydataframe.loc[17031875, ['Substance Abuse - How Caller heard about Hopeline - Substance Abuse']], 'GAMBLING ONLY')

    def test_clients_mental_health_concerns_primary(self):
        self.assertEqual(mydataframe.loc[17032018, ['Clients MH and SA concerns/treatment - Mental Health Concerns - Primary']], 'Depressive Disorders')

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner(verbosity=2).run(suite)