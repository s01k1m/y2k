<!-- Mypage vue  -->
<template>
  <div class="user">
    <h1>MyPage</h1>
    <UserProfile></UserProfile>
    <UserCollection></UserCollection>
    <button @click="logout">logout</button>

    <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
    <v-app>
    <v-container>
      <!-- mypage nav button -->
      <v-row>
        <v-col cols="2">
          <v-btn @click="showStills">My stills</v-btn>
        </v-col>
        <v-col cols="2" >
          <v-btn @click="showCollections">My collections</v-btn>
        </v-col>
        <v-col cols="1" offset="7" class="mypage_nav" v-bind:class="{ visible: collectionsActive }" >
          <!-- 콜렉션을 추가하는 버튼 -->
          <v-btn icon="md:widgets" size="small" @click="dialog = true"></v-btn>
        </v-col>
      </v-row>
      <!-- mypage content -->
      <v-row v-bind:class="{ visible: stillsActive}" >
        <v-col class="mypage">
          STillCARD
          <StillCard>
          </StillCard>
        </v-col>
      </v-row>
      <v-row class="mypage" v-bind:class="{ visible: collectionsActive}" >
        <v-col >
        collections
          <StillCard>
          </StillCard>
        </v-col>
      </v-row>
    </v-container>


    <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
    <!-- %%%%%%%% 콜렉션 생성 모달 창  %%%%%%%% -->
    <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->

    <v-dialog v-model="dialog" width="auto" >
                    <v-card>
                      <v-card-text>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                      </v-card-text>
                      <v-card-actions>
                        <v-btn color="primary" rounded="xl" text @click="dialog = false">Close Dialog</v-btn>
                        <v-btn color="primary" rounded="xl" text  @click="dialog = false">submit</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
  </v-app>
  </div>
</template>

<script>
import UserProfile from '@/components/UserProfile.vue'
import UserCollection from '@/components/UserCollection.vue'
import StillCard from '@/components/StillCard.vue'


export default {
  name: 'UserView',
  components: {
    UserProfile,
    UserCollection,
    StillCard,
  },
  data() {
    return {
      dialog : false,
      stillsActive: false,
      collectionsActive: true,
    }
  }
,
  methods: {
    logout() {
      return this.$store.dispatch('logout')
    },
    showStills() {
      this.stillsActive = false,
      this.collectionsActive = true
    },
    showCollections() {
      this.stillsActive = true,
      this.collectionsActive = false
    }
  }
}
</script>

<style scoped>
div.user {
  background-color: rgb(173, 165, 255);
}

.mypage {
  background-color: aquamarine;
}

.mypage_nav {
  background-color: rgb(195, 110, 216);
  color: black;
}

.visible {
  display: none;
}
</style>