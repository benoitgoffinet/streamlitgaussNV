
import streamlit as st

#les fonctions

def trouverafficherX(matrice):
    z = len(matrice)-1
    n = 1
    X = []
    
    # je commence par remplir le tableau avec le premier X
    # si le nombre que l on divise = 0 le resultat = 0
    if matrice[z][len(matrice[z])-2] == 0:
      X.append(0)

    # sinon le x = resulat/par le nombre de X
    else:
      X.append(matrice[z][len(matrice[z])-1]/matrice[z][len(matrice[z])-2])

    # je remplis le tableau avex les autres X
    z-=1
    indice=1
    while(z >= 0):
        if matrice[z][len(matrice[z])-1-n] ==0:
           X.append(0)
           indice +=1
        else:
           P = n
           Total = 0
           # x = (resulat - total des autres X de la ligne)/par le nombre de X
           while(P>0):
                Total += (matrice[z][len(matrice[z])-2-n+P] * X[indice-P])
                P -=1
           X.append((matrice[z][len(matrice[z])-1] - Total)/matrice[z][len(matrice[z])-2-n])
           indice +=1
        n +=1
        z-=1
    indX = 0
    nX = len(X)
    # affichage des X
    while(nX>0):
         st.write('X'+str(nX)+' = '+str(round(X[indX], 3)))
         indX +=1
         nX -=1

         
def transformationmatrice(matrice):
 I = 0
 while(matrice[len(matrice)-1].count(0) <= len(matrice)-2 ):
    var1 = 0
    for e in matrice:
        if var1+I<len(matrice)-1:
                       if matrice[var1+1+I][0+I] != 0:
                                Q = matrice[var1+1+I][0+I]/matrice[0+I][0+I]
                                Q1 = round(Q, 15)
                                var2 =0
                                for elem in matrice[var1+1+I][I:]:
                                       if var2+I<len(matrice[0]):
                                            nelem = matrice[0+I][var2+I]
                                            nelem2 = elem - (nelem*Q)
                                            nelem3 = round(nelem2, 3)
                                            matrice[var1+1+I][var2+I]=nelem3
                                            var2 +=1       
        var1+=1
    I+=1



def affichagematrice(matrice, ligne):
         l=1
         while(l<ligne):
              F =1
              cols = st.columns(len(matrice[l-1]))
              for col, item in zip(cols, matrice[l-1]):
                  with col:
                       if F == len(matrice[l-1]):
                            aitem = round(item, 2)
                            st.metric(label ='', value='X'+str(l)+' =  '+str(aitem))
                       else:
                           aitem = round(item, 2)
                           st.metric(label ='', value=aitem)
                  F+=1
              l+=1


st.title("Ma belle Gauss")
st.write("Equation gaussienne")


#initialisation des variables au demarrage de la session
if "bigmatrice" not in st.session_state:
    st.session_state.bigmatrice = [] 
    st.session_state.bigmatriceinit = [] 
    st.session_state.ligne = 1 


matrice = []
matrices = st.text_input("Constuisez votre matrice", key="input_text")

    

st.write('exemple = 4,9,85,0,895 pour la 1er ligne puis recommencer pour les lignes suivantes')

#si le bouton n a pas ete appuye
if not st.button("Resolution de l'equation"):

    #initialisation des variables
    A = []
    st.session_state.bigmatrice = [] 
    matricestring = matrices.split(',')
    matrice =[]
    x =0
    # je remplis la matrice et verifie les erreurs
    if len(matricestring)>0:
           for item in matricestring:
               erreur = 0
               try:
                   matrice.append(int(matricestring[x]))
               except:
                   erreur = 1
                   st.markdown("<p style='color:red;'>Tapez uniquement des chiffres et des ' , '.</p>", unsafe_allow_html=True)
                   matrice = []
                   st.session_state.bigmatriceinit = []
                   st.session_state.ligne = 1 
                   break
               x+=1
               
               if x == len(matricestring) and erreur == 0:
                   st.session_state.ligne +=1
                   st.session_state.bigmatriceinit.append(matrice)
    
    l=1

    
    #j affiche les valeures de la matrice
    if erreur ==0:
       affichagematrice(st.session_state.bigmatriceinit, st.session_state.ligne)
    
         
else:  
   #Verification de la matrice(largeur et longueur)
   MC = len(st.session_state.bigmatriceinit[0])
   ML = len(st.session_state.bigmatriceinit)+1
   erreur2 = 0
   for matrice in st.session_state.bigmatriceinit:
       if len(matrice) != MC or len(matrice) != ML:
          erreur2 = 1
          matrice = []
          st.session_state.bigmatriceinit = []
          st.session_state.ligne = 1 
          break
   if erreur2 == 1:
        st.markdown("<p style='color:red;'>La longueur de votre matrice doit etre identique a sa hauteur(Ne pas prendre en compte ' X ').</p>", unsafe_allow_html=True)
   else:        
       
    I = 0
    var = 0
    l=1
    st.session_state.bigmatriceinit2 = st.session_state.bigmatriceinit
    st.session_state.bigmatriceinit = [] 

    #affichage matrice initiale
    st.title('Matrice initiale')
    affichagematrice(st.session_state.bigmatriceinit2, st.session_state.ligne)

    #je transforme la matrice
    st.session_state.bigmatrice = st.session_state.bigmatriceinit2   
    transformationmatrice(st.session_state.bigmatrice)
    
   
    #affichage matrice transforme
    st.title('Matrice transforme')
    affichagematrice(st.session_state.bigmatrice, st.session_state.ligne)

    #reinitialisation des variables
    st.session_state.ligne = 1
    matricetr = []

    #recherche de X
    matricetr = st.session_state.bigmatrice
    trouverafficherX(matricetr)
    
    
