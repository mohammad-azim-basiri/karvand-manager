import uuid
import json
import os

target_path = r"G:\Maktabsharif_AI\CW2\karvand-manager\data"

bootcamp_data = {
    "bootcamp": {
        "title": "Karvand Python",
        "year": 2026
    },
    "karvands": []
}
karvands = []
def create_new_karvand(karvand_name,karvand_email
                       ,karvand_city,karvand_degree,karvand_field
                       ,karvand_id,skills):
    new_karvand = {
        
            "id": str(karvand_id),
            "full_name": karvand_name,
            "email": karvand_email,
            "city": karvand_city,
            "education": {
                "degree": karvand_degree,
                "field": karvand_field
            },
            "skills": skills
    }
    return new_karvand

skills = []

def create_skill_list(karvand_skill_name,karvand_skill_level,karvand_skill_score):
    new_skill = {
        "name": karvand_skill_name,
        "level": karvand_skill_level,
        "score": karvand_skill_score
    }
    return new_skill

while True:
    user_order = input("""Please enter the order: 
                    1.Add
                    2.Show
                    3.Search(id)
                    4.Search(skills)
                    5.Edit
                    6.Delete
                    7.Repport
                    8.Exit
                    """)

    match user_order:
        case "1" | "Add":
            karvand_name = input("Enter name of karvand: ")
            karvand_email = input("Enter email of karvand: ")
            karvand_city = input("Enter city of karvand: ")
            karvand_degree = input("Enter degree of karvand: ")
            karvand_field = input("Enter field of karvand: ")
            karvand_id = uuid.uuid4()

            while True:
                karvand_skill_name = input("Enter skill\' name of karvand(enter 0 to exit from skill part): ")
                if karvand_skill_name == "0" :
                    break
                else:
                    karvand_skill_level = input("Enter level of skill: ")
                    try:
                        karvand_skill_score = int(input("Enter score of skill: "))
                    except ValueError:
                        print("You can only enter number in this field.")
                        karvand_skill_score = int(input("Enter score of skill: "))
                    if karvand_skill_score < 0 | karvand_skill_score > 100:
                        print("enter skill score between 0 - 100")
                    while 100 <  karvand_skill_score < 0:
                        karvand_skill_score = int(input("Enter score of skill: "))
                    skill = create_skill_list(karvand_skill_name,karvand_skill_level,karvand_skill_score)         
                    skills.append(skill)
            karvand = create_new_karvand(karvand_name,karvand_email
                       ,karvand_city,karvand_degree,karvand_field
                       ,karvand_id,skills)
            karvands.append(karvand)    
        
            bootcamp_data["karvands"].append(karvand)
            os.makedirs(target_path, exist_ok=True)
            with open("data/karvands.json", "w") as file:
                json.dump(bootcamp_data, file, indent=4)

            skills = []
        case "2" | "Show":
            
            if not os.path.exists("data/karvands.json"):
                print("No data found yet.")
                continue
                
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                
                if len(current_karvands) == 0:
                    print("There is no karvand in karvands.json")
                else:
                    for karvand in current_karvands:
                        # چاپ اطلاعات اصلی
                        print(f"\nID: {karvand['id']} -- Name: {karvand['full_name']}")
                        print(f"Email: {karvand['email']} -- City: {karvand['city']}")
                        print(f"Education: {karvand['education']['degree']} in {karvand['education']['field']}")
                        
                        
                        print("Skills:")
                        for sk in karvand["skills"]:
                            print(f"  - {sk['name']} (Level: {sk['level']}, Score: {sk['score']})")
                        print("-" * 30)
        case "3" | "Search(id)":
            search_id = input("Please enter an id: ")
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                flag = False

                for karvand in current_karvands:
                    if karvand["id"] == search_id:
                        print(f"\nID: {karvand['id']} -- Name: {karvand['full_name']}")
                        print(f"Email: {karvand['email']} -- City: {karvand['city']}")
                        print(f"Education: {karvand['education']['degree']} in {karvand['education']['field']}")
                        
                        print("Skills:")
                        for sk in karvand["skills"]:
                            print(f"  - {sk['name']} (Level: {sk['level']}, Score: {sk['score']})")
                        print("-" * 30)
                        flag = True

                if not flag:
                    print(f"There is no karvand with this id: {search_id}")
         
        case "4" | "Search(skills)":
            search_skill = input("Enter an skill to search: ")
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                flag = False
                for karvand in current_karvands:
                    for sk in karvand["skills"]:
                            if sk['name'] == search_skill:
                                print(f"{karvand['id']} -- {karvand["full_name"]} -- {karvand["email"]}")
                                flag = True
                if not flag:
                    print(f"There is no karvand with this skill: {search_skill}")
                                
        case "5" | "Edit":
            edit_id = input("Please enter an id: ")
            with open("data/karvands.json", "+r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                flag = False

                for karvand in current_karvands:
                    if karvand["id"] == edit_id:
                        flag = True
                        edit_option = input("""which one you want to edit:
                              1.Email
                              2.City
                              3.Degree
                              4.Field
                               """)
                        match edit_option:
                            case "1" | "Email":
                                edit_email = input("Please enter new email: ")
                                karvand["email"] = edit_email
                            case "2" | "City":
                                edit_city = input("Please enter new city: ")
                                karvand["city"] = edit_city
                            case "3" | "Degree" :
                                edit_degree = input("Please enter new degree: ")
                                karvand["education"]["degree"] = edit_degree
                            case "4" | "Field" :
                                edit_field = input("Please enter new field: ")
                                karvand["education"]["field"] = edit_field

                with open("data/karvands.json", "w") as file:
                    json.dump(data, file, indent=4)
                if not flag:
                    print(f"there is no karvand with this id: {edit_id}")        

        case "6" | "Delete":
            delete_id = input("Please enter an id: ")
            with open("data/karvands.json", "+r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                flag = False

                for karvand in current_karvands:
                    if karvand["id"] == delete_id:
                        flag = True
                        current_karvands.remove(karvand)

                with open("data/karvands.json", "w") as file:
                    json.dump(data, file, indent=4)

                if not flag:
                    print(f"There is no karvand with this id: {delete_id}")

        case "7" | "Repport":
            with open("data/karvands.json","+r") as file:
                data = json.load(file)
                current_karvands = data["karvands"]
                count_of_karvand = 0
                count_of_skills = 0
                sum_of_scores = 0
                list_of_cities = []
                list_of_skills = []
                for karvand in current_karvands:
                    list_of_cities.append(karvand["city"])
                    count_of_karvand += 1
                    for sk in karvand["skills"]:
                        count_of_skills += 1
                        sum_of_scores += sk["score"]
                        if not sk["name"] in list_of_skills:
                            list_of_skills.append(sk["name"])


                print(f"\"total_karvands\" : {count_of_karvand}")  
                print(f"\"total_skills\" : {count_of_skills}") 
                print(f"\"average_skill_score\" : {sum_of_scores / count_of_skills}") 
                print(f"\"cities\":{list_of_cities}")
                print(f"\"unique_skills\":{list_of_skills}")
                
                data_of_repport = {"total_karvands":count_of_karvand,
                                   "total_skills":count_of_skills,
                                   "average_skill_score":sum_of_scores / count_of_skills,
                                   "cities":list_of_cities,
                                   "unique_skills":list_of_skills}

                with open("data/report.json","+w") as f:
                    json.dump(data_of_repport, f , indent=4)

        case "8" | "Exit":
            break