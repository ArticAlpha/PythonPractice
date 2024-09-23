check={}
check['key1']="(hey there i'm the value of key1)"
check['key2']="(hey there i'm the value of key2)"

dq_rules = "({0})".format("AND ".join(check.values()))
dq_rules1 = f"({' AND '.join(check.values())})"
print(dq_rules)
print(dq_rules1)