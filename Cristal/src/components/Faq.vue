<template>
    <div id="faq">
      <Nav></Nav>
      <b-container>
        <h1 class="titre">FAQ</h1>
        <hr class="style-four">
        <div role="tablist">
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-btn block class="btn" href="#" v-b-toggle.accordion1>Cela fait plusieurs fois que je frappe à la
                porte de l'association mais je ne vois personne. Comment puis-je vous voir ?</b-btn>
            </b-card-header>
            <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p class="card-text">
                  N'hésitez à nous envoyer un mail à <a id="mail" href="mailto:contact@cristal.je">
                  contact@cristal.je</a>. Nous mettrons prochainement en ligne un
                  calendrier de nos disponibilités, vous permettant de savoir quel membre sera présent dans les locaux.
                  Étudiants comme vous, nous faisons notre possible pour être présents !
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-btn block class="btn" href="#" v-b-toggle.accordion2>J'ai un client mais je n'ai pas de statut
                d'auto-entrepreneur, est-ce-que Cristal peut m'aider ?</b-btn>
            </b-card-header>
            <b-collapse id="accordion2" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p class="card-text">
                  Tout à fait ! Nous mettons à votre disposition un bon de commande, téléchargeable ici. Le bon commande
                  vous permet d'effectuer votre mission dans un cadre légal, c'est-à-dire qu'un contrat tri-partie est
                  établi : entre le client et Cristal ainsi qu'entre vous et Cristal. De ce fait, en cas de litige,
                  vous êtes couverts.
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-btn block class="btn" href="#" v-b-toggle.accordion3>Quand vais-je recevoir mon paiement ?</b-btn>
            </b-card-header>
            <b-collapse id="accordion3" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p class="card-text">
                  Vous pourrez récupérer votre paiement lorsque la mission sera terminée. Vous recevrez un mail vous
                  notifiant que le chèque peut être récupéré à l'association. Une exception est faite pour les
                  prestations en régie qui sont étalées sur plusieurs mois, dans ce cas le paiement est mensuel.
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-btn block class="btn" href="#" v-b-toggle.accordion4>Qu'est-ce-que je vais devoir aux impôts ?</b-btn>
            </b-card-header>
            <b-collapse id="accordion4" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <p class="card-text">
                  Tout dépend de vos revenus sur l'année fiscale précédente. Référez-vous ici. Au moment de déclarer vos
                  impôts, si vous avez effectué des missions avec Cristal, nous vous indiquerons le montant total net
                  imposable à déclarer aux impôts. En fonction de votre rattachement fiscal (individuel ou parents), et
                  du plafond dépassé ou non, vous aurez un somme à payer ou non.
                </p>
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
      </b-container>
      <Footer></Footer>
    </div>
</template>

<script>
import Nav from './Nav'
import Footer from './Footer'
export default {
  name: 'Faq',
  components: {Footer, Nav}
}
</script>

<style scoped>
  .titre{
    color: #0c365a;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 20px;
  }
  hr.style-four {
    height: 12px;
    border: 0;
    box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);
  }
  .btn {
    background-color: #79b249;
    border-color: #79b249;
    padding-bottom: 2%;
    padding-top: 2%;
    font-size: larger;
  }
</style>
