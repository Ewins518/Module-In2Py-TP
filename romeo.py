romeo = {'SE':[18,16,14], 'SDA':[15,16,16],  'Langage C':[15,14,16], 'Uml':[15.75,16.25,18], 'Algèbre':[14,16,16], 'base de donné':[18,16,17], 'java':[16,18,16], 'Programmation systeme':[19,18,16], 'Web':[15,16,17], 'LTP':[18,16,18]}

moyenne_par_matiere = [ (romeo['SE'][0] + romeo['SE'][1] + romeo['SE'][2])/3,  (romeo['Langage C'][0] + romeo['Langage C'][1] + romeo['Langage C'][2])/3 ,  (romeo['Uml'][0] + romeo['Uml'][1] + romeo['Uml'][2])/3,  (romeo['Algèbre'][0] + romeo['Algèbre'][1] + romeo['Algèbre'][2])/3,  (romeo['base de donné'][0] + romeo['base de donné'][1] + romeo['base de donné'][2])/3,  (romeo['Programmation systeme'][0] + romeo['Programmation systeme'][1] + romeo['Programmation systeme'][2])/3,  (romeo['java'][0] + romeo['java'][1] + romeo['java'][2])/3,  (romeo['Web'][0] + romeo['Web'][1] + romeo['Web'][2])/3,  (romeo['SE'][0] + romeo['SE'][1] + romeo['SE'][2])/3,  (romeo['LTP'][0] + romeo['LTP'][1] + romeo['LTP'][2])/3]

moyenne = (moyenne_par_matiere[0] + moyenne_par_matiere[2] + moyenne_par_matiere[3] + moyenne_par_matiere[4] + moyenne_par_matiere[5] + moyenne_par_matiere[6] + moyenne_par_matiere[1] + moyenne_par_matiere[7] + moyenne_par_matiere[8] + moyenne_par_matiere[9] )/len(moyenne_par_matiere)

print(moyenne)

#E0

L =   [1,2,3,4,5,6,7,8,9,10]

L[0] = L[0] + 11
L[1] = L[1] + 11
L[2] = L[2] + 11
L[3] = L[3] + 11
L[4] = L[4] + 11
L[5] = L[5] + 11
L[6] = L[6] + 11
L[7] = L[7] + 11
L[8] = L[8] + 11
L[9] = L[9] + 11

L.append(22)
L.extend([23,24])

L1 = L[0::2]
print(L1)

L2 = L[1::2]
print(L2)

#L.delete(3)

print(L)

#E1

d = {'nom':'Dupuis', "prenom":'Jacque','age':30}
d['prenom'] = 'Jacques'

print(d.keys())
print(d.values())
print(d)

phrase = d['prenom'] +' '+ d['nom'] +' ' +'a'+' '+ (str)(d['age'])+ ' '+ 'ans'

print(phrase)
