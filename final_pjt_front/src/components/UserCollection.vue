<template>
  <v-card>
    <!-- <v-system-bar
      color="indigo darken-2"
      dark
    >
      <v-spacer></v-spacer>

      <v-icon icon="mdi-window-minimize"></v-icon>

      <v-icon icon="mdi-window-maximize"></v-icon>

      <v-icon icon="mdi-close"></v-icon>
    </v-system-bar>

    <v-toolbar
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Discover</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon="mdi-magnify"></v-btn>
    </v-toolbar> -->

    <v-container fluid>
      <v-row dense>

        <v-col
        :key="index"
        :cols="card.flex"
        >
        <v-card>
          <a @click="reveal = true">
          <v-img
            :src="'http://127.0.0.1:8000' + card.stills[0]?.still_image"
            class="align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200px"
            cover
            >
            <v-card-title class="text-white" v-text="card.collection_name"></v-card-title>
          </v-img>
        </a>
          <v-expand-transition>
            <v-card
            v-if="reveal"
            class="v-card--reveal"
            style="height: 100%;"
            >
        <v-card-text class="pb-0">
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
import StillCard from './StillCard.vue';

export default {
  name: 'UserCollection',
  data(){
    return {
      reveal : false,
    }
  },
  components : {
    StillCard
  },
  props: {
    card: Object,
  },
  methods: {
    },
  }

</script>

<style>

</style>