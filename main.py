import streamlit as st

st.set_page_config(layout="wide")

col1, col2, = st.columns(2)

with col1:
    st.image("images/photo.png", width= 480)
    
with col2:
    st.title("Jordan Cesar")
    content = """
     Olá, me chamo Jordan Cesar e sou programador Python estou cursando Tecnólogo de Redes de Computadores pela Universidade Estácio de Sá
     e cursando o Data Expert da dnc.group onde estudo a parte de Data Science e Marchine Learning.
     
     Tenho experiência em gestão de projetos, analise de dados e desenvolvimento de aplicações, associando metodologias ágeis com boas práticas de programação.
     Sou apaixonado por programação, entusiastas de temas relacionados a educação e acredito que a revolução seja a prática!
      
     Minhas primeiras experiências profissionais foram direcionadas a área de Auxiliar Administrativo e na área de Analises de Vendas em Auxiliar de Vendas.

     Meu objetivo é ingressar totalmente na área de dados e mostrar que tenho muito a acrescentar.

     Ambas experiências foram extremamente edificantes e me moldaram como profissional, no entanto, descobri uma paixão pela Ciência de Dados e, como parte de uma nova jornada, decidi me especializar realizando a formação em Dados da Escola DNC.

     Principais Habilidades adiquiridas:
 
     • Linguagem Python e suas Libraries (Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, ...);
     
     • Linguagem de Banco de Dados Relacionais (MySQL e PostgreSQL) e Não Relacionais (Mongo DB);
     
     • Ambientes de Programação e Versionamento (VSCode, Jupyter, Pycharm, Git e GitHub);
     
     • Estatística (Descritiva, Inferencial e Avançado);
     
     • Visualização de Dados(Power BI e R);
     
     • Data Cleaning, Data Wrangling e Data Storytelling;
     
     • Machine Learning (Supervisonado, Não Supervisonado, AutoML, ...);
     
     • Processos e Metodologias Ágeis como CRISP-DM e SCRUM, respectivamente;
     
      """
    st.info(content)

content2 = """
Abaixo, você pode encontrar alguns dos aplicativos que eu construí em Python.Senti-se livre para entrar em contato comigo!
"""