from paddl.langs.mysql import definition as mysql


ddl_s = open('test/fixtures/hello.sql').read()

result = mysql.parseString(ddl_s, parseAll=False)

print(ddl_s)
print(result)
