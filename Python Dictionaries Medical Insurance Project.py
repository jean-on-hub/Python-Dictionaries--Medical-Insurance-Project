# Add your code here
medical_costs = {}
medical_costs.update({"Marina" : 6607.0,"Vinay":3225.0})
medical_costs.update({"Connie":6607.0,"Valentina":6420.0,"Isaac":16444.0})
medical_costs["Vinay"]=3325.0
total_cost = 0
for a in medical_costs.values():
  total_cost += a
average_cost = total_cost/len(medical_costs)
names = ["Marina","Vinay","connie","Isaac","Valentina"]
ages = [27,24,43,35,52]
zipped_ages = list(zip(names,ages))
names_to_ages = {a:b for a,b in zipped_ages }
marina_age = names_to_ages.get("Marina",None)
print("Marina's age is "+str(marina_age))
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records.update({"Vinay":{"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0},"Connie":{"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0},"Isaac":{"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},"Valentina":{"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})
print(medical_records)
print("Connie's insurance cost is "+str(medical_records.get("Connie").get("Insurance_cost"))+" dollars.")
medical_records.pop("Vinay")
ans = []
for name,data in medical_records.items():
    print(name+" is a "+ str(data.get("Age")) +" year old "+data.get("Sex")+" "+data.get("Smoker")+ " with a BMI of "+str(data.get("BMI"))+" and insurance cost of "+str(data.get("Insurance_cost")))
  #19
def update_medical_records(name,age,sex,bmi,children,smoker,insurance_cost):
  data.update({"Age": age, "Sex": sex, "BMI": bmi, "Children": children, "Smoker": smoker, "Insurance_cost": imsurance_cost})
  medical_records.update({name:{data}})