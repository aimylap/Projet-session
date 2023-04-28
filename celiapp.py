import streamlit as st


def main():
    #titre
    st.title("Le CELIAPP, est-ce pour moi?")
    
    #introduction
    st.write(""" Le CELIAPP est un nouveau régime enregistré qui permet d’épargner de l’argent à l’abri de l’impôt en vue d’acheter une première habitation admissible. Ce court questionnaire vous aidera à identifier si ce véhicule de placement pourrait vous aider à atteindre votre projet.""")

    # Question 1
    q1 = st.radio("1. Êtes-vous âgé de 18 ans ou plus?", ("Oui", "Non"))
    
    # Question 2
    q2 = st.radio("2. Êtes-vous résident canadien?", ("Oui", "Non"))
    
    # Question 3
    q3 = st.radio("3. Avez-vous vécu dans une propriété qui vous appartenait ou à votre conjoint(e) dans les 5 dernières années", ("Oui", "Non"))
    
    # Question 4
    q4 = st.selectbox("4. Quel est le montant que vous prévoyez cotiser à votre CELIAPP par année??", ("8 000$ et moins", "Plus de 8 000$"))
    
    # Question 5
    q5 = st.selectbox("5. Dans combien d'années prévoyez-vous acheter votre première maison?",  ("Moins de 15 ans", "Plus de 15 ans"))
    
    # Question 6
    q6 = st.checkbox("7. Je comprends que ces questions ne sont pas exhaustives et que je dois vérifier mon admissibilité au CELIAPP avec un conseiller financier.")
    
    if st.button("Vérifier si vous êtes un bon candidat"):
        # Vérifier l'admissibilité en fonction des réponses
        if q1 == "Oui" and q2 == "Oui" and q3 == "Non" and q4 == "8 000$ et moins" and q5 == "Moins de 15 ans" :
            st.write("Félicitations, vous êtes admissible au CELIAPP !")
        else:
            st.write("Oups... Quelque chose semble nous indiquer que le CELIAPP n'est peut-être pas pour vous. Informez-vous auprès d'un professionnel pour plus d'informations.")
        
if __name__ == '__main__':
    main()
