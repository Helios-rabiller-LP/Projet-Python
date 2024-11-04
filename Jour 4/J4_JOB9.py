def moyenne(note1,note2,note3):
    note1 = float(note1)
    note2 = float(note2)
    note3 = float(note3)
    return float((note1 + note2 + note3) / 3)
moyenne_etudiant = moyenne(input(),input(),input())
if 15 <= moyenne_etudiant <=20:
    print("trés bon élève")
elif 11 <= moyenne_etudiant <=14:
    print("bon élève")
elif 8 <= moyenne_etudiant <=10:
    print("élève moyen")
else :
    print("élève devant faire des efforts")