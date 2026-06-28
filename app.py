import uuid
import json

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
        
            bootcamp_data["karvands"].append(karvands)
            with open("karvands.json", "w") as file:
                json.dump(bootcamp_data, file, indent=4)


        case "2" | "Show":
            with open("karvands.json", "r") as file:
                data = json.load(file)
                karvands = data["karvands"]
                if len(karvands) == 0:
                    print("There is no karvand in karvands.json")
                else:
                    for karvand in karvands:
                        print(f"{karvand_id} -- {karvand_name}\n{karvand_email} -- {karvand_city}\n{karvand["education"]["degree"]} -- {karvand["education"]["field"]}\n{karvand["skills"]["name"]} -- {karvand["skills"]["level"]} -- {karvand["skills"]["score"]}")
        
        case "3" | "Search(id)":
            ...
        case "4" | "Search(skills)":
            ...
        case "5" | "Edit":
            print(karvands)
        case "6" | "Delete":
            ...
        case "7" | "Repport":
            ...
        case "8" | "Exit":
            ...