

#above 65 or health issue True
# def vaccination_portal(**kwargs):
#     age=kwargs["age"]
#     hel=kwargs["health_issue"]
#     if(age>=65)|(hel==True):
#         print("request is allowed location ekm")
#     else:
#         print("failed allocation")
# vaccination_portal(name="anju",age=25,address="address",health_issue=False)
# vaccination_portal(name="annam",age=72,address="address",health_issue=False)
# vaccination_portal(name="joseph",age=67,address="address",health_issue=True)
# vaccination_portal(name="ammu",age=28,address="address",health_issue=True)


def vaccination_eligibility(func):
    def wrapper(**kwargs):
        age=kwargs["age"]
        hel=kwargs["health_issue"]
        if (age>=65)|(hel==True):
            return func(**kwargs)
        else:
            print("allocation failed")
    return wrapper
@vaccination_eligibility
def vaccination_portal(**kwargs):
    print("request is allowed location ekm")

vaccination_portal(name="anju",age=25,address="address",health_issue=False)
vaccination_portal(name="annam",age=72,address="address",health_issue=False)
vaccination_portal(name="joseph",age=67,address="address",health_issue=True)
vaccination_portal(name="ammu",age=28,address="address",health_issue=True)
