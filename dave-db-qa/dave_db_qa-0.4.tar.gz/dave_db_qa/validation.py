from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, BooleanType, MapType
from pyspark.sql.functions import udf, struct
import pandas as pd

class ClassValidator:

    def __init__(self):
        print("here's my validator")
        self.count = 0

    def addCount(self, input: int):
        self.count = self.count + 1
        return input + self.count






# Simple check for an int. Does not (current pass negatives)
def checkInt(input):
    # Check for Null
    if (not input):
        return False
    # Check for an instance of int
    if (isinstance(input, int)):
        return True
    # Check if it only contains digits.
    # TODO look for negative integers too
    if (isinstance(input, str) and input.isdigit()):
        return True
    else:
        return False


# Parent path is used to handle recursion.
def validate(data, rules, parentPath=None, logging=False):
    print(data)

    valid = True
    action = None

    fieldResponses = []

    # for each key, check if there is a list of rules.
    for ruleKey in rules.keys():
        if (logging):
            print(f'Evaluating field [{ruleKey}]')
        fieldRules = rules[ruleKey]

        ## TODO
        # Check that ruleKey has parentPath as prefix if it exists.

        value = None
        if ruleKey in data:
            value = data[ruleKey]

        if (logging):
            print(f'Check field [{ruleKey}] with value [{value}]')

        messages = []
        failedRules = []
        fieldValid = True

        # if there are lists of rules, process each one.
        for keyRule in fieldRules:
            ruleId = keyRule['ruleId']

            if (logging):
                print(f'For field [{ruleKey}], evaluating [{ruleId}]')

            if (keyRule['type'] == 'NULL_CHECK'):
                isNull = (None == value)
                if (isNull):
                    fieldValid = False
                    message = 'Rule [{ruleId}], Field [{ruleKey}] was NULL'.format(ruleId=ruleId, ruleKey=ruleKey)
                    if (logging):
                        print(message)

                    messages.append(message)
                    failedRules.append(ruleId)

                    # TODO Ensure that a DROP overrides a FLAG_INVALID label.
                    action = keyRule['action']

            if (keyRule['type'] == 'TYPE'):
                expectedType = keyRule['expectedType']
                isType = True

                if (expectedType == 'int'):
                    isType = checkInt(value)

                if (not isType):
                    fieldValid = False
                    message = 'Rule [{ruleId}], Field [{ruleKey}] was not type [{expectedType}]'.format(ruleId=ruleId, ruleKey=ruleKey, expectedType=expectedType)
                    if (logging):
                        print(message)

                    messages.append(message)
                    failedRules.append(ruleId)

                    # TODO Ensure that a DROP overrides a FLAG_INVALID label.
                    action = keyRule['action']




        if (not fieldValid):
            if (logging):
                print(f'Adding invalid field response for [{ruleKey}]')
            fieldResponse = {
                'name': ruleKey,
                'valid': False,
                'messages': messages,
                'action': action,
                'failedRules': failedRules
            }
            fieldResponses.append(fieldResponse)
            valid = False

    return {
        'valid': valid,
        'fields': fieldResponses,
        'action': action
    }


class Validator:

    def __init__(self, spark):
        self.spark = spark

    def create_rule_schema(self):
        return StructType([
            StructField('ruleId', StringType(), False),
            StructField('type', StringType(), False),
            StructField('action', StringType(), False),
            StructField('break', BooleanType(), True),
            StructField('expectedType', StringType(), True),
            StructField('minValue', IntegerType(), True)
        ])

    def build_validation_df(self, validation_rules):
        ruleSchema = self.create_rule_schema()

        validationRuleSchema = MapType(StringType(), ArrayType(ruleSchema))

        validationRulesDf = self.spark.createDataFrame([validation_rules], validationRuleSchema)

        return validationRulesDf.withColumnRenamed('value','_rules')

    def _createSchema(self):
        fieldValidationResultSchema = ArrayType(StructType([
            StructField("name", StringType(), True), \
            StructField("valid", BooleanType(), True), \
            StructField("messages", ArrayType(StringType()), True), \
            StructField("action", StringType(), True)
        ]))

        validationResultSchema = StructType([ \
            StructField("valid", BooleanType(), True), \
            StructField("fields", fieldValidationResultSchema, True), \
            StructField("action", StringType(), True)
        ])
        return validationResultSchema

    def buildUdfs(self):

        validationResultSchema = self._createSchema()

        validate_udf = udf(validate, validationResultSchema)
        #self.spark.udf.register("validate", validate, validationResultSchema)
        return validate_udf



    def testValidate(self, inputDict, dataSchema, validationRules, useSpark=False):

        validationResultSchema = self._createSchema()
        rule_schema = MapType(StringType(), ArrayType(self.create_rule_schema()))
        print(validationRules)

        if (useSpark):
            # Wrap input dict in an array and convert to a dataframe
            df = self.spark.createDataFrame([inputDict], dataSchema)

            # Convert the validation rules into a dataframe.
            validationRulesDf = self.spark.createDataFrame([validationRules], rule_schema)

            # join the row.
            joinedWithValidation = df.join(validationRulesDf)

            validate_udf = self.buildUdfs()
            validatedDf = joinedWithValidation.withColumn("validation", validate_udf(struct(['a', 'b']), '_rules')).select(
                'a', 'b', 'validation')

            validationResult = validatedDf.collect()[0]['validation']
            return {'valid': validationResult['valid'], 'fields': validationResult['fields'],
                    'action': validationResult['action']}
        else:
            validationResult = validate(inputDict, validationRules, logging=True)
            return validationResult

    def assertValid(self, validationResult):
        if (validationResult['valid']):
            print("Success - result was [valid] as expected")
        else:
            raise Exception("Failure - expected success but was failure: " + pd.DataFrame(validationResult['fields']))


    def assertInvalid(self, validationResult, expectedRuleFailure, expectedAction):
        if (not validationResult['valid']):
            print("Success - result was [invalid] as expected")
        else:
            raise Exception("Failure - expected failure but was success")

        numFailures = len(validationResult['fields'])
        if numFailures != 1:
            raise Exception(f"Expected single field failure but were {numFailures}")

        numFieldFailures = len(validationResult)


        actualRuleFailure = validationResult['fields'][0]['failedRules'][0]
        if (actualRuleFailure != expectedRuleFailure):
            raise Exception(f"We were expecting rule [{expectedRuleFailure}] but received [{actualRuleFailure}]")

        actualAction = validationResult['action']
        if (actualAction != expectedAction):
            raise Exception(f"We were expecting action [{expectedAction}] but received [{actualAction}]")

