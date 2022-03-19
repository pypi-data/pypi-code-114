from .TestProperties import TestProperty, Qarg
from .TestCaseGeneration import TestCaseGenerator
from .TestExecutionEngine import TestExecutor
from .StatisticalAnalysisEngine import StatAnalyser
from math import cos, radians

class QiskitPropertyTest():



    def assertEqualData(self, qu0, qu1, qu0_pre, qu1_pre, basis, filter_qc):

        #Error handling for the parameters
        if not isinstance(qu0, int) or not isinstance(qu1, int) or not isinstance(qu0_pre, bool) or not isinstance(qu1_pre, bool):
            raise Exception(f"Incorrect arguments supplied to assertEqual: qu0: {qu0}, qu1: {qu1}; (Optional: qu0_pre: {qu0_pre}, qu1_pre: {qu1_pre}\nThere should be 2 integers, followed by 2 optional booleans, defaulted to False)")

        #TODO add more error handling

        generatedTests = [qc.copy() for qc, theta, phi in self.initialisedTests]

        numberedGeneratedTests = [x for x in enumerate(generatedTests)]

        filteredNumbered = list(filter(lambda x: len(list(filter(filter_qc, [x[1]]))) != 0, numberedGeneratedTests))

        indexNotFilteredOut = [x[0] for x in filteredNumbered]

        self.nbFiltered = len(indexNotFilteredOut)

        filteredTests = [x[1] for x in filteredNumbered]
        #print(f"DEBUG\nfilteredTests: {filteredTests}\nEND DEBUG\n")


        if qu0_pre == qu1_pre:

            #Applies the function to the generated tests only if they are both sampled after running the full program
            if not qu0_pre and not qu1_pre:
                for filteredTest in filteredTests:
                    self.quantumFunction(filteredTest)


            dataFromExec = TestExecutor().runTestsAssertEqual(filteredTests, self.testProperty.nbTrials, \
                self.testProperty.nbMeasurements, qu0, qu1, self.testProperty.nbClassicalBits, \
                self.testProperty.nbClassicalBits + 1, basis)

            testResults = StatAnalyser().testAssertEqual(self.testProperty.p_value, dataFromExec)

            qu0Params = [(x[1].get(qu0, 0), x[2].get(qu0, 0)) for x in self.initialisedTests]
            qu1Params = [(x[1].get(qu1, 0), x[2].get(qu1, 0)) for x in self.initialisedTests]
            params = tuple(zip(qu0Params, qu1Params))

            testResultsWithInit = tuple(zip(testResults, params))

        else:
            generatedTestsPre = [qc.copy() for qc, theta, phi in self.initialisedTests]
            filteredTestsPre = [generatedTestsPre[x] for x in indexNotFilteredOut]

            for filteredTest in filteredTests:
                self.quantumFunction(filteredTest)

            if not qu0_pre:
                dataFrom_qu0 = TestExecutor().runTestsAssertProbability(generatedTests, self.testProperty.nbTrials, \
                    self.testProperty.nbMeasurements, qu0, self.testProperty.nbClassicalBits + 1, basis)
            else:
                dataFrom_qu0 = TestExecutor().runTestsAssertProbability(filteredTestsPre, self.testProperty.nbTrials, \
                    self.testProperty.nbMeasurements, qu0, self.testProperty.nbClassicalBits + 1, basis)

            if not qu1_pre:
                dataFrom_qu1 = TestExecutor().runTestsAssertProbability(generatedTests, self.testProperty.nbTrials, \
                    self.testProperty.nbMeasurements, qu1, self.testProperty.nbClassicalBits + 1, basis)
            else:
                dataFrom_qu1 = TestExecutor().runTestsAssertProbability(filteredTestsPre, self.testProperty.nbTrials, \
                    self.testProperty.nbMeasurements, qu1, self.testProperty.nbClassicalBits + 1, basis)


            formattedData = tuple(zip(dataFrom_qu0, dataFrom_qu1))
            testResults = StatAnalyser().testAssertEqual(self.testProperty.p_value, formattedData)

            qu0Params = [(x[1].get(qu0, 0), x[2].get(qu0, 0)) for x in self.initialisedTests]
            qu1Params = [(x[1].get(qu1, 0), x[2].get(qu1, 0)) for x in self.initialisedTests]
            params = tuple(zip(qu0Params, qu1Params))

            testResultsWithInit = tuple(zip(testResults, params))

        return testResultsWithInit




    def assertEqual(self, qu0, qu1, qu0_pre=False, qu1_pre=False, basis="z", filter_qc=lambda qc:True):
        results = self.assertEqualData(qu0, qu1, qu0_pre, qu1_pre, basis, filter_qc)

        if not qu0_pre and not qu1_pre:
            print(f"AssertEqual({qu0}, {qu1}) results using basis {basis.upper()}:")
        elif qu0_pre and qu1_pre:
            print(f"AssertEqual({qu0}_pre, {qu1}_pre) results using basis {basis.upper()}:")
        elif not qu0_pre and qu1_pre:
            print(f"AssertEqual({qu0}, {qu1}_pre) results using basis {basis.upper()}:")
        else:
            print(f"AssertEqual({qu0}_pre, {qu1}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0][0]} Phi = {testResult[1][0][1]}")
                print(f"qu1: Theta = {testResult[1][1][0]} Phi = {testResult[1][1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {self.nbFiltered - nbFailed} / {self.nbFiltered} succeeded\n")
        else:
            print(f"All {self.nbFiltered} tests have succeeded!\n")


        return results


    def assertNotEqual(self, qu0, qu1, qu0_pre=False, qu1_pre=False, basis="z", filter_qc=lambda qc:True):
        oppositeResults = self.assertEqualData(qu0, qu1, qu0_pre, qu1_pre, basis, filter_qc)

        results = [(not x[0], x[1]) for x in oppositeResults]

        if not qu0_pre and not qu1_pre:
            print(f"AssertNotEqual({qu0}, {qu1}) results using basis {basis.upper()}:")
        elif qu0_pre and qu1_pre:
            print(f"AssertNotEqual({qu0}_pre, {qu1}_pre) results using basis {basis.upper()}:")
        elif not qu0_pre and qu1_pre:
            print(f"AssertNotEqual({qu0}, {qu1}_pre) results using basis {basis.upper()}:")
        else:
            print(f"AssertNotEqual({qu0}_pre, {qu1}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0][0]} Phi = {testResult[1][0][1]}")
                print(f"qu1: Theta = {testResult[1][1][0]} Phi = {testResult[1][1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {self.nbFiltered - nbFailed} / {self.nbFiltered} succeeded\n")
        else:
            print(f"All {self.nbFiltered} tests have succeeded!\n")


        return results



    def assertEntangledData(self, qu0, qu1, basis):

        generatedTests = [qc.copy() for qc, theta, phi in self.initialisedTests]

        for generatedTest in generatedTests:
            self.quantumFunction(generatedTest)

        dataFromExec = TestExecutor().runTestsAssertEntangled(generatedTests,
                                                              self.testProperty.nbTrials,
                                                              self.testProperty.nbMeasurements,
                                                              qu0,
                                                              qu1,
                                                              self.testProperty.nbClassicalBits,
                                                              self.testProperty.nbClassicalBits + 1,
                                                              basis)

        testResults = StatAnalyser().testAssertEntangled(self.testProperty.p_value, dataFromExec)


        qu0Params = [(x[1].get(qu0, 0), x[2].get(qu0, 0)) for x in self.initialisedTests]
        qu1Params = [(x[1].get(qu1, 0), x[2].get(qu1, 0)) for x in self.initialisedTests]
        params = tuple(zip(qu0Params, qu1Params))

        testResultsWithInit = tuple(zip(testResults, params))


        return testResultsWithInit


    def assertEntangled(self, qu0, qu1, basis="z"):
        results = self.assertEntangledData(qu0, qu1, basis)

        print(f"AssertEntangled({qu0}, {qu1}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0][0]} Phi = {testResult[1][0][1]}")
                print(f"qu1: Theta = {testResult[1][1][0]} Phi = {testResult[1][1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {len(self.initialisedTests) - nbFailed} / {len(self.initialisedTests)} succeeded\n")
        else:
            print(f"All {len(self.initialisedTests)} tests have succeeded!\n")


        return results



    def assertNotEntangled(self, qu0, qu1, basis="z"):
        oppositeResults = self.assertEntangledData(qu0, qu1, basis)

        results = [(not x[0], x[1]) for x in oppositeResults]

        print(f"AsserNotEntangled({qu0}, {qu1}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0][0]} Phi = {testResult[1][0][1]}")
                print(f"qu1: Theta = {testResult[1][1][0]} Phi = {testResult[1][1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {len(self.initialisedTests) - nbFailed} / {len(self.initialisedTests)} succeeded\n")
        else:
            print(f"All {len(self.initialisedTests)} tests have succeeded!\n")


        return results




    def assertProbabilityData(self, qu0, expectedProba, qu0_pre, basis, filter_qc):

        #Error handling
        if not isinstance(qu0, int) or not (isinstance(expectedProba, float) \
           or isinstance(expectedProba, int)) or not isinstance(qu0_pre, bool):
            print(f"qu0: {qu0}, expectedProba: {expectedProba}; (Optional: qu0_pre: {qu0_pre}")
            print(f"There should be an integer, followed by either a float or an int, followed by an optional boolean")
            raise Exception(f"Incorrect arguments supplied to assertProbability")

        expectedProbas = [expectedProba for _ in range(self.testProperty.nbTests)]

        generatedTests = [qc.copy() for qc, theta, phi in self.initialisedTests]

        #Only apply the functions if specified
        if not qu0_pre:
            for generatedTest in generatedTests:
                self.quantumFunction(generatedTest)

        filteredTests = list(filter(filter_qc, generatedTests))

        self.nbFiltered = len(filteredTests)



        dataFromExec = TestExecutor().runTestsAssertProbability(filteredTests,
                                                                self.testProperty.nbTrials,
                                                                self.testProperty.nbMeasurements,
                                                                qu0,
                                                                self.testProperty.nbClassicalBits + 1,
                                                                basis)

        testResults = StatAnalyser().testAssertProbability(self.testProperty.p_value, expectedProbas, dataFromExec)

        qu0Params = [(x[1].get(qu0, 0), x[2].get(qu0, 0)) for x in self.initialisedTests]

        testResultsWithInit = tuple(zip(testResults, qu0Params))



        return testResultsWithInit



    def assertProbability(self, qu0, expectedProba, qu0_pre=False, basis="z", filter_qc=lambda qc:True):
        results = self.assertProbabilityData(qu0, expectedProba, qu0_pre, basis, filter_qc)

        if not qu0_pre:
            print(f"AssertProbability({qu0}, {expectedProba}) results using basis {basis.upper()}:")
        else:
            print(f"AssertProbability({qu0}_pre, {expectedProba}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0]} Phi = {testResult[1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {self.nbFiltered - nbFailed} / {self.nbFiltered} succeeded\n")
        else:
            print(f"All {self.nbFiltered} tests have succeeded!\n")


        return results




    def assertNotProbability(self, qu0, expectedProba, qu0_pre=False, basis="z", filter_qc=lambda qc:True):
        oppositeResults = self.assertProbabilityData(qu0, expectedProba, qu0_pre, basis, filter_qc)

        results = [(not x[0], x[1]) for x in oppositeResults]

        if not qu0_pre:
            print(f"AssertNotProbability({qu0}, {expectedProba}) results using basis {basis.upper()}:")
        else:
            print(f"AssertNotProbability({qu0}_pre, {expectedProba}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"qu0: Theta = {testResult[1][0]} Phi = {testResult[1][1]}")

        if failed:
            print(f"Not all tests have succeeded: {len(self.initialisedTests) - nbFailed} / {len(self.initialisedTests)} succeeded\n")
        else:
            print(f"All {len(self.initialisedTests)} tests have succeeded!\n")


        return results




    def assertTeleportedData(self, sent, received, basis):

        generatedTests = [qc.copy() for qc, theta, phi in self.initialisedTests]

        for generatedTest in generatedTests:
            self.quantumFunction(generatedTest)


        expectedProbas = []
        for qc, thetas, phis in self.initialisedTests:
            expectedProba = cos(radians(thetas[sent]) / 2) ** 2
            expectedProbas.append(expectedProba)

        dataFromReceived = TestExecutor().runTestsAssertProbability(generatedTests,
                                                                    self.testProperty.nbTrials,
                                                                    self.testProperty.nbMeasurements,
                                                                    received,
                                                                    self.testProperty.nbClassicalBits + 1,
                                                                    basis)

        testResults = StatAnalyser().testAssertProbability(self.testProperty.p_value, expectedProbas, dataFromReceived)

        qu0Params = [(x[1].get(sent, 0), x[2].get(sent, 0)) for x in self.initialisedTests]
        qu1Params = [(x[1].get(received, 0), x[2].get(received, 0)) for x in self.initialisedTests]
        params = tuple(zip(qu0Params, qu1Params))

        testResultsWithInit = tuple(zip(testResults, params))


        return testResultsWithInit


    def assertTeleported(self, sent, received, basis="z"):
        results = self.assertTeleportedData(sent, received, basis)

        print(f"AssertTeleported({sent}, {received}) results using basis {basis.upper()}:")

        failed = False
        nbFailed = 0
        for testIndex, testResult in enumerate(results):
            if not testResult[0]:
                failed = True
                nbFailed += 1
                print(f"Test at index {testIndex} failed with qubits initialised to:")
                print(f"sent: Theta = {testResult[1][0][0]} Phi = {testResult[1][0][1]}")

        if failed:
            print(f"Not all tests have succeeded: {len(self.initialisedTests) - nbFailed} / {len(self.initialisedTests)} succeeded\n")
        else:
            print(f"All {len(self.initialisedTests)} tests have succeeded!\n")


        return results






    def run(self):
        print(f"Running tests for {type(self).__name__}:\n")

        self.testProperty = self.property()

        self.initialisedTests = TestCaseGenerator().generateTests(self.testProperty)

        self.assertions()

        print(f"Tests for {type(self).__name__} finished\n")

    def runTests(self):
        self.run()
