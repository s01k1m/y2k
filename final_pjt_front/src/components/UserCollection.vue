<template>
  <v-card>
    <v-container fluid >
      <v-row dense>

        <v-col
        :key="card.id"
        :cols="card.flex"
        name="outside"
        
        >
        <v-card id="theone" style="box-shadow: 0 4px 6px 0 #adaaaa; ">
          <a @click="reveal = true">
          <v-img
            :src="'http://127.0.0.1:8000' + card.stills[0]?.still_image"
            class="align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200px"
            cover
            sytle= "border-radius : 7px;"
            >
            <v-card-title class="text-white" v-text="card.collection_name"></v-card-title>
          </v-img>
        </a>
          <v-expand-transition>
            <v-card
            v-if="reveal"
            class="v-card--reveal"
            style="height: 100%; border: none;"
            >
        <v-card-text class="pb-0" style="box-shadow: none; border:none;">
          <p class="text-h4 text--primary">
            saved Stills
          </p>
          <div v-show="!card.stills.length" class="noContents">There's no Stills!
            <br>
            :'(
          </div>
          <div id="columns">
            <figure v-for="(still, index) in card.stills" :key="index">
              <StillCard :still="still" :index="index"></StillCard>
            </figure>
          </div>
        </v-card-text>
        <v-card-actions class="pt-0">
          <v-btn
            variant="text"
            color="teal-accent-4"
            @click="reveal = false"
          >
            Close
          </v-btn>
          <v-btn
            variant="text"
            class=" white--text"
            @click="deleteCollection"
            id="delete_btn"
            >Delete</v-btn>
          
        </v-card-actions>
      </v-card>
    </v-expand-transition>
        </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
// import { BIconArrowRightSquare } from 'bootstrap-vue';
import StillCard from './StillCard.vue';
import axios from "axios";

export default {
  name: 'UserCollection',
  data(){
    return {
      reveal : true,
      collection: this.card,
    }
  },
  components : {
    StillCard
  },
  created: {
    find
  },
  props: {
    card: Object,
    renew: Number,
  },
  // emits: ['child'],
  methods: {
    deleteCollection () {
      console.log('######################',this.collection.id)
      let collection_id = Number(this.collection.id)
      const username = localStorage.getItem('username')
      let token = localStorage.getItem('access_token')
      let data = {
        collection_pk : collection_id,
        
      }
      console.log(data, username, 'axios시작')
      axios
        .delete(`http://127.0.0.1:8000/stills/user/${username}/collection/delete/${collection_id}/`, {
          headers: {
            Authorization: "Token " + token,
          }
        })
        .then((response) => {
          alert(response.data.message);
          this.$emit('child')
        })
        .catch((error) => {
          console.log(error);
        });
    },
    gogo() {
      
    }
  }
}
</script>

<style scoped>
.v-sheet.v-card:not(.v-sheet--outlined) {
  box-shadow: none;
  border : none;
}
div.mypage > .row--dense > .col, .row--dense > [class*=col-]{
  border: none;
  background-color: palegreen;
}


#delete_btn {
 background-color: #e08b8b;
}
</style>