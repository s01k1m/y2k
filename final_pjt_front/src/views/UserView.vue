<template>
  <div class="user" style="text-align:center;">
    <v-app>
      <v-container>
    <br>
    <UserProfile></UserProfile>
    <UserCollection></UserCollection>
    <div style="text-align: right; margin-right: 30px;">
      <button sy @click="logout" id="logout">Bye.. {{ getUserName }} </button>
    </div>
        <!-- mypage nav button -->
        <v-row>
          <v-col cols="2" class="mypage_nav">
            <v-btn @click="getUserStills">My stills</v-btn>
          </v-col>
          <v-col cols="2" class="mypage_nav">
            <v-btn @click="getUserCollections">My collections</v-btn>
          </v-col>

          <v-col
            cols="1"
            offset="7"
            class="mypage_nav"
            v-bind:class="{ visible: collectionsActive }"
          >
            <!--  -->
            <v-dialog v-model="dialog" persistent width="1100">
              <template v-slot:activator="{ props }">
                <v-btn
                  fab
                  small
                  v-bind="props"
                  @click="dialog = true"
                  class="create_Collection"
                  >+</v-btn
                >
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Create Collection</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          label="Collection Name*"
                          required
                          hint="20자 이하"
                          v-model="amount"
                          oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                          type="text"
                          maxlength="20"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                  <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="dialog = false"
                  >
                    Close
                  </v-btn>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="createUserCollection"
                  >
                    Save
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <!-- 콜렉션을 추가하는 버튼 -->
          </v-col>
        </v-row>

        <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% mypage content 내용 섹션 -->
        <v-row v-bind:class="{ visible: stillsActive }">
          <v-col class="mypage">
            <div v-show="!stillsResult" class="noContents">There's no Stills!
            <br>
            :'(
            </div>
            <div id="columns">
              <figure v-for="(still, index) in stillsResult" :key="index">
                <StillCard :still="still" :index="index"></StillCard>
              </figure>
            </div>
          </v-col>
        </v-row>
        <v-row class="mypage" v-bind:class="{ visible: collectionsActive }">
          <v-col>
            <div v-for="(card, index) in collectionsResult" :key="index" >
            <UserCollection  style="margin:10px;" :card="card" :renew="rew" @child="addRenew" ></UserCollection>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";
import UserProfile from "@/components/UserProfile.vue";
import UserCollection from "@/components/UserCollection.vue";
import StillCard from "@/components/StillCard.vue";

export default {
  name: "UserView",
  components: {
    UserProfile,
    UserCollection,
    StillCard,
  },
  data() {
    return {
      stillsActive: false,
      collectionsActive: true,
      stillsResult: null,
      collectionsResult: null,
      dialog: false,
      amount: '',
      rew: 0,
    };
  },
  computed: {
    getUserName() {
      console.log('computed', localStorage.getItem('username'))
      return localStorage.getItem('username')
    }
  },
  created() {
    this.forStart()

  },
  mounted() {
    if (localStorage.getItem('username')) {
      this.getUserStills();
    }
  },
  methods: {
    logout() {
      return this.$store.dispatch("logout");
    },
    forStart() {
      console.log('forStart 시작')
      const username = this.getUserName
      console.log('local username:' ,this.getUserName)
      if (username) {
        axios
          .get(`http://127.0.0.1:8000/stills/user/${username}/stills`)
          .then((response) => {
            this.stillsResult = response.data;
            console.log(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
    }
  },
    getUserStills() {
      this.stillsActive = false;
      this.collectionsActive = true;
      const username = this.getUserName
      console.log('local username:' ,this.getUserName)
      if (username) {
        axios
          .get(`http://127.0.0.1:8000/stills/user/${username}/stills`)
          .then((response) => {
            this.stillsResult = response.data;
            console.log(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    getUserCollections() {
      this.stillsActive = true;
      this.collectionsActive = false;

      const username = this.getUserName
      console.log('local username:' ,this.getUserName)
      let token = localStorage.getItem('access_token')
      if (username) {
        axios
          .get(`http://127.0.0.1:8000/stills/user/${username}/collections`, {
            headers: {
              Authorization: "Token " + token,
            }})
          .then((response) => {
            this.collectionsResult = response.data;
            console.log(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    createUserCollection() {
      this.dialog = false
      console.log(this.amount)
      let collection_title = this.amount
      this.$store.dispatch('getMemberInfo')
      const username = localStorage.getItem('username')
      let data = {
        collection_name : collection_title
      }
      let token = localStorage.getItem('access_token')
      console.log(username, data, token)
      if (username) {
        axios
          .post(`http://127.0.0.1:8000/stills/user/${username}/collections/`, data, {
            headers: {
              Authorization: "Token " + token,
            }})
          .then((response) => {
            this.collectionsResult = response.data;
            console.log(response.data);
            this.getUserCollections()
            
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    addRenew() {
      this.rew += 1
      console.log(this.rew)
      this.getUserCollections()
    }
  },
};
</script>

<style scoped>
div.user {
  /* background-color: #e9e9e9; */
}

.mypage {
  /* background-color: aquamarine; */
}

.mypage_nav {
  /* background-color: rgb(195, 110, 216); */
}

.visible {
  display: none;
}

.create_Collection {
  font-size: 20px;
}
#logout{
  color: #8c8c8c;
}

</style>
